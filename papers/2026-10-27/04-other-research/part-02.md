# 📦 其他研究 | 2026年10月27日

> 本类共 **198** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-198](./part-04.md)

---

### 51. [RADIANT: Object-Centric Feed-Forward Global Illumination](https://arxiv.org/abs/2610.32075)

**<font color=#1a73e8>作者：</font>** Sarah Zhang, Zhiyang Dou, Minghao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward neural renderers synthesize global illumination across novel 3D scenes without per-scene optimization or runtime ray tracing. Existing transformer-based renderers tokenize individual triangles, so self-attention scales quadratically with mesh resolution. Yet macroscopic radiative transport is governed by the underlying surface geometry and object arrangements rather than a particular mesh discretization; finer tessellation can thus inflate token counts without changing the underlying transport physics, motivating a discretization-agnostic and object-centric representation. We introduce RADIANT (RADiance-based Inter-Actor Neural Transformer), an object-centric architecture for feed-forward global illumination from point inputs. By representing each object with a compact budget of 32 surface-patch tokens, RADIANT decouples attention sequence length from polygon counts. In a single network, an inter-object scene transformer models 3D radiative exchange and a view decoder renders images at target camera poses. To capture light transport without materializing O(N^2) bias matrices, invariant form-factor attention embeds geometric distances and surface orientations directly into query-key dot products as SE(3)-invariant inner products weighted by learned area and material gains. For primary visibility without mesh connectivity, camera rays cross-attend scene tokens guided by depth-tested point splats in a shared spherical frame. Across a 1.03M-scene benchmark under matched model capacity, RADIANT reaches 25 dB tone-mapped PSNR in 5x fewer training steps than RenderFormer, and achieves 32.2 dB at 600k steps (+3.3 dB over RenderFormer and +7.6 dB over RenderFormer-V2). We further demonstrate the scalability of RADIANT, which completes a 512x512 forward pass of a 500-object scene in 0.83 s, with computational cost scaling with the number of objects rather than polygons.

---


### 52. [Learning Nonlinear Waveform Fusion Across Scales for Integrated Sensing and Communication](https://arxiv.org/abs/2610.32099)

**<font color=#1a73e8>作者：</font>** Jiayu Liu, Kai Wan, Shuo Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fixed source superposition and frequency partitioning constrain how communication content interacts with a probing reference in integrated sensing and communication (ISAC). We learn nonlinear waveform fusion across scales for image transmission and localization of multiple targets in range and angle. Reception uses the information available at each end. Adaptive temporal feature weighting and spectral updates combine image features and a deterministic linearly frequency-modulated reference in a shared complex state, generating a waveform with fixed total energy over the array frame. At the user equipment (UE), the reference and channel state information condition a neural demixer for image reconstruction. At the base station, the realized transmit pulse defines a coherent dictionary for sequential localization with learned local correction, physical refinement, and residual updates. We compare the proposed waveforms with superposition in the time domain and learned spectral linear fusion on 512 independent test images, using a shared fixed UE receiver and a baseline sensing receiver using coherent peak search. Averaged across eleven task weights, the proposed waveforms reduce normalized localization error by 29.0\% and 27.0\%, respectively, while increasing mean peak signal-to-noise ratio by 1.40 and 0.82~dB. With the proposed waveforms fixed, learned local correction reduces mean normalized localization error by 12.2\% relative to the same sequential receiver without learned correction.

---


### 53. [Data Quality in RVL-CDIP: A Systematic Audit](https://arxiv.org/abs/2610.32126)

**<font color=#1a73e8>作者：</font>** Stefan Larson, Kevin Leach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RVL-CDIP is the de facto standard benchmark for document classification, and reported accuracy on it is now 98.8%. In this paper, we audit RVL-CDIP for data quality issues and find that approximately 10.5% of its 400,000 documents have erroneous labels and that 35.2% of the test set has a duplicate or near-duplicate in the training set. Identification codes on the pages are sufficient to classify at 69% accuracy, and a state-of-the-art model loses 11 points without them. Image-only models trained on RVL-CDIP lose 16 to 28 points on documents from other sources, and the choice of OCR engine changes accuracy by 4.1 to 8.3 points. We find that nearly 16,000 RVL-CDIP documents contain sensitive personal data, and produce de-identified versions of these documents. We re-benchmark 25 models, and with all defects remediated, the 13 that we retrain are 0.9 to 2.9 points more accurate than in the original condition; the most accurate of them, LayoutLMv3, is 96.5% accurate. We release the corrected corpus, the annotations and the out-of-distribution data.

---


### 54. [SyncPro: Synchronous Reasoning and Responding for Proactive Streaming Video Understanding](https://arxiv.org/abs/2610.32132)

**<font color=#1a73e8>作者：</font>** Xueyun Tian, Bingbing Xu, Jiaming Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive streaming video understanding requires assistants to track unfolding events and respond when a user's requested condition is met. To make these decisions, assistants must accumulate relevant evidence and reassess response conditions as new observations arrive. Existing work offers complementary capabilities for this process: proactive video assistants learn when to respond, while streaming video reasoning methods generate scheduled intermediate text to organize observations and support subsequent answers. Together, these capabilities provide a foundation for proactive reasoning, but how to coordinate ongoing reasoning with timely responses remains underexplored. In a direct adaptation, fixed reasoning intervals can trigger updates when nothing relevant has changed or postpone useful updates until the next scheduled step. Sharing one generation path also couples two distinct requirements: preserving evidence for future decisions and producing only the response requested by the user. Moreover, responses generated after reasoning must wait for it to finish, even when sufficient evidence is already available. To address these challenges, we introduce SyncPro, a synchronous dual-stream framework with specialized generation paths for evidence tracking and user-facing responses. Its Inner and Response branches share causal history and activate independently, allowing relevant evidence changes to trigger internal updates and responses to proceed concurrently with ongoing reasoning. We construct 189K dual-stream examples and train SyncPro through supervised fine-tuning followed by trajectory-level reinforcement learning. Experiments across three proactive benchmarks show improved response timing and more accurate answers to user requests.

---


### 55. [Sparsity-driven emergence of functional modularity in multitask neural networks](https://arxiv.org/abs/2610.32153)

**<font color=#1a73e8>作者：</font>** Bowen Shi, Qi Ouyang, Long Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks can learn multiple tasks, but how learning organizes shared computation into specialized and reusable components remains poorly understood. In this work, we show that sparsity inducing regularization promotes functional modularity in multitask networks without predefined module boundaries. Using functional profiling in multilayer perceptrons and a lightweight transformer, we identified compact, task-selective subnetworks, termed functional tokens. Across rule-based task families, selectively retaining these tokens preserves their associated functions while reducing performance on other tasks. Such specialization develops preferentially in deeper layers during training, while earlier layers retain shared computation. Regularization strength and form shape module compactness and specialization, while task weighting alters functional allocation. Moreover, extracted functional tokens can be recombined through alternative pathways to reconstruct a learned composite computation without retraining, preserving their connectivity and learned weights. Our results suggest that sparsity-constrained optimization shapes not only parameter use but also the organization and reuse of learned computation.

---


### 56. [Forging Emotions: a deep learning experiment on emotions and art](https://arxiv.org/abs/2610.32163)

**<font color=#1a73e8>作者：</font>** Amalia Foka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affective computing is an interdisciplinary field that studies computational methods that relate to or influence emotion. These methods have been applied to interactive media artworks, but they have focused on affect detection rather than affect generation. For affect generation, computationally creative methods need to be explored that have recently been driven by the use of Generative Adversarial Networks (GANs), a deep learning method. The experiment presented in this paper, Forging Emotions, explores the use of visual emotion datasets and the working processes of GANs for visual affect generation, that is, for generating images that can convey or trigger specified emotions. This experiment concludes that the methodology used so far by computer science researchers to build image datasets for describing high-level concepts such as emotions is insufficient and proposes utilizing emotional networks of associations according to psychology research. Forging Emotions also concludes that to generate affect visually, merely corresponding to basic psychology findings, such as bright or dark colours, does not seem adequate. Therefore, research efforts should aim to understand the structure of trained GANs and compositional GANs in order to produce genuinely novel compositions that can convey or trigger emotions through the subject matter of generated images.

---


### 57. [Present Drawing: Exploring Avatar-Mediated Drawing Events with Physical Traces](https://arxiv.org/abs/2610.32166)

