/** 單一貼圖資料 */
export type OneStickerData = {
  name: string,
  type: string,
}
/** 貼圖包資料 */
export type StickerPackData = {
  name: string,
  type: string,
  children: OneStickerData[],
}

export type StickerDataLib = {
  name: string,
  type: string,
  children: StickerPackData[],
}