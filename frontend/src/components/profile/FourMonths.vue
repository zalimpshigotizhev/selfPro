<script setup>


</script>
<template>
    <div class='root'>
        <div class="title">Four months</div>
        <div class="intensive">
            <div class="two-months">
                <div class="month">
    
                </div>
                <div class="month">
                    
                </div>
            </div>
            <div class="two-months">
                <div class="month">
    
                </div>
                <div class="month">
                    
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.root
    display: flex
    flex-direction: column
    margin-left: 30px
    padding-right: 60px

    @media (min-width: $min_mobile) and (max-width: $max_mobile)
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
            height: 161px
            margin: 10px
            background-color: orange

            .month
                width: 142px
                height: 161px
                background-color: black
                &:not(:last-child)
                    margin-right: 30px
</style>