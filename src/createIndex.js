import lunr from 'lunr'

export default function createIndex(data) {
  
  var idx = lunr(function () {
    this.ref('title')
    this.field('title', { boost: 10 })
    this.field('description', { boost: 10 })
    this.field('tags', { boost: 10 })
    this.field('section', { boost: 10 })
    this.field('snippet')
    data.forEach(function (doc) {
      this.add(doc)
    }, this)
  })
  console.log('index made')
  return idx
}