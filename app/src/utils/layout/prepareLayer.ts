export default (config: number[]) => config.map(count => ([...Array(count)]).map(() => null))
