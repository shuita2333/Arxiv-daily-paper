# 📦 其他研究 | 2026年07月24日

> 本类共 **192** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-192**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-192**

---

### 151. [Real-Time EEG Cap Electrode Detection for Guided Point-of-Care Placement](https://arxiv.org/abs/2607.20142)

**<font color=#1a73e8>作者：</font>** William Lehn-Schiøler, Mads Sverker Nilsson, Nicki Skafte Detlefsen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a two-stage vision system that detects EEG cap electrodes in a live webcam stream and validates their anatomical placement in real time. A single-class YOLO detector localises electrodes; a geometric stage assigns each detection to a named 10-20 role from facial landmarks. Evaluating under subject-disjoint leave-one-subject-out (LOSO) cross-validation across five subjects wearing the clinically-validated Small/Medium/Large caps, the detector attains mAP@.5 = 0.94 +/- 0.07 across five held-out folds (0.96 pooled). A dedicated leave-one-cap-out axis, holding out every frame of a cap regardless of subject, leaves Medium and Large mAP@.5 within 0.01 of LOSO (0.97, 0.97) while Small drops to 0.72 +/- 0.28, a gap confounded with subject familiarity rather than cap style. Geometric augmentation (rotation, perspective, mixup) improves in-plane-roll robustness and temporal-electrode recall at no inference cost, and a landmark-driven head crop extends the usable distance range, lifting mAP@.5 from 0.23 to 0.45 at 0.6 x apparent scale. A compact mobile-candidate backbone (YOLOv10n) keeps the detector at real-time throughput (19 FPS) on a commodity CPU at 640 px.

---


### 152. [Gotta Catch them all: the modes of Sycophancy](https://arxiv.org/abs/2607.20146)

**<font color=#1a73e8>作者：</font>** Shreyans Jain, Alexandra Yost, Amirali Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often align with users' beliefs at the expense of factual accuracy, a behavior known as sycophancy. Prior mechanistic studies largely treat sycophancy as a single behavioral dimension that can be uniformly amplified or suppressed. We challenge this assumption by analyzing three hypothesized modes of sycophancy across 948 social pressure situations. Although the modes produce highly similar outputs, with a text-only classifier achieving just 57.8 percent accuracy, their internal representations are perfectly linearly separable from layer 14 onward. We further find the modes emerge at different processing stages, rely on distinct attention circuitry, and fire strongest on different inputs. These results show that sycophancy is not a monolithic tendency, but a structured family of representationally and computationally distinct modes, motivating more precise measurement and intervention.

---


### 153. [Active Inference as a Convex Markov Decision Process](https://arxiv.org/abs/2607.20152)

**<font color=#1a73e8>作者：</font>** Nikola Milosevic, Nicolás Hinrichs, Nico Scherf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active Inference (AIF) frames adaptive behavior as the minimization of expected free energy (EFE), combining epistemic and pragmatic objectives within a single variational principle. We frame AIF as policy optimization and show that, for closed-loop control policies, EFE minimization can be formulated as a convex Markov decision process (MDP). In this formulation, the pragmatic terms are linear in the predictive state marginals and therefore equivalent to reward maximization in a latent MDP, while the epistemic value introduces a nonlinear component that distinguishes EFE minimization from standard reinforcement learning. This perspective further reveals the epistemic drive of active inference as a policy-dependent (performative) reward. We analyze finite-horizon, discounted, and average-reward formulations of EFE and derive a mirror descent (MD) algorithm that locally linearizes the objective around the current state marginals, yielding a policy-dependent reward that is compatible with actor-critic methods and dynamic programming. Finally, we argue that coupling world-model learning with policy optimization gives active inference the structure of performative reinforcement learning, providing a route toward grounding active inference within modern reinforcement learning and optimization theory, including convergence analysis and principled policy improvement guarantees.

---


### 154. [Local Stability and Gaussian Smoothing of Quantized Neural Networks](https://arxiv.org/abs/2607.20153)

**<font color=#1a73e8>作者：</font>** Sergey Salishev, Anton Makarov, Oleg Granichin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Gaussian averaging as a smooth surrogate for quantized neural models. Under bounded local oscillation, we derive a local dimension-dependent bound on |f-g|, linking Gaussian smoothing to the stability analysis of discontinuous networks. We compute closed-form Gaussian averages of the rectified linear unit (ReLU) and sign activation functions, and illustrate the mechanism on a high-dimensional binary perceptron, where layer-preactivation aggregation under an explicit quantization-noise surrogate yields the Gaussian envelope used in inference-side smoothing and training-side smooth surrogate gradients.

---


### 155. [SHFormer: Dynamic Spectral Filtering Convolutional Neural Network and High-pass Kernel Generation Transformer for Adaptive MRI Reconstruction](https://arxiv.org/abs/2607.20159)

**<font color=#1a73e8>作者：</font>** Sriprabha Ramanarayanan, Rahul G. S., Mohammad Al Fahim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention Mechanism (AM) selectively focuses on essential information for imaging tasks and captures relationships between distant pixel neighborhoods to compute feature representations. Accelerated MRI reconstruction benefits from AM, as the imaging process involves Fourier domain measurements that influence image representation non-locally. However, AM-based models are more adept at capturing low-frequency information with limited capacity for high-frequency representations, restricting models to smooth reconstruction. Additionally, AM-based models need mode-specific retraining for multimodal MRI data, as their knowledge is restricted to local contextual variations that may be inadequate to capture transferable features across heterogeneous domains. To address these challenges, we propose a neuromodulation-based discriminative multi-spectral AM for scalable MRI reconstruction that can (i) propagate context-aware high-frequency details for high-quality reconstruction, and (ii) capture features reusable across deviated unseen domains in multimodal MRI. The proposed network consists of a spectral filtering CNN to capture mode-specific transferable features and a dynamic high-pass kernel generation transformer focusing on high-frequency details. We evaluate our model on comparative studies in supervised and self-supervised learning, diffusion model-based training, closed-set and open-set generalization under heterogeneous MRI data, and interpretation-based analysis. Our method offers scalable, high-quality reconstruction with best improvement margins of ~1 dB in PSNR and ~0.01 in SSIM under unseen scenarios. Code: this https URL

---


### 156. [Self-organizing Architecture of Receptron Units: a Hardware-Aware Framework for Edge Intelligence](https://arxiv.org/abs/2607.20162)

**<font color=#1a73e8>作者：</font>** Stefano Radice, Ludovico Casaccia, Riccaro Emanuele Beccalli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing demand for intelligent processing at the edge of IoT networks is constrained by the severe computational and memory limitations of microcontroller units, which render impractical conventional deep learning approaches. We propose a neuromorphicinspired classifier based on the Receptron model, a single-unit architecture capable of implementing non-linearly separable decision boundaries, without resorting to multi-layer networks. The model is designed for direct deployment on mid-range MCUs, while supporting continuous on-device adaptation. Experimental evaluation on basic dataset benchmarks yields cross-validated accuracies compatible with standard machine learning method baselines. These results position the Receptron as a viable and interpretable alternative for resource-constrained neuromorphic edge systems operating in dynamic, non-stationary environments.

