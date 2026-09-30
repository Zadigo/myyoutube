export default defineEventHandler(async (event) => {
  const options = await readBody(event)
  console.log(options)
})