**<font color=#1a73e8>作者：</font>** Kojiro Tanaka, Takuya Iwamoto, Yuki Okafuji  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce Present Drawing, an approach for staging an avatar-mediated drawing event that leaves physical traces in the real world. Present Drawing aims to reconfigure conventional drawing events by relaxing their physical constraints. We describe an organizer-oriented design space for such an event along four elements: Time, Site, Control Source, and Avatar Embodiment. To ground this concept, we developed a proof-of-concept prototype in which an observer wears a head-mounted display to view an avatar. The avatar's motion is synchronized with a customized pen plotter whose mechanical parts are hidden from the observer. We also developed five application examples spanning live, playback, multi-site, mascot, and system-controlled configurations. We conducted an initial evaluation of one representative playback autograph configuration, showing the basic plausibility of the core Present Drawing experience as an avatar-mediated drawing event and highlighting factors associated with perceiving the avatar as the drawer.

---


### 58. [Real-Time Localisation of Dorsal Anatomical Regions on Dairy Cows in Commercial Rotary Parlours from RGB-D](https://arxiv.org/abs/2610.32174)

**<font color=#1a73e8>作者：</font>** Vineet Prasad, Shiron Melvin, Sheikh Azid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated monitoring of dairy cows increasingly measures one part of the body, such as the rump for temperature or the back for posture, yet the region itself is usually placed by hand. Existing systems either score the cow as a whole or detect sparse keypoints, often in controlled walkways, and neither yields the named region masks that such measurements need on a crowded commercial rotary platform. We present a perception front end that finds the target cow, ten bony landmarks and four named dorsal regions (withers, back, rump and tail-head) in a single forward pass over a whole RGB-D frame from a commercial rotary parlour. Two encoders, one for colour and one for depth, are fused late and share one decoder with three heads. On an anatomical region dataset that we built on public rotary-parlour RGB-D images (538 annotated frames, cow-disjoint test set), the network reaches PCK@10 0.905 for landmarks and region IoU 0.70 to 0.91, and runs end to end in 26.4 ms per frame on a T4 GPU, against an 11 fps camera. Dense region supervision is what makes the landmarks accurate: removing the region head costs 0.15 PCK@10. Agreement between the two heads flags unreliable frames without labels. On our own rig at the largest dairy farm in Western Australia, the model transfers with ten labelled frames (PCK@10 0.84), and its regions are carried through depth into a radiometric thermal camera, giving one repeatable temperature per region and cow.

---


### 59. [Curvature-Aware Clipping: Mitigating Bias in DPSGD via Approximate Second-Order Information](https://arxiv.org/abs/2610.32175)

**<font color=#1a73e8>作者：</font>** Xincheng Xu, Thilina Ranbaduge, Thierry Rakotoarivelo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially Private Stochastic Gradient Descent (DPSGD) has become the de facto standard for training deep neural networks with rigorous privacy guarantees. However, the utility of DPSGD is constrained by gradient clipping bias and DP noise. While existing work has tried to address these issues, the geometric misalignment caused by clipping bias remains a critical challenge. To bridge this gap, we propose a novel framework, Curvature-Aware Differentially Private Stochastic Gradient Descent (CA-DPSGD), which leverages approximate second-order information to construct an optimal, curvature-aware clipping space. CA-DPSGD integrates a rectified estimator for the curvature matrix and is coupled with an anisotropic noise mechanism to ensure privacy guarantees. Extensive empirical experiments demonstrate that our approach outperforms state-of-the-art clipping methods.

---


### 60. [$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model](https://arxiv.org/abs/2610.32177)

**<font color=#1a73e8>作者：</font>** Khai Loong Aw, Klemen Kotar, Baihan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds. Achieving this flexibility is a major open challenge in AI: capabilities often remain separated across specialized models, limiting how they can be composed and jointly adapted to a task. We introduce $\Psi$-0.6, a unified vision-language world model that adaptively composes perception, language, geometry, and simulation within a shared reasoning process we call streams of thought. These streams interleave images, text, and explicit representations of geometry and motion, all of which the model can generate and interpret through a shared token interface. $\Psi$-0.6 surpasses leading open-weight models zero-shot on multi-view spatial reasoning, with further gains from reasoning through geometric intermediates. It also supports counterfactual simulation: generating and interpreting imagined scenes to determine, for example, whether moving an object would obstruct a pathway. Reinforcement learning from task feedback jointly optimizes the selection, generation, and use of intermediate representations, improving visual question-answering accuracy with gains that transfer to unseen benchmarks. $\Psi$-0.6 offers a path toward adaptive physical reasoning -- not only predicting the physical world but also choosing the representations through which to reason.

---


### 61. [Searching with Sparse Histories: Cross-Task Architecture Search from Incomplete Search Logs and Zero-Cost Proxies](https://arxiv.org/abs/2610.32179)

**<font color=#1a73e8>作者：</font>** Yuefeng Xu, Jun Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural architecture search (NAS) is expensive, but cross-task transfer can reduce costs by reusing knowledge from previous tasks. However, existing methods struggle with sparse search histories and task-specific transfer failures. We propose a method, a risk-robust strategy that combines sparse source logs with zero-cost proxies through champion-based initialization and joint pairwise-ranker pretraining. On TransNAS-Bench-101, the proposal mitigates severe worst-case failures, reducing worst-10% ranks from 290 to 43 for Micro autoencoding and from 465 to 45 for Macro room layout. Across 13 cell-space targets, it outperforms a proxy-only ranker on 10 targets in both mean and worst-case performance, while maintaining competitive average performance.

---


### 62. [CFBrainAug: Modularity-Induced Counterfactual Brain Network Augmentation for Interpretable fMRI-based Autism Diagnosis](https://arxiv.org/abs/2610.32184)

**<font color=#1a73e8>作者：</font>** Yifan Qiao, Sheng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning on resting-state functional magnetic resonance imaging (rs-fMRI) brain networks is promising for diagnosing Autism Spectrum Disorder (ASD), but existing methods are prone to overfitting on limited training data, and their post-hoc statistical attribution offers limited clinical interpretability. We propose CFBrainAug, a counterfactual brain network learning framework that unifies data augmentation and counterfactual explanation by learning label-altered brain networks. Unlike conventional label-preserving augmentation, CFBrainAug first retrieves a label-opposite yet topologically similar candidate and then refines it under a module-number constraint. Jointly training on factual and counterfactual networks enriches the training distribution around the decision boundary, enabling a lightweight feature-selection-based SVM to perform competitively with recent graph deep learning methods. Meanwhile, the counterfactuals provide intrinsic explanations by identifying the connectivity differences between each subject and its counterfactual. Experiments on the ABIDE I dataset show that CFBrainAug reaches an accuracy of 74.1% on the NYU site, suggesting that counterfactual augmentation can complement more complex models in small-sample brain network analysis.

---


### 63. [EVOLVE: Uncertainty-Aware Multivariate Time Series Anomaly Prediction with Adaptive Prototype Memories](https://arxiv.org/abs/2610.32189)

**<font color=#1a73e8>作者：</font>** Jianxin Jin, Kai Zhao, Shiyan Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised multivariate time series anomaly prediction (AP) aims to estimate future anomaly risks from current observations, providing early-warning signals for proactive intervention and maintenance in complex systems. Existing unsupervised AP methods follow a perturbation-based paradigm, where predefined or random perturbations are injected into historical windows to simulate abnormal future evolution. However, these methods share perturbations across different variables and contexts, and learn deterministic history-to-future evolution. In reality, anomaly evolution is variable- and context-dependent: the same perturbation may be amplified into abnormal future dynamics in one variable or context, while being absorbed as normal fluctuation in another. In addition, future evolution is not uniquely determined by a historical window, since similar histories may lead to multiple plausible trajectories, such as gradual degradation or abrupt changes. To address these problems, we propose EVOLVE, a unified framework that models unsupervised AP via variable- and context-conditioned perturbations and uncertainty-aware future reasoning. EVOLVE constructs context-specific anomaly perturbations through an adaptive anomaly prototype memory, which can dynamically update and retrieve relevant perturbations at the variable level. EVOLVE models uncertainty by sampling multiple latent historical states and decoding through complementary smooth and deviation-amplifying evolution hypotheses, and the disagreement among decoded future trajectories is used to estimate future anomaly risk. Extensive experiments on six real-world benchmark datasets demonstrate that EVOLVE consistently outperforms state-of-the-art anomaly prediction baselines.

---


### 64. [Markets of Minds: A 51-Billion-State Economy of Intelligence](https://arxiv.org/abs/2610.32190)

