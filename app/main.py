import utils 
import read_csv
import charts


def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    country = input('Tipe country : ')

    result = utils.population_by_country(data, country)
    
    if len(result)>0:
        country = result[0]
        labels, values = utils.get_populations(country)
        charts.generate_bar_chart(labels, values)
 

    
    

if __name__ == '__main__':
    run()
    