---


### 157. [Instance Hardness-Based Relevance for Imbalanced Regression](https://arxiv.org/abs/2607.20173)

**<font color=#1a73e8>作者：</font>** Vitor M. Leitao, Juscimara G. Avelino, George D. C. Cavalcanti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced regression problems arise when the target variable has an asymmetric distribution, resulting in underrepresented value ranges in the dataset. Traditional approaches for identifying rare instances rely on a relevance function that assigns higher importance to specific regions of the target distribution. However, the effectiveness of imbalance-aware learning methods depends strongly on how relevance is defined. In more complex scenarios, such as bimodal distributions, traditional relevance functions struggle to capture rarity, as they assign fixed relevance values based solely on target values, thereby compromising the distinction between truly rare and normal instances. To address these limitations, this study proposes an Instance Hardness-based relevance function (InHaR) for identifying rare instances in regression problems. Unlike traditional relevance functions, the proposed approach incorporates learning difficulty, allowing rarity to be inferred not only from the target distribution but also from the difficulty of instances for the learning algorithm. This property is particularly important in bimodal scenarios, where rarity cannot be accurately inferred from target values alone. Experimental results demonstrate that the InHaR correctly identifies rare regions under bimodal distributions and, when used to guide resampling strategies such as Random Oversampling (RO) and Gaussian Noise (GN), leads to significant improvements in predictive performance compared to traditional relevance-based approaches. The code, dataset, and further details about the proposed method are publicly available at this https URL.

---


### 158. [StreamHOI: Interaction-aware Temporal Memory Adaptation for Streaming HOI Video Generation](https://arxiv.org/abs/2607.20174)

**<font color=#1a73e8>作者：</font>** Zejing Rao, Haoxian Zhang, Xiaoqiang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing human--object interaction (HOI) video generation methods are largely limited to offline short-video generation with complex driving conditions, making them unsuitable for real-time interactive applications. We present \emph{StreamHOI}, a low-latency streaming framework for long-duration HOI video generation. Instead of converting heavily conditioned HOI pipelines into streaming systems, we study how an image-to-video streaming generator should organize historical memory to preserve interactions under bounded latency. We find that the standard sink-local memory design faces a trade-off in streaming HOI generation, and different transformer blocks show different historical-memory preferences for HOI regions and surrounding regions. To match memory composition with block behavior, StreamHOI performs offline HOI-aware block profiling and applies bias-guided memory-specialized training to adapt the generator to block-specific memory layouts. We further introduce a memory distance scaling module to strengthen long-range access to early interaction states. Extensive comparisons with both long-video baselines and recent HOI generation methods demonstrate that StreamHOI achieves strong interaction plausibility, object fidelity, human quality and efficiency, reaching 17.6 FPS with 0.75s first-chunk latency.

---


### 159. [PerceptDrive: Perception Prior World-Action Modeling with Adaptive Expert Routing for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.20175)

**<font color=#1a73e8>作者：</font>** Yushan Liu, Tianxiong Lv, Bohua Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen perception foundation models encode rich geometric, semantic, and dynamic knowledge. Yet narrow conditioning interfaces may attenuate task-relevant cues, while static fusion cannot adjust expert contributions to each scene. We cast this challenge as the prior-to-plan transfer problem and introduce PerceptDrive, a perception prior world-action modeling framework with adaptive expert routing. PerceptDrive feeds teacher-distilled priors from a frozen, driving-adapted provider and dense observation latents from a frozen self-supervised video encoder into a trainable expert-routed world-action model. Expert-specific query branches process these signals, while a prior-retention objective anchors each branch to its prior. A router predicts soft gates from a shared scene representation and combines the expert conditions before trajectory generation. During training, privileged rule-based sub-metric estimates for branch-specific trajectory drafts provide soft-gate distillation targets. The predicted action-free future latent conditions a flow-matching actor. At inference, privileged components are absent; with one front-facing camera, PerceptDrive generates one trajectory per planning step without test-time scoring, reranking, or search. Experiments show that PerceptDrive achieves state-of-the-art performance with 90.4 PDMS on NAVSIM v1 and 90.2 EPDMS on NAVSIM v2, outperforming existing methods. Ablations confirm complementary gains from prior retention and scene-conditioned routing, alongside differential reliance on the three priors. These results demonstrate that preserving and adaptively routing perception priors improves direct planning without test-time candidate selection.

---


### 160. [On Optimization Complexity of Second-Order Certified Unlearning](https://arxiv.org/abs/2607.20192)

**<font color=#1a73e8>作者：</font>** Nikita Doikov, Anastasia Koloskova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study machine unlearning: the removal of memorized training data from a trained model. Specifically, we investigate the algorithmic complexity of certified unlearning from an optimization perspective. We formalize the goal of an unlearning algorithm as simultaneously achieving certified unlearning and optimization accuracy. Utilizing the notion of uniformly convex regularizers, we prove new bounds on the distance between initial and unlearned models using a novel substitute for generalization error. Thus we theoretically demonstrate that if the removed data is well-predicted by the unlearned model, the corresponding optimization problem is simple. Furthermore, we develop a new second-order unlearning algorithm with an anisotropic Gaussian mechanism and state-of-the-art global convergence. We prove fast rates for our method in achieving certified unlearning for linear models with quasi-self-concordant losses. As a direct application, our theory covers unlearning for logistic and exponential regressions and shows a provable benefit of utilizing second-order information compared to first-order unlearning methods.

---


### 161. [RS-RIE-Bench: Benchmarking Reasoning-Guided Remote Sensing Image Editing](https://arxiv.org/abs/2607.20197)

**<font color=#1a73e8>作者：</font>** Zihan Qin, Boao Xu, Zhao Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image editing aims to modify remote sensing images according to natural language instructions while preserving geographic rules and sensor observation characteristics. Existing benchmarks mainly target natural images or general visual scenes, and thus may not fully capture the reasoning, regional control, and sensor-consistency abilities required in remote sensing editing. To fill this gap, we introduce RS-RIE-Bench, the first benchmark for reasoning-guided remote sensing image editing. RS-RIE-Bench organizes tasks into three categories: temporal reasoning, causal reasoning, and spatial reasoning. These categories capture temporal evolution, causal consequence, and spatial imaging consistency in remote sensing scenes. The evaluation protocol covers three dimensions: target region plausibility, non-target region preservation, and image quality consistency. We further demonstrate the feasibility of MLLM-based evaluation through cross-judge consistency analysis and stratified expert review. Systematic evaluation on eight open-source and closed-source image editing models shows that current models still have clear limitations in reasoning-guided remote sensing editing. Even the strongest model achieves only 24.28\% overall accuracy under the strict joint-satisfaction criterion, while the mean relaxed joint-4 success rate across all eight models is 32.23\%. Causal reasoning and spatial reasoning remain especially challenging, and several open-source models are close to zero in some categories. These results show that RS-RIE-Bench can effectively reveal the limitations of current models in geographic reasoning, regional control, and sensor-consistent generation. It also provides a standardized benchmark and a clear research direction for future remote sensing intelligent editing models.