**<font color=#1a73e8>作者：</font>** Jusheng Zhang, Xuekun Wu, Wenhao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When intelligence is shared, reasoning becomes a constrained allocation problem. In a population of agents with limited access to expert models, an intervention can benefit its recipient yet still be a poor use of shared capacity if another feasible intervention has greater expected value. Assistance must therefore be evaluated through both its marginal benefit and the opportunity cost induced by budgets, access, scarcity, and service capacity. To this end, we introduce Markets of Minds, a framework for allocating expert reasoning across agents before expert outputs are observed. For each feasible agent-service pair, the framework estimates the expected gain from assistance relative to the agent's default continuation, explicitly separating repair benefit from regression risk, and jointly clears assistance contracts under shared resource constraints. We then study this problem in a dependency-aware agent economy with 51.2 billion addressable persona-market states spanning capabilities, cognitive budgets, provider access, scarcity, and network roles. These dependencies couple allocation feasibility across agents rather than the outcome of a fixed contract. Empirically, in a matched replay of 240 cases under a common 30% assistance quota, the frozen allocator reaches 85.42% task-level persona adherence versus 73.86% for equal-capacity random allocation, a gain of 11.56 percentage points. The results show that assistance value is heterogeneous and can be negative, and that scarcity changes which interventions are worth purchasing. Together, these findings motivate a population-level view of intelligence where the value of assistance depends not only on what it can achieve, but also on which alternative uses of scarce cognitive capacity it displaces.

---


### 65. [Dual-Adaptive Z-Score PPO: Dynamic Clipping Using Action Confidence and Normalized Advantage Magnitude](https://arxiv.org/abs/2610.32194)

**<font color=#1a73e8>作者：</font>** Taha M. Mahmoud, Naima Kaabouch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) remains a popular on-policy reinforcement learning algorithm owing to its stability and ease of implementation. Its clipping threshold, however, is fixed, so every training sample receives the same trust-region width regardless of how reliable the corresponding policy update is. This work examines adaptive-clipping variants of PPO in which the constant clipping parameter is replaced by sample-dependent thresholds computed from policy and return statistics. The central method, Dual-Adaptive Z-Score PPO (PPO-DAZ3), sets the clipping interval for each sample from two signals: action confidence, given by the probability of the selected action under the current policy, and update confidence, given by the normalized advantage magnitude. The rest of the standard PPO training pipeline is left unchanged. Evaluation on three classic control benchmarks (LunarLander-v3, CartPole-v1, and Acrobot-v1) indicates that adaptive clipping improves learning in some settings but not all. PPO-DAZ3 performs best on LunarLander-v3, the smooth advantage-based variant PPO-AZ3S leads on Acrobot-v1, and standard PPO stays competitive on CartPole-v1, suggesting that adaptive clipping is most beneficial on harder control tasks.

---


### 66. [DS-BiCA-Net: Pair-Preserving Cross-Temporal Modeling for Remote Sensing Change Captioning](https://arxiv.org/abs/2610.32200)

**<font color=#1a73e8>作者：</font>** Licheng Zhang, Naveed Akhtar, Siew-Kei Lam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image change captioning (RSICC) describes in natural language the semantic changes between two images of the same scene captured at different times. Previous methods commonly merge the pair during repeated processing or combine intra-image and cross-image relations in one operation, weakening source identity and leaving the two temporal directions implicit. Without separate modules for intra-image and cross-temporal processing and a separate path for each direction, the contribution of each part cannot be measured on its own, so it remains unclear which part matters most, and the design of later models has no such evidence to build on. To address these issues, we propose DS-BiCA-Net, which assigns the two kinds of processing to separate modules and keeps the two images as separate streams throughout the encoder. A windowed state-space module models context within each image, and a bidirectional cross-attention module compares the two images along two directed paths that share their projections. The two modules use the same pre-normalisation residual architecture and differ only in their mixers, and the two streams are fused only in the aggregation head, so each module and each direction can be removed and its contribution measured on its own. Controlled experiments on LEVIR-CC and Dubai-CC examine operator interaction, temporal direction and module order, showing that intra-image refinement carries no benefit alone and becomes beneficial only when followed by bidirectional cross-attention, an order that outperforms the reverse at matched parameter count and FLOPs. The bidirectional module also outperforms either temporal direction alone. Our method reaches an S_m^* of 82.65 on LEVIR-CC, the highest among the published results compared, and 66.72 on Dubai-CC without geometric augmentation, the second-highest among the published results compared.

---


### 67. [Neural Disjunctive Normal Forms for Learning Exact Rank Filters](https://arxiv.org/abs/2610.32203)

**<font color=#1a73e8>作者：</font>** Diego Marcondes, Wonder A. L. Alves, Ronaldo F. Hashimoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-based learning of morphological operators is hindered by locally sparse derivatives with respect to the structuring elements. We develop a method for learning rank filters that retains exact operator evaluation while distributing the derivatives across the window. Using threshold decomposition, we construct a neural disjunctive normal form representation and establish a sufficient condition for exactness with integer-valued images and structuring elements. We then derive a smooth surrogate from the unique root of a smooth threshold equation. Implicit differentiation gives closed-form derivatives with normalised local weights, whose distribution is controlled by a smoothing parameter. These derivatives are used in a straight-through procedure: the forward pass evaluates the exact rank filter, while the backward pass uses the surrogate. For fixed ranks, the procedure learns real-valued structuring elements of any rank filter, including the median, and extends to compositions, infima, and suprema of rank filters. Experiments on image denoising using MNIST and Fashion-MNIST and retinal vessel segmentation show that, starting from a generic random initialisation, the proposed approach consistently improves performance over training with exact subgradients in every setting. In image denoising, our best network also outperforms smooth morphological networks in all settings. On vessel segmentation, the learned erosions recover structuring elements that fit the vessels, as theoretically expected, whereas most of those trained with exact subgradients remain close to their initialisation.

---


### 68. [The 3DS Oracle: BIN Attack via the Network](https://arxiv.org/abs/2610.32206)

**<font color=#1a73e8>作者：</font>** Wasif Faisal, Suprava Saha Dibya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EMV 3-D Secure (3DS) requires a client-visible continuation boundary in browser-mediated flows; in some deployments, that boundary exposes a pre-authorization classification channel. This paper studies 3DS as a protocol, integration surface, and governance problem, combining standards analysis, architectural reconstruction, formal modeling, a documentation audit, disclosure history, and a bounded live evaluation. We show that client-visible integrations can reflect routing and authentication state before financial authorization, allowing 3DS to function as a profiling and screening channel for issuer controls and cardholder/account state rather than only as a defense. In the tested browser-channel Braintree/Cardinal path, the first client-visible result separated researcher-owned anchor cards from bounded adjacent same-range comparison PANs in six of seven distinct ACS/card-range cohorts; separate public evidence, including openly accessible attacker tooling, rotating-proxy support, and illicit paid 3DS card-testing services, shows that comparable signals are already operationalized in the wild. Our live study was deliberately bounded for ethical reasons, so the empirical ceiling reported here reflects researcher restraint rather than an attacker-side scalability limit, although we do not claim network-wide prevalence or candidate issuance. The deeper issue is systemic: decoupled pre-authorization authentication, weak requestor-boundary assumptions, identifier-linked routing invariants, and fragmented accountability let the exposure persist even when individual actors appear locally conformant. Meaningful remediation therefore requires consortium-level reform, including stricter minimization of client-visible pre-authorization responses, more uniform continuation behavior, and stronger client authenticity and session binding.

---


### 69. [Benchmarking Data-Free Continual Model Merging for Whole-Slide Image Survival Analysis](https://arxiv.org/abs/2610.32207)

**<font color=#1a73e8>作者：</font>** Vu Minh Tran, Doanh C. Bui, Maï K. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual survival analysis on whole-slide images (WSIs) requires models to integrate knowledge from sequentially arriving cancer cohorts while preserving previously learned information. Model merging offers a data-free alternative by combining independently fine-tuned task experts without retaining previous training data. However, the relative behavior of different merging strategies for WSI-based survival prediction remains insufficiently understood. In this work, we establish an end-to-end benchmark for data-free continual model merging, covering task-specific fine-tuning, sequential merging, and inference under both TASK-IL and CLASS-IL settings. We systematically evaluate six representative merging strategies across four TCGA cancer cohorts and three task orders using C-index, IPCW C-index, Forgetting, and Backward Transfer under a controlled protocol. Results show that no merging strategy consistently dominates across all evaluation criteria, while censoring-aware evaluation can substantially alter the relative ranking of the compared methods. This benchmark provides a unified foundation for developing and evaluating more effective continual model merging methods for WSI-based survival analysis.

