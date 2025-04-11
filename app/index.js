const data = [{ name: "Afghanistan", score: 2 },{ name: "Albania", score: 4 },{ name: "Algeria", score: 7 },{ name: "Andorra", score: 1 },{ name: "Angola", score: 1 },{ name: "Antigua and Barbuda", score: 1 },{ name: "Argentina", score: 12 },{ name: "Armenia", score: 3 },{ name: "Australia", score: 20 },{ name: "Austria", score: 12 },{ name: "Azerbaijan", score: 5 },{ name: "Bahrain", score: 3 },{ name: "Bangladesh", score: 3 },{ name: "Barbados", score: 1 },{ name: "Belarus", score: 4 },{ name: "Belgium", score: 16 },{ name: "Belize", score: 1 },{ name: "Benin", score: 3 },{ name: "Bolivia (Plurinational State of)", score: 7 },{ name: "Bosnia and Herzegovina", score: 4 },{ name: "Botswana", score: 2 },{ name: "Brazil", score: 23 },{ name: "Bulgaria", score: 10 },{ name: "Burkina Faso", score: 3 },{ name: "Cabo Verde", score: 1 },{ name: "Cambodia", score: 4 },{ name: "Cameroon", score: 2 },{ name: "Canada", score: 22 },{ name: "Central African Republic", score: 2 },{ name: "Chad", score: 2 },{ name: "Chile", score: 7 },{ name: "China", score: 57 },{ name: "Colombia", score: 9 },{ name: "Congo", score: 2 },{ name: "Costa Rica", score: 4 },{ name: "Côte d'Ivoire", score: 5 },{ name: "Croatia", score: 10 },{ name: "Cuba", score: 9 },{ name: "Cyprus", score: 3 },{ name: "Czechia", score: 17 },{ name: "Democratic People's Republic of Korea", score: 2 },{ name: "Democratic Republic of the Congo", score: 5 },{ name: "Denmark", score: 11 },{ name: "Dominica", score: 1 },{ name: "Dominican Republic", score: 1 },{ name: "Ecuador", score: 5 },{ name: "Egypt", score: 7 },{ name: "El Salvador", score: 1 },{ name: "Eritrea", score: 1 },{ name: "Estonia", score: 2 },{ name: "Ethiopia", score: 11 },{ name: "Fiji", score: 1 },{ name: "Finland", score: 7 },{ name: "France", score: 52 },{ name: "Gabon", score: 2 },{ name: "Gambia", score: 2 },{ name: "Georgia", score: 4 },{ name: "Germany", score: 52 },{ name: "Ghana", score: 2 },{ name: "Greece", score: 19 },{ name: "Guatemala", score: 4 },{ name: "Haiti", score: 1 },{ name: "Holy See", score: 2 },{ name: "Honduras", score: 2 },{ name: "Hungary", score: 8 },{ name: "Iceland", score: 3 },{ name: "India", score: 42 },{ name: "Indonesia", score: 10 },{ name: "Iran (Islamic Republic of)", score: 27 },{ name: "Iraq", score: 6 },{ name: "Ireland", score: 2 },{ name: "Israel", score: 9 },{ name: "Italy", score: 59 },{ name: "Jamaica", score: 1 },{ name: "Japan", score: 25 },{ name: "Jerusalem (Site proposed by Jordan)", score: 1 },{ name: "Jordan", score: 6 },{ name: "Kazakhstan", score: 6 },{ name: "Kenya", score: 7 },{ name: "Kiribati", score: 1 },{ name: "Kyrgyzstan", score: 3 },{ name: "Lao People's Democratic Republic", score: 3 },{ name: "Latvia", score: 3 },{ name: "Lebanon", score: 6 },{ name: "Libya", score: 5 },{ name: "Lithuania", score: 5 },{ name: "Luxembourg", score: 1 },{ name: "Madagascar", score: 3 },{ name: "Malawi", score: 2 },{ name: "Malaysia", score: 4 },{ name: "Mali", score: 4 },{ name: "Malta", score: 3 },{ name: "Marshall Islands", score: 1 },{ name: "Mauritania", score: 2 },{ name: "Mauritius", score: 2 },{ name: "Mexico", score: 35 },{ name: "Micronesia (Federated States of)", score: 1 },{ name: "Mongolia", score: 6 },{ name: "Montenegro", score: 4 },{ name: "Morocco", score: 9 },{ name: "Mozambique", score: 1 },{ name: "Myanmar", score: 2 },{ name: "Namibia", score: 2 },{ name: "Nepal", score: 4 },{ name: "Netherlands", score: 13 },{ name: "New Zealand", score: 3 },{ name: "Nicaragua", score: 2 },{ name: "Niger", score: 3 },{ name: "Nigeria", score: 2 },{ name: "Norway", score: 8 },{ name: "Oman", score: 5 },{ name: "Pakistan", score: 6 },{ name: "Palau", score: 1 },{ name: "Panama", score: 5 },{ name: "Papua New Guinea", score: 1 },{ name: "Paraguay", score: 1 },{ name: "Peru", score: 13 },{ name: "Philippines", score: 6 },{ name: "Poland", score: 17 },{ name: "Portugal", score: 17 },{ name: "Qatar", score: 1 },{ name: "Republic of Korea", score: 16 },{ name: "Romania", score: 9 },{ name: "Russian Federation", score: 31 },{ name: "Rwanda", score: 2 },{ name: "Saint Kitts and Nevis", score: 1 },{ name: "Saint Lucia", score: 1 },{ name: "San Marino", score: 1 },{ name: "Saudi Arabia", score: 7 },{ name: "Senegal", score: 7 },{ name: "Serbia", score: 5 },{ name: "Seychelles", score: 2 },{ name: "Singapore", score: 1 },{ name: "Slovakia", score: 8 },{ name: "Slovenia", score: 5 },{ name: "Solomon Islands", score: 1 },{ name: "South Africa", score: 10 },{ name: "Spain", score: 50 },{ name: "Sri Lanka", score: 8 },{ name: "State of Palestine", score: 4 },{ name: "Sudan", score: 3 },{ name: "Suriname", score: 3 },{ name: "Sweden", score: 15 },{ name: "Switzerland", score: 13 },{ name: "Syrian Arab Republic", score: 6 },{ name: "Tajikistan", score: 4 },{ name: "Thailand", score: 7 },{ name: "Tunisia", score: 9 },{ name: "Türkiye", score: 21 },{ name: "Turkmenistan", score: 5 },{ name: "Uganda", score: 3 },{ name: "Ukraine", score: 8 },{ name: "United Arab Emirates", score: 1 },{ name: "United Kingdom of Great Britain and Northern Ireland", score: 33 },{ name: "United Republic of Tanzania", score: 7 },{ name: "United States of America", score: 25 },{ name: "Uruguay", score: 3 },{ name: "Uzbekistan", score: 7 },{ name: "Vanuatu", score: 1 },{ name: "Venezuela (Bolivarian Republic of)", score: 3 },{ name: "Viet Nam", score: 8 },{ name: "Yemen", score: 5 },{ name: "Zimbabwe", score: 5 },{ name: "North Macedonia", score: 2 },{ name: "Republic of Moldova", score: 1 },{ name: "Togo", score: 1 },{ name: "Guinea", score: 1 },{ name: "Lesotho", score: 1 },{ name: "Zambia", score: 1 },];