---


### 162. [The Quadrilateral Loss: Additivity as a Measurable Behavior of Dense Neural Networks](https://arxiv.org/abs/2607.20201)

**<font color=#1a73e8>作者：</font>** Antonio Di Cecco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Additive models buy interpretability by forbidding feature interactions, a constraint that neural instantiations enforce architecturally. We introduce the quadrilateral loss, a differentiable penalty that treats additivity as a measurable behavior instead: a second-order mixed difference on pairs of training points swapping one coordinate, which vanishes if and only if the coordinate carries no interaction, remains informative for piecewise-linear networks, and equals in expectation the per-coordinate interaction mass of the interventional Shapley-GAM. The loss turns additivity into a dial - most learned interactions prove removable almost for free, and on small datasets a moderate penalty improves accuracy and additivity simultaneously - and into an online observable: its per-feature surrender curves show, across seeds and datasets, that pre-regularization interaction magnitude barely predicts what a regularized model retains, undermining post-hoc interaction rankings. Against this instrument we compare routes to exact additivity, spanning structural masks, behavioral penalties (optionally crystallized into exact structure), weight decay, backfitting, the shared-section model, and bagged boosted stumps: constraining behavior before structure dominates weight-space constraints, rankings reverse between data regimes, and converging routes agree on the shape functions themselves. Three silent failure modes we document share one anatomy: guarantees imported into settings that quietly void their preconditions.

---


### 163. [surprisal is Not a Theory](https://arxiv.org/abs/2607.20208)

**<font color=#1a73e8>作者：</font>** Andrés Buxó-Lugo, Aniello De Santo, Morgan Grobol 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal Theory is often characterized as a computational-level explanation per (Marr, 1982). We argue in this work that, even though a computational level narrative has been used to support "representation-agnostic research" within computational psycholinguistics, the movement toward black box systems embodied by large language models (LLMs) does not exempt modelers using the surprisal metric from the representational decisions required by computational-level characterizations. In fact, we argue that the uncritical use of LLM-surprisal obfuscates the representational and algorithmic-level commitments of different models. In three analyses, we show that the choice of algorithm and model architecture play significant roles in the computation of language model probabilities. We advise that researchers who wish to test Surprisal Theory re-evaluate the practice of treating large language model probabilities as interchangeable

---


### 164. [ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers](https://arxiv.org/abs/2607.20214)

**<font color=#1a73e8>作者：</font>** Mahdi Heidari, Mohammad Mahdi Rahimi, Jaekyun Moon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic $N\times N$ attention score matrix remains a central obstacle to extending Transformers to longer input lengths. Existing efficient attention methods usually reduce this bottleneck by either imposing sparsity, so that each query attends to only a small subset of keys, or by using low-rank/kernel sketches, so that global interactions are compressed into a lower-dimensional representation. We propose \emph{ELSAA}, an efficient low-rank and sparse approximation of attention. Importantly, ELSAA does \emph{not} decompose the learned projection or output matrices of the Transformer into sparse and low-rank factors. Instead, after dense projections produce $Q,K,V$, ELSAA approximates the induced attention score operator itself: a sparse branch captures selected high-similarity interactions, while a low-rank branch summarizes diffuse global interactions. Since the two branches can be normalized over supports with very different denominator mass, ELSAA introduces a denominator-aware fusion term that scales the sparse branch according to its estimated attention mass relative to the low-rank branch. This gives a practical framework for constructing low-rank and sparse attention outputs without materializing the full quadratic score matrix, aiming to enable longer-context training while preserving both sharp token-level interactions and broad contextual mixing.

---


### 165. [User-Centric Modeling of Transactional Sequences with Explainable State Space Models](https://arxiv.org/abs/2607.20228)

**<font color=#1a73e8>作者：</font>** Ivan Palagin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a hybrid approach for user-centric modeling of transactional event sequences that combines contrastive representation learning (CoLES) with State Space Models (SSMs). While contrastive methods yield high-quality compressed user representations, existing encoders -- RNNs and Transformers -- suffer from vanishing gradients or quadratic complexity, respectively. Mamba, a selective SSM, efficiently handles long-range dependencies but remains underexplored for personalized user analysis. We investigate two integration strategies: (1)~initializing the Mamba hidden state with a CoLES embedding, and (2)~prepending the projected CoLES embedding as a prefix token to the input sequence. Both approaches supply the model with an informative user prior from the first step. Experiments on three public datasets -- Age (multiclass age-group prediction), MBD (multi-label product acquisition), and Taobao (binary purchase prediction) -- demonstrate consistent improvements over standalone Mamba and CoLES with a linear classifier, with the hybrid models converging 2--3$\times$ faster than the plain SSM baseline. Explainability analysis via discretization-step maps and Integrated Gradients reveals selective event filtering on behavior-rich datasets and identifies the most informative transaction features.

---


### 166. [PIER: Physics-Informed Environmental Retrieval for Time-Series Modeling](https://arxiv.org/abs/2607.20230)

**<font color=#1a73e8>作者：</font>** Shiyuan Luo, Runlong Yu, Chonghao Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of environmental systems is fundamental to scientific understanding and decision-making, yet remains challenging because observations are limited and physical dynamics vary across systems. Retrieval-augmented approaches offer a natural path to transfer knowledge across systems, but standard embedding-based retrieval does not guarantee consistency of underlying physical processes, since scenarios with similar embeddings may arise from different underlying mechanisms. We propose Physics-Informed Environmental Retrieval (PIER), a model-agnostic framework that augments embedding-based retrieval with a physics-aware stream that scores candidates by flux-response consistency with the target, using local verifiers trained on physics-derived flux features. A weight adjustment mechanism then learns per-scenario weights that adaptively balance the two retrieval streams based on diagnostic features summarizing physics-stream reliability. Experiments on 356 lakes across the Midwestern United States spanning 41 years show that PIER consistently outperforms baselines for water temperature and dissolved oxygen prediction, and serves as a general augmentation strategy across diverse backbones.

---


### 167. [PhaseAware: Interpretable Human-in-the-Loop Rehabilitation Scoring with Boundary Monitoring](https://arxiv.org/abs/2607.20237)

**<font color=#1a73e8>作者：</font>** Yankai Zheng, Yuhe Liu, Yuxin Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rehabilitation scoring systems are most useful when their outputs can be reviewed and interpreted within clinical workflows. This study presents PhaseAware, a compact framework for continuous rehabilitation quality assessment that combines a temporal backbone with phase- and body-group descriptors through a backbone-conditioned gated residual pathway. The model was evaluated on the UI-PRMD deep-squat protocol and further tested on the KIMORE squatting subset. On UI-PRMD, PhaseAware achieved an RMSE of 0.0230, corresponding to an 88.9% reduction relative to the accepted baseline. It also maintained favorable performance on KIMORE, suggesting that the phase-aware design transfers across related squatting protocols. In addition to score prediction, PhaseAware generates structured review cues based on phase- and body-level sensitivity, highlighting the movement stages and body regions most relevant to each prediction. The architecture employs a backbone-conditioned gated residual mechanism to stabilize feature representation, supporting use in resource-constrained settings. These cues are intended to support clinician review, boundary-case monitoring, and human-in-the-loop triage rather than autonomous decision-making. Overall, PhaseAware offers a practical and interpretable approach to rehabilitation scoring that may help integrate automated assessment into information systems while preserving clinician oversight.

