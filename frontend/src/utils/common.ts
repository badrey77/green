export const getRandomItem = (items) =>
  items[Math.floor(Math.random() * items.length)];

export const get_ingredients_from = (results) => {
  
  const elements = JSON.parse(results)
  const ings = elements.map(elem=>(elem.food.label)).join(',');
  return ings;
}

