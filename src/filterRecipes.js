export default function filterRecipes(index, searchText, data) {
  var sorted_recipes = data.sort((obj1, obj2) => {return obj1.section > obj2.section})
  var documents_lookup = sorted_recipes.reduce(function (out, doc) {
  out[doc.title] = doc
  return out
  }, {})

  var recipes_filtered
  if (searchText === "") {
      recipes_filtered = sorted_recipes
  } else {
      var results = index.search(searchText);
      recipes_filtered = results.map((res) => documents_lookup[res.ref])
  }

  var sectioned_result = recipes_filtered.reduce(function(out, doc){
    out[doc.section] = out[doc.section] || [];
    out[doc.section].push(doc)
    return out
  },{})
 // convert the object to list then sort and then convert back to obj
  return Object.entries(sectioned_result).sort().reduce( (o,[k,v]) => {
    o[k]=v
    return o}, {} )
}