---


### 168. [On the Systematic Challenges of Culturally Loaded Machine Translation: Dream of the Red Chamber as the Cultural Lens](https://arxiv.org/abs/2607.20241)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Jiayuan Di  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Culturally loaded translation poses unique challenges for machine translation (MT), as meanings are deeply embedded in socio-cultural contexts beyond surface linguistic forms. Although large language models (LLMs) have enabled MT systems to achieve human-like quality in many scenarios, their ability to handle culturally loaded expressions remains underexplored. In this study, we systematically investigate the challenges posed by culturally loaded translation in LLM-based MT systems. We construct a Chinese-Japanese bilingual dataset from the culturally representative corpus Dream of the Red Chamber, containing 500 segments across diverse cultural categories. Using a comprehensive evaluation protocol, we reveal three main challenges: (1) task challenges, where frontier LLMs exhibit notable performance gaps and struggle with culturally loaded content; (2) human evaluation challenges, where evaluator backgrounds lead to substantial disagreement in translation judgments; and (3) automatic evaluation challenges, where widely used metrics fail to reliably assess translation quality for this task. These findings may offer valuable insights for culture-oriented translation research in both computational science and linguistics.

---


### 169. [Vera: Identity-Faithful Human Subject-to-Video Generation](https://arxiv.org/abs/2607.20247)

**<font color=#1a73e8>作者：</font>** Yulong Xu, Xinyue Liu, Shujuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-to-video (S2V) generation has made substantial progress in preserving reference subjects across diverse categories, yet generic subject consistency remains insufficient for human-centric generation. A video may appear globally consistent while identity-critical human details still drift across frames, poses, and interactions. This issue becomes more severe in multi-person scenarios, where incorrect identity-role binding leads to subject confusion, attribute swapping, and excessive copying of reference-specific appearance cues. We propose Vera, a unified human-centric S2V framework for single- and multi-person generation. We first construct a million-pair identity-aligned human image-video dataset through person-level cross-clip retrieval, providing explicit identity correspondence and diverse references. Built on this dataset, Vera introduces two complementary designs. Identity-Focal Masked Supervision (IFMS) strengthens identity-aware learning with spatially focused supervision while reducing interference from irrelevant artifacts. Reference-Aware Layer-wise Attention (RALA) regulates how video tokens interact with reference identity cues in the DiT backbone, preserving stable identity anchors and enhancing layer-aware identity readout. Extensive experiments demonstrate that Vera improves human identity consistency, multi-person subject binding, and motion naturalness, while reducing identity confusion and excessive reference-image copying.

---


### 170. [The Ethics of Autonomous AI Agents for Offensive Security](https://arxiv.org/abs/2607.20255)

**<font color=#1a73e8>作者：</font>** Andreas Happe, Jürgen Cito, Jasmin Wachter  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-driven autonomous agents are reshaping offensive security. Unlike traditional penetration-testing tooling -- deterministic, narrowly scoped, and operated by trained practitioners -- agentic security tools exhibit \textit{indeterminacy} along three independent dimensions. First, their actions are drawn from a non-deterministic policy whose outputs resist both ex-ante and ex-post explanation, frustrating incident attribution and pre-deployment safety review. Second, their impact is open-ended due to the non-deterministic actions, agency of utilized models, and opaque LLM supply-chains. Third, their user population is indeterminate in both size and required skill: the operating skill floor for using or developing offensive capabilities has dropped sharply. These three properties are linked thematically, but are not derivable from one another. Combined with the structural cost asymmetry between offense and defense, they enable the industrialization of offensive capability. The net short-term effect favors attackers, even if the same technology may, in the long run, democratize access to defensive practice. Existing dual-use cybersecurity and AI-ethics frameworks were not designed for this combination. Our work analyzes how moral attribution becomes diffuse between users, tool-makers, and third parties when employing autonomous AI agents for offensive security. We also examine the stakeholder impact of this technology and provide stratified recommendations.

---


### 171. [Breaking the $T^{3/4}$ Barrier for Regret Minimization With Bi-Dimensional CDFs](https://arxiv.org/abs/2607.20258)

**<font color=#1a73e8>作者：</font>** Matteo Castiglioni, Anna Lunghi, Alberto Marchesi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study regret minimization for learning CDF-related objectives of the form \[ g(x)\cdot\mathbb{P}_{X\sim\mathcal{D}}(X\le x), \] over $[0,1]^2$, where $g$ is a known Lipschitz function and $\mathcal{D}$ is an unknown distribution. At each round $t$, the learner selects a point $x_t$ and observes the binary feedback $\mathbb{I}(X_t\le x_t)$, where $X_t\sim\mathcal{D}$. We design an algorithm achieving regret $\widetilde{\mathcal{O}}(T^{7/10})$, improving over the previous best-known bound of $\widetilde{\mathcal{O}}(T^{3/4})$ and showing that the curse of dimensionality can be at least partially lifted for this class of objectives, though a gap remains with the $\Omega(T^{2/3})$ lower bound. As an application, our techniques yield the same $\widetilde{\mathcal{O}}(T^{7/10})$ regret bound for profit maximization in repeated bilateral trade with fixed prices.

---


### 172. [How Does Urban Context Relate to Residential Building Health? A Vision-POI Fusion Framework for Building-Level Housing Inspection](https://arxiv.org/abs/2607.20263)

**<font color=#1a73e8>作者：</font>** Kun Zhao, Helei Ren, Guilin Tang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Housing-level urban physical examination is essential for identifying residential building problems and supporting targeted urban renewal. Existing automated inspection studies primarily rely on individual images and rarely examine whether surrounding urban functional context can provide supplementary information for building-level assessment. This study proposes a vision-POI fusion framework that combines multi-view visual inspection with POI-derived neighborhood context for residential building health assessment. The empirical dataset covers 92 old residential communities, 3,237 residential buildings, and 25,608 field-acquired inspection images in Qingdao, China, encompassing seven categories of housing-related issues. First, multiple object detection models are evaluated to extract issue locations, categories, and confidence scores from individual images. The image-level outputs are subsequently aggregated across multiple views to construct interpretable building-level representations. Second, POI features are extracted within 500m, 1,000m, and 1,500m neighborhood buffers to characterize surrounding functional environments. Pearson and Spearman correlation analyses, combined with false discovery rate correction, are used to identify candidate contextual features. Finally, visual and POI features are integrated using a cost-sensitive Random Forest classifier under community-isolated spatial cross-validation. The results show that multi-view aggregation provides the main performance improvement, increasing the building-level Macro-F1 from 60.84% under Direct Detection to 74.95%. Incorporating POI context further increases Macro-F1 to 76.79%, although the additional gain is modest and category-dependent. POI information therefore functions as a supplementary contextual prior rather than a substitute for direct visual evidence or a causal determinant of building condition.

---


