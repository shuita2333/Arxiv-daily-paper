# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-509**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-509**

---

### 501. [Filtered Conformal Ellipsoids for Graph-Native Time Series](https://arxiv.org/abs/2606.17014)

**<font color=#1a73e8>作者：</font>** Yannick Limmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint prediction sets for multivariate time series should control a single event while adapting to cross-coordinate dependence. We study filtered conformal ellipsoids: a frozen state-space filter emits a one-step predictive mean and covariance, and split-conformal calibration is applied to the resulting Mahalanobis scores. The filter is used to choose the ellipsoid shape; conformal calibration chooses the scalar radius, so the construction benefits from a learned predictive covariance without relying on Gaussian tail probabilities for coverage. The main difficulty is that filtered scores are dependent and learned recurrent filters need not contract in their raw hidden state; we therefore analyse contraction in an observable predictive-law quotient that identifies hidden states producing the same future sequence of emitted Gaussian laws. Under a stable Bayes Gaussian-projection filter, covariance bounds, and a finite-horizon observability Fisher condition, small excess Gaussian negative log-likelihood implies contraction of the learned emitted laws. Combined with a threshold-autocovariance envelope this yields a Chebyshev-type approximate coverage bound for filtered split-conformal prediction under dependence; a sharper Bernstein-type bound requires an additional geometric-mixing concentration assumption. Under Gaussian oracle realisability we also obtain a near-oracle log-volume comparison within the class of conditionally valid Gaussian ellipsoid rules. We instantiate the framework with a GCN-GRU filter with diagonal-plus-low-rank covariance. On moderate-size graph-native traffic benchmarks (METRLA-$20$ and PEMSBAY-$50$), the learned filter gives sharper at-target ellipsoids than static-covariance and non-filter baselines; at full-graph scale and on non-graph-native datasets, factor and copula baselines can be stronger.

---


### 502. [MeshLoom: Feed-Forward Non-Rigid Registration of Mesh Sequences](https://arxiv.org/abs/2606.17027)

**<font color=#1a73e8>作者：</font>** Jianqi Chen, Jiraphon Yenphraphai, Xiangjun Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MeshLoom, a feed-forward registration network that directly reconstructs vertex deformations across mesh sequences. Our approach advances non-rigid registration beyond existing models, which are typically constrained by costly per-instance optimization, narrow object categories, pairwise-only inputs, or merely intermediate outputs. The network is simple and efficient, registering multiple meshes within seconds. At its core lies a topology-aware encoder--decoder design. Specifically, we first introduce a topology-aware point representation that encodes the anchor (reference) mesh's topology into its per-vertex features. This representation strengthens the network's understanding of the anchor-mesh geometry and disambiguates points that are Euclidean-close yet geodesically distant. We then propose a multi-modal encoder that fuses this anchor-mesh representation with complementary cues from each frame, such as shape latents and image features. These multi-source signals are compressed into a compact global motion embedding that captures dense inter-frame correspondence. A lightweight decoder then queries this global embedding with the anchor-mesh point representation, retrieving per-vertex deformations at target timestamps. Through extensive experiments across diverse motions and object categories, we show that MeshLoom achieves state-of-the-art results on non-rigid registration. In addition, we find that our global embedding-then-query paradigm naturally enables the network to generate deformations at intermediate timestamps, which extends MeshLoom to motion interpolation and mesh morphing. Project page: this https URL .

---


### 503. [HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting](https://arxiv.org/abs/2606.17028)

