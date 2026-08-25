# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 51. [Power-Performance Characterization of TinyML Systems](https://arxiv.org/abs/2608.21646)

**<font color=#1a73e8>作者：</font>** Yujie Zhang, Dhananjaya Wijerathne, Zhaoying Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TinyML systems are enabling machine learning (ML) inference at the edge. However, there is little quantitative analysis of such systems. This paper presents a systematic performance and power characterization of diverse TinyML applications on microcontrollers (MCUs), spanning neural network models, software libraries, operating systems, and hardware architectures. We focus on the impact of the multiple layers of abstraction that provide higher programmability at the expense of performance and energy efficiency. We propose a model to estimate the costs of different abstraction layers and make recommendations for minimizing those costs. Our findings can help designers with Neural Architecture Search (NAS) and CNN inference optimization on edge devices.

---


### 52. [GeoQ: Geometry-Aware Conditional Quantile Error Estimation for Scientific Surrogate Models](https://arxiv.org/abs/2608.21652)

**<font color=#1a73e8>作者：</font>** Khoa Nguyen, Daniel Serino, Aviral Prakash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural-network surrogate models are increasingly used to accelerate scientific simulations, but their deployment in extrapolative and autoregressive settings requires input-dependent estimates of prediction error. In this work, we introduce GeoQ (Geometry-Aware Conditional Quantile Error Estimation), a non-intrusive calibration framework for estimating surrogate error at individual query points. GeoQ represents the error at a query point as an anchor-averaged calibration error plus a learned nonnegative correction. This correction is modeled as an upper conditional quantile of the anchor-relative error increment, using geometry-based features that encode representation-space displacement and local support density. A cross-fitting procedure generates approximately out-of-sample calibration tuples, while a feature-space k-nearest-neighbor support score identifies regions \textcolor{black}{where the learned error model is supported by calibration data}. We evaluate GeoQ on scalar regression, chaotic dynamics, medium-range weather forecasting, and Richtmyer-Meshkov instability prediction. The results demonstrate that geometry-aware conditional quantile modeling provides a practical and non-intrusive approach for validity-aware error estimation in scientific surrogate models.

---


### 53. [Bounded Precision-Geometry Scaling for Robust Multi-Task Learning under Loss Scale Mismatch](https://arxiv.org/abs/2608.21653)

**<font color=#1a73e8>作者：</font>** Krishna Subedi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning often combines losses that span several orders of magnitude, causing homoscedastic uncertainty weighting to degrade severely. We propose Bounded Precision-Geometry Scaling (BPGS), a method that maps each task's log-variance through a bounded sigmoid parameterisation anchored to detached batch loss statistics, and decouples network optimisation from uncertainty optimisation. Its normalised task weights are provably invariant to uniform rescaling under non-degenerate loss scales. We evaluate BPGS on synthetic stress tests and three real-world benchmarks: NYUv2 dense prediction, Yeast multi-label classification, and RF1 multi-target regression. Under pure loss rescaling from $\times 1$ to $\times 1000$, its macro score changes from 0.777 to 0.778, whereas Kendall weighting drops from 0.780 to 0.637; $\ell_1$-normalising Kendall's weights does not close the gap. On NYUv2, BPGS records the lowest depth absolute relative error (0.223), depth RMSE (0.790), and total loss (1.891) among all compared methods, including Nash-MTL. Sensitivity studies on batch size and calibration show small variation across the tested ranges, and runtime overhead relative to Kendall is under 1%. BPGS posts the highest Yeast micro-F1 (0.616) and is competitive on RF1, though PCGrad leads RMSE and MAE there. These findings establish BPGS as a scale-robust alternative to homoscedastic uncertainty weighting, notably effective when loss-scale disparities dominate multi-task optimisation.

---


### 54. [SketchFlow: Zero-Shot Vector Sketch Generation via GMM Prior Flow in CLIP Latent Space](https://arxiv.org/abs/2608.21659)

**<font color=#1a73e8>作者：</font>** Jin Zhou, Hongliang Yang, Pengfei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector sketches remain one of the most concise and immediate mediums for abstract human expression. However, generating high-quality vector strokes that exhibit human-like drawing styles remains an open challenge due to the severe scarcity of fine-grained, high-quality text-to-sketch paired data. Existing text-conditioned generation methods often rely on unstable, time-consuming optimization or struggle to generalize to unseen categories in a zero-shot manner. To address these limitations, we present SketchFlow, a novel generative framework rooted in Optimal Transport (OT) theory and flow matching. By leveraging pre-trained CLIP models to bypass labor-intensive image-level text annotations, we formulate cross-modal alignment as a continuous mapping problem directly within the CLIP latent space. To bridge the inevitable modality gap between discrete text concepts and continuous sketch features, we first inject noise into discrete category embeddings to construct a continuous Gaussian Mixture Model (GMM) prior. We then utilize an Optimal Transport Conditional Flow Matching (OT-CFM) model to learn a deterministic vector field mapping from this continuous GMM prior to the target sketch feature distribution. Finally, a Hybrid Diffusion Decoder, fusing 1D U-Net and Transformer architectures, is designed to decode these features into fast and high-fidelity stroke trajectories. Extensive experiments demonstrate that SketchFlow substantially outperforms existing baselines in visual quality and adherence to natural human drawing styles. Furthermore, our geometry-preserving framework demonstrates promising local zero-shot synthesis for prompts beyond the QuickDraw training vocabulary, including unseen concept labels and semantic modifiers, while enabling smooth, continuous semantic interpolation between distinct concepts. Source code is available at: this https URL.

---


### 55. [Variational Structure at the Edge of Stability](https://arxiv.org/abs/2608.21660)

**<font color=#1a73e8>作者：</font>** Eric Regis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When discrete-time optimizers operate at the edge of stability, they exhibit near-two-periodic behavior. These oscillatory dynamics are reminiscent of conservative systems, such as the dynamics generated by symplectic integrators. However, a precise formulation of the connection between discrete-time optimizers at the edge of stability and discrete mechanics remains underexplored. Recently, Litman introduced the "edge coupling": a functional on consecutive gradient descent iterates whose critical points encode the fixed points and two-point orbits of the gradient descent dynamics. Here we extend the edge coupling to heavy-ball and Nesterov momentum. We show that its critical points characterize the fixed points and two-point orbits, with its Hessian characterizing their stability. We also show that the edge coupling can be identified with the symmetric Verlet action, formalizing the connection between the edge of stability and discrete mechanics.

---


### 56. [Who Bears the Cost of Honesty? A FAccT Workshop Synthesis and Research Agenda for Equitable AI Disclosure](https://arxiv.org/abs/2608.21671)

**<font color=#1a73e8>作者：</font>** Runlong Ye, Jessica He, Finola Finn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI disclosure is increasingly promoted and sometimes required as a route to transparency, accountability, provenance, and trust. Yet disclosure can also expose AI users to suspicion, stigma (e.g., competence penalties), and surveillance, affecting minoritized groups in particular. This paper reports on Who Bears the Cost of Honesty?, a CRAFT workshop at the 2026 ACM Conference on Fairness, Accountability, and Transparency that used scenario-anchored power mapping and design fiction to explore the benefits, harms, tensions, and power asymmetries that emerge under AI disclosure norms and mandates. We document the workshop design and analyze the disclosure approaches participants co-created, comprising four completed power maps, three context cards, and one interface prototype. These artifacts span education, workplace, politics/journalism, and interpersonal contexts. They depict disclosure as a multi-actor accountability process, surface concerns that the use of accessibility-related AI could be held against workers in performance evaluations, and explore how context-specific, bottom-up disclosures may support transparency while mitigating some risks of stigma and misinterpretation. We contribute (1) a documented two-stage workshop method; (2) an artifact-grounded thematic synthesis; and (3) a diagnostic framework, the Cost-of-Honesty Stack, with provisional design suggestions and research directions.

---


### 57. [Read, Write, Relax: Why Neural PDE Surrogates Need Both Global and Local Processing](https://arxiv.org/abs/2608.21677)

**<font color=#1a73e8>作者：</font>** Anuj Kumar, Heiko Zimmermann, Josiah Bjorgaard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent mesh-based simulation advances have, in no small part, relied on neural surrogates of two distinct families: global models that route information through a small set of latent tokens, and local models that perform message passing across mesh edges. Consistent with both classes is the inability to perform beyond low-dimensional problems and small-scale or oversimplified meshes, the simulation regimes where industrial problems reside. Our work shows this explicitly and presents a unified formulation. In global approaches, latent-token attention acts as a spatial low-pass filter, while local message passing lacks the global reach necessary to propagate information across large mesh spaces. Viewed through the error, the two operators are the halves of a multigrid cycle: one corrects errors at the lower end of the spectrum, the other at the higher end, and neither can do the other's job. We introduce Read-Write-Relax (RWR), which interleaves latent attention with message-passing relaxation under a unified formulation. The interleaved processor lowers error across the entire spectrum, making RWR the most accurate model in nearly every comparison across our industrial and public benchmarks. It is also markedly data-efficient in the scarce-data regimes, accurate on the engineering quantities of interest, and scales full-field predictions to challenging, large-scale problems.

---


### 58. [UrbanGazeVis: A Visualization System for Analyzing Eye-Tracking Data on Urban Safety Perception](https://arxiv.org/abs/2608.21686)

**<font color=#1a73e8>作者：</font>** Andres De La Puente, Felipe Moreno, Luis Sante 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Perceived safety in streetscapes depends on where people look, yet how gaze relates to visual cues of urban disorder remains poorly understood. Prior work treats safety as an image-level label, offering little insight into how attention to specific elements (e.g, buildings, greenery, people, signs of decay) shapes these judgments. We present a head-mounted eye-tracking study in which 30 participants viewed and rated the safety of 150 street-view images from Rio de Janeiro using a HoloLens 2 headset. Gaze traces were mapped onto semantic segments and disorder cues (e.g., damaged walls, graffiti, overhead cables), yielding a multimodal dataset linking gaze dynamics, scene semantics, and safety scores. To analyze it, we introduce UrbanGazeVis, an interactive visual analytics system with image- and participant-centric views that connects the spatial, temporal, and semantic dimensions of gaze to perceived safety, supporting comparisons between safe and unsafe scenes, inspection of divergent ratings for similar images, and region-of-interest analysis via glyph-based summaries. Statistical models show that sustained attention to physical disorder is associated with lower perceived safety, while the visual analysis reveals context-specific effects often masked by global aggregation. Together, these analyses offer actionable insights for urban design and planning.

---


### 59. [Emotion Intensity Matters: Generating Realistic Expressions in Virtual Humans with CVAEs](https://arxiv.org/abs/2608.21697)

**<font color=#1a73e8>作者：</font>** Vitor Miguel Xavier Peres, Lara Volpato, Gabriel Ferri Scnheider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating expressive facial behavior in virtual humans (VHs) remains a central challenge in affective computing and character animation. This paper presents a novel approach based on Conditional Variational Autoencoders (CVAEs), trained on real human facial expression data, to synthesize controllable emotional expressions at varying intensities. Using a dataset comprising six basic emotions represented at two intensity levels (low and high), we train a CVAE model to generate synthetic facial expression data while preserving semantic consistency with real human expressions. Despite the limited amount of training data (only 7,680 facial expression samples), the proposed approach learns meaningful latent representations and generates coherent emotional variations. Our method enables control over emotional intensity, making it suitable for animating virtual characters without requiring actor performances or manual artistic intervention. Our research aimed to evaluate whether the method (CVAE) preserves the characteristics associated with the different intensity levels present in the dataset. Results show that the proposed model preserves key expressive characteristics across intensity levels while supporting generalization across emotional intensity levels, contributing to the creation of emotionally expressive virtual characters from relatively small datasets.

---


### 60. [Posterior Information Dynamics of Diffusion Models for Linear Inverse Problems](https://arxiv.org/abs/2608.21709)

**<font color=#1a73e8>作者：</font>** Xiangming Meng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are widely used as priors for linear inverse problems, yet endpoint quality does not reveal when measurement information enters reverse denoising or how it is allocated across signal directions. We study this process through the smoothed likelihood force, the difference between exact posterior and prior scores at each noise level. For a fixed measurement, its expected squared norm gives both posterior--prior relative-entropy dissipation and reverse-path relative-entropy growth. Averaging over measurements yields an information--minimum mean-square error (I-MMSE) identity linking information gain to denoising-error reduction. Under finite second moments, the force energy and its ratio to prior-score energy decay quadratically in the noising kernel's signal coefficient at high noise. Solvable models show that conditioning removes class separation already explained by the measurement, reduces a uniform index entropy over \(n\) empirical samples from \(\log n\) to \(H(I\mid r)\), and makes assimilation depend on operator--prior alignment even for identical singular values. Experiments in models with tractable posteriors evaluate these predictions. In a separate illustration with a frozen FFHQ model, masks sharing the same spectrum yield different prior-normalized null-space trajectory statistics.

---


### 61. [StereoDiffuer: Diffusion-based Progressive Geometry Modeling with Saliency Attention Perception for Stereo Matching](https://arxiv.org/abs/2608.21710)

**<font color=#1a73e8>作者：</font>** Bohan Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advance of deep neural networks, the quality of disparity maps obtained through stereo matching has steadily improved. However, existing stereo matching methods still struggle to preserve fine-grained geometric details, resulting in blurred edges and over-smoothed predictions in challenging regions. To address these limitations, we propose StereoDiffuer, an iterative diffusion-based stereo matching framework that explicitly models geometric details and progressively refines disparity estimates. The framework incorporates a Saliency Attention Perception (SAP) module to extract salient geometric cues, including object boundaries, thin structures, and sharp edges. Confidence-guided SAP features are combined with the initial disparity estimate to condition an iterative denoising diffusion process, which corrects residual disparity errors and restores geometric details suppressed during cost-volume regularization and upsampling. Experimental results on the Scene Flow and KITTI benchmarks demonstrate the effectiveness of the proposed framework and its competitive performance relative to the compared stereo matching methods.

---


### 62. [The Plan, Not the Decoder: Diagnosing and Repairing Compositional Failure in Reasoning-Augmented Text-to-Image Generation](https://arxiv.org/abs/2608.21713)

**<font color=#1a73e8>作者：</font>** Ashritha Gonuguntla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning-augmented text-to-image models such as GoT-R1 emit an explicit textual plan - object names, attributes, and bounding boxes - before generating image tokens. When such a model fails a compositional prompt, is the plan wrong, or is the plan right and the decoder unfaithful? Because the plan is machine-readable it can be edited before decoding, which makes the two separable. We first validate the ruler. Swapping the two bounding boxes inside the model's own chain demonstrably flips the generated layout: detector-based accuracy falls 0.75 -> 0.48 (p<1e-3), while a widely used VQA-based spatial metric rises. A five-rater human study agrees with the detector on 81% of items and with the VQA judge on 57%. All spatial results therefore use geometric scoring. Under sound measurement the decoder is a faithful executor: 94% of generated layouts realize the planned relation, and object-box binding survives reordering of the plan's object segments. The planner is the bottleneck. It writes wrong relations for phrasing-dependent reasons - 98% accuracy on "left" against 54% on "right" for semantically identical layouts, a raster-order bias we isolate with a mention-order control - and cluttered geometry that the decoder faithfully reproduces. Editing the plan therefore fixes the image without retraining: symbolic verification with resampling gives +5.0 points (p<1e-3), minimal in-place repair +6.0 (p=.02), rewriting only box geometry +10.7 (p<1e-4), and replacing the plan outright +13.3 (p=1e-4). Gains are indifferent to the plan's prose style and to its likelihood under the planner, but not to its geometry. Modular planner-decoder designs are therefore viable, provided the plan is internally consistent: box-text contradictions induce object duplication and identity fusion. We release the plan-fidelity evaluation protocol, all plans, and 12k generated images.

---


### 63. [Ask or Answer: A Decision Framework for Multi-Turn Health Misinformation Intervention](https://arxiv.org/abs/2608.21721)

**<font color=#1a73e8>作者：</font>** Xiaoying Song, Anirban Saha Anik, Jinyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correcting health misinformation in dialogue requires more than producing a factual rebuttal: users differ in what they know, what they believe, and what they need to hear, so an effective intervention often depends on first asking the right clarifying question. Yet existing methods either respond immediately or probe indiscriminately, treating clarification as either unnecessary or always beneficial. We propose Reward-Optimized Probe-and-Respond (RO-PnR), a framework that learns when asking is worth its cost. At each turn, RO-PnR chooses between probing for more information and committing to a final correction, guided by a turn-level reward that weighs the expected gain from probing against its interaction cost. To capture how user heterogeneity affects probing value, we model each simulated user with a latent state along health literacy and belief commitment. Experiments show that RO-PnR achieves the highest cost-adjusted utility across three health-misinformation datasets and three base models, using 30% fewer turns than always-probe baselines.

---


### 64. [CALM-BP: Observation-Matched Physiological Semantic Grounding for Non-Contact Blood Pressure Estimation](https://arxiv.org/abs/2608.21744)

**<font color=#1a73e8>作者：</font>** Haiyang Sun, Boyuan Gu, Yongjie Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Language grounding increasingly involves non-text observations whose structure is not naturally expressed as words or objects. We study this problem for physiological time series in non-contact blood pressure (BP) estimation: remote photoplethysmography (rPPG) provides measured evidence about bodily state, but numerical pipelines expose little semantic structure about why a window is reliable or how its cues should be fused. We introduce observation-matched physiological semantic grounding, where language-derived priors must be constructed from the same rPPG observation, remain bounded by an auditable prior contract, and avoid BP-label or identity leakage. CALM-BP does not treat language as new physiological evidence; instead, it verbalizes rPPG descriptors into a controlled semantic interface while rPPG remains the primary haemodynamic evidence source. FlowBP-Set pairs forehead observations, synchronized BP labels, and structured physiological prompts from 81 participants. Main BP results, direct cross-dataset evaluation, language-realization ablation, and observation-mismatch controls test whether language helps because it organizes the current physiological observation rather than because it is arbitrary auxiliary text. The FlowBP-Set dataset contains sensitive facial video and physiological recordings and is therefore not publicly available due to privacy and ethical restrictions. Data access may be considered upon reasonable request and subject to applicable ethical and institutional approval.

---


### 65. [Calibrate What You SHIP: Post-Selection Risk Control for Verifier-Guided Text-to-Image Generation](https://arxiv.org/abs/2608.21748)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Shunqi Mao, Wei Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Verifier-guided text-to-image systems increasingly use test-time search to select, refine, or stop among multiple candidates, yet release thresholds are often calibrated on individual images. This creates a candidate-to-policy calibration mismatch: search changes both which prompts receive an output and which candidate is released, so candidate-level risk control need not imply control of released-output risk. We formalize this estimand shift through prompt reweighting and within-prompt selection, and introduce SHIP, Selection-aware Held-out calibration of Inference Policies. SHIP runs or replays the complete deployed policy on held-out prompts, evaluates the image it actually releases using an independent target judge, and selects the most permissive threshold whose risk upper bound satisfies a prescribed budget. For replayable policies with a prespecified threshold grid, simultaneous confidence control provides finite-sample validity. Experiments across fixed, sequential, and adaptive T2I inference procedures show that policy-level calibration recovers lower-risk operating points while exposing policy-dependent tradeoffs among risk, coverage, and compute. On GenEval2 with FLUX at N=16, a pooled-candidate threshold yields released risk 0.310, whereas SHIP reduces it to 0.162. Across 200 cached-stream splits, the fixed-grid certificate has no target crossing. Reliable inference-time scaling therefore requires calibrating the output distribution induced by the complete deployed policy.

---


### 66. [Width-Independent Compressibility of Deep Neural Networks](https://arxiv.org/abs/2608.21752)

**<font color=#1a73e8>作者：</font>** Hong-Yi Wang, Mingze Wang, Liu Ziyin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It has long been known that well-trained neural networks can be compressed very strongly without affecting their performance, an important phenomenon that remains poorly understood. We prove a uniform compressibility theorem for deep multilayer perceptrons with analytic activations. For a deep, wide fixed teacher network, there exists a narrow (same depth) network that approximately represents the same function as the original. The reachable compressed width is strikingly independent of the original width, but is $O((\log(1/\varepsilon))^{d_{in}})$, where $\varepsilon$ is the error budget and $d_{in}$ is the effective input dimension. Our construction involves a novel derivative-matching technique which is aware of the low-dimensional input, and a layer-wise reweighting that preserves the input-output mapping.

---


### 67. [Fidelity-Diversity-Consistency (FDC): Data Pruning for Remote Sensing Change Detection](https://arxiv.org/abs/2608.21754)

**<font color=#1a73e8>作者：</font>** Dongyao Zhu, Ranga Raju Vatsavai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the success of data pruning (DP) in reducing training data sizes and improving downstream model performance in classification and segmentation tasks, its potential in remote sensing change detection remains unexplored. For the first time, we benchmark six representative DP methods across building- and forest-change datasets, CNN- and transformer-based models, and three pruning budgets, and show that existing baselines yield no reliable advantage over random selection. Notably, even the strongest evaluated baseline, Feature Diversity, is matched or exceeded by $\sim$33\% of randomly sampled subsets. To understand the underlying mechanism, we conduct a systematic regression study over 540 randomly sampled data subsets, characterizing each with four descriptors covering label statistics, image diversity, and feature-space geometry. Random Forest models show that \emph{change distribution fidelity} is the most prominent factor in determining the quality of change detection data subsets, a property absent from the existing pruning literature. Our analyses further show that pixel-wise image diversity and label-feature consistency are secondary factors. We translate these findings into Fidelity-Diversity-Consistency (FDC), a simple two-stage pruning method that shows consistent improvements over existing baselines across change detection benchmarks and backbones, especially at lower pruning ratios. Code is available at \href{this https URL}{this https URL}.

---


### 68. [ECHO: A Cognitively Inspired, Auditable Memory Plane for Long-Horizon Agents](https://arxiv.org/abs/2608.21755)

**<font color=#1a73e8>作者：</font>** Yu Qian, Hong Miao, Boyang Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents need memory that identifies relevant experience, resolves revisions, and exposes checkable provenance. We present ECHO (Embodied Context and History Orchestration), an auditable memory architecture and service prototype inspired by episodic encoding, consolidation, contextual reinstatement, reconsolidation, and executive control. This is functional inspiration, not neural equivalence; the empirical analysis focuses on retrieval and context construction. Development runs reach 96.29% Hit@10 and 73.64% turn Recall@5 on 1,536 LoCoMo category 1-4 questions, and 97.60% Hit@10, 88.84% turn Recall@5, and 88.71% session Recall@5 on all 500 LongMemEval-S questions. A five-history BEAM gate fails, and in a separate matched 91-question QA sample Mem0 OSS scores 64.84% versus ECHO's 41.76% (exact McNemar p = 0.00107), with a history-cluster interval crossing zero. A post-hoc audit found source-specific phrases in the query-expansion rules. Although no gold answer field entered the runtime, expansion-enabled retrieval scores are therefore descriptive development measurements, not independent confirmation.

---


### 69. [How Architecture and Training Affect TPC Representations Across Experiments](https://arxiv.org/abs/2608.21756)

**<font color=#1a73e8>作者：</font>** Tyler Wheeler, Michelle P. Kuchera, Raghuram Ramanujan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep-learning efforts have increasingly shifted toward foundation model approaches. In experimental physics, this allows models and learned representations to be reused beyond the experiments in which they were developed. This work evaluates the reusability of representations across experiments and detector systems using probes on frozen encoders. These probes reveal task-relevant structure before downstream adaptation, complementing fine-tuning. Together with random-weight controls, they distinguish contributions from architecture and encoder training that downstream performance alone cannot resolve.
Time projection chamber (TPC) data provide a useful testbed because events from TPC systems can be represented as variable-length sparse tensors, while detector geometries, event topologies, and scientific tasks can differ substantially. We investigate whether fixed-dimensional TPC event representations can be reused across classification tasks, experiments, and detector systems. Sparse ResNet and PointNet-style encoders produce 512-dimensional embeddings for four datasets from the GADGET II TPC and AT-TPC. Randomly initialized encoders isolate the contribution from architecture before supervised training. We then train each encoder on a classification task, freeze its parameters, and train a linear or nonlinear probe for each downstream task. We find that this architecture-induced structure remains useful across experiments and detector systems. The randomly initialized PointNet-style representation is highly informative on several tasks. The two architectures organize their embedding spaces differently, but neither exhibits a large, systematic loss of utility cross-detector. These results show that architecture is a major source of task-relevant structure in TPC embeddings and should be treated explicitly when assessing representation learning and developing reusable detector models.

---


### 70. [What Does CLIP Learn for Regional Geolocalization? Probing Visual Cues and Scene Configuration After Adaptation](https://arxiv.org/abs/2608.21761)

**<font color=#1a73e8>作者：</font>** Changyu Lee, Yeonsoo Park, Abdullah Alfarrarjeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large collections of street-view imagery provide rich visual information about urban environments, but extracting fine-grained geographic information from such data remains challenging. In particular, fine-grained regional geolocalization is challenging because nearby areas often share coarse geographic cues. We study regional geolocalization within a metropolitan area and ask whether pretrained CLIP features are sufficient for regional discrimination, and what visual information supports performance after adaptation. Using 9,085 street-view images from eight Greater Los Angeles regions, we compare zero-shot CLIP, frozen-encoder readouts, partial encoder updating, Low-Rank Adaptation (LoRA), and full fine-tuning. Frozen readouts remain near the 39.03% zero-shot accuracy, whereas encoder adaptation achieves 75.94-82.10%. Full fine-tuning also reduces the mean distance to the predicted region center from 12.30 km to 3.86 km. We probe these gains through semantic cue removal, appearance reduction using edge maps and blur, and scene-configuration disruption using patch scrambling. Adapted models achieve higher edge and blur accuracy and switch 42.92-45.56% of predictions after scrambling, compared with 10.79-14.60% for frozen methods. However, adaptation does not improve the fraction of performance retained after appearance reduction, while vegetation and sky remain influential. A Caltech101 control further shows that scrambling sensitivity is not unique to geolocalization. Overall, encoder adaptation substantially improves nearby-region discrimination and is associated with greater sensitivity to intact scene configuration, without evidence that coarse structure alone becomes sufficient for prediction. These conclusions concern viewpoint variation near known locations rather than geographically disjoint generalization.

---


### 71. [LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices](https://arxiv.org/abs/2608.21764)

**<font color=#1a73e8>作者：</font>** Riadul Islam, Joey Mule, Dhandeep Challagundla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based vision has emerged as a promising paradigm for energy-aware artificial intelligence (AI), offering sparse, low-latency visual signals that reduce redundant data processing and support sustainable edge computing. However, the asynchronous and noise-prone nature of event streams creates challenges for conventional deep learning models, which are often too computationally intensive for low-power embedded platforms. This work presents a compact and configurable event-driven autoencoder that efficiently compresses neuromorphic data while preserving essential spatiotemporal structure for downstream inference. The architecture integrates lightweight convolutional encoding with robust performance under adaptive event thresholding and a minimal classifier head, enabling substantial reductions in computational cost without degrading recognition fidelity. Extensive evaluations on the Smart Event Face Dataset (SEFD) and Event-Based Crossing Dataset (EBCD) show that the proposed framework achieves competitive or superior accuracy compared to YOLOv9 while requiring up to 35.6$\times$ fewer parameters. To assess real-world sustainability, the model is deployed on resource-constrained hardware: a Raspberry Pi 4B and a NVIDIA Jetson Nano. On NVIDIA Jetson Nano, it delivers real-time throughput of 44.8 FPS. On a Raspberry Pi 4B CPU, the 50\% autoencoder classifier consumes 16.19 J for the evaluated inference workload, corresponding to approximately 726.3$\times$ lower energy consumption than YOLOv9 under the same evaluation protocol. These results demonstrate the potential of compact event-driven models to advance environmentally conscious, low-power AI systems for high-speed perception in autonomous, mobile, and embedded computing environments.

---


### 72. [Physics-Knowledge-Guided Hybrid Neural Learning for Arctic Sea Ice Concentration Evolution and Short-Range Prediction](https://arxiv.org/abs/2608.21767)

**<font color=#1a73e8>作者：</font>** Maqun Zhang, Feng Gao, Wankun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of sea ice concentration (SIC) evolution is essential for polar climate assessment and short?range sea ice prediction. Numerical and data-driven approaches constitute major foundations for SIC modeling, but the former often require complex parameterizations and substantial compu?tation, whereas the latter rarely encode physical dependencies explicitly. This study presents the Physics-Informed Hybrid Ice Model (PIHIM), a differentiable data-driven hybrid ice model for daily SIC evolution that organizes its network structure according to the physical dependencies encoded in the sea ice continuity equation and explicitly accounts for dynamical transport, ther?modynamically driven areal growth and loss, and unresolved local processes. PIHIM preserves the representation capacity of deep learning while providing a process-decomposed formulation of ice displacement, freeze-melt areal change, and local error closure. Two evaluation settings are adopted: reanalysis-forced simulation examines SIC evolution stability under reanalysis forcing, and forecast-forced prediction assesses short-range performance un?der forecast-forced conditions, with reanalysis and observational SIC serving as verification references. Results indicate enhanced ice-edge preservation and error-growth control in reanalysis?forced simulation, while PIHIM retains measurable short-range prediction skill under forecast-forced conditions. Our code will be made publicly available after the paper is accepted.

---


### 73. [SpatialDiff: 3D-Aware Object Movement via Implicit Spatial Modeling](https://arxiv.org/abs/2608.21776)

**<font color=#1a73e8>作者：</font>** Zheng Liu, Zijian He, Huiguo He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image editing allow impressive manipulation of objects, existing methods still struggle to handle spatial movement in complex scenes, such as objects span different depth layers or are partially occluded. Most image editing methods focus solely on prior information from 2D datasets, emphasizing planar features while lacking support for spatial structures. Even approaches that incorporate explicit positional information fail to capture true 3D spatial relationships, thus limiting accurate object movement in complex scenes. In this paper, we present SpatialDiff, a method that effectively captures 3D spatial structures, enabling precise and consistent object movements in complex scenes. Our core innovations are twofold: (1) Implicit 3D Spatial Modeling, which introduces 3D prior knowledge and enables the model to internally build a comprehensive understanding of the three-dimensional spatial structure; and (2) Global Spatial Supervision, which constrains the latent spatial features to enable the model to perceive changes in object spatial positions caused by editing operations. Experimental results demonstrate that our method significantly improves the accuracy and fidelity of spatial movement in complex scenes.

---


### 74. [A Fixed-Radius Distance-Band Benchmark for Dimensionality-Reduction Fidelity](https://arxiv.org/abs/2608.21779)

**<font color=#1a73e8>作者：</font>** Yoshio Takaeda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality-reduction (DR) methods are routinely judged by how well each point's k nearest neighbors survive the 2-D embedding (recall@k, trustworthiness, continuity). We argue this family is a biased measure of distance fidelity: its per-point variable radius and hard inclusion threshold favor neighbor-graph methods (t-SNE, UMAP) and penalize methods that preserve absolute distances. We instead score DR fidelity with a fixed-radius distance-band Shepard rho: the Spearman correlation between high-D and 2-D pairwise distances, restricted to cumulative distance bands so that near and global structure are reported separately, with every point judged on the same absolute radius. On synthetic datasets with known ground-truth geometry (non-uniform density, dense clusters, a closed-loop transition, off-subspace outliers, imbalanced two-population data) at realistic noise (SNR=1, D=768, N=1000), we benchmark eight methods -- PCA, Isomap, t-SNE, UMAP, PyMDE, PCC, DREAMS, and the closed-source toorPIA -- and show that (i) high global Shepard rho can coexist with a ~93x collapse of within-cluster scale, invisible to rank-based scores but obvious in a value-based over-compression metric; (ii) recall@k and the fixed-radius band disagree systematically, in the direction the bias predicts; (iii) a membership-restricted Shepard rho resolves single-point and minority-population questions that many-pair statistics cannot -- questions on which even DREAMS, a recent local-plus-global hybrid, fails silently. A supplementary out-of-sample (addplot) test asks whether a never-seen anomaly lands outside the normal region and whether its direction identifies its source. All metrics are computed exactly on all pairwise distances, independently of any method's internals, and every number is reproducible offline: the closed-source method's output coordinates (not its algorithm) are committed to the artifact.

---


### 75. [DefaultShift: Auditing Semantic Default Shift in Accelerated Text-to-Image Models](https://arxiv.org/abs/2608.21784)

**<font color=#1a73e8>作者：</font>** Xuanhua Yin, Chuanzhi Xu, Shunqi Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step text-to-image models increasingly replace slower generators, yet acceleration can silently change distributions over unspecified attributes even when individual outputs remain plausible and aligned. We call these distributions semantic defaults and their change under replacement semantic default shift. Existing quality, preference, and diversity evaluations do not test whether a replacement preserves its reference model's semantic defaults. We introduce DefaultShift, a paired audit that labels repeated samples with closed semantic vocabularies, measures probability-mass movement, and separates interpretable ranking from confirmatory cross-fit inference. Across 14 reference and replacement pairs, adjusted color discrepancies range from 0.054 to 0.303 with recipe-specific directions. A 1,000-image human audit reproduces the ordering. We further introduce DefaultShift-Select, an offline calibration method that reduces human-measured shift by 10.3 percent to 35.1 percent across Turbo, DMD2, and FLUX without material quality loss. Under balanced evaluation, selected data recover 4.3 accuracy points and 7.5 worst-group points over uncalibrated replacement data. DefaultShift makes semantic preservation under acceleration measurable and actionable.

---


### 76. [HP-UniIF: Hierarchical Prompt Learning for Unified Image Fusion](https://arxiv.org/abs/2608.21786)

**<font color=#1a73e8>作者：</font>** Xingxin Xu, Siqi Zhao, Xin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General image fusion seeks to integrate complementary information from multiple source images, yet real-world applications often require a single system to support heterogeneous fusion, degradation restoration, and task-oriented perception simultaneously. Existing unified frameworks struggle with these orthogonal objectives, resulting in entangled representations and degraded performance across subtasks. We propose HP-UniIF, a unified vision framework that leverages diffusion priors to bridge heterogeneous fusion, visual restoration, and downstream perception. To address the limited adaptability of diffusion models to domain-, degradation-, and task-level objectives within one pipeline, HP-UniIF introduces a depth-wise hierarchical conditional modulation strategy that decouples these objectives across network stages. Task prompt modulation at bottleneck layers adapts the backbone to different fusion paradigms, the degradation prompt router at shallow layers injects degradation-aware constraints for local restoration, and the application prompt bank at decoding stages aligns generation with downstream tasks. This hierarchical design enables HP-UniIF to produce visually faithful results while preserving task-relevant semantics. Extensive experiments across multiple fusion tasks, diverse degradations, and various downstream applications demonstrate the superior performance of HP-UniIF.

---


### 77. [Lexical Coupling in GUI Element Grounding: Sentence Embeddings Track Labels across Mobile and Web](https://arxiv.org/abs/2608.21794)

**<font color=#1a73e8>作者：</font>** Qijia Chen, Giulio Jacucci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GUI grounding evaluations that expose UI elements as text metadata often treat high instruction-element embedding similarity as evidence of semantic grounding. Across three mobile and web benchmarks, we show that this interpretation is frequently confounded by visible-label recovery. Lexical baselines remain competitive at top-1, label-poor targets remain weak for text-only methods, and encoder top-1 hits are predictable from lexical rank, candidate-pool size, and label type. We evaluate each action as a same-screen ranking task, comparing five off-the-shelf single-vector encoders with lexical baselines. Encoders recover some lexical misses, but deployable fusion gains are much smaller than target-aware oracle gains. These findings show that embedding-based evaluations can conflate visible-label recovery with semantic GUI grounding. Embedding-based evaluations should therefore report lexical baselines, label-type stratification, and deployable-fusion diagnostics. Our released repository provides analysis scripts and detexted per-step panels: this https URL.

---


### 78. [ExplainGuard: A Zero Trust Framework for Post-Hoc Explanation Integrity Guarantees in Blackbox XAI Models](https://arxiv.org/abs/2608.21803)

**<font color=#1a73e8>作者：</font>** Maraz Mia, Shovan Roy, Mir Mehedi A. Pritom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As machine learning (ML) models are increasingly deployed in high-stakes environments, explainable AI (XAI) methods like SHAP and LIME have become essential for regulatory compliance and trust. However, the current auditing paradigm relies on an implicit "chain of trust" where third-party auditors are assumed to be trusted. Recent research demonstrates that this assumption is flawed and adversarial auditors can manipulate XAI explanations through manipulation attacks such as output shuffling or scaffolding out-of-distribution (OOD) to conceal model biases while maintaining high prediction accuracy aiming for fairwashed explanation. In this paper, we introduce a novel defense framework, ExplainGuard, that leverages a Zero-Trust architecture (ZTA) design to be incorporated within the XAI explanation supply chain and ensures the integrity of the generated explanation. This framework would help us to replace the ambiguous default assumption of "auditor is trustworthy," with a continuous "verify-then-trust" approach. Our design architecture establishes a Policy Decision Point (PDP) that enforces three distinct pillars of verification before any explanation is released to the user: (1) asset integrity via behavioral fingerprint to detect model substitution, (2) semantic validity using axiomatic consistency checks to reject mathematically impossible explanations, and (3) feature faithfulness verification utilizing a ranking stability approach with minimal computational overhead. Finally, we evaluate how ExplainGuard can effectively neutralize state- of-the-art explanation manipulation attacks while transforming the auditing process into a verifiable operation.

---


### 79. [FlashReg: GPU-Accelerated 3-Clique Point Cloud Registration for Real-Time Correspondence-to-Pose Estimation](https://arxiv.org/abs/2608.21804)

**<font color=#1a73e8>作者：</font>** Ziyang Yu, Xiang Li, Qiong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph-based point cloud registration achieves high robustness by identifying geometrically consistent correspondence sets, but constructing second-order compatibility graphs and enumerating candidate cliques remain compute- and memory-intensive. This work presents FlashReg, a GPU-oriented correspondence-to-pose estimator that avoids materializing the dense scored second-order graph. Its Fast First- and Second-Order Graph (FFSOG) construction builds a capacity-bounded sparse second-order graph directly from the binary first-order graph. A dataflow-optimized three-node clique (3-clique) search then selects pivots from compact per-row candidate pools and enumerates triples through sorted sparse-neighborhood intersections. Across indoor and outdoor benchmarks, FlashReg reduces correspondence-to-pose latency by 2--3x relative to TurboReg at comparable registration recall, while using about 50% of its peak allocated tensor memory on an embedded GPU. These results make FlashReg suitable as a high-throughput registration backend within onboard perception pipelines.

---


### 80. [More Computational Resources Do Not Ensure Higher Scholarly Impact: Evidence from Leading NLP Conference Papers](https://arxiv.org/abs/2608.21806)

**<font color=#1a73e8>作者：</font>** Shuai Chen, Tong Bao, Jitong Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational resources are increasingly central to NLP research, but how closely reported GPU capability aligns with scholarly impact remains unclear. We analyze 13,921 ACL, EMNLP, and NAACL main-conference papers published between 2020 and 2025, using GPU resources as our operational measure of computational resources. From full texts, we extract GPU models and counts, standardize each paper's largest reported configuration into a comparable hardware-capability measure, and link these data to citation, award, topic, and institutional metadata. GPU reporting became more common but remained incomplete, while reported capability increased mainly through newer hardware generations and medium-scale multi-GPU configurations. Resource concentration substantially exceeded impact concentration: the annual top 20% of GPU-quantifiable papers accounted for 83.9%-89.9% of reported GPU capability, but only 27%-32% of citations and 20%-33% of paper awards. In adjusted models, a tenfold increase in aggregate reported GPU capability was associated with a 3.52-percentage-point increase in within-NLP topic-year citation percentile, but increased model R^2 by only 0.0042. GPU count showed more consistent positive associations with citation and award outcomes than newer hardware generation. Overall, reported GPU resources are associated with scholarly impact but provide little standalone explanation of research influence.

---


### 81. [Through the Schrödinger Bridge: Benchmarking Antemortem Image Restoration from Postmortem Autolysis to Enhance Forensic Diagnostics](https://arxiv.org/abs/2608.21813)

**<font color=#1a73e8>作者：</font>** Shuang Hao, Jiacheng Yue, Yaxuan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forensic histopathology, essential for determining cause of death and disease diagnosis, is severely impeded by postmortem autolysis, i.e., an irreversible, stochastic degradation process that distorts tissue morphology and introduces diagnostic subjectivity, thereby underscoring the value of restoring autolyzed images to a diagnostically plausible, pre-autolysis state for improving objectivity in forensic practice. This restoration task is fundamentally challenging due to the large, non-deterministic morphological changes caused by autolysis and the infeasibility of pixel-wise paired data, which invalidates assumptions underlying supervised and cycle/structure-consistent unpaired translation methods. To address this, we formalize forensic histopathology autolysis restoration as a new task: under unpaired supervision, transform postmortem images with severe autolysis into diagnostically meaningful ``antemortem'' representations. We contribute AutoPath, the first homologous yet unpaired dataset for this problem, constructed by splitting specimens into adjacent tissue blocks---one processed immediately, the other exposed to induce autolysis---yielding nearly ten thousand $10\times$ patches from 69 cases with varying liver conditions. We further frame the problem as a Schrödinger Bridge between the autolyzed and non-autolyzed distributions, offering a principled approach to modeling stochastic, severe morphological degradation. Critically, we demonstrate the misalignment of generic image-level generative metrics (e.g., FID) with diagnostic utility and propose a forensically grounded, slide-level diagnostic distribution consistency evaluation. Overall, this work establishes a reproducible benchmark (encompassing task definition, a real-world dataset, and an evaluation methodology) toward rigorous and practically meaningful progress in autolysis restoration for forensic pathology.

---


### 82. [Resilient Concurrent Causal Discovery for Topological Event Sequences](https://arxiv.org/abs/2608.21815)

**<font color=#1a73e8>作者：</font>** Jiyu Tian, Junhao Dong, Mingchu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery on topological event sequences is crucial for ensuring the reliability of networks. However, existing methods struggle to capture the complex causal relationships arising from concurrent events and lack robustness to incomplete event sequences. To address these issues, we propose a resilient concurrent causal discovery method, termed RCCD, enabling robust learning of causal graphs from topological event sequences. Specifically, we first introduce an influence-aware hyperedge causal attention mechanism, which incorporates event duration into the embedding representation, aggregates concurrent event features via hyperedge causal convolution, and injects network prior knowledge to capture the complex many-to-one causal interactions. Furthermore, we design a masked-based alternating causal optimization framework, which forces the model to recover masked event types based on context through self-supervised mask reconstruction, thereby enhancing the resilience of the predictor to missing data. To validate the effectiveness of our method, we conduct extensive experiments on both simulated and real-world telecommunication network datasets. Experimental results demonstrate that the proposed method significantly outperforms existing state-of-the-art methods in both accuracy and robustness, making it more suitable for real-world telecommunication network environments.

---


### 83. [A Physics-informed Neural Network Approach for Robust Buckling Load Prediction and Reliability-Based Design of Thin Truncated Conical Shells](https://arxiv.org/abs/2608.21818)

**<font color=#1a73e8>作者：</font>** Devasmit Dutta, Budhaditya De, Rohan Majumder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thin-walled truncated conical shells are widely used in aerospace, marine, offshore, and lightweight infrastructure systems due to their high strength-to-weight ratio and geometric efficiency. Their buckling resistance under axial compression, however, is highly sensitive to geometric imperfections, manufacturing tolerances, material variability, and nonlinear instability effects. Conventional design procedures rely on conservative knockdown factors (KDFs), such as those recommended in NASA SP-8019, which do not explicitly account for shell geometry, fabrication quality, data uncertainty, or target reliability. This study develops a physics-informed neural network (PiNN) framework for predicting critical buckling loads of thin truncated conical shells and integrates the trained surrogate within a reliability-based design (RBD) formulation. The model combines geometric and material descriptors with mechanics-informed features derived from shell stability theory and the localized reduced stiffness method (LRSM). A physics-informed loss function penalizes mechanically inadmissible predictions exceeding the theoretical elastic buckling load. The framework is trained and evaluated using 133 experimental Mylar conical shell tests under axial compression. Compared with a conventional deep neural network (DNN), the PiNN improves predictive accuracy, reduces mean absolute error, and enhances physical consistency. The trained PiNN is then used to evaluate reliability indices and calibrate safety-consistent KDFs for prescribed target reliability levels. Results demonstrate that the PiNN-RBD framework provides an efficient approach for uncertainty-aware design of imperfection-sensitive shell structures.

---


### 84. [Convergence in Science, Divergence in Religion: Calibrated Framing Differences Across Wikipedia's Language Editions](https://arxiv.org/abs/2608.21821)

**<font color=#1a73e8>作者：</font>** Hung-Hsuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When Wikipedia's language editions describe the same concept, how differently do they frame it? Prior work measures coverage gaps between editions; we measure framing distance for matched concepts. We analyze 2,799 valid articles from 3,000 possible concept-language observations, spanning 150 Wikidata-anchored concepts, 20 language editions, 4 domains, and a calibration set. Raw embedding distances reflect both content differences and how well the encoder aligns each language pair. Even among calibration concepts with stable cross-cultural denotations (e.g., chemical elements, numbers, colors), the largest language-pair mean distance is 3.6 times the smallest, and distances are typically smaller within language families. We define a baseline-adjusted distance (calibrated distance): the distance between two language versions of a concept minus the mean distance for calibration concepts in the same language pair. This adjustment substantially reduces pair-specific alignment differences and the language-family pattern. Across three multilingual encoders (LaBSE, multilingual MPNet, and CMLM), scientific articles align more closely than calibration articles, and all three rank religion first and science/technology last. Concept-level rankings are highly consistent across encoders (Spearman rho=0.75-0.79 for MPNet and CMLM relative to LaBSE). Religion lies significantly above the calibration baseline under LaBSE. Within politics, divergence concentrates on concepts such as censorship and refugee, while democracy and human rights are among the most aligned. Code, data, and per-language-pair calibration baselines are released.\footnote{this https URL}

---


### 85. [VisAdj: Learning Adjacency Matrices from Node-Link Images](https://arxiv.org/abs/2608.21825)

**<font color=#1a73e8>作者：</font>** Jiahao Xie, Guangmo Tong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning adjacency matrices from node-link images is a fundamental problem for recovering structured graph information from visual observations. Existing methods typically rely on fixed KNN-based heuristics for candidate edge selection and fail to capture dependencies among edges. To overcome these limitations, we propose VisAdj, a new framework for topology-aware adjacency prediction. VisAdj introduces an attention-sparse neighbor sampler to adaptively select a high-recall set of candidate node pairs and performs joint edge inference using a line-graph transformer that treats candidate edges as tokens and explicitly models dependencies among incident edges. Extensive experiments on synthetic graphs, road networks, and vessel images demonstrate that VisAdj consistently outperforms existing baselines by clear margins.

---


### 86. [Towards Alias-Free 4D Gaussian Representations with Motion-Aware Filtering](https://arxiv.org/abs/2608.21828)

**<font color=#1a73e8>作者：</font>** Ankit Dhiman, Kunal A Kathare, Pranav Vignesh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel-view synthesis of dynamic scenes, crucial for AR/VR applications, remains a challenging problem. Recent methods adapt representations like 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) for dynamic scenes by incorporating time as the fourth dimension (4D representations). These 4D representations still suffer from aliasing artifacts, especially when generating novel views from divergent viewpoints (zoom-in/zoom-out operations). While using 3D smoothing filters like those proposed in Mip-Splatting might seem like a possible solution, they fail to account for local motion and also exhibit aliasing. To address this, we propose a motion-aware 3D smoothing filter specifically designed for 4D representations. Our approach adapts the filter strength based on local motion information, effectively mitigating aliasing without compromising rendering quality. This is achieved by estimating the joint density function of time and focal-to-depth ratio using a non-parametric estimation method. During inference, we sample from this joint distribution to determine the appropriate smoothing filter. This flexible strategy can be integrated with various 4D representations. Our evaluations on standard datasets demonstrate superior performance compared to state-of-the-art methods.

---


### 87. [Towards Bitstream-corrupted Harsh Visual Understanding: Through Bitstream Language Modeling as Robust Semantic Priors](https://arxiv.org/abs/2608.21837)

**<font color=#1a73e8>作者：</font>** Chaoran Huang, Fangcheng Li, Tianyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bitstream-corrupted Harsh Visual Understanding (BcHVU) aims to understand harshly degraded videos originally decoded from a severely corrupted bitstream in real-world multimedia communication. The ill-posed nature of BcHVU poses a major challenge for existing vision models, as even subtle bitstream corruption can lead to irreversible pixel distortion and significant semantic loss. To address these challenges in BcHVU, we propose Bitstream Language Modeling as Robust Semantic Priors (BLMSP), a framework for learning and injecting bitstream-native semantic cues. Our proposed BLMSP framework learns to extract bitstream-native semantic cues by bitstream language modeling, and leverages them as priors by injecting into off-the-shelf vision models of BcHVU tasks. Specifically, we present a Video Bitstream Byte Model (VBBM) that integrates byte-level modeling and cross-codec semantic distillation, enabling it to interpret robust semantics from byte sequences in multiple corrupted bitstream formats. The learned bitstream semantics are leveraged as robust priors and fused into BcHVU model backbones for improving the quality of video restoration, captioning, and human pose estimation. To train BLMSP, we construct a large-scale multi-source Corrupted-bitstream Harsh-video Paired (CHP) dataset containing 607k corrupted bitstream segments and 287k paired harsh video clips. Extensive experimental results show that the learned bitstream priors improve video restoration, captioning, and human pose estimation by 2.51 dB in PSNR, 0.20 in CIDEr, and 0.18 in PCK@0.2 on average, respectively. These results demonstrate that corrupted bitstream can serve as robust semantic priors in solving pixel distortion and semantic loss in BcHVU.

---


### 88. [AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations](https://arxiv.org/abs/2608.21841)

**<font color=#1a73e8>作者：</font>** Rachel Poonsiriwong, Chayapatr, Archiwaranguprok 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational AI increasingly shapes consequential decisions, yet users have limited support for recognizing and resisting manipulation. We present AI Watchdog, a browser-based agent interface that monitors live conversations, detects five dark-pattern categories, including sycophancy, brand bias, anthropomorphization, sneaking, and harmful generation, and alerts users when they occur. Its open-weight turn-level classifier supports independent deployment and a path toward local inference, preserving user privacy while remaining separate from the conversational AI. We evaluated AI Watchdog in a preregistered, five-condition between-subjects experiment (N = 150) comparing a no-intervention control with four configurations varying nudge timing (prebunking vs. just-in-time) and engagement mode (without vs. with cognitive forcing). Results show that participants rarely flagged manipulative turns across all conditions, and post-task awareness did not differ significantly across groups. However, just-in-time warnings without cognitive forcing were the only intervention to significantly reduce compliance with AI-steered recommendations containing dark patterns, lowering compliance from 71.7% to 53.7%, an 18 percentage-point reduction. Exploratory analyses further showed that lower misinformation susceptibility was associated with greater flagging but not lower compliance, while higher AI trust was associated with greater compliance and lower reported awareness. Together, these findings suggest that explicit recognition of conversational dark patterns and behavioral resistance to AI steering may be distinct outcomes, motivating further investigation of timely, low-friction defensive interfaces.

---


### 89. [BC-IHV: Conditioning the Color Space for Stable Rectified-Flow Low-Light Enhancement](https://arxiv.org/abs/2608.21847)

**<font color=#1a73e8>作者：</font>** Yi Ai, Zheng Chen, Yuanhao Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) must correct ambiguous exposure without overwriting structure already supported by the input. Generative transport can model exposure ambiguity; however, its flexibility may also alter observable geometry and chromatic content. Moreover, fixed invertible color coordinates are usually treated only as representations, although their inverse mappings reshape the RGB-domain gradients received by the enhancement network. To address these issues, we propose Structure-Anchored Rectified Flow (SA-RF), which maintains correspondence through separate chromaticity/intensity stems, a scale-matched condition pyramid, and HybridAda. HybridAda assigns location-specific retrieval to spatial cross-attention and global exposure modulation to pooled AdaLN. We further introduce BC-IHV, a learnable Box--Cox polar color space whose analytically invertible intensity mapping controls the inverse-gradient dynamic range through a single exponent. This allows the representation to balance dark-range expansion and gradient conditioning instead of adopting a fixed linear or logarithmic law. Experiments on three LOL benchmarks, blind image-quality evaluation, and cross-dataset tests demonstrate consistent reconstruction and perceptual advantages over the sota. Controlled studies further support the effectiveness of both the proposed framework and color representation.

---


### 90. [GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849)

**<font color=#1a73e8>作者：</font>** Xinhui Liu, Can Wang, Wei Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has achieved remarkable success in novel view synthesis; however, reconstructions under sparse views often exhibit noticeable artifacts. While recent video diffusion models provide strong spatio-temporal priors for 3DGS restoration, directly fine-tuning them for restoration is suboptimal, as they lack awareness of the underlying multi-camera geometry, resulting in multi-view inconsistencies. In this work, we propose a novel 3D-aware video restoration framework designed to enhance the quality of sparse 3DGS reconstruction. Specifically, we construct a large-scale 3DGS video dataset to enable specialized fine-tuning. To bridge the gap between 2D video generation and 3D multi-view constraints, we introduce a camera-conditioned geometric prior. By using the first and last frames as boundary anchors and encoding the corresponding camera relationships, we explicitly inject spatial structure into the video generation pipeline. This boundary-anchored, camera-aware prior guides the network toward geometrically grounded restoration that remains coherent across viewpoints. Extensive experiments show that, among video-prior restoration methods, our approach attains the best pixel- and structure-level fidelity (PSNR/SSIM) and improves multi-view consistency, while remaining competitive in perceptual quality (LPIPS).

---


### 91. [Frame-Level Evaluation in Weakly Supervised Video Anomaly Detection Mostly Measures Video-Level Ranking](https://arxiv.org/abs/2608.21854)

**<font color=#1a73e8>作者：</font>** Inpyo Song, Jangwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised video anomaly detectors are trained with video-level labels but are commonly evaluated as temporal localizers using Micro-AUROC or AP over pooled test frames. Because these metrics compare frames from different videos, a detector can score well by separating videos without accurately ordering moments within them. We exactly decompose Micro-AUROC by video identity into Within-AUROC for temporal ordering within videos and Cross-AUROC for comparisons across videos. Across ShanghaiTech, XD-Violence, and UCF-Crime, only 0.071-0.388% of comparisons between anomalous and normal frames occur within the same video. When both classes remain distributed across V videos, this share decreases as O(1/V), a benchmark property we call temporal dilution. We train anomaly video binary classifiers under the same video-level supervision and repeat each video score across all frames. These video-constant outputs reach 81.40-97.18 Micro-AUROC despite having no within-video variation. Across 72 controlled runs, replacing every frame score with its video mean preserves a median 98.6% of the Micro-AUROC margin above chance. The same empirical pattern holds for author-released outputs and for XD-Violence under its official AP evaluation. A detector can therefore achieve a high pooled score even when it assigns the same score to every moment within each video.

---


### 92. [HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews](https://arxiv.org/abs/2608.21868)

**<font color=#1a73e8>作者：</font>** Ao Chen, Xiaojiang Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Depression assessment from multimodal clinical interviews requires integrating dispersed evidence from multiple symptoms into a coherent PHQ-8 profile. This process is hierarchical: relevant evidence is often sparse and context-dependent within local question-answer exchanges, multiple exchanges jointly support symptom-level judgments, and the final assessment depends on the coherence of the complete symptom profile. Existing LLM systems either process interviews holistically or distribute work across generic agent roles; neither design necessarily provides an explicit orchestration mechanism that coordinates evidence access, item-score authority, bounded feedback, and state recording across these levels. To address this gap, we introduce HiMA-MDD, a hierarchical multi-agent harness that aligns this assessment hierarchy with three agent layers. After non-agentic preprocessing constructs context-preserving multimodal QA units, Layer 1 identifies candidate QA-to-item relations and supports bounded item-grounded evidence routing. Layer 2 assigns symptom groups to operational factor specialists, with one specialist responsible for each provisional item score. Layer 3 audits the complete provisional profile, requests at most one round of targeted revision, and reconstructs the verified PHQ-8 profile. This layered design naturally yields a Hierarchical Evidence Trace, preserves all intermediate evidence, judgments, and revisions for auditability. The final item scores then deterministically produce the total score and screening decision. Using Qwen2.5-72B-Instruct as the harness backbone, our experiments on E-DAIC demonstrate that HiMA-MDD outperforms the compared state-of-the-art methods.

---


### 93. [Region-Weighted Losses and Model Fusion for Cross-Modal PET Attenuation Correction](https://arxiv.org/abs/2608.21881)

**<font color=#1a73e8>作者：</font>** Khoa Tuan Nguyen, Joris Vankerschaver, Wesley De Neve  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our approach to the Big Cross-Modal Attenuation Correction (BIC-MAC) challenge, which asks for a pseudo-CT in Hounsfield Units to be synthesized from Non-Attenuation-Corrected PET (NAC-PET), DIXON MRI and a topogram, and scores both the pseudo-CT and the Attenuation-Corrected PET (AC-PET) reconstructed from it. Three ideas carried our improvements over the organizers' 3D U-Net baseline. The loss matters more than the architecture: we compute the $L_1$ error in the Carney attenuation-coefficient ($\mu$) space that the CT metric itself uses, weighted by anatomical region. Only once that loss was in place did the unregistered DIXON MRI work as extra input channels. A fixed convex combination of two independently trained models then beat both of its members on three of the four metrics and ranks first overall on the public validation leaderboard.

---


### 94. [Pixel-Space Diffusion via Observation Operators](https://arxiv.org/abs/2608.21885)

**<font color=#1a73e8>作者：</font>** Shaojie Guo, Lichen Ma, Haoyang Tong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models directly model image distributions but remain difficult to optimize. Recent methods alleviate this challenge through target reparameterization, while still relying on a fixed clean-image target throughout denoising. Through empirical analysis, we identify a scale-time mismatch: image structures become predictable from coarse to fine as noise decreases, whereas existing models are forced to predict the full image even under high noise, resulting in low-SNR gradients that hinder optimization. To resolve this mismatch, we propose Observation Operator Diffusion, a unified framework that aligns both the supervision trajectory and feature refinement with the intrinsic recovery order of image structures. Specifically, we replace fixed full-image supervision along the standard flow path with a time-indexed observation trajectory that evolves from coarse structures to the full image during denoising. This trajectory is instantiated with a family of Gaussian-Lanczos operators at varying observation scales, yielding a path-consistent training objective. We further introduce GL-CoDA, a decoder that injects scale-specific Gaussian-Lanczos observations across decoding stages for coarse-to-fine feature refinement. Extensive experiments show that the proposed approach converges substantially faster while consistently improving generation quality, achieving an FID of 1.52 on ImageNet-256.

---


### 95. [A Scalable Vector Graphics Latent Space](https://arxiv.org/abs/2608.21893)

**<font color=#1a73e8>作者：</font>** Leonardo Zini, Elia Frigieri, Lorenzo Baraldi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics are a fundamental medium for resolution-independent visual content, yet the deep learning community lacks a continuous, dense, and invertible latent space for vector representations, the kind of foundational building block that Variational Autoencoders and their descendants have long provided for raster images. We introduce SLS (SVG Latent Space), a Transformer-based autoencoder that learns compact dense representations of individual SVG paths, the atomic visual elements from which any SVG image can be composed. By modeling SVG commands, coordinate data, and visual properties within a unified BPE-based token vocabulary, SLS learns fixed-size latent representations that jointly capture structure and appearance, and can be decoded back into valid, style-consistent SVG paths with high fidelity. The resulting embedding space is robust, invertible, and structured: embeddings lie on a unit hypersphere, enabling efficient similarity search, composition, and downstream conditioning through simple vector-space operations. Finally, we demonstrate that SLS generalizes across diverse tasks reducing their FLOPs by over 150 times compared to token-based approaches, and establishing a general-purpose latent foundation for vector graphics research.

---


### 96. [Entity-Constrained CBCT Retrieval for Low-Resource Dental Record Completion](https://arxiv.org/abs/2608.21913)

**<font color=#1a73e8>作者：</font>** Nhi Ngoc-Yen Nguyen, Thai Nguyen, Kiet Huynh Cao Tuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Completing dental records from cone-beam computed tomography (CBCT) is difficult when annotation is scarce and individual clinical fields are supported by different types of evidence. MMDental Task 3 requires seven-field record completion from only 50 labeled CBCT cases and scores the correctness of structured FDI positions and ICD codes; consequently, a visually plausible retrieved record can still be harmful when it introduces an unsupported entity. We propose Entity-Constrained CBCT-Guided Retrieval (ECCR), a parameter-free framework that separates evidence availability from evidence authority. A corpus-derived prior first supplies the complete record. A frozen 3D encoder retrieves image-conditioned Diagnosis evidence, which is appended only if it does not expand the prior FDI or ICD entity set, so the asserted entity set is invariant by construction. On public validation, ECCR reaches a weighted score of 0.3134, improving on both full-record multimodal retrieval (0.2237) and a static text-only prior (0.2915); the guard blocks 63.3% of retrieved candidates, each of which would otherwise have injected an FDI position or ICD code absent from the prior. On the final test evaluation, ECCR obtains 11.37 of a 97.4-point attainable maximum, securing second place overall. The result indicates that, in an extreme low-resource setting, controlling what multimodal evidence is allowed to modify can be more reliable than transferring an entire retrieved record.

---


### 97. [Consistency Is Not Coherence: Orientation Search for Certified Alignments Between 4D Defence Upper Ontologies](https://arxiv.org/abs/2608.21914)

**<font color=#1a73e8>作者：</font>** Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We align three upper ontologies that sit under UK and NATO defence data infrastructure: the Information Exchange Standard (IES), the Higher Quality Data Model (HQDM) that underpins the National Digital Twin, and Basic Formal Ontology (BFO). No public alignment between IES and HQDM existed. Promoting a hand-curated 17-correspondence crosswalk to OWL and reasoning over the complete merged ontologies with HermiT produces three results that we believe matter beyond this pair.

---


### 98. [Modeling Claim Dependency Structure for Patent Litigation Prediction with Graph Attention Networks](https://arxiv.org/abs/2608.21924)

**<font color=#1a73e8>作者：</font>** Takao Arai, Hiroyasu Inoue  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patent litigation imposes substantial costs on firms and distorts R&D incentives, making early risk identification a practically important task. While prior work has applied BERT-based models to patent claim text, two fundamental limitations remain: flat sequence encoding loses the dependency structure between independent and dependent claims that legally determines patent scope, and feeding the entire claim set to a single encoder discards legally critical text. A six-model ablation on 1.34 million USPTO utility patents confirms that per-claim encoding, graph connectivity, attention, and Attentional Aggregation each provide independent, additive predictive value. We propose ClaimGAT, a Graph Attention Network that encodes each claim independently, constructs a directed claim dependency graph, processes it with GATConv layers, and aggregates independent claims via Attentional Aggregation to yield both a litigation risk score and claim-level gate weights that enable post-hoc structural analysis. ClaimGAT achieves an AUC-ROC of 0.818 and a lift of 4.89x at the top 10%, using only information observable at the time of patent grant. It reveals a tendency in high-risk patents for structural selection and content sensitivity to diverge, a pattern consistent with defensive claim drafting.

---


### 99. [AirAlign: Geometry-Aware Relative Pose Alignment for UAV Last-Meter Navigation](https://arxiv.org/abs/2608.21926)

**<font color=#1a73e8>作者：</font>** Jinyi Zhou, Shuo Feng, Yufei Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) navigation in modern low-altitude environments requires more accurate pose alignment in the final approach stage for target information acquisition or manipulation, making "last-meter" navigation increasingly important. However, severe viewpoint and appearance variations make this task challenging. To tackle this problem, we propose AirAlign, a framework for RGB-only image-pair relative pose alignment for UAVs. AirAlign uses a pretrained visual geometry reconstruction model as the backbone to extract geometry-aware features from source-target image pairs. In addition, to better utilize the limited training data, we split the training set into multiple scene-disjoint folds for unseen cross-validation and model selection. During inference, the predictions of the selected models are averaged to form the ensemble output of the overall framework. Experiments on the PairUAV challenge at the ACMMM 2026 Workshop on UAVs in Multimedia demonstrate the effectiveness and robustness of our method, while comprehensive ablation studies validate the contribution of each component.

---


### 100. [C$^2$Path: Class-Conditional Pathway Decoupling for Vision-Language Incremental Object Detection](https://arxiv.org/abs/2608.21937)

**<font color=#1a73e8>作者：</font>** Lecheng Xu, Feifei Shao, Ouyangzi Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental Object Detection (IOD) aims to enable detectors to continuously learn novel categories while preserving previously acquired knowledge. However, existing methods suffer from two forms of \textbf{class knowledge coupling}: class boundary erosion induced by shared parameter updates and class representation entanglement arising from mixed feature encoding. We argue that effective incremental learning requires class-specific computational pathways that enable isolated parameter updates and separated class-wise injection. To this end, we propose \textbf{C$^2$Path}, a class-conditional pathway decoupling framework for vision-language incremental object detection that leverages token-level class cues to establish dedicated and updatable computational pathways for different categories. Specifically, C$^2$Path introduces a category expert library and a class-conditional decoupling module. The expert library consists of learnable low-rank computational nodes that capture category-specific knowledge, while the decoupling module generates class-aware routing signals to dynamically compose \textit{ClassLoRA} adapters from these experts, thereby forming class-specific computational pathways for isolated updates and separated injection across categories. Extensive experiments on COCO 2017 under multiple incremental learning settings demonstrate that C$^2$Path consistently outperforms state-of-the-art methods, providing an effective and scalable solution for continual category expansion in vision-language detectors.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