### 173. [PoTRE: Test-Time Reasoning inspired by Cognitive Heterogeneity](https://arxiv.org/abs/2607.20268)

**<font color=#1a73e8>作者：</font>** Anmol Kankariya, Sercan Ö. Arık  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel at many tasks, they frequently struggle with complex reasoning that requires long-horizon planning and iterative error correction. Furthermore, standard single-stream prompting proves brittle when models encounter novel abstractions or rigorous domain constraints. We introduce PoTRE (Poly-Topological Reasoning Ensembles), a heterogeneous framework that decouples inference into four agents: (1) Adversarial Refinement Agent, (2) Hierarchical strategic Planning Agent, (3) Spectrum Search Agent, and (4) Direct Chain Agent. A final Task-Adaptive Aggregation Layer dynamically reconciles these perspectives -- via final candidate selection, semantic synthesis, or neuro-symbolic verification -- to produce a robust global solution. We evaluate PoTRE on three frontier benchmarks: ARC-AGI-2, Humanity's Last Exam (HLE), and PRBench Finance. PoTRE achieves state-of-the-art accuracy of 49.92% on HLE, surpassing the previous best official score. We demonstrate that this architectural heterogeneity achieves improved reasoning performance using similar or fewer inference tokens compared to heavily scaled homogeneous baselines.

---


### 174. [Interpretable Fuzzy Rule-Based Regression Extension for Ex-Fuzzy Library](https://arxiv.org/abs/2607.20277)

**<font color=#1a73e8>作者：</font>** Cayan Deniz Kucuktopana, Javier Fumanal-Idocin, Richard Pitts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models achieve high predictive accuracy in regression tasks, but their deployment in safety-critical and regulated domains requires interpretability. While fuzzy rule-based systems offer transparent, linguistically explicit interpretable models, Mamdani-style fuzzy regression remains underrepresented in modern machine learning software libraries. This paper presents an interpretable regression extension for the Ex-Fuzzy library, enabling Mamdani fuzzy inference with scalar consequents learned directly from data. For this, a target-aware partition initialisation strategy based on Fuzzy C-Means clustering is introduced, in which linguistic variables are derived from an augmented input-output space to emphasise output-relevant regions of the feature space. The proposed extension is evaluated on ten regression datasets from the KEEL repository, comparing Gaussian and trapezoidal partition strategies against standard baselines including linear regression, multilayer perceptron, and random forests. Experimental results show that Gaussian partitions consistently outperform uniform trapezoidal partitions, achieving a mean coefficient of determination of approximately 0.86 while producing compact rule bases of 10-15 human-readable rules. The proposed implementation provides a transparent and competitive alternative to black-box regression models, supporting practical interpretability with competitive predictive performance.

---


### 175. [Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation](https://arxiv.org/abs/2607.20280)

**<font color=#1a73e8>作者：</font>** Suleiman Muhammad Sabo, Hamed Alkharsh, Peilin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge Intelligence (EI) has emerged as a transformative model for mission-critical unmanned platforms, such as drone swarms, by enabling collaborative model training at the network periphery. However, the security of FL deployments depends on both network availability and robust client authentication mechanisms. This paper investigates a chained attack against drone-based FL systems that combines network-layer denial-of-service with credential-based impersonation. We demonstrate that an adversary can: (1) force legitimate drones offline using 802.11 deauthentication attacks, and (2) subsequently impersonate the disconnected drone using extracted credentials. Through a systematic literature review and empirical validation using the Flower framework on two distinct testbeds of Raspberry Pi and Jetsons, we quantify the impact of availability disruptions under Independent and Identically Distributed (IID) and Non-Independently and Identically Distributed (Non-IID) data distributions, and confirm that single-factor authentication permits post-disconnect impersonation. Our findings reveal that even short-term wireless interruptions cascade into substantial training instability, particularly under non-IID conditions, while the authentication gap enables adversaries to seamlessly replace disconnected nodes. We discuss the compounded implications for mission-critical drone deployments and outline directions for future defenses addressing both availability and authentication vulnerabilities.

---


### 176. [Diverse-Intent Multi-Turn Fashion Image Retrieval](https://arxiv.org/abs/2607.20291)

**<font color=#1a73e8>作者：</font>** Mingqiang Tang, Haokun Wen, Meng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world fashion search involves interactive retrieval across multiple turns. However, existing multi-turn retrieval methods are built on a restrictive assumption that every interaction follows the same attribute-editing paradigm, leaving heterogeneous intent transitions unexplored. Moreover, existing approaches often rely on textification to bridge multimodal queries and visual retrieval, which may lose fine-grained visual cues. To address these gaps, we introduce DIM-Fashion, a benchmark of 26K multi-turn sessions constructed from 13 fashion retrieval datasets across 7 tasks, featuring diverse intent transitions and rollback behaviors. We further propose FashionAM, an MLLM-VLP framework that directly aligns multimodal conversational queries with a fashion-oriented gallery embedding space, avoiding intermediate textification. Extensive experiments demonstrate the effectiveness of FashionAM over existing approaches. The dataset and code will be made publicly available upon acceptance.

---


### 177. [Evolving Cache Schedules for Fast Diffusion Policy Inference](https://arxiv.org/abs/2607.20293)

**<font color=#1a73e8>作者：</font>** Siying Wang, Kangye Ji, Di Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion policies achieve strong visuomotor control by iteratively denoising action chunks, but repeated denoising makes real-time deployment computationally demanding. Cache-based methods reduce inference cost by reusing intermediate activations, but existing training-free schedules typically allocate computation uniformly across blocks, ignoring heterogeneous redundancy across blocks and leading to a suboptimal performance-efficiency trade-off. To bridge this gap, we introduce Evolving Cache Schedules (EVO), a training-free acceleration framework that globally schedules cache refreshes via evolutionary search. EVO represents each candidate as a complete schedule over the block-timestep lattice. Thus, redundant transformer computations during iterative denoising can be skipped through cache reuse while preserving closed-loop rollout performance. To make the search practical, EVO introduces redundancy-aware initialization, which seeds the population with promising schedules, and target-conditioned early stopping, which verifies and terminates once a desired performance target is reached. The offline-optimized schedule can be directly plugged into pretrained diffusion policies without retraining. Extensive manipulation benchmarks show that EVO preserves near-full performance while substantially reducing computation, achieving up to 8.05x action-generation speedup and reducing FLOPs from 15.77G to as low as 1.96G. Source code is available at this https URL.

---


### 178. [Classical Hardware Acceleration of Quantum Autoencoders for Real-Time Anomaly Detection in Collider Experiments](https://arxiv.org/abs/2607.20302)

**<font color=#1a73e8>作者：</font>** Ivan Ge, Sagar Addepalli, Abhilasha Dave 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum machine learning (QML) algorithms in high energy physics (HEP) can efficiently represent and leverage long-range, high-order correlations in high-dimensional collider data, potentially with fewer parameters and favorable scaling relative to classical models. Deployment of QML in real-time collider applications such as trigger systems requires the ability to emulate and compile quantum circuits classically, then synthesize the resulting quantum gates onto low-latency hardware accelerators, namely field-programmable gate arrays (FPGAs). We present a study of variational quantum autoencoder models for real-time anomaly detection triggers in modern collider experiments. The models achieve performance comparable to state-of-the-art classical approaches and, after FPGA synthesis, satisfy resource usage and timing constraints consistent with trigger applications in future colliders. This work provides one of the first FPGA implementations of QML models for HEP triggers, enabling higher-capability models in today's classical data acquisition pipelines while advancing quantum readiness of collider experiment infrastructure.

