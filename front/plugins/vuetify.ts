// plugins/vuetify.js
import '@/assets/main.scss'
import '@/assets/settings.scss'

import { IconProps, IconSet, createVuetify } from 'vuetify'
import { mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import customIcons from '@/utils/customIcons'

const inputsProps =  {
  variant: 'filled',
  rounded: 'lg',
  hideDetails: 'auto'
}

const custom: IconSet = {
  component: (props: IconProps) => 
    h(props.tag, [h(customIcons[props.icon as string], { class: 'v-icon__svg' })])
}

export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    ssr: true,
    components,
    directives,
    icons: {
      defaultSet: 'mdi',
      sets: {
        mdi,
        custom
      }
    },
    theme: {
      themes: {
        light: {
          dark: false,
          colors: {
            primary: '#363636',
            secondary: '#363636',
            amarillo: '#eac102',
          }
        },
        dark: {
          dark: true,
          colors: {
            primary: '#363636'
          }
        }
      }
    },
    defaults: {

      VTextField: inputsProps,
      VSelect: inputsProps,
      VAutocomplete: inputsProps,
      VCombobox: inputsProps,
      VTextarea: {
        ...inputsProps,
        autoGrow: true,
        rows: 1
      },
      VAlert: {
        variant: 'tonal'
      },

      VBtn: {
        rounded: 'lg'
      },

      VList: {
        color: 'primary'
      },
      
    }
  })

  nuxtApp.vueApp.use(vuetify)
})