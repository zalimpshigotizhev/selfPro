<script setup>


</script>
<template>
    <div>
        <div class="header">
            
            <div class="icon">
                <div class="img"></div>
                <div class="icon-span">
                    <span class="self">self</span><div class="glick"></div><span class="progressive">Progressive</span>
                </div>
            </div>
            <div class="nav">

                <div class="nav-btn active">
                    Мой профиль
                </div>
                <div class="nav-btn">
                    Intensive
                </div>
                <div class="nav-btn">
                    ToDo <span class="soon">скоро</span>
                </div>
                <div class="nav-btn">
                    Pomodoro <span class="soon">скоро</span>
                </div>
                <div class="nav-btn">
                    Anki <span class="soon">скоро</span>
                </div>

                <div class="burger"></div>


            </div>
        </div>
        <hr>
    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'
.header
    display: flex
    align-items: center
    justify-content: space-between
    padding-top: 40px
    padding-bottom: 40px

.icon
    cursor: pointer
    display: flex
    flex-direction: column
    align-items: center
    margin: 10px
    width: 130px
    .img
        width: 52px
        height: 52px
        background-image: url('../assets/img/neuron.png')
        background-position: center
        background-size: 52px
        background-repeat: no-repeat
        
    
    .icon-span
        display: flex
        align-items: center 
    
        .self
            font-family: "Prompt", sans-serif
            font-weight: 900
            font-style: normal
            font-size: 15px
        
        .glick
            width: 13px
            height: 13px
            background-image: url('../assets/img/glick.svg')
            background-repeat: no-repeat

        .progressive
            font-family: "Prompt", sans-serif
            font-weight: 400
            font-style: normal
            font-size: 15px

    &:hover
        .glick
            background-image: url('../assets/img/glick-hover.svg')

.nav
    display: flex
    align-items: center



    .nav-btn
        cursor: pointer
        font-family: "Prompt", sans-serif
        font-weight: 600
        font-style: normal
        font-size: 20px

        &:not(:last-child)
            margin-right: 74px
        span
            font-family: "Prompt", sans-serif
            font-weight: 400
            font-style: normal
            font-size: 15px
            color: $textMuted
        
        @media (min-width: $min_mobile) and (max-width: $max_pad)
            display: none
    
    .active
        background-color: $text
        color: #ffffff
        padding: 14px 24px
        border-radius: 8px

            
.burger
    display: none
    margin: 15px
    cursor: pointer
    background-image: url('../assets/img/burger.png')
    background-repeat: no-repeat
    background-size: cover
    height: 35px
    width: 35px

    @media (min-width: $min_mobile) and (max-width: $max_pad)
        display: block



</style>