---


### 179. [Constant-time decoding of Gabidulin codes and their generalizations with application to RQC](https://arxiv.org/abs/2607.20305)

**<font color=#1a73e8>作者：</font>** Nicolas Aragon, Chloé Baïsse, Anthony Fraga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gabidulin codes are a rank metric analog of Reed-Solomon codes. Although these codes are used in different very efficient rank-based cryptosystems like the RQC cryptosystem or the Loidreau cryptosystem, there was no constant-time implementation of Gabidulin codes, when having a constant-time implementation is crucial for real-life development of cryptosystems. In this paper, we propose the first constant-time decoding algorithm of Augmented Gabidulin (AG) codes, a simple variation on Gabidulin codes where one adds zero columns to Gabidulin codes, and which contains the case of Gabidulin codes. These AG codes are used in practice in the most efficient variations of the RQC cryptosystem. We prove that AG code decoding can be achieved with quadratic complexity. We further present a constant-time algorithm for the left division of $q$-polynomials along with a complete description of the AG code decoding procedure. These algorithms are integrated into the RQC-Block-MS-AG scheme, and we evaluate the performance of our implementation through benchmarks. Our results show that our implementation outperforms the original RQC, though it remains approximately four times slower than HQC. However, it achieves ciphertexts and key sizes about four times smaller, highlighting an appealing trade-off between performance and compactness.

---


### 180. [Multi-modal transformer for signal classification in nanopore blockade experiments](https://arxiv.org/abs/2607.20323)

**<font color=#1a73e8>作者：</font>** Sandro Kuppel, Julian Hoßbach, Samuel Tovey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nanopore devices have emerged as powerful tools for single-molecule sensing, with potential for rapid, portable diagnostics. They detect changes in ionic current as analytes enter nanometer-scale pores, providing a means of identifying diverse biomarkers from their characteristic signal patterns. However, these signals are highly complex, and reliably assigning them to specific molecules remains a major challenge. Here, we address this by introducing a multi-modal deep learning architecture that jointly processes multiple signal representations, including raw time-series data, wavelet-based images, and static feature vectors. Our approach surpasses existing methods by more than 10 percentage points on a 42-peptide benchmark and transfers to a 20-amino-acid dataset with near-perfect accuracy. The model integrates complementary information from these representations, with attention analysis showing that the time-series and wavelet-image inputs emphasize different features of the same event. Together, these results demonstrate the potential of machine learning to enable robust, high-accuracy molecular identification with nanopore sensors.

---


### 181. [Toward Reliable RGB-D Semantic Segmentation: Handling Missing Modalities via Condition Dropout](https://arxiv.org/abs/2607.20326)

**<font color=#1a73e8>作者：</font>** Xuchen Zhu, Yajuan Wei, Shuang Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-D semantic segmentation has achieved remarkable progress, yet most models assume that RGB and depth are always available. In practice, failures or occlusions of surveillance sensors often remove one modality. Although RGB or depth alone can contain sufficient cues, models trained only on full-modality inputs fail to exploit the remaining modality once one is missing, causing severe degradation. We tackle this issue with a simple continued-training paradigm, \emph{Condition Dropout (ConD)}, which mitigates degradation while preserving full-modality accuracy. Starting from a pretrained RGB-D model, ConD adds a second stage that randomly simulates complete, RGB-missing, and depth-missing inputs, freezes the original encoders, and trains copied encoders with zero-initialized feature injection. Experiments on NYU-Depth V2 and SUN RGB-D show that ConD improves robustness under missing modalities and even yields slight gains when modalities are complete. Our code will be made publicly available upon acceptance.

---


### 182. [Interval and fuzzy physics-augmented neural networks (iPANN and fPANN) for uncertainty quantification and propagation in constitutive modeling](https://arxiv.org/abs/2607.20339)

**<font color=#1a73e8>作者：</font>** Somesh Pratap Singh, Govinda Anantha Padmanabha, Jingye Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constitutive modeling under uncertainty remains a central challenge for reliable mechanics simulations, particularly when the available stress-deformation data are sparse, noisy, or heterogeneous. We propose interval and fuzzy physics-augmented neural networks (iPANNs and fPANNs) for uncertainty-aware hyperelastic constitutive modeling. iPANNs learn sparse lower, mean, and upper free energy density branches whose stresses, obtained by automatic differentiation, ultimately enclose noisy stress observations. In contrast to this deterministic interval description, fPANNs embed the learned iPANN branches into a fuzzy-set representation through alpha-cut interpolation, yielding a nested family of admissible responses. iPANNs and fPANNs encode mechanistic constraints - preserving objectivity, consistency and promoting polyconvexity - and smoothed L0 regularization promotes interpretable energy representations. The bound models are trained through a two-stage transfer-learning procedure in which a sparse mean constitutive response is learned first and then fine-tuned into lower and upper energy branches. We evaluate the framework on synthetic isotropic hyperelastic data with heteroscedastic noise, varying random realizations, shifted noise means, and varying noise magnitudes. The results show that the learned bounds enclose noisy stress observations while generalizing to the test set. Further, we examine the propagation of uncertainty through the mean, upper and lower bound predictions of the learned iPANN models in a finite element setting. The proposed framework provides a compact, physics-consistent route for distribution-free aleatoric uncertainty quantification in hyperelastic constitutive modeling, and propagation in downstream finite element simulations.

---


### 183. [Generative AI floods and dilutes the market for books](https://arxiv.org/abs/2607.20349)

**<font color=#1a73e8>作者：</font>** Tuhin Chakrabarty, Xinyue Liu, Jane C. Ginsburg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI can produce book-length works of fiction at near-zero cost. These books are often dismissed as low-quality ``slop'' that buyers will ignore, and are assumed to carry little commercial weight. We test that assumption with full-text AI detection across 14,419 self-published genre-fiction books sold on Amazon from 2023 to 2026, matched to daily sales records through June 2026. None of these books disclose whether or not they contain AI-produced content. We find that books for which we detected substantial AI text ($>$ 25\%) make up a large share of the catalog but a smaller share of sales. Even so, they reach commercial scale, winning a growing share of sales over time and taking more of the scarce top-rank positions once held by books with no detected AI text. Over this period, the number of books with observed sales in a quarter grew 19.2-fold, while quarterly revenue grew only 8.9-fold. The market therefore added selling books faster than it added revenue, and revenue per selling book fell across most genres. Books with no AI text lose the most ground in genres with high AI diffusion, and most of all where Kindle Unlimited availability is high. Among top-selling books, those with substantial AI text draw on more distinctive language from existing books than do books with no AI text; for these books overlap rises with revenue, a gradient we do not detect for books with no AI text. Generative AI can thus reshape a creative market through scale rather than quality. Our results bear directly on the market-effect question at the center of the fair use defense to copyright infringement.

