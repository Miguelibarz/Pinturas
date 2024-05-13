import axios from "axios";
import { useAuthStore } from "@/stores/auth";
import { Ref, ref } from "vue";
import { storeToRefs } from "pinia";

function updateOptions(options, url) {
  const store = useAuthStore();
  const { token } = storeToRefs(store)
  if (options === undefined)
    return {
      headers: {
        Authorization: token.value,
      },
      url,
    };
  options.url = url;
  options.headers = {
    Authorization: token.value,
    ...options.headers
  };
  return options;
}

type httpResponseAxios = {
  data: Ref<any>;
  error: Ref<Error | Boolean>;
  pending: Ref<Boolean>;
  refresh: () => Promise<Boolean>;
};

async function httpRequest(...args: any[]) {
  return new Promise<httpResponseAxios>(async (resolve) => {
    let [url, options] = args;
    if (!options && typeof url === "object") {
      options = url;
      url = options.url;
    }

    options = updateOptions(options, url);
    const data = ref<any>(null);
    if (options.default) data.value = options.default();

    const error = ref<Error | Boolean>(null);
    const pending = ref<Boolean>(false);

    const makeRequest = (extra_options? : Object) => {
      return new Promise<Boolean>(async (resolve) => {
        pending.value = true;
        try {
          options = { ...options, ...extra_options }
          const { data: json } = await axios(options);
          if (options.transform) data.value = options.transform(json);
          else data.value = json;
          pending.value = false;
          resolve(true);
        } catch (e) {
          error.value = e.response;
          pending.value = false;
          resolve(false);
        }
      });
    };

    if (!options.lazy) {
      if (options.block) await makeRequest();
      else if (!options.block) makeRequest();
    }

    resolve({ data, error, pending, refresh: makeRequest });
  });
}

export default defineNuxtPlugin((nuxtApp) => {
  return {
    provide: {
      axios: httpRequest,
    },
  };
});
