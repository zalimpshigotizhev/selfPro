<script setup>
import { reactive, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ROUTES_PATHS from '../constans/router'


const route = useRoute();
const router = useRouter();
const routeName = computed(() => route.name);
console.log(routeName);

const nav_mob = reactive({
    state: null
}
)
function setStateNavMobile(val){
    nav_mob.state = val
}

const navigateTo = (routeName) => {
      router.push({ name: routeName });
};

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

                <div
                :class="routeName === ROUTES_PATHS.PROFILE ? 'nav-btn active' : 'nav-btn'"
                @click="navigateTo(ROUTES_PATHS.PROFILE)"
                >
                    Мой профиль
                </div>
                <div
                :class="routeName === ROUTES_PATHS.HOME ? 'nav-btn active' : 'nav-btn'"
                @click="navigateTo(ROUTES_PATHS.HOME)"
                >
                    Intensive
                </div>
                <div class="nav-btn">
                    Anki <span class="soon">скоро</span>
                </div>
                <!-- Mobile -->
                <div class="burger" @click="setStateNavMobile('open')"></div>
                <div v-if="nav_mob.state == 'open'" class="nav-mob" >
                    <div class="upper">
                        <div class="closed" @click="setStateNavMobile(null)">

                        </div>
                    </div>
                    <div class="nav-mob-btns">
                        <div 
                        :class="routeName === ROUTES_PATHS.PROFILE ? 'mob-btn active-mob' : 'mob-btn'"
                        @click="navigateTo(ROUTES_PATHS.PROFILE)"
                        >
                            Мой профиль
                        </div>
                        <div 
                        :class="routeName === ROUTES_PATHS.HOME ? 'mob-btn active-mob' : 'mob-btn'"
                        @click="navigateTo(ROUTES_PATHS.HOME)"
                        >
                            Intensive
                        </div>
                        <div class="mob-btn">
                            Anki <span >скоро</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
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
        .img
            background-image: url('../assets/img/neuron1.png')


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
        color: $background
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

.nav-mob
    @media (min-width: $min-mobile) and (max-width:$max-pad)
        display: block

    display: none
    position: fixed
    width: 95%
    height: 95%
    background-color: $background

    top: 1em
    left: 1em
    bottom: 1em
    right: 1em
    border-radius: 10px
    border: solid 0.1px

    .upper
        display: flex
        justify-content: flex-end

        .closed
            cursor: pointer
            background-image: url('../assets/img/x.png')
            background-repeat: no-repeat
            background-size: cover
            margin: 30px
            opacity: 80%
            width: 50px
            height: 50px

    .nav-mob-btns
        display: flex
        align-items: center
        flex-direction: column
        justify-content: center
        padding-top: 60px 
        .mob-btn
            cursor: pointer
            font-family: "Prompt", sans-serif
            font-weight: 600
            font-style: normal
            font-size: 20px

            span
                font-family: "Prompt", sans-serif
                font-weight: 400
                font-style: normal
                font-size: 15px
                color: $textMuted
            
        .active-mob
            color: $textMuted




</style>