---


### 184. [Variance-reduced Domain Adaptation using Paired Sampling](https://arxiv.org/abs/2607.20367)

**<font color=#1a73e8>作者：</font>** Andrea Napoli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Correlation alignment and the maximum mean discrepancy are two widely used distribution-matching frameworks for unsupervised domain adaptation (UDA). However, high variance in these losses has been shown to undermine their effectiveness in minibatch optimisation settings. Furthermore, the losses lack finite-sum structure, which renders them incompatible with classical stochastic variance reduction (SVR) methods. This paper proposes Paired Sampling for Domain Adaptation (PSDA), a novel SVR technique tailored to such objectives. PSDA pairs observations both within and across domains, to form quadruplets that are always sampled together during training. The pairings are designed to minimise expected gradient variance, and reduce to solving a set of linear assignment problems. Our simulations demonstrate reduced variance compared to related methods, and experiments on three domain shift datasets show improved target domain accuracy.

---


### 185. [Self Gradient Forcing: Native Long Video Extrapolation](https://arxiv.org/abs/2607.20368)

**<font color=#1a73e8>作者：</font>** Junhao Zhuang, Shiyi Zhang, Yuxuan Bian 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent autoregressive video diffusion methods are increasingly built upon Self Forcing, where the student is trained on histories produced by its own rollout rather than ground-truth video contexts. This reduces exposure bias, but the historical key-value cache is still used by future frames only as frozen rollout state. As a result, future losses cannot supervise how earlier generated latents should be written into more useful keys and values for later video-latent generation. We call this the historical context-gradient gap. We propose Self Gradient Forcing (SGF), a two-pass training strategy that restores this missing supervision signal without backpropagating through the full serial rollout. Pass 1 performs a no-gradient autoregressive rollout matching inference and, at a sampled denoising exit step, records both the self-generated context and the noisy latents fed to the model. Pass 2 performs parallel context-gradient reconstruction for the recorded exit step. The generated context is used as stop-gradient clean-latent input, while the model recomputes the context KV representations and future-to-context causal attention. Thus, SGF provides the missing memory-writing supervision within the native autoregressive training objective, using losses on future video latents to train the model to encode context into more effective causal memory. Across extensive long-horizon frame-wise and chunk-wise experiments under different initializations, SGF achieves stronger native long-video extrapolation than Self Forcing, especially in subject identity, background/layout consistency, and temporal stability. Remarkably, using only a 5-second training window, SGF can extrapolate to videos lasting several minutes. Code and models will be released to advance research on autoregressive video generation.

---


### 186. [Online Variance Reduction for Domain Adaptation on Streaming Data](https://arxiv.org/abs/2607.20374)

**<font color=#1a73e8>作者：</font>** Andrea Napoli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of stochastic variance reduction (SVR) for the maximum mean discrepancy (MMD) and correlation alignment (CORAL) loss functions. Although various offline SVR algorithms for these losses have been proposed, these are incompatible with online, distributed, or incremental learning settings. This paper presents Adaptive vaRiance Reduction via Online reWeighting (ARROW), the first online SVR algorithm for the MMD and CORAL for streamed data. The method maintains moving average references of the alignment statistics, and adaptively reweights incoming minibatches so that the minibatch and reference statistics are aligned. Further, we propose a relaxed reweighting scheme so that the ensuing weight-optimisation problem is tractable. In experiments and simulations, we show that ARROW performs competitively with offline algorithms in terms of runtime, degree of variance reduction achieved, and target domain accuracy.

---


### 187. [PG-KINN: A Physics-Informed Petrov-Galerkin Kolmogorov-Arnold Network for Solving Forward and Inverse PDEs](https://arxiv.org/abs/2607.20378)

**<font color=#1a73e8>作者：</font>** Amirhossein Sadr, Nima Soltani, Vahideh Moghtadaiee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed learning of partial differential equations (PDEs) has been dominated by multilayer perceptrons (MLPs), whose spectral bias and dense parameterization limit both accuracy and interpretability. Kolmogorov Arnold Networks (KANs) mitigate these limitations because their learnable spline activations are structurally aligned with the piecewise-polynomial bases of classical discretizations. However, the way a PDE is cast into a loss functional is as decisive as the choice of approximator: strong-form residual minimization requires high-order derivatives and heavily weighted losses, the energy (Bubnov-Galerkin) form is restricted to self-adjoint operators and, as we show, collapses to a trivial solution for parameter-identification problems, and boundary integral forms require a known fundamental solution. We propose PG-KINN, a physics-informed KAN built on a Petrov-Galerkin formulation in which the trial space is a KAN and the test space is an independent, compactly supported, piecewise-polynomial space evaluated with Gauss-Legendre quadrature. Integration by parts lowers the differentiation order while retaining applicability to general non-self-adjoint, nonlinear, and inverse problems; the localized test functions turn the global residual into a set of element-wise weak residuals with favorable conditioning. On a suite of benchmarks spanning crack singularities, stress concentration, Neo-Hookean hyperelasticity, inverse parameter identification in heterogeneous media, and complex geometries, PG-KINN consistently outperforms legacy MLP baselines and state-of-the-art KAN-based strong/energy/inverse formulations (PIKAN). These results position the Petrov-Galerkin coupling of KAN trial spaces and polynomial test spaces as a robust and accurate route for AI-based computational mechanics.

---


### 188. [Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations](https://arxiv.org/abs/2607.20379)

**<font color=#1a73e8>作者：</font>** Hiskias Dingeto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language autoencoders score explanations of hidden activations by reconstruction: an explanation is deemed faithful if the activation can be regenerated from it. The test is structurally insensitive to individual false claims: if flipping a claim does not change the reconstruction, the claim is never penalized. We show the test is passed in two ways, neither faithful. On a released Qwen-2.5-7B verbalizer, explanations reconstruct well above chance while ~2% of specific claims are reconstruction-dependent, so the score tracks gist, not specific facts. Under exact synthetic ground truth, the standard recipe develops co-adapted private codes (false wording the reconstruction depends on) in 5/5 runs, and fixes that leave the target model unchanged do not help. We contribute two audit protocols, the grounded-vs-true cross and the evaluator swap, and RECAP (Readable Encodings via Co-trained Auxiliary Predictors): linear heads trained alongside the target model to keep designated content decodable. On RECAP-trained sandbox models, fresh verbalizers state the designated content truly and the codes vanish, at a +0.001-nat cost. This replicates on a pretrained Pythia-160M: the content becomes reliably probe-decodable, though a fresh verbalizer conveys it only in part (truth 0.44-0.46 vs a near-zero control). For interpretability, high reconstruction does not certify individual claims. For AI safety, RECAP makes designated internal content independently checkable against probes rather than asserted by prose a model can game: an independent probe scores the verbalizer's true claims above its false ones (AUC 0.96, vs 0.82 without RECAP). Against an adversary that edits an explanation to maximize the reconstruction score while lying (suppressing ~87% of its lie penalty), the RECAP probe still flags the lies (AUC 0.95) while the control probe collapses to chance (0.51).

