class LocalServices{
  changeState = async (path, queryParams) => {
    await fetch(`http://${path}${queryParams}`, { mode: 'no-cors' })
  }
}

export default new LocalServices()