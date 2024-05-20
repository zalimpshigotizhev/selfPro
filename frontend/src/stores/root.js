import { defineStore } from 'pinia'



export const useRootStore = defineStore('root', {
  state: () => ({
    four_months: [],

  }),
  actions: {
    // Функция для создание диапазонов
    range(start, end) {
        const array = [];
        for (let i = start; i <= end; i++) {
            let  dictionary = {};
            dictionary['date'] = i
            array.push(dictionary);
        }
        return array;
    },
    // Функция для генерации списка с четыремя последними месяцами 
    getLastFourMonths(){
      const today = new Date();

      const results = []

      for (let i = 4; i > 0; i--){
          let year = today.getFullYear()
          let month = today.getMonth() - i
          let daysInMonth = new Date(year, month + 2, 0);

          let monthName = daysInMonth.toLocaleString('default', { month: 'long' })
          let normalize_name = monthName.charAt(0).toUpperCase() + monthName.slice(1)

          results.push({
              'name': normalize_name,
              'days': this.range(1, daysInMonth.getDate())
          })
      }
      this.four_months = results
    } 

  }
})
