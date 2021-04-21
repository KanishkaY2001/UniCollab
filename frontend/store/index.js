import createPersistedState from 'vuex-persistedstate'

export const plugins = [createPersistedState()]

export const state = () =>({
  userId: 0,
  user: "",
  defPhoto: "/img/spaceman.pg"
})

export const mutations = {
  SAVE_USER(state, info) {
    if (!info) return;
    state.user = info;
    state.userId = info.id;
    console.log(state.user.name)
  }
}