const width = 900;
const height = 450;
const margin = { top: 50, bottom: 50, left: 50, right: 50 };

const svg = d3.select('#d3-container')
  .append('svg')
  .attr('width', width - margin.left - margin.right)
  .attr('height', height - margin.top - margin.bottom)
  .attr("viewBox", [0, 0, width, height]);

const x = d3.scaleBand()
  .domain(d3.range(data.length))
  .range([margin.left, width - margin.right])
  .padding(0.1)

const y = d3.scaleLinear()
  .domain([0, 100])
  .range([height - margin.bottom, margin.top])

svg
  .append("g")
  .attr("fill", 'royalblue')
  .selectAll("rect")
  .data(data.sort((a, b) => d3.descending(a.score, b.score)))
  .join("rect")
    .attr("x", (d, i) => x(i))
    .attr("y", d => y(d.score))
    .attr('title', (d) => d.score)
    .attr("class", "rect")
    .attr("height", d => y(0) - y(d.score))
    .attr("width", x.bandwidth());

function yAxis(g) {
  g.attr("transform", `translate(${margin.left}, 0)`)
    .call(d3.axisLeft(y).ticks(null, data.format))
    .attr("font-size", '20px')
}

function xAxis(g) {
  g.attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).tickFormat(i => data[i].name))
    .attr("font-size", '20px')
}

svg.append("g").call(xAxis);
svg.append("g").call(yAxis);
svg.node();
