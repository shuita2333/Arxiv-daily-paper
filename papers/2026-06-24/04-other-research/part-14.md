# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**651-654**（第 14/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-654**

---

### 651. [IMAGIN-4D: Image-Guided Controllable Interaction Generation](https://arxiv.org/abs/2606.23675)

**<font color=#1a73e8>作者：</font>** Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints, controlling action semantics and object trajectories. However, these signals underspecify interaction: the same prompt and trajectory can produce different grasps, approach directions, body poses, object poses, contacts, and body-object layouts. We address this ambiguity with a reference image as a visual specification of the desired interaction snapshot. However, a single global image representation conflates distinct cues and conditions all frames on identical visual evidence. We therefore introduce IMAGIN-4D, a diffusion-based HOI generator that decomposes image conditioning spatio-temporally. For spatial conditioning, IMAGIN-4D extracts supervised interaction-state tokens for body pose, object pose, body-object contact, and spatial relationships at the depicted frame. For temporal conditioning, it computes frame-aware tokens by querying image patches per generated frame, allowing sequence segments to attend to different visual cues from the same image. To balance image, text, and waypoint cues, IMAGIN-4D uses role-aware conditioning: text, waypoints, and interaction-state tokens use separate AdaLN streams, while frame-aware visual tokens cross-attend with motion tokens. Since HOI motion datasets lack paired images, we build a synthetic motion-to-image rendering pipeline from FullBodyManipulation (FBM) and introduce an image-adherence metric to evaluate whether generated motions match the reference snapshot. Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine-grained interaction control over single-token and uniformly image-conditioned baselines while preserving waypoint-following and motion quality. Code and models will be released at this https URL.

---


### 652. [Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?](https://arxiv.org/abs/2606.23676)

**<font color=#1a73e8>作者：</font>** Dingzhi Yu, Hongyi Tao, Yuanyu Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AdamW is the de facto optimizer for training large language models (LLMs), yet the theory behind it still lives mostly in finite-variance regimes. This is increasingly unsatisfying, as empirical evidence indicates that stochastic gradient noise in LLM pretraining is typically heavy-tailed. Recent work shows that sign-based optimizers such as Lion and Muon achieve sharp heavy-tailed rates, and that AdaGrad can also converge under heavy-tailed noise. However, no rigorous convergence theory for AdamW has yet been established in this regime. Can AdamW converge under the same heavy-tailed assumptions, or does its second-moment accumulator create a genuine obstruction? We formulate this as an open problem, prove a positive weighted-metric benchmark, and give a corridor lower-bound mechanism showing how denominator memory can hide large gradients.

---


### 653. [Keep The Essentials: Efficient Reference Conditioned Generation via Token Dropping](https://arxiv.org/abs/2606.23682)

**<font color=#1a73e8>作者：</font>** Rishubh Parihar, Ayush Raina, R. Venkatesh Babu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based diffusion models enable highly controllable image generation by leveraging elements from input images to guide prompt-driven synthesis. However, these models are computationally expensive in runtime, and their cost scales severely with the number of input references. While the efficiency of diffusion models has been extensively studied in the context of prompt-driven generation, it remains largely under-explored in the realm of reference-based models. This setting presents unique challenges not addressed by methods focusing solely on generation. In particular, the wasteful representation of references as dense token grids offers significant opportunities for improvement. In this work, we present Sparse Context, a method for constructing sparse reference representations by retaining only a reduced subset of reference tokens. We observe that even without modifying the model, dropping a significant portion of reference tokens at inference time largely preserves its generation capabilities. To fully realize this potential, we fine-tune the model with random token dropping at varying ratios, encouraging robustness to partial reference representations. Crucially, this training strategy decouples the model from any specific token selection rule, allowing flexible control at inference time. At inference time, instead of random dropping, we apply task-aware token selection strategies that prioritize the most informative regions of the reference images, adapting the token budget to the input and task requirements. Extensive experiments show our method achieves a 4x increase in inference speed for multi-reference generation and an 2x for single reference generation. Importantly, this efficiency is achieved without compromising visual quality across both spatially-aligned editing and subject-driven generation.

---


### 654. [Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688)

**<font color=#1a73e8>作者：</font>** Yehonathan Litman, Xiaoxuan Ma, Manan Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic non-rigid objects from monocular video requires integrating visual cues from direct observations with data-driven priors over geometry and appearance. Prior approaches either learn to directly predict 4D representations from visual input or initialize a 3D representation that is subsequently deformed and refined based on video evidence. However, the former are constrained by the scarcity of 4D training data, while the latter leverage priors only for the initial reconstruction and rely solely on video supervision thereafter; neither handles complex in-the-wild scenarios with large deformations and occlusions well. We present Lift4D, a test-time optimization framework that addresses both limitations. First, we adapt an existing single-view 3D reconstruction model to yield temporally consistent per-frame predictions via causal latent conditioning, providing a coherent initialization for a deformable 3D Gaussian Splatting representation. We then ``sculpt'' this representation to match the input video through an occlusion-aware optimization that faithfully recovers visible surface details while completing unobserved regions using a view-conditioned diffusion prior. We demonstrate that Lift4D clearly improves over prior 4D reconstruction methods, particularly on challenging in-the-wild sequences with severe occlusions and non-rigid motion.

---


> [!TIP]
> 当前位于：**651-654**（第 14/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | **651-654**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