---


### 70. [Tracing Money Laundering Across DeFi, Bridges, and Mixers on Ethereum](https://arxiv.org/abs/2610.32210)

**<font color=#1a73e8>作者：</font>** Huan Xing, Gaohe Jin, Bang Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Illicit actors exploit Ethereum's deep liquidity and diverse on-chain services to launder criminal proceeds by combining decentralized finance (DeFi) protocols, cross-chain bridges, and mixers in multi-stage processes. Existing anti-money laundering tracing methods fail to disentangle the underlying asset-flow paths in complex transactions, potentially misdirecting subsequent tracing; cannot identify cross-chain intent without pre-collected bridge information; and treat mixers as generic exit services, overlooking post-mixer laundering flows. We present FPTracer, a framework for tracing illicit assets across Ethereum services. First, we propose a method based on the Context-Aware Transfer Tree (CATT) to recover intra-transaction asset-flow paths, which guide accurate tracing and service analysis. Second, we extract discriminative features from asset-flow and execution-evidence perspectives and train a classifier to identify transactions with cross-chain intent. Third, we leverage evidence from the upstream laundering network to analyze potential post-mixer laundering activities. Evaluation on 20 real-world laundering cases demonstrates FPTracer's effectiveness. It achieves the highest recall for both known laundering addresses (98.6%) and destinations (94.2%). It identifies all known uses of bridges in these cases and uncovers 30 previously unreported ones. Among 18 cases with identified Tornado Cash usage, FPTracer can identify potential withdrawal-side activities, which are corroborated by public reports where available.

---


### 71. [DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation](https://arxiv.org/abs/2610.32214)

**<font color=#1a73e8>作者：</font>** Jeongsoo Choi, Junseok Ahn, Joon Son Chung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose DIAL-S2ST, a post-training method for learning inference-time latency control in simultaneous speech-to-speech translation models. Our approach reuses pretrained translation capabilities through self-distillation from lookahead predictions, while limiting the influence of large text distillation losses to account for the imitation gap. This provides supervision for earlier emission without paired target data or reward computation. To make the learned timing adjustable at inference, we jointly train a single LoRA adapter across scales with matched lookahead guidance. Experiments on French-to-English translation with Hibiki demonstrate that only 10 hours of source speech enable this adaptation, providing flexible latency control with a favorable quality-latency trade-off.

---


### 72. [ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences](https://arxiv.org/abs/2610.32222)

**<font color=#1a73e8>作者：</font>** Shibo Hong, Siyu Ren, FengJiao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matching optimization. Realizing this potential requires reward signals that reliably rank videos by both VQ and AF. However, existing rewards capture only one dimension: metric-based rewards assess VQ but require ground-truth videos and do not directly assess AF, while inverse dynamics model (IDM) rewards assess AF without references but do not guarantee VQ. Moreover, IDMs, typically trained on real videos, may provide unreliable rewards for generated videos containing visual artifacts and physical inconsistencies. In this work, we introduce the Action and Video Mismatch Benchmark (AVM-Eval), comprising 67.2k pairs that evaluate how reliably IDMs assess AF on real and generated videos. We then propose ACWM-RM, a reward model that jointly assesses VQ and AF without ground-truth videos during reward computation. To train it, we first construct the Action and Video Mismatch Preference Dataset (AVM-Pref) with 506.3k pairs providing complementary supervision: action-mismatch pairs supervise AF, while video-mismatch pairs supervise VQ and expose the model to generated videos. We then pretrain an action-conditioned predictor on real videos to learn forward dynamics before jointly training it with a patch-weighted score head on AVM-Pref to transfer these dynamics to AF assessment on generated videos. Evaluation on AVM-Eval reveals the limited reliability of IDMs on generated videos, while downstream RL experiments show that ACWM-RM outperforms reward baselines in both criteria.

---


### 73. [Towards Effective and Transferable Physical Camouflage against Multi-View BEV-based 3D Perception in Autonomous Driving](https://arxiv.org/abs/2610.32230)

**<font color=#1a73e8>作者：</font>** Linye Lyu, Jiawei Zhou, Daojing He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern autonomous driving systems widely adopt multi-view Bird's-Eye-View (BEV) based 3D perception models due to their superior performance. Despite their success, the robustness of these models against adversarial camouflage attacks remains largely unexplored. Existing camouflage attacks primarily target single-view 2D detectors, limiting their effectiveness in multi-view 3D perception settings. To address this gap, we propose BEVCA, a novel adversarial camouflage generation framework tailored for multi-view BEV-based 3D perception. Our framework integrates a BEV-feature-based adversarial loss with a multi-view neural rendering module, enabling effective and transferable camouflage attacks across different models and tasks. Extensive experiments in both digital and physical settings demonstrate that BEVCA outperforms state-of-the-art baselines and exhibits strong robustness under real-world conditions. Our code is available at this https URL.

---


### 74. [Virtual Placebo: a scoping review of control conditions in randomized controlled trials of psychological immersive virtual reality interventions](https://arxiv.org/abs/2610.32232)

**<font color=#1a73e8>作者：</font>** Madis Vasser, Mary-Ann Kubre, Kadi Tulver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research on immersive virtual reality (IVR) as a therapeutic tool is growing rapidly, with randomized controlled trials (RCTs) now commonplace. Yet the control conditions in many of these studies that claim strong specific IVR effects vary from usual care to active immersive experiences, making it difficult to draw clinically meaningful conclusions. We conducted a scoping review of recent literature on psychological IVR interventions to assess the main forms of control conditions used and their relations to study outcomes. In this paper, we make the case that most of the recent RCTs studying the effects of specific IVR interventions compare active immersive VR to usual care with no multimedia component. This can lead to strong yet potentially misleading study outcomes and can potentially inflate the IVR interventions' effect. Namely, the lack of an appropriate immersive control condition may risk misattributing general effects of VR devices to the specific content of the intervention. In this review, we discuss the implications of these design choices and propose strategies for including a suitable "virtual placebo" condition to improve the methodological rigor and interpretability of results.

---


### 75. [TileShare: Training-Free Acceleration of Overlapping Tiled ViT Decoding](https://arxiv.org/abs/2610.32233)

**<font color=#1a73e8>作者：</font>** Xiangzhong Ye, Zhongshen Li, Shen You 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fixed-window Vision Transformer (ViT) decoders run at deployment resolution as overlapping tiles: every token in an overlap band is processed by several full decoder instances. In the 2.4B-parameter MiniMax-H3 video decoder, about half of all per-token computation is duplicated. Removing the tiles fails because attention, global tokens and coordinates are bound to them. TileShare keeps each released tile's attention and computes every other operation once per token. The released computation changes at one kind of step only: an overlap token's per-tile results are blended into one shared state with the released weights. Interventions show that this blend costs quality where attention reads the shared states, mainly in the first few layers, which TileShare therefore keeps per tile. Without training, keeping six layers per tile decodes 1.38-1.51x faster than batched and compiled tiling on two GPU types (up to 1.96x with FP8) and is equivalent to the released decoder in PSNR, LPIPS and DISTS on DAVIS videos. On unseen UVG videos with the setting frozen beforehand, it matches PSNR and DISTS and improves LPIPS. TileShare carries over to two further decoders and is again confirmed on unseen data. It is equivalent in PSNR and DISTS on MAGI-1. On the ViTok-v2 image autoencoder at 2K-4K, it matches overlapping tiling in PSNR, improves LPIPS and DISTS and decodes 1.5-1.8x faster. How many layers stay per tile is measured once per model (for decoders, without labels); we report it for 14 decoders and encoders. Optionally, two GPU-hours of self-distillation let MiniMax-H3 share every layer without a loss in PSNR, and a coordinate field trained while the network stays frozen brings fully shared CLIP-based open-vocabulary segmentation to parity with sliding windows on seven benchmarks.

---


### 76. [Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading](https://arxiv.org/abs/2610.32237)

