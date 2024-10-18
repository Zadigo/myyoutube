// const webFontLoader = await import(/* webpackChunkName: "webfontloader" */'webfontloader')
import webFontLoader from 'webfontloader'

webFontLoader.load({
  google: {
    families: ['Roboto', 'Ubuntu', 'Lato']
  }
})
// export async function loadFonts () {
// }
