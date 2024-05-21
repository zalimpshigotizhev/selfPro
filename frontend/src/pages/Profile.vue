<script setup>
import Header from 'components/Header.vue'
import FourMonths from 'components/profile/FourMonths.vue'
import GraphPie from 'components/profile/GraphPie.vue'
import { useRootStore } from '../stores/root';
import { storeToRefs } from 'pinia';


const rootStore = useRootStore()
const { tip } = storeToRefs(rootStore)


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
                    <br>
                    <VTooltip style="cursor: pointer; width: 18px;">
                        <div :class="tip === true ? 'info-icon' : 'info-icon-off'"  @click="rootStore.onOffTip()"></div>
                        <template #popper>
                            <div class="tip">
                                Вкл/Выкл подсказки
                            </div>
                        </template>
                    </VTooltip>
                </div>
            </div>
            <div class="graphs">
                <GraphPie/>
                <FourMonths/>
            </div>
            
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'

.profile
    display: flex
    flex-direction: column
    padding-bottom: 100px

    .wrapper
        display: flex
        justify-content: space-between

        @media (min-width: $min_mobile) and (max-width: $max_mobile)
            flex-direction: column
            
        .info
            display: flex
            @media (min-width: $min_mobile) and (max-width: $max_pad)
                flex-direction: column
            .img

                width: 280px
                height: 345px
                @media (min-width: $min_mobile) and (max-width: $max_pad)
                    
                    width: 200px
                    height: 280px
                    min-width: 200px
                    min-height: 280px
                    border-radius: 12px

                border-radius: 32px
                background: url("../assets/img/myPhoto.jpg")
                background-repeat: no-repeat
                background-size: cover
            
            .name-email
                display: flex
                flex-direction: column
                margin-left: 40px 
                
                @media (min-width: $min_mobile) and (max-width: $max_pad)
                    margin-top: 10px
                    margin-left: 15px

                .name
                    font-family: "JetBrains Medium", sans-serif
                    font-size: 55px
                    overflow-y: auto
                    width: 360px

                .email
                    font-family: "JetBrains ExtraLight", sans-serif
                    font-size: 18px
                    color: $textMuted            


    .title
        font-family: "JetBrains ExtraBold", sans-serif
        font-size: 64px
        margin-bottom: 40px

        @media (min-width: $min_mobile) and (max-width: $max_pad)
            font-size: 44px
            margin-bottom: 20px
    
    .graphs
        display: flex
        justify-content: space-around
        @media (min-width: $min_mobile) and (max-width: $max_mobile)
            align-items: center
            flex-wrap: wrap


</style>