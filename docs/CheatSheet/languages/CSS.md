 
## 隐藏滚动条

https://segmentfault.com/a/1190000019710081

## 不允许文字换行：
`text-wrap: nowarp`
`overflow`

## Flex布局(uesful)
https://www.runoob.com/w3cnote/flex-grammar.html

## box-sizing
box-sizing 属性定义如何计算一个元素的总宽度和总高度，主要设置是否需要加上内边距(padding)和边框等。
<table class="reference">
  <tbody><tr>
    <th align="left" width="25%">值</th>
    <th align="left" width="75%">说明</th>
  </tr>  
  <tr>
    <td> content-box</td>
    <td>默认值。如果你设置一个元素的宽为 100px，那么这个元素的内容区会有 100px 宽，并且任何边框和内边距的宽度都会被增加到最后绘制出来的元素宽度中。</td>
  </tr>
  <tr>
    <td> border-box</td>
    <td>告诉浏览器：你想要设置的边框和内边距的值是包含在 width 内的。也就是说，如果你将一个元素的 width 设为 100px，那么这 100px 会包含它的 border 和 padding，内容区的实际宽度是 width 减 去(border + padding) 的值。大多数情况下，这使得我们更容易地设定一个元素的宽高。<br>
<strong>注：</strong>border-box 不包含 margin。
</td>
  </tr>
  <tr>
    <td> inherit</td>
    <td>指定 box-sizing 属性的值，应该从父元素继承</td>
  </tr>
  </tbody></table>

总的来说，就是设置border和padding要不要算在width和height内。

## 常用textarea样式设置

```css
.text-area {
    overflow: auto;
    border: none; 
    padding: 10px 0px 10px 0px; 这样设置可以保留右边的滚动条
    margin-left: 10px;
    font-size: 16px;
    resize: none; 不能被用户调整大小（右下角拉动不了）
    outline: none; （取消默认的强调效果）
    text-wrap: nowrap; （不自动换行）
}
```

## px, em, rem的区别
https://www.runoob.com/w3cnote/px-em-rem-different.html

## TailwindCSS
https://www.tailwindcss.cn/