**<font color=#1a73e8>作者：</font>** Alper Yıldırım  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simple linear and frequency-domain models remain surprisingly competitive in long-horizon time-series forecasting, and recent mechanistic evidence suggests that standard forecasting benchmarks may not require the dense superposed representations that make transformers powerful in other domains. This raises a substrate-level question: if the core forecasting operator is often low-complexity and approximately linear, does it need to be implemented as learned digital temporal mixing? We introduce HAMON, a passive diffractive optical forecasting core in which historical values are encoded onto an optical aperture, future positions are left dark, and cascaded trainable phase masks with free-space diffraction shape the forecast directly in the output field. At inference, prediction is performed by a single passive optical propagation pass with no trainable digital sequence-mixing layer.
Across standard benchmarks, HAMON outperforms the strongest digital baselines considered on ETTm2 at all horizons and on ETTh2 at all but the longest horizon, improving MSE by up to 14\% and doing so consistently across horizons rather than at isolated points. It is competitive on Weather and trails the strongest baselines on the remaining ETT settings and on the high-channel-count Traffic and Electricity datasets. Phase encoding, intensity-compatible readout, and phase-scrambling ablations, together with a TorchOptics cross-simulator check, indicate that the forecasts arise from the data-bearing optical field rather than from a digital forecasting head. Because the passive core uses standard Fourier optics, HAMON defines a concrete target for optical hardware and for passive physical sequence mixing.

---


### 504. [DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/abs/2606.17029)

**<font color=#1a73e8>作者：</font>** Minghang Zhu, Chuyang Wei, Junhao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents synthesize long-form reports by searching and reasoning over retrieved evidence. Reinforcement learning with rubric-based rewards improves these agents by optimizing them against checkable criteria that translate report quality into reward signals, but its efficiency depends on whether those criteria reliably capture the task scope and evidence needs. Most existing studies ask an LLM to generate rubrics for a given query, but when the model fails to infer the underlying information needs, the generated rubrics may be incomplete and reduce RL efficiency. To obtain more reliable query--rubric supervision, we introduce DeepRubric, a data construction framework that reverses this process: instead of inferring evaluation criteria for a given query, it first determines what an evidence-backed report should be evaluated on and then synthesizes aligned query--rubric pairs from those evaluation targets. Starting from a sampled seed topic, DeepRubric builds an evidence tree by recursively expanding evidence-backed sub-questions, whose leaves serve as atomic and verifiable evaluation targets. It then uses the evidence tree to synthesize the training query and rubrics, ensuring that the reward evaluates exactly the information requested by the query. Using DeepRubric, we construct 9K query--rubric supervision examples and train DeepRubric-8B with rubric-based GRPO, achieving comparable performance to prior open state-of-the-art deep research models across three benchmarks with roughly 13x fewer RL GPU-hours.

---


### 505. [KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing](https://arxiv.org/abs/2606.17034)

**<font color=#1a73e8>作者：</font>** Mufei Li, Shikun Liu, Dongqi Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-hoc context erasing over the KV cache is challenging because a local edit has a global consequence: once a span has been processed, its influence propagates into the cached states of all subsequent tokens. This issue arises naturally in long-context LLM applications, where stale retrieved facts, incorrect tool observations, retracted user preferences, or harmful prompt injections may be identified only after prefill. Exact erasing must then recompute all tokens after the deleted span, making its computational cost depend on suffix length rather than erased-span length. We introduce KVEraser, a learned KV-cache editing method for efficient localized context erasing. Given a processed context and a span to remove, KVEraser replaces only the KV states of the erased interval with learned steering states while reusing the remaining cache unchanged. To learn a transferable erasing mechanism, we build a two-stage training pipeline: generic span-neighbor pre-training teaches the eraser to suppress the influence of the erased span, while task-specific fine-tuning adapts this capability to downstream scenarios. Experiments show that KVEraser nearly matches full recomputation in post-erasure performance on in-domain tasks across 1K--32K context lengths, while its latency increases by only 24% compared with a 17.6x increase for full recomputation. KVEraser also generalizes to unseen long-document QA tasks with harmful factual distractors, achieving the best performance among approximate baselines with a 3--4x speedup over full recomputation.

---


### 506. [Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning](https://arxiv.org/abs/2606.17035)