**<font color=#1a73e8>作者：</font>** Hrishikesh Singh, Aarti Sharma, Millie Pant  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In modern financial markets, more than 3/4th of the large volume trade is executed by algorithmic trading based on advanced trading strategies to attain higher precision and speed than traditional human traders. The conventional strategies focused on price-based indicators are inadequate in capturing the market dynamism arising from real-world events such as social sentiments, political instability, or sudden economic shifts. With the rise of Deep Reinforcement Learning (DRL) and data availability, there is a requirement for more efficient algorithms that can incorporate these external factors in trading strategies. DRL has shown potential in simulating real-world scenarios and in simplifying complex decision-making since DRL agents can automate the trading process i.e. executing trades in a manner comparable to human traders. They have shown reliable performance since they can update their policies based on risk and quantitative factors. In this paper, we propose a DRL approach based on partial and deep-infusion of sentimental analysis. It features distinct policy designs of actor-critic-based agents: only policy optimization (A2C & PPO) and policy optimization along with Q-learning principles (DDPG, TD3 & SAC). Our findings reveal, that the agents based on policy optimization combined with Q-learning, significantly and consistently demonstrate improved performance upon sentiment deep-infusion in profit maximization as well as risk-averse trading.

---


### 77. [Spatial Heuristic Strategy based Diffusion Reinforcement Learning for Online 3D Bin Packing](https://arxiv.org/abs/2610.32241)

**<font color=#1a73e8>作者：</font>** Tong Li, Qingyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional heuristic methods have accumulated mature experience in core objectives, such as space utilization and layout compactness of 3D bin packing, relying on artificially designed rule-based logic. However, they exhibit obvious limitations in generalization ability and adaptability to dynamic scenarios. Diffusion reinforcement learning, which integrates the spatial search capability of reinforcement learning and the data distribution modeling capability of diffusion learning, has achieved certain progress in action distribution modeling and decision compliance constraints. Nevertheless, there remain issues including insufficient perception of the spatial topological structure in 3D bin packing and limited layout optimization capability. To address these problems, we propose a diffusion reinforcement learning method integrated with spatial heuristic strategies, which combines classical bin packing heuristic rules with a diffusion reinforcement learning framework. Specifically, it compresses the action space through heuristic action pre-screening, introduces a graph neural network to model the spatial structure, and designs a composite reward function incorporating flatness to suppress spatial fragmentation, thereby realizing the organic integration of prior knowledge and adaptive optimization. Experimental results demonstrate that the pro

---


### 78. [Minimum Description Length Unsupervisedly Separates Law-Grade from Statistical-Grade Knowledge in a Self-Improving Science Agent - and Reveals 86% of Its Own Discoveries Are Statistical](https://arxiv.org/abs/2610.32245)

**<font color=#1a73e8>作者：</font>** Wenbin Mao, Pei Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems that discover scientific relations now generate candidate "laws" at scale, but the bottleneck has shifted from generation to vetting: which candidates deserve belief? We show that a deployed self-improving science agent - one that has admitted 252 relations through held-out prediction courts - already computes the quantity that answers this question: the Minimum Description Length compression ratio used for model selection doubles, when read under discrete accounting, as an unsupervised epistemic grader. The compression-ranked top band of the agent's ledger recovers exactly the canonical laws among its discoveries (vis-viva across seven planets, Balmer/Rydberg) plus cross-measurement identities - enrichment $p=3.6\times10^{-12}$ under a hypergeometric test - with zero counterexamples and physically coherent band structure. The same lens retroactively reveals that 86% of the ledger compresses nothing ($\mathrm{cr}\approx 1$): the agent had been recording statistical regularities, including a learned predictor with held-out $R^2=0.541$ admitted through the prediction gate, under a narrative of compression as the unified value of knowledge - a narrative that was never true for them. We formalize the resulting dual-axis bookkeeping - prediction value ($R^2$) and compression value (cr) as nearly decoupled axes of knowledge - demonstrate its robustness to quantization, and register forward falsifiable predictions. The episode is, to our knowledge, the first measured instance of a discovery agent auditing its own knowledge ledger by an internal measure and finding itself over-claiming.

---


### 79. [Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction](https://arxiv.org/abs/2610.32250)

**<font color=#1a73e8>作者：</font>** Ziang Zhang, Wenyou Yi, Zehan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D scene construction is a fundamental problem in 3D vision. Recent methods such as SAM-3Dfy enable end-to-end reconstruction of 3D assets and their scene layouts, but still struggle with fine-grained scene geometry and asset quality. Meanwhile, specialized 3D object generators provide detailed object geometry, while 3D foundation models offer strong and generalizable spatial understanding. We propose Easy-3Dfy, a compositional workflow that decouples object generation from scene layout estimation, allowing specialized models to fully exploit their respective strengths. An RPF-based aligner then bridges these capabilities by establishing geometric correspondence between object-local meshes and partial scene pointmaps, recovering object layout for scene composition. Without requiring complete scene-level supervision, the proposed workflow consistently outperforms SAM-3Dfy across multiple geometric metrics on Scene-Maker and 3D-FUTURE200. Our results demonstrate that explicit geometric composition can effectively combine high-quality object generation with strong spatial understanding, while enabling the workflow to benefit independently from advances in both 3D object generation and foundation models.

---


### 80. [RSIHub: A Composable Framework for Agent-Evolution Methods](https://arxiv.org/abs/2610.32253)

**<font color=#1a73e8>作者：</font>** Zimu Wang, Xiaobo Wang, Siyu Ye 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-evolution methods use execution feedback to improve prompts, skills, tools, and orchestration, but their implementations often rebuild the same experimental machinery. We present RSIHub, an open-source framework for building, comparing, and extending these methods on shared infrastructure. Recipes compose reusable operators and declare mutable resources; RSIHub supplies execution, evaluation, recovery, and lineage. Researchers can focus on evolution policy while evaluation stays outside the mutable surface and results remain tied to candidates and evaluation conditions. We instantiate AHE, Hyperagents, A-Evolve, and GEPA without modifying the framework core, keeping method-specific logic in recipes and operators. We evaluate them with MiniSWE and Codex on Terminal Bench 2 and $\tau^3$ Banking under fixed model and evaluator configurations. The largest observed overall pass@1 gain is 13.5 percentage points, while method rankings vary across settings and optimization gains do not always transfer to held-out tasks. RSIHub provides a common protocol for comparing evolution policies, inspectable candidate histories, and reusable components for developing new methods.

---


### 81. [Anti-coherence Regularized Absolute Scaling for Out-of-Distribution Detection](https://arxiv.org/abs/2610.32255)

**<font color=#1a73e8>作者：</font>** Donghwan Kim, Youngwoong Jin, Hyunsoo Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection is recognized as a critical problem in AI safety. SCALE is an effective post-hoc OOD detection method in the activation-shaping family that requires no training data and rescales penultimate activations using a percentile-based magnitude ratio. However, this ratio is ill-defined when negative activations are present, since positive and negative contributions cancel within the underlying sum, causing SCALE to degenerate on backbones such as ViT. We address this with an Absolute Fix that computes the ratio over absolute-valued activations rather than discarding negative activations through ReLU. Building on this corrected scale, we propose Anti-coherence regularization, which penalizes the scaling factor by the fraction of a sample's max-logit contributions to the max logit that are sign-mismatched and thereby suppresses unreliable evidence for the predicted class. Despite requiring no access to training data or training labels, our method ties or outperforms activation-shaping methods that rely on training data in terms of AUROC and FPR@95 on CIFAR-10 and ImageNet under the OpenOOD v1.5 protocol.

---


### 82. [Representation Learning via Composite Subspace Flow Matching](https://arxiv.org/abs/2610.32256)

**<font color=#1a73e8>作者：</font>** José Afonso, Mário Figueiredo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling semantic meaning from raw image data remains a challenge in machine learning. Current self-supervised paradigms face a trade-off: joint-embedding architectures produce relevant features by aggressively discarding intra-class variance, irreversibly spatial and reconstruction. Conversely, generative models preserve spatial details but struggle to isolate semantics, as their optimization is dominated by pixel variations. To bridge this divide, we propose composite subspace flow matching (CSFM). Rather than corrupting data with unstructured isotropic noise, CSFM formulates representation learning as the variance-minimizing inversion of a deterministic degradation curriculum across spectral, color, and illumination subspaces. By bounding trajectory variance with hard temporal style truncation, a capacity-constrained encoder is driven to ignore transient style artifacts and encode persistent content. Empirical evaluations across CIFAR-10, CIFAR-100, and STL-10 show that CSFM yields competitive discriminative transferability while preserving generative synthesis across both convolutional and vision transformer architectures. By avoiding the collapse pathologies of non-generative methods, CSFM forms a smooth latent space that outperforms standard optimal transport flows on linear probing and few-shot classification, while enabling coherent synthesis and trajectory interpolation. These results confirm that steering the physical dynamics of generative flows offers a scalable paradigm for learning representations that are simultaneously linearly separable and generatively invertible.

