<script setup>
import Header from 'components/Header.vue'
import FourMonths from 'components/profile/FourMonths.vue'


</script>
<template>
    <Header/>
    <div class="profile">
        <div class="title">Мой профиль</div>
        <div class="wrapper">
            <div class="info">
                <div class="img"></div>
                <div class="name-email">
                    <div class="name">Залим</div>
                    <div class="email">zalim.lox@gmail.com</div>
                </div>
            </div>

            <FourMonths/>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'

.profile
    display: flex
    flex-direction: column
    .wrapper
        display: flex
        justify-content: space-between
        .info
            display: flex
            .img
                width: 280px
                height: 345px
                @media (min-width: $min_mobile) and (max-width: $max_mobile)
                    width: 200px
                    height: 280px
                    border-radius: 12px

                border-radius: 32px
                background-color: black
            
            .name-email
                margin-left: 40px 
                @media (min-width: $min_mobile) and (max-width: $max_mobile)
                    margin-left: 15px

                .name
                    font-family: "JetBrains Medium", sans-serif
                    font-size: 55px
                .email
                    font-family: "JetBrains ExtraLight", sans-serif
                    font-size: 18px
                    color: $textMuted            

        @media (min-width: $min_mobile) and (max-width: $max_mobile)
            flex-direction: column
    .title
        font-family: "JetBrains ExtraBold", sans-serif
        font-size: 64px
        margin-bottom: 40px

        @media (min-width: $min_mobile) and (max-width: $max_mobile)
            font-size: 44px
            margin-bottom: 20px


</style>