---


### 189. [FMRP-LEAN: A HIPAA-Compliant AI-Augmented LIMS Architecture for End-to-End Clinical Assay Workflow Optimization](https://arxiv.org/abs/2607.20382)

**<font color=#1a73e8>作者：</font>** Eva McCord, Ernest Pedapati, Zag ElSayed  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinical biomarker workflows in translational research settings often rely on spreadsheet-driven tracking, manual quality control (QC) reconciliation, and loosely integrated systems, resulting in limited state visibility, delayed reporting, and increased operational risk. These challenges are particularly pronounced in multi-day assays such as Luminex-based quantification of Fragile X Messenger Ribonucleoprotein (FMRP), where HIPAA-compliant data governance, deterministic workflow progression, and coordinated communication across laboratory and clinical teams are required. This paper presents FMRP-LEAN, a HIPAA-compliant, AI-augmented Laboratory Information Management System (LIMS) architecture that formalizes biospecimen lifecycle management through a finite-state workflow model with explicit transition guards and dwell-time observability. The system integrates a self-hosted Supabase/PostgreSQL stack deployed within hospital-controlled infrastructure, hybrid edge-internal isolation with encrypted tunneling and loopback-only services, and bi-directional REDCap synchronization. A unified MRN-UUIDv7 identifier framework with QR-based tracking ensures traceable clinical-research linkage under PHI residency constraints. FMRP-LEAN incorporates automated statistical QC pre-screening and a governance-constrained AI operations module that operates exclusively on aggregate projections, with deterministic fallback guarantees. Deployment demonstrates improved workflow observability, reduced QC latency, and enhanced cross-role transparency between laboratory technicians, research coordinators, and patient-facing teams. The architecture provides a reproducible model for secure, state-explicit, and AI-augmented clinical research workflows in regulated healthcare environments.

---


### 190. [Persian Pixel: A large-scale synthetic OCR dataset for Persian language](https://arxiv.org/abs/2607.20385)

**<font color=#1a73e8>作者：</font>** Pouria Mahdi, Haq Nawaz Malik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) for Persian remains substantially less mature than for Latin-script languages despite Persian being spoken by more than 110 million people across multiple countries. This gap arises from two fundamental challenges: the intrinsic complexity of the Perso-Arabic writing system and the limited availability of large-scale, high-quality annotated datasets. Persian script exhibits obligatory cursive connectivity, context-dependent glyph shaping, extensive ligatures, diacritic placement, and stylistic variation across writing forms such as Naskh and Nastaliq, all of which significantly complicate text recognition. At the same time, the high cost and labor-intensive nature of manual annotation have created a persistent data bottleneck, limiting the development of robust OCR systems and slowing progress in Persian document this http URL this paper, we introduce Persian Pixel, a comprehensive synthetic OCR dataset specifically designed to address these challenges. Comprising over 343,000 high-fidelity image text pairs, the dataset spans sentence, paragraph, and full-page document layouts generated from a carefully curated seven-million-word Persian corpus using the SynthOCR-Gen rendering framework. The generation pipeline faithfully models the typographic characteristics of Persian script, including contextual character joining, positional glyph variants, diacritic placement, and multiple representative Persian typefaces. To bridge the synthetic-to-real domain gap, the rendered images are further enriched with more than twenty-five stochastic degradation models that emulate realistic document acquisition artifacts, including ink bleed, paper aging, blur, illumination variation, scanner imperfections, compression artifacts, and multiple noise this http URL overcoming the long-standing scarcity of annotated Persian OCR data, Persian Pixel provides a scalable and openly available resource for training and fine-tuning modern OCR architectures, including transformer-based models such as TrOCR and Donut. The dataset establishes a strong foundation for research in Persian document analysis, historical manuscript digitization, and end-to-end document understanding, while demonstrating that programmatic synthetic data generation offers a practical, cost-effective, and scalable alternative to manual annotation for advancing OCR in low-resource and typographically complex scripts.

---


### 191. [SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data](https://arxiv.org/abs/2607.20402)

**<font color=#1a73e8>作者：</font>** Wael AbdAlmageed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In many reasoning problems, the premises are not observed as discrete symbols, but must be inferred from high-dimensional inputs. Further, the predicate vocabulary, argument structure, and trusted evidence are supplied by a Knowledge Graph (KG), or rule definitions. Classical neuro-symbolic pipelines have a discrete interface between perception and deduction. We present a neuro-soft-symbolic architecture for differentiable deductive reasoning over latent perceptual facts and knowledge-provided predicates. SoftReason removes the gradient gap by representing the deductive state as a local soft interpretation tensor over candidate constants and predicates. Perception proposes probabilistic base facts, KG triples enter as high-confidence soft evidence, and every query anchor, predicate choice, and closure update remains differentiable. Our core innovation is a learned differentiable lift of the immediate-consequence operator. It uses predicate-definition embeddings and latent composition channels to form soft body-predicate mixtures, aggregate over all possible witnesses, propose query-conditioned head facts, and update the interpretation through a monotone probabilistic OR. We instantiate the framework on Knowledge-aware Visual Question Answering (KVQA), and demonstrates how SoftReason supports end-to-end perceptual grounding, KG evidence injection, and differentiable deductive closure in one trainable architecture.

---


### 192. [ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion](https://arxiv.org/abs/2607.20417)

**<font color=#1a73e8>作者：</font>** Cho In, Jeonghwan Cho, Mijin Yoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves high-quality novel-view synthesis by optimizing freely placed primitives in 3D and adaptively densifying them in under-reconstructed regions. However, this scene-adaptive capacity allocation is largely lost in existing feed-forward 3DGS methods, which commonly regress Gaussians at input pixels and lift them along camera rays. Such pixel-aligned formulations make the number and placement of primitives depend on image resolution and input viewpoints rather than scene complexity, resulting in dense and often redundant Gaussian sets. We present ATSplat, a feed-forward 3DGS framework that restores the adaptive allocation capability of 3DGS optimization through Adaptive 3D Tokens. ATSplat first lifts coarse patch-level depth and camera cues into sparse 3D anchor tokens, forming a compact scaffold of the scene. Each token is then regressed into local Gaussians with learnable 3D offsets, decoupling primitive placement from input image grids. An Adaptive Token Expansion module predicts a token-level uncertainty score, supervised by rendering error maps, and selectively expands high-uncertainty tokens through learnable expansion layers. This sparse-to-adaptive formulation enables ATSplat to concentrate primitives in challenging regions while maintaining a compact representation. Experiments on two representative datasets, RealEstate10K and DL3DV, show that ATSplat achieves state-of-the-art rendering quality while reducing the number of Gaussians by more than $5.7\times$ compared with dense feed-forward 3DGS methods. From 12 input images at $512 \times 960$ resolution, ATSplat completes reconstruction in less than a second using a single commercial GPU, and renders high-quality novel views at 1136 FPS ($512 \times 960$) with only 311K Gaussians.

---


> [!TIP]
> 当前位于：**151-192**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-192**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