**<font color=#1a73e8>作者：</font>** Xiaolin Li, Ning Wang, Ninghui Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an empirical analysis of two baseline attack strategies, we uncover a fundamental tension in DP-FL: while bypassing DP allows state-of-the-art defenses to detect and filter malicious updates, complying with DP inadvertently masks their distinguishing statistical characteristics. Consequently, existing defenses become ineffective as DP reduces the raw backdoor signal. Building on this masking effect, we propose RING, a novel attack that explicitly exploits DP to conceal malicious contributions while maximizing attack impact. By collaboratively crafting adversarial perturbations, compromised clients reconstruct a strong backdoor signal during aggregation without triggering anomaly detection. RING operates as a perturbation layer that is agnostic to the underlying backdoor technique, making it broadly applicable and composable with existing attacks -- a property that significantly amplifies the threat it poses to DP-FL. Extensive evaluations across four image and text datasets under non-iid distributions show that RING achieves an average attack success rate of 90.3% against six state-of-the-art defenses under a moderate privacy budget, an improvement of up to 26.08x over baseline strategies. Finally, we evaluate potential countermeasures and find that mitigating this threat incurs significant utility trade-offs, exposing a fundamental security gap in the deployment of differentially private FL.

---


### 507. [The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers](https://arxiv.org/abs/2606.17037)

**<font color=#1a73e8>作者：</font>** Alper Yıldırım  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oppenheim and Lim (1981) showed that natural images stay recognizable when reconstructed from their Fourier phase alone, while the magnitude carries little of their identity. We ask whether trained image classifiers reproduce this asymmetry inside their hidden layers, and we test it causally: given two images, we transplant the phase of one onto the magnitude of the other at a chosen layer and record which image the prediction follows. In PRISM2D, GFNet, and ViT-B/16 the prediction follows the phase or sign donor, and deleting all image-specific magnitude barely moves accuracy, so identity rides on phase while image-specific magnitude is largely dispensable to the readout. ResNet-50 at first seems to break the pattern, because transplanting sign after its ReLUs does nothing; a fair intervention before the ReLU reveals a strong latent sign code in the late blocks, and a DC-only control shows the readout consumes a channel-wise spatial average. Controls rule out the trivial case in which magnitude simply stops depending on the image. The architectures therefore share a phase/sign identity code but expose it in different bases, set by rectification and readout geometry, which gives a mechanistic account of the texture--shape gap between CNNs and attention models.

---


### 508. [Exact Posterior Score Estimation for Solving Linear Inverse Problems](https://arxiv.org/abs/2606.17048)

**<font color=#1a73e8>作者：</font>** Abbas Mammadov, Ozgur Kara, Kaan Oktay 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. We derive the exact posterior score in closed form for linear Gaussian inverse problems under general Gaussian interpolants, and show that posterior sampling reduces to a denoising problem at an operator-dependent shifted pivot under an anisotropic noise covariance. We turn this identity into Exact Posterior Score (EPS), a denoising training objective that preserves the input/output structure of standard pretraining and can therefore be trained from scratch or fine-tuned from a pretrained denoiser. At inference, EPS uses the same sampler as the underlying backbone, with no likelihood gradients or projections. We evaluate EPS on five linear inverse problems across FFHQ and ImageNet, where it outperforms training-free and training-based baselines on fidelity, perceptual, and distributional metrics, while using roughly an order of magnitude fewer denoiser evaluations than gradient-based posterior samplers.

---


### 509. [BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering](https://arxiv.org/abs/2606.17049)

**<font color=#1a73e8>作者：</font>** Yi-Ruei Liu, Jie-Ying Lee, Zheng-Hui Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specifically, BRDFusion recovers explicit, consistent scene properties with physical modeling and alleviates optimization ambiguity with generative priors. During forward rendering, the physical model provides controllable rendering from the scene configuration, and the generative model denoises and fixes artifacts. Therefore, our method produces high-quality videos while allowing precise control, outperforming baselines in real and synthetic scenes. Moreover, BRDFusion supports novel-view relighting, night simulation, and dynamic object insertion/editing. Project page: this https URL

---


> [!TIP]
> 当前位于：**501-509**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-509**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
