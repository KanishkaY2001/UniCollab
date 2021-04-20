export const state = () =>({
  userId: 0,
  user: ""
})

export const mutations = {
  SAVE_USER(state, info) {
    if (!info) return;
    state.user = info;
    state.userId = info.id;
  },
}