---


### 83. [Hyperparameter-Free Boundary-Interior t-vMF Dice Loss for Medical Image Segmentation](https://arxiv.org/abs/2610.32266)

**<font color=#1a73e8>作者：</font>** Hinako Mitsuoka, Kazuhiro Hotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class imbalance and errors near anatomical boundaries remain challenges in medical image segmentation, motivating loss functions that account for these difficulties. Adaptive t-vMF Dice Loss adjusts the similarity function during training but requires hyperparameter tuning. We propose Self-Tuned Boundary-Aware t-vMF Dice Loss (STB-tvMF Dice), which adapts the function separately for boundary and interior regions without tuning shape-adaptation parameters. Each region's shape parameter of t-vMF function is determined from its mean prediction-target cosine similarity in the preceding epoch and remains fixed throughout the current epoch. This rule maximizes the slope of the similarity function at the observed mean similarity, providing a principled basis for adaptation without validation-based parameter selection. Experiments on three datasets and architectures demonstrated its effectiveness. On Synapse with U-Net, STB-tvMF Dice achieved a mean DSC of 70.75%, compared with 63.03% for Adaptive t-vMF Dice Loss. Our code will be available soon.

---


### 84. [RootDown: Deploying and Benchmarking Models for Beet-Root Detection on Edge Devices](https://arxiv.org/abs/2610.32275)

**<font color=#1a73e8>作者：</font>** Gerardus Croonen, Andreas Trondl, Julia Simon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quality inspection of sugar beets after harvest and storage is critical to preserve sugar content and ensure optimal processing efficiency. The transfer of harvested beets to field clamps or trucks provides an opportunity to visually inspect individual beets automatically on loader conveyors. However, this is a challenging task as the large number of beets causes partial overlap and occlusion, complicating both annotation and detection. In this work, we propose an end-to-end image-based pipeline for detecting partially occluded sugar beets in loading scenarios as a first step toward automated quality inspection. We introduce a dedicated benchmark and present an automatic annotation strategy that leverages the SAM 3 foundation model to generate bounding boxes. We compare models trained on manually annotated and automatically generated labels. Additionally, we investigate deployment considerations by benchmarking multiple inference configurations, including execution on an edge device, under realistic operational constraints regarding precision, inference time and power consumption. Our results show that, despite substantial occlusion and inherent annotation ambiguity, foundation-model-based labels can substitute for a substantial share of manual annotation, trading labeling effort for data volume at a modest accuracy cost. Furthermore, we demonstrate that a Raspberry Pi 5 equipped with a Hailo accelerator enables high-performance, low-power inference, making it a practical solution for mobile outdoor deployment.

---


### 85. [Empirically Calibrated Differential Games for Simulating Driver Interactions](https://arxiv.org/abs/2610.32276)

**<font color=#1a73e8>作者：</font>** Amirmohammad Khakpour, Nachuan Li, Pedram Beigi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Game-theoretic models can resolve vehicle interactions without hand-written priority rules, but whether they describe human drivers once calibrated has rarely been tested. This study formulates a general-sum differential game of vehicle interactions at urban intersections, calibrates it to observed driving, and evaluates it on data not used for calibration. Each vehicle minimizes a cost that combines speed tracking, adherence to a map-derived lane route, control effort, gap keeping based on the intelligent driver model, a predictive conflict term, and a contact barrier, while perceiving the other vehicles with a delay. The game is solved with a feedback iterative linear-quadratic algorithm, and ten behavioral parameters per vehicle are calibrated by Bayesian optimization on trajectories recorded at four intersections in Washington, D.C. The calibrated game reproduces the trajectories of 819 vehicles with a mean position error of 1.00 m. When only each vehicle's route is known, as in a simulator, it is the most accurate of the compared models on 96 held-out vehicles (7.42 m), and ten-fold cross-validation shows that it is significantly more accurate than calibrated SUMO (by 3.61 m), an inverse reinforcement learning model (by 0.93 m), and independent and cooperative variants of the same model (by 0.33 and 0.32 m). The solutions, computed in 2.1 s for a typical interaction, are verified approximate equilibria. Finally, the conflict and steering weights, which the data do not identify, can be set from safety and comfort targets; together with a stiffer contact barrier, this removes the collisions that otherwise occur in 43% of tight closed-loop conflicts.

---


### 86. [Automated Post-Exploitation Attack Chain Exploration Based on a Phase-guided Hybrid Planning-Monte Carlo Tree Search Algorithm](https://arxiv.org/abs/2610.32278)

**<font color=#1a73e8>作者：</font>** Jie Ying, Mengce Zheng, Ruoxi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced attackers in post-exploitation scenarios increasingly craft attack chains that combine benign operations, configuration errors, and vulnerability exploitation to achieve objectives like privilege escalation. While such chains pose significant threats, manually discovering them in complex modern host environments is prohibitively labor-intensive. Automating this discovery is therefore essential for proactive defense, yet existing methods still suffer from inefficiency and lack diversity when exploring these attack chains. To address these limitations, we present APEX, an Automated Post-EXploitation attack chain exploration system. This system transforms attack chain discovery into a planning problem and solves it with a novel phase-guided hybrid Planning-Monte Carlo Tree Search (MCTS) algorithm. By organizing attack actions into semantic phases and integrating symbolic planning with MCTS, APEX enables efficient exploration of the state space while generating multiple diverse chains. Evaluations on a benchmark comprising 5 virtual machines, 30 synthetic problems and 291 cloud instances demonstrate that APEX successfully discovers both known and previously unreported attack chains--including 9 novel privilege escalation vectors--providing actionable intelligence for hardening complex production environments.

---


### 87. [Polyp-VSSD: A Pre-trained Transformer with Local-Global Joint VSSD Decoding for Polyp Segmentation](https://arxiv.org/abs/2610.32282)

**<font color=#1a73e8>作者：</font>** Xiaobo Zhu, Shiwei Wu, Yu An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection of colorectal polyps is essential for preventing colorectal cancer, making accurate polyp segmentation a key component in computer-aided diagnosis systems. However, existing endoscopic segmentation methods often exhibit limited representational capacity and insufficient integration of global and local contextual information. To address these limitations, we propose Polyp-VSSD, a novel local-global joint decoding framework built upon a pre-trained Transformer backbone for high-precision polyp segmentation. Polyp-VSSD leverages the strong feature expressiveness of large-scale visual pre-training and unifies global semantic modeling with local fine-grained reconstruction to enhance segmentation fidelity. Extensive experiments on multiple public endoscopic datasets demonstrate that our approach significantly outperforms state-of-the-art methods in both Dice and IoU. On the EndoScene dataset, Polyp-VSSD achieves mIoU and mDice scores of 0.903 and 0.946, respectively, highlighting its robustness and strong generalization capability. This work presents an effective and scalable solution for intelligent endoscopic image analysis.

---


### 88. [ReLEAP: Upcycling Vision Datasets through Cross-Task Unification and Semi-Supervised Annotation](https://arxiv.org/abs/2610.32289)

**<font color=#1a73e8>作者：</font>** Julia Simon, Daniel Steininger, Andreas Trondl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing robust vision models requires large amounts of annotated data, especially for tasks involving fine-grained class distinctions under variable environmental conditions. Even in domains with numerous existing datasets, differences in annotation formats, label definitions and targeted learning tasks hinder data reuse and integration. To address this challenge, we introduce ReLEAP, a scalable Python framework for unifying heterogeneous image datasets through data-source abstraction, systematic reuse of annotations across learning tasks, and mapping of labels to a shared hierarchical taxonomy. We demonstrate its applicability in precision agriculture by integrating fifteen diverse datasets covering a broad range of plant species and annotation types. Beyond unification, ReLEAP enables systematic recycling of existing data and provides a robust foundation for learning-based annotation upcycling. Leveraging this foundation, we conduct extensive cross-dataset and fine-tuning experiments to investigate how domain-specific models trained on unified data and foundation models can be used to automatically generate higher-level annotations under unsupervised, weakly supervised and semi-supervised settings, and how dataset characteristics influence their effectiveness. Our results show that unified data access and annotation upcycling substantially expand the pool of reusable training data and annotations while improving data transparency, enabling more sustainable and resource-efficient use of existing datasets. We release the framework and trained models for academic use to support accessible and collaborative research, particularly in data-scarce and heterogeneous domains.

---


### 89. [Complementing DINO Features with Image Structure for Part Discovery](https://arxiv.org/abs/2610.32293)

**<font color=#1a73e8>作者：</font>** Samyak Rawlekar, Nikhil Chowdary Paleti, Amey Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised Vision Transformers (ViTs) like DINO encode rich semantics, enabling training-free segmentation of objects from the background and discovery of their parts via feature clustering. This paper focuses on part discovery: partitioning a foreground object into semantic parts. Existing approaches produce imprecise part boundaries. We trace this to the rigid ViT patch grid used in training DINO, where patches straddling boundaries contain pixels from multiple parts. While DINO's invariance-based training could absorb this pixel-level mixing into clean features, experiments with over 26K foreground patches show it does not: boundary-overlapping patches produce features with higher entropy and lower assignment confidence, blurring predicted part boundaries. Rather than make the massive effort of retraining DINO over geometrically coherent regions, an easier approach is to take boundaries directly from a boundary detector, which supplies the geometric information DINO's features lack. Motivated by this, we introduce Part-DINO, a training-free framework that combines boundaries from low-level image segmentation with DINO's semantic features. We use the boundaries to partition the image into regions, pool DINO features within each region, and group them to discover parts. Without any training, Part-DINO produces structurally coherent part assignments, outperforming training-free baselines across four standard benchmarks (CUB, CelebA, PartImageNet-OOD, PartImageNet-Seg) and remaining competitive with weakly-supervised and unsupervised methods.

---


### 90. [OlmoEarth v1.3: Embeddings](https://arxiv.org/abs/2610.32294)

**<font color=#1a73e8>作者：</font>** Gabriel Tseng, Favyen Bastani, Patrick Alan Johnson 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We make some OlmoEarth embeddings. To do this, we train a new model: OlmoEarth v1.3. OlmoEarth v1.3 is designed to condense multimodal, multitemporal remote sensing data into a single digestible 64 or 128-dimensional vector. OlmoEarth v1.3 produces state-of-the-art embeddings. In addition, OlmoEarth v1.3 is a strong encoder backbone -- competitive with OlmoEarth v1 and v1.2 -- while requiring 18% and 53% of the GPU hours to train, respectively. We use OlmoEarth v1.3 to compute global, annualized 10m embeddings, which we release under the OlmoEarth artifact license.

---


### 91. [GeoLEON-CLIP: Graph-Anchored Multimodal Contrastive Learning for Geographic Region Representation](https://arxiv.org/abs/2610.32311)

**<font color=#1a73e8>作者：</font>** Radoslaw Malek, Szymon Soltysiak, Aleksandra Kawala-Sterniuk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geographic regions are multimodal: satellite imagery captures visual morphology, text conveys human-interpretable semantics, and map structures describe urban context. Existing geospatial contrastive methods typically align image-text or image-location pairs, underusing structured map data. We introduce GeoLEON-CLIP, a graph-anchored contrastive framework that aligns three views of each H3-indexed region: an OpenStreetMap-derived graph embedding, a satellite image crop, and a textual description. Frozen pretrained LEON graph embeddings provide a semantic anchor between vision and language. Frozen graph, image, and text encoders are connected by trainable residual projection heads and trained with a symmetric tri-modal contrastive objective. Experiments show strong graph-image and graph-text alignment; graph-image retrieval achieves the best cross-modal performance in a mixed-resolution pool. To evaluate the anchoring hypothesis, we propose chained cross-modal recall $\mathrm{R}@A@B$, which routes retrieval through the graph modality and compares it with direct retrieval under a matched candidate budget. At $\mathrm{R}@1@1$, image$\rightarrow$graph$\rightarrow$text and text$\rightarrow$graph$\rightarrow$image outperform direct image-text retrieval by 4.8 and 4.4 points, respectively, despite using a single intermediate cell. Downstream probes show task-dependent gains, with the largest improvements on Airbnb and Beijing housing. These results indicate that OpenStreetMap graph structure can anchor multimodal representations combining maps, imagery, and language.

---


### 92. [SKG in Practice: OOD Generalization Cases Across FourDomains](https://arxiv.org/abs/2610.32314)

**<font color=#1a73e8>作者：</font>** Jian An, Chaoshi Wu, Xinpan Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents the engineering implementation methods of the SKG inference framework and provides complete case studies across four domains. Case 1, 2D Dissipative Mechanical System: OOD MSE is 1.69 to 4.12 times lower than the best neural baseline; the state-dependent metric yields a 10^8-order improvement under controlled conditions. Case 2, Target Detection Sim-to-Real: Real-machine mAP increases from 0.2564 to 0.4964 (+24.00 points, single-run experiment, 32 images, point estimate), and AP75 increases from 0.1736 to 0.5765 (+40.29 points), with no real-machine retraining required. Case 3, Sequence Modeling sine to square: OOD MSE is 0.0296 versus Transformer 0.0641 (mean of 5 seeds, p=0.024). Case 4, Molecular Dynamics MD17: ID@100 ADE is 0.0285 versus ESTAG 0.1467; OOD@100 is 0.0316 versus 0.1411 (single seed). For each case, we present the objective, applied SKG theory, parameter settings, baseline comparison protocol, data results, and sources of advantage. Following the cases, we provide the complete methodology: pre-validation, task invariant construction, three-stage training, residual training, and the four theorems and one proposition supporting these methods. This paper not only demonstrates effective configurations of SKG across four domains but also honestly reports the variance of single-run experiments, limitations of single-seed results, negative updates caused by parameterization mismatch, and practical experience of using engineering thresholds as diagnostic signals rather than hard constraints.

---


### 93. [Organizing Temporal Evidence in Hyperbolic Space for Video Moment Retrieval](https://arxiv.org/abs/2610.32317)

**<font color=#1a73e8>作者：</font>** Mengnan Liu, Sanping Zhou, Kun Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video moment retrieval aims to localize a query-relevant temporal segment in an untrimmed video. Existing methods typically perform video-text alignment in Euclidean space, where representations are embedded in a flat geometry. However, accurate moment localization requires organizing query-relevant evidence across multiple grounding states, where target regions, boundary transitions, and contextual distractors exhibit distinct temporal structures and relevance patterns. Such Euclidean representations lack an explicit geometry to jointly capture these relationships, motivating us to explore structured temporal evidence organization from a geometric perspective. Specifically, we propose Hyperbolic Temporal Evidence Organization (HTEO), a geometric framework that organizes query-aware temporal memory in hyperbolic space. HTEO maps temporal representations into a Poincaré ball and organizes temporal evidence through Radial Evidence Organization (REO) and Orthogonal Angular Refinement (OAR). REO adjusts temporal tokens' radial positions to encode the structural differences among temporal evidence, while OAR enhances query-conditioned semantic alignment through orthogonal rotation. The organized representation is then projected back to the Euclidean tangent space and injected into the decoder through a lightweight residual memory update, enabling hyperbolic geometric cues to be incorporated into standard Transformer decoders while preserving the original cross-modal memory. Furthermore, we introduce radial structure regularization and angular relevance supervision to explicitly guide temporal evidence organization and query-conditioned semantic alignment, respectively. Extensive experiments and analyses across multiple benchmarks demonstrate that HTEO improves temporal localization while providing an interpretable geometric organization of temporal evidence.

---


### 94. [DeformStruct: Deformable Structure Modeling for Point-Supervised Temporal Action Localization](https://arxiv.org/abs/2610.32321)

**<font color=#1a73e8>作者：</font>** Mengnan Liu, Sanping Zhou, Kun Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-supervised Temporal Action Localization (PTAL) aims to localize action instances using only a single annotated timestamp for each instance. Such sparse supervision offers limited guidance for modeling the structural organization of an action instance. Existing PTAL methods primarily infer action regions from classification responses, leaving the structural organization of multiple action-related parts within each instance insufficiently modeled. To address this problem, we propose DeformStruct, an instance-level deformable structure modeling framework for PTAL. DeformStruct progressively constructs the structure of each action instance through three stages. First, Structural Anchor Mining discovers multiple anchors from annotated points and action-responsive regions, providing structural nodes grounded in the current instance. Second, Deformable Part Alignment associates latent structural parts with these anchors through deformation-aware matching, allowing their temporal supports to adapt to instance-dependent variations. Third, Relational Structural Organization explicitly models the relative temporal relations among the aligned parts, forming a relational representation that characterizes how different action-related parts are organized together. Extensive experiments on THUMOS14, ActivityNet-v1.3, GTEA, and BEOID demonstrate consistent improvements in point-supervised temporal localization and validate the effectiveness of deformable structural modeling.

---


### 95. [From Visual Affinity to Learning Credit in Multimodal Reinforcement Learning](https://arxiv.org/abs/2610.32324)

**<font color=#1a73e8>作者：</font>** Yuhang Han, Dingning Liu, Yujie Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves multimodal reasoning, but uniformly assigning a single response-level advantage to all tokens overlooks the distinct roles of visual observations and subsequent reasoning. Visual affinity alone is insufficient: predictive states may align with both image and prompt-context representations, and upweighting valid visual observations can amplify their negative-advantage updates when later reasoning fails. To address this issue, we propose \textbf{Outcome-Conditioned Visual Credit (OVC)}, a plug-in framework that separates visual-association measurement from token-level credit assignment and is adaptable to policy-optimization methods with uniform response-level advantage allocation. Relative Visual Encoding constructs a context-relative visual coordinate by contrasting each predictive state's affinity to image and prompt-context representations. Outcome-conditioned Evidence Calibration combines this coordinate with uncertainty-scaled predictive features and calibrates their contributions to outcome-discriminative evidence through mean contrasts between positive- and negative-advantage responses, scaled by regularized within-side variation. Visual association thus informs credit through observed outcome differences rather than directly determining update priority. Normalized Credit Allocation conditions the calibrated evidence on the response's advantage sign to produce positive token weights with unit global mean. These detached weights preserve advantage signs while modulating individual token-gradient contributions. OVC reuses existing rollouts without auxiliary reward models, process annotations, or inference-time modules. Instantiated through GSPO-token, OVC retains sequence-level clipping and consistently improves six-benchmark mean accuracy over GSPO across three models, with gains of 1.86-2.39 percentage points.

---


### 96. [When to Trust Memory: Retrieval-Guided Probabilistic Spatiotemporal Forecasting under Distribution Shift](https://arxiv.org/abs/2610.32329)

**<font color=#1a73e8>作者：</font>** Haochen Lv, Jianhao Zhang, Zhichen Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal forecasting plays an important role in real-world applications, where probabilistic approaches provide uncertainty estimates for decision-making. Real-world systems are inherently non-stationary, leading to distribution shifts between training and test data. However, existing probabilistic methods mainly focus on modeling data distributions under standard settings, while distribution shift methods often handle such shifts in a coarse manner, failing to characterize shift degree and adapt prediction strategy accordingly. As a result, they often produce miscalibrated and unreliable forecasts. To address this issue, we propose REMIND, a retrieval-guided probabilistic framework for spatiotemporal forecasting under distribution shift. REMIND leverages retrieval to estimate how well current observation are supported by historical patterns, enabling adaptive prediction under different shift regimes. It employs spatiotemporal retrieval to construct a memory bank and introduces a dual branch architecture, combining a memory-calibrated probabilistic branch for mild shifts with a deviation-aware probabilistic branch for severe shifts. A shift-adaptive gate, guided by retrieval similarity and memory dispersion, balances the two branches according to shift degree. We further design a hierarchical Gaussian mixture to capture heterogeneous uncertainty over the dual branch predictions, and introduce a memory perturbation training scheme to improve generalization. Experiments on real-world datasets with distribution shifts demonstrate that REMIND consistently outperforms state-of-the-art methods in both forecasting accuracy and probabilistic prediction quality.

---


### 97. [Data-Efficient Backdoor Attacks on Code Models via Trigger-Neutralized Counterfactual Scoring](https://arxiv.org/abs/2610.32334)

**<font color=#1a73e8>作者：</font>** Yu-Yu Lee, Ming-Feng Tsai, Tomohiro Morikawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pre-trained code models are exposed to backdoor poisoning, in which crafted training samples make the model misbehave on a trigger. A capable attacker minimizes the number of such samples, since each adds cost and exposure and a lower poisoning rate leaves a smaller footprint for defenses. Which samples to poison therefore matters, but existing data-efficient selection methods target image classification, offer no scoring mechanism for autoregressive generation, and have not been studied on code. We propose Trigger-Neutralized Counterfactual Scoring (TNCS), which isolates a trigger's contribution to the target behavior by comparing the scoring model's output on a triggered input with its output on a trigger-neutralized counterfactual, covering classification and generation alike. TNCS attains higher attack success rates than the baselines at very low poisoning ratios, across three CodeXGLUE tasks and five trigger families, without degrading clean-task performance, and its margin grows as the ratio decreases. It is the only method effective on every trigger family, and its selected poison set transfers to mismatched victims.

---


### 98. [TENET: Time-point Encoding Network for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2610.32337)

**<font color=#1a73e8>作者：</font>** Dongchan Cho, Juwon Hwang, Keumyeong Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In unsupervised multivariate time series anomaly detection (MTSAD), local variation can inflate reconstruction and forecasting errors, making observation-space discrepancy an unreliable indicator of abnormal system behavior. Since latent-space scoring can mitigate this limitation, we reframe one-class MTSAD as current-point system-state compatibility estimation and propose TENET, the Time-point Encoding Network for Multivariate Time Series Anomaly Detection. We define the current-point system state as a latent representation of the target time point, constructed from variable-level temporal context in the input window. TENET constructs this state through a temporal layer that retrieves window context relative to the current point, encodes time with current-point-centered embeddings, and adaptively mixes the retrieved context with the current representation. With this design, TENET treats the input window not as the object to reconstruct, forecast, summarize, or score, but as context for constructing a latent representation evaluated with a fixed standard-normal negative log-likelihood score. Across benchmark datasets, TENET achieves state-of-the-art performance. Additional experiments further show that TENET remains effective under alternative one-class objectives and outperforms substitutions based on generic sequence encoders, suggesting that its advantage comes from decision-aligned representation construction rather than from a specialized scoring rule. These results indicate that one-class MTSAD can be strong when the latent representation is designed around the current time point.

---


### 99. [Optimal Multiclass Online Regret with Arbitrary Label Spaces](https://arxiv.org/abs/2610.32339)

**<font color=#1a73e8>作者：</font>** Sajad Ashkezari, Shai Ben-David  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We determine the optimal regret in agnostic multiclass online learning with arbitrary, possibly infinite, label spaces. For every hypothesis class of multiclass Littlestone dimension $d<\infty$, we prove a regret upper bound of $O(\min\{T,\sqrt{dT}\})$ over $T$ rounds, matching the known lower bound. This resolves a question of Hanneke et al. (2023) and extends the optimal binary regret bound of Alon et al. (2021). Our proof strengthens the one-sided expert cover of Hanneke et al. (2023) to a fractional cover. We combine this cover with a minimax reduction to a finite expert game, whose best-response rewards provide the disagreement bounds needed for chaining.

---


### 100. [Embedding Large PQC KEMs in IKEv2](https://arxiv.org/abs/2610.32356)

**<font color=#1a73e8>作者：</font>** Daniel Herzinger, Marco Thomas, Tobias Handirk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum key encapsulation mechanisms carry public keys far larger than the established VPN handshake protocol IKEv2 was designed for. At the same time, its initial exchange comprising the public keys cannot be fragmented. In response, the IETF discusses a range of protocol adjustments, yet these proposals have never been compared in terms of their performance and stability under identical conditions. We systematically screened the IETF document corpus for such proposals, added three of our own (one using forward error correction and two using IKEv2 with QUIC, namely QUIKE and QUIKE with a composite key exchange), identified two specification gaps in existing acknowledgment drafts, and implemented all eight on the same open-source codebase. Measurements across different bandwidths, latencies, and packet loss rates, and with ML-KEM, FrodoKEM, and Classic McEliece, total 126 500 handshakes in 1296 different configurations and show that no mechanism fully compensates for the effect of the key size on performance. For Classic McEliece, no approach handles challenging conditions acceptably. The approaches either congest the link or take up to nearly two minutes per handshake on average. For ML-KEM and FrodoKEM, there are two ways forward: building on already standardized extensions or delegating the transport. The former requires the larger implementation change and needs further optimization, such as acknowledgment mechanisms or error-correcting codes, but grants continuity and compatibility. The latter can use a composite key exchange to avoid these drawbacks and achieve a faster, more resilient handshake and leaner implementation, with QUIKE-composite offering the best overall performance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-198](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
