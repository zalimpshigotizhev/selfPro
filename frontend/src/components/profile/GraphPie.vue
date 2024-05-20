<script setup>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

const data = {
  labels: ['VueJs', 's', 'ReactJs', 'AngularJs'],
  datasets: [
    {
      backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
      data: [40, 0, 80, 10],
    },
  ],
};

const options = {
  responsive: true,
};


</script>
<template>
    <div class='graph'>
        <div class="title">Pie Stats</div>
        <Pie :data="data" :options="options" />
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.graph
    display: flex
    flex-direction: column
    max-width: 280px

    @media (min-width: $min_mobile) and (max-width: $max_pad)
        margin-top: 40px

    .title
        font-family: "JetBrains Bold", sans-serif
        font-size: 25px
    
    .intensive
        display: flex
        flex-direction: column

        .two-months
            display: flex
            width: 314px
            margin: 10px

</style>