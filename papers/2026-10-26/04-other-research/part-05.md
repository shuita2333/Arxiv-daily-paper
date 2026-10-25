# 📦 其他研究 | 2026年10月26日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-211**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-211**

---

### 201. [Efficient and Optimal Learning of Discrete Distributions with Person-Level Privacy](https://arxiv.org/abs/2610.31612)

**<font color=#1a73e8>作者：</font>** Gautam Kamath, Mahbod Majid, Ankur Moitra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning a discrete distribution under person-level differential privacy in the batched setting. Given $n$ users, each contributing $m$ i.i.d. samples from an unknown distribution $\mu$ over $[k]$, we seek an estimate of $\mu$ with total-variation error $\alpha$. We give polynomial-time algorithms under both pure and approximate differential privacy. Under pure $(\varepsilon,0)$-DP, we achieve $n = \widetilde O(k/(\alpha^2 m)+k/(\alpha\sqrt{m}\varepsilon)+k/\varepsilon)$, the first polynomial-time pure-DP guarantee matching the information-theoretic optimum up to logarithmic factors. Under approximate $(\varepsilon,\delta)$-DP, we achieve $n = \widetilde O(k/(\alpha^2 m)+k/(\alpha\sqrt{m}\varepsilon)+k+\log(1/\delta)/\varepsilon)$. At $\delta=2^{-\Theta(k)}$, this is $\widetilde O(k)$ for fixed $\alpha,\varepsilon,m$ and failure probability. Our algorithms use a new degree-6 sum-of-squares estimator for learning from untrusted batches. Its key ingredient is a trace-bounded diagonal majorizer for the difference between the empirical covariance of the repaired batch averages and the multinomial covariance predicted by their mean. We prove that clean data admit this certificate through semidefinite-programming duality and a new application of the stronger symmetric form of Grothendieck's inequality due to Friedland and Lim. The certificate preserves the mean-dependent variance of multinomial batch averages, yielding the near-optimal robust rate $O(\eta\sqrt{\log(1/\eta)/m})$ and providing the score required by the privacy reduction. We also prove a statistical query lower bound ruling out a uniformly smaller order of error under fixed polynomial SQ resource bounds.

---


### 202. [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](https://arxiv.org/abs/2610.31635)

**<font color=#1a73e8>作者：</font>** Zunnan Xu, Shangchen Zhou, Yihang Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level $\mathrm{Sim}(3)$ graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared $\mathrm{SE}(3)$ camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at this https URL.

---


### 203. [WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models](https://arxiv.org/abs/2610.31640)

**<font color=#1a73e8>作者：</font>** Chenxi Song, Yanming Yang, Tong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have learned rich 3D/4D priors, making them promising for scene generation and video re-rendering. However, their use in spatial tasks is limited by imprecise camera control, spatial and temporal inconsistencies, and entangled camera motion with scene dynamics. Existing approaches, such as task-specific fine-tuning and post-process warping, often introduce visual artifacts, generalize poorly, or incur high computational costs. We propose WorldForge V2 to achieve accurate camera control while preserving the generative capabilities of pretrained video models. We first develop a training-free guidance framework using warped references to iteratively refine generation along a target camera path. Optical-flow analysis identifies motion-related latent channels for selective guidance, helping separate motion control from appearance. A dual-path strategy further compares guided and unguided predictions to correct artifacts from imperfect references. Together, these components guide viewpoint changes while preserving scene appearance and object motion. To reduce refinement costs, v-cache approximates the correction using the preceding denoising prediction, avoiding an additional model evaluation. We further extend motion localization from latent channels to network blocks and introduce Trajectory LoRA, which concentrates adaptation on blocks most responsive to trajectory guidance. A two-stage training strategy teaches these adapters to denoise the states encountered during guided generation, using limited supervision effectively. This enables reliable camera control with very little training data, with a single training scene already supporting generalization to unseen scenes. Quantitative and qualitative evaluations across multiple datasets show that our method achieves state-of-the-art generation quality and trajectory accuracy in camera-controlled video generation.

---


### 204. [UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object Editing](https://arxiv.org/abs/2610.31641)

**<font color=#1a73e8>作者：</font>** Shuzhou Yang, Lanqing Guo, Lingen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object removal and injection are reciprocal editing operations between object-present and object-absent video states, yet they differ substantially in training difficulty. Removal can be effectively bootstrapped from video inpainting and further adapted to erase object-related interaction effects. Injection, however, requires large-scale paired supervision to model object appearance, dynamics, and scene-dependent effects, while perfectly aligned real-world pairs are difficult to collect and synthetic data lacks sufficient realism and diversity. To address this challenge, we present UniVOE, a removal-driven framework for training both video object removal and injection models. We first train an effect-aware remover by transferring video inpainting priors and finetuning on object-present/object-absent pairs. The trained remover converts real object-present videos into object-absent counterparts, creating large-scale paired supervision for injection. An injection model is trained on these pairs in the reverse direction to recover objects together with their dynamics and interaction effects. Moreover, since pixel-level reconstruction alone cannot adequately capture perceptual realism, we introduce a reward-based post-training method that aligns injection results with human preferences using a proprietary reward model. Experiments against strong open-source and commercial systems demonstrate that UniVOE achieves state-of-the-art performance on both object removal and injection, particularly in challenging interaction-effect cases.

---


### 205. [A Fix for Softmax and Cross-Entropy](https://arxiv.org/abs/2610.31642)

**<font color=#1a73e8>作者：</font>** Jonathan T. Barron, Dan Gnanapragasam, Michael Tschannen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard implementations of softmax, log-softmax, and cross-entropy have two numerical bugs. The first bug, Softmax Collapse, rounds the target logit's gradient to zero if that one logit is much larger than the others, resulting in gradients that no longer sum to zero. The second bug, Softmax Cancellation, occurs when student logits are close to teacher logits, and produces non-zero gradients even when the student and teacher logits are equal. We present simple implementations of log-softmax, softmax, and cross-entropy that fix both bugs. Our fix eliminates the previously-observed "Slingshot" phenomenon, speeds up grokking with weight decay, prevents accuracy collapse without weight decay, stops student networks from drifting away from the teacher during distillation, and shows that after memorization, logit growth is bounded by an equilibrium between weight decay and Adam's $\epsilon$ hyperparameter.

---


### 206. [GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution](https://arxiv.org/abs/2610.31644)

**<font color=#1a73e8>作者：</font>** Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimental evaluation focused on deploying LRs with gigapixel imagery. GigaBench includes images collected, acquired, and synthetically rendered across diverse domains, and addresses image compression and super-resolution. We adapt a representative set of LRs, spanning Implicit, Hybrid, and Explicit methods, so as to operate reliably at the gigapixel scale on consumer hardware. Through systematic evaluation across reconstruction quality, model size, compression and inference times, we identify consistent trends across methods and suggest actionable guidance for future investigation.

---


### 207. [OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields](https://arxiv.org/abs/2610.31645)

**<font color=#1a73e8>作者：</font>** Namitha Guruprasad, Abhay Yadav, Cheng Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera projection and its finer variations. We argue that camera geometry can be viewed as having a hierarchy of complexity for representing rays. We present OmniRay, a feed-forward model whose Ray Module is composed of three components: a monotone radial base that captures radially symmetric structure, a spherical-harmonic residual for smooth deviations from it, and a free-form residual for remaining local variation. These components are composed as successive rotations on the sphere, allowing the representation to accommodate diverse camera geometries. Given a single image, OmniRay predicts a ray direction and an up-to-scale radial distance for every pixel, from which a 3D point cloud is recovered without needing camera information at inference time. Extensive experiments across different camera configurations demonstrate that OmniRay establishes a new state-of-the-art in camera-agnostic monocular 3D reconstruction.

---


### 208. [METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656)

**<font color=#1a73e8>作者：</font>** Ali Najar, Hosein Hasani, Amir Kooshan Fattah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation with linear sequence complexity, while compact episode-level summaries support long-range cross-episode task inference without attending over the full interaction history. Moreover, equipping agents with neural memory provides sufficient expressive capacity and test-time training capability, enabling effective adaptation to unseen held-out tasks and task families at meta-test time. On unseen held-out Meta-World ML10/45 test environments, METTA achieves a success rate over $50\%$ while maintaining a low training budget and short wall-clock time. On long-context sparse-reward PointMaze tasks, it outperforms transformer-based baselines by exhibiting more structured exploration behavior. These results show that METTA provides an efficient path toward more adaptive and scalable long-context meta-RL.

---


### 209. [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659)

**<font color=#1a73e8>作者：</font>** Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary}$, which uses a smooth low-pass mask to blend a fixed canary image into every collection image while leaving captions unchanged and requiring neither auxiliary generation nor per-image optimization. A lightweight verifier detects the transferred signal in suspect-model outputs. Across eight tests on the Pokemon dataset and three realistic data transformations, spanning two architectures families, SpectralCanary achieves the highest average per-generation TPR@$1\%$ FPR ($91.1\%$) and fixed threshold model-level accuracy using 30 generations ($94.8\%$) among the evaluated methods. Across five datasets spanning artistic, medical, satellite, and fashion domains with SD3.5, SpectralCanary averages $92.4\%$ per-generation TPR@$1\%$ FPR while preserving the released images (SSIM $0.989$, LPIPS $0.022$) with a near-zero mean change FID (mean $\Delta$FID $0.05$) across datasets. Matched-energy ablations on Pokemon and ROCOv2 support our design choice, low-frequency placement transfers more reliably compared to mid/high-frequency placement. Under the evaluated adaptive attacks, the most effective removal requires aggressive modification and incurs more than $25$ $\Delta$FID points. These results identify low-frequency visual signals as effective carriers for collection-level T2I audit traces.

---


### 210. [Reading, Writing, Sharing, and Interacting with the World through Video](https://arxiv.org/abs/2610.31668)

**<font color=#1a73e8>作者：</font>** Shengqiong Wu, Meng Luo, Bobo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an observed video as a partial, lossy, and temporally ordered projection of a latent temporal world, we organize the literature around four complementary operations: reading infers world properties from observed video; writing synthesizes video from specified or learned world conditions; sharing integrates understanding and generation through common modeling mechanisms; and interacting predicts and updates world states under actions and evolving observations. This perspective distinguishes temporal coherence in observed or generated sequences from consistency in the underlying world state. Across tasks, representations, models, datasets, and benchmarks, we trace a shift in emphasis from clip-level recognition and perceptual fidelity toward persistent state, controllable evolution, physical and causal validity, and evaluation grounded in interaction and downstream decisions, and we distill the open challenges that follow.

---


### 211. [A Unified Framework for Image-to-3D Part Generation via Variable Granularity](https://arxiv.org/abs/2610.31671)

**<font color=#1a73e8>作者：</font>** Qiwen Gu, Xin Zhou, Xiwu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable 3D part generation is pivotal for digital asset creation, yet existing methods lack the flexibility to accommodate diverse user workflows requiring varying levels of control. In this paper, we introduce FlexPart, a unified image-to-3D part generation framework that supports variable-granularity geometric conditions within a single model. By seamlessly integrating heterogeneous inputs, ranging from sparse points to dense bounding boxes and masks, via gated adaptive modulation, FlexPart unlocks a powerful cross-modal synergy. We also propose an asymmetric geometric guidance mechanism that leverages strong spatial priors to align representations across granularities, improving geometric consistency and facilitating inter-task synergy. Under mask conditioning on PartVerseXL, FlexPart reduces Part CD by 16.6% relative to TripoSG + SAM3D and by 10.5% relative to OmniPart, while maintaining competitive whole-mesh quality. The code can be found at this https URL

---


> [!TIP]
> 当前位于：**201-211**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-211**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
