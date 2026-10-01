# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

---

### 201. [Jacobian Rank Collapse in Decision-Focused Learning](https://arxiv.org/abs/2609.39261)

**<font color=#1a73e8>作者：</font>** Aojie Yuan, Haiyue Zhang, Zijian Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning (DFL) trains predictors through downstream objectives, but a different loss need not provide an independent parameter-update direction. We characterize this restriction through the predictor Jacobian, using sparse index tracking to distinguish the covariance entries read by the optimizer from the parameter directions available to learning. Rank-one Jacobians make nonzero per-example gradients collinear; a conditional spectral bound describes near-collinearity. A batch-subspace characterization and counterexamples show why these local statements imply neither common minimizers nor collinear batch updates.
Experiments examine when geometry translates into decision quality. Across 38 one-parameter equity configurations, DFL gains over MSE remain below 1.8%; a 385-parameter conditional predictor also has pointwise rank one. In validation-tuned shortest-path and knapsack experiments, full-capacity SPO+ reduces mean regret by 11.6% and 10.6%, respectively; only knapsack survives correction across eight comparisons. The capacity contrast persists on fresh datasets across batch orders and training budgets. Holding expressivity fixed, invertible coordinate scaling lowers spectral effective rank and ordinary SGD gains; compensating for the scaling restores the original trajectories. Financial forward-target controls separate forecast accuracy from decision quality; a matched neural comparison finds no aggregate DFL advantage in the tested architecture. These findings distinguish local rank restrictions, coordinate-dependent optimization and predictive accuracy. Predictor geometry helps explain available learning directions, while held-out decision quality remains the test of practical benefit.

---


### 202. [Concept Subspaces Compute Beyond the Logit Lens: A Weights-Only Test for Locating Representations Upstream of Readout](https://arxiv.org/abs/2609.39263)

**<font color=#1a73e8>作者：</font>** Aojie Yuan, Zhiyuan Julian Su, Haiyue Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A concept subspace's effect on model behavior does not establish how it relates to the output readout. We introduce a two-sided geometric diagnostic that measures an extracted subspace's overlap with the dominant right-singular directions of the unembedding matrix, evaluated against output-oriented positive controls. Given an extracted basis, the raw diagnostic requires only model weights. Our testbed is the Format-Agnostic Reasoning Subspace (FARS), a ten-dimensional basis extracted from eighteen reasoning concepts expressed in six surface forms. Across nine rank-matched estimators and twenty-six models, four activation-derived concept estimators carry only 0.38--0.80% mean energy in the top-ten readout span. Final-layer PCA carries 3.56%, exceeding FARS in 25 of 26 models. A same-layer next-token control, evaluated using a fitted linear translator for depth matching, carries approximately thirteen times more energy than FARS, with separation in all 25 tested models. Re-extracting FARS on ten disjoint concepts yields 62--100% cross-format retrieval across twenty-four generative models, demonstrating transfer of the extraction procedure rather than a fixed basis. A complementary four-model, three-seed intervention study finds model-dependent source-directed effects that remain well below full-vector replacement. Together, the geometry and intervention controls distinguish concept structure from dominant readout directions while limiting claims of causal sufficiency.

---


### 203. [Universal Cross-Prompt Adversarial Attacks on Promptable Concept Segmentation](https://arxiv.org/abs/2609.39265)

**<font color=#1a73e8>作者：</font>** Ziqi Zhou, Yifan Hu, Yufei Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model (SAM) achieves remarkable performance in visual segmentation. The latest SAM3 extends promptable segmentation to concept-level prediction, broadening the scope of segmentation foundation models. While recent works reveal that SAM and SAM2 are vulnerable to adversarial examples, the robustness of SAM3 under the concept segmentation paradigm remains unexplored. In addition, existing adversarial attacks on SAM-series models exhibit limited cross-prompt transferability. To this end, we propose AdvPCS, a universal cross-prompt adversarial attack for Promptable Concept Segmentation (PCS), including a min-max prompt optimization strategy, a global-local perception deception attack, and a temporal transition deviation attack. Specifically, we first identify the hardest-to-attack prompts via min-max bilevel optimization. In the inner maximization, we enhance diversity over candidate point, box, and text prompts. In the outer minimization, we select prompts with the highest responses based on the confidence scores output by the detector. Given the selected prompts, we apply the perception deception attack to minimize both global and local existence probabilities under joint prompting and employ the temporal memory misalignment attack to maximize inter-frame semantic inconsistency and corrupt memory pointers. Extensive experiments on four benchmark datasets show that a single universal adversarial perturbation (UAP) generated by our method generalizes across frames from different videos and achieves strong attack performance under point, box, and text prompts. In particular, it reduces the average mIoU of various PCS models on the SA-CO dataset to below 5% under text prompts, demonstrating strong attack ability.

---


### 204. [PLRS-IC: A Dual-Calibration Framework for Chest X-Ray Vision-Language Alignment](https://arxiv.org/abs/2609.39266)

**<font color=#1a73e8>作者：</font>** Qixing Zhao, Jinpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained vision-language alignment in chest radiography enables zero-shot classification, grounding, and segmentation without task-specific annotations. However, this alignment is fundamentally hindered by two intertwined sources of ambiguity: projection-induced visual mismatch and patient-agnostic semantic overlap. First, at the local feature level, frontal and lateral radiographs exhibit distinct appearances for the same clinical finding, rendering a shared patch-text similarity geometry inherently suboptimal. Compounding this visual ambiguity is a semantic mismatch during global contrastive optimization, where instance-level objectives penalize cross-patient pairs as strict negatives even when they share identical positive clinical concepts. To address this dual ambiguity, we propose PLRS-IC, a unified dual-calibration framework for chest X-ray representation learning. At the local alignment stage, Projection-Conditioned Low-Rank Residual Similarity (PLRS) dynamically adapts patch-text matching to projection-specific manifolds using a bounded, parameter-efficient low-rank residual. At the global optimization stage, Information-Content-Calibrated Soft False-Negative Suppression (IC-SFNS) leverages a corpus-derived information-theoretic prior to soften the penalty of semantically overlapping negatives without altering original contrastive assignments. Extensive experiments across nine public zero-shot benchmark settings demonstrate that our framework yields consistent improvements in classification, grounding, and segmentation, validating the necessity of dual-calibration in medical vision-language pre-training.

---


### 205. [A Time-Aware Bag-of-Receptive-Fields for Interpretable Irregular Time Series Classification](https://arxiv.org/abs/2609.39268)

**<font color=#1a73e8>作者：</font>** Francesco Spinnato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregular time series, characterized by non-uniform sampling intervals, missing observations, and variable lengths, are ubiquitous in healthcare, mobility, and environmental monitoring, yet effective and interpretable classifiers for this setting are limited. Existing approaches often rely on imputation, which can obscure the temporal structure of the data, or require complex neural architectures that are opaque and difficult to explain. In this work, we extend the Bag-Of-Receptive-Fields (BORF), a fast, deterministic, and interpretable transform for time series, to the irregular setting. Our key contribution is a time-weighted normalization scheme in which each observation is weighted proportionally to its associated time delta, making pattern extraction sensitive to the actual temporal distribution of samples rather than only their index position. This requires deriving an efficient sliding-window recurrence for the time-weighted standard deviation, preserving the linear time complexity of BORF. We benchmark the resulting method against state-of-the-art irregular time series classifiers on datasets from the PYRREGULAR repository, demonstrating competitive classification performance with the added benefit of human-interpretable explanations.

---


### 206. [RW-Flow: One-Step Generation on Compact Manifolds via Wasserstein Gradient Flows](https://arxiv.org/abs/2609.39271)

**<font color=#1a73e8>作者：</font>** Ualibyek Nurgulan, Seungwoo Yoo, Prin Phunyaphibarn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manifold-valued data, and consequently the distributions they induce, are prevalent across many domains, ranging from the locations of geospatial events, such as earthquakes, to biomolecular torsion angles that encode information about three-dimensional structure. While diffusion and flow-based generative models have been successfully extended to compact manifolds, sampling typically requires tens or hundreds of sequential network evaluations. We introduce RW-Flow, a theoretically grounded framework for learning one-step generative models on compact manifolds via Wasserstein gradient flows. The main challenge is identifiability: driving the velocity field to zero should guarantee that the model distribution matches the target distribution. We establish a necessary and sufficient condition for identifiability on compact, connected Riemannian manifolds. We specifically show that, for a symmetric, Lipschitz-continuous cost function, the velocity field induced by the Sinkhorn divergence is identifiable if and only if the associated Gibbs kernel is nondegenerate. This characterization provides a general principle for designing identifiable costs on compact manifolds. It also reveals that the squared geodesic distance, the natural manifold analogue of the squared Euclidean distance, does not always guarantee identifiability. Across benchmarks involving geospatial events, protein side chain torsion angles, RNA backbone torsion angles, and general manifolds discretized as triangular meshes, RW-Flow outperforms existing one-step methods in nearly all settings under fair comparison conditions.

---


### 207. [MegaAvatar: Controllable Talking Avatar Generation](https://arxiv.org/abs/2609.39273)

**<font color=#1a73e8>作者：</font>** Junyao Gao, Sibo Liu, Weidong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents \textbf{MegaAvatar}, a controllable talking avatar generation framework built on top of the Wan2.2-TI2V-5B model. Compared with previous talking-avatar methods that mainly rely on audio or reference-image conditioning, we introduce additional SMPL-X-derived 3D guidance, enabling global control over body pose and head motion. Specifically, we render the driving SMPL-X sequence into dense mesh frames and encode them with a lightweight 3D convolutional encoder, whose outputs are injected into the latent tokens to provide overall motion control. Furthermore, we extend Wan2.2-TI2V-5B with additional audio and face cross-attention modules to enable fine-grained expression control and preserve the input identity, respectively. In addition, we implement an audio-to-SMPL-X model to predict an SMPL-X sequence conditioned on the reference image and input audio, allowing MegaAvatar to support audio-driven inference without user-provided SMPL-X frames. Experiments show that MegaAvatar achieves high-quality talking avatar generation with controllable body and head motion, speech-synchronized facial expressions, and consistent identity preservation. MegaAvatar also supports inference with flexible resolutions and video lengths. Codes, dataset, models will be avaliable in this https URL

---


### 208. [A Tilted Bowl Is Not a Slippery Slope: Compressing Looped Models](https://arxiv.org/abs/2609.39277)

**<font color=#1a73e8>作者：</font>** Steven Kolawole, Pearse Jim, Opegbemi M. Busoye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped models reason by applying the same block of weights many times, so compressing that block saves memory traffic on every loop. Compressed looped models, however, often collapse, and the collapse is usually blamed on rounding error that accumulates from loop to loop. In this work we test that account on more than 30 models from five families and find, to our surprise, that it holds only for loops that never settle. When a loop settles, a fixed rounding error does not accumulate. It moves the point where the loop settles, much as tilting a bowl moves where a ball comes to rest, and the answer is lost only when the shift is larger than the readout tolerates. This picture lets us predict which models fail from a single label-free measurement, and it tells us why failed models recover: their loops still settle, so a few final loops with 8-bit weights bring the answer back. Motivated by these findings, we build a controller that stops when the model's halting head fires and then finishes with 8-bit loops. On Sudoku-Extreme and Maze-Hard it beats fixed-depth inference by up to 15 points under a third of the weight traffic.

---


### 209. [Present After Presence: Subtraction, Givenness, and the Structure of Being-There](https://arxiv.org/abs/2609.39289)

**<font color=#1a73e8>作者：</font>** Koichi Toida  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Presence research has often proceeded by addition, treating immersion, embodiment, agency, ownership, co-presence, reciprocity, and temporal simultaneity as conditions that stabilise the sense of being there. Yet immersive video suggests that several of these conditions can be weakened without eliminating Presence. Building on Bodyless Presence and Bodyless Presentness, this paper asks what is disclosed when such conditions are progressively subtracted. I distinguish three levels that should not be conflated: stabilising conditions that strengthen or support Presence; empirically resilient articulation-forms through which Presence is lived as here and now; and a transcendental limit-condition concerning the first-personal givenness of experience. Subtraction provides evidence for the resilience of here and now, but empirical resilience does not by itself establish constitutivity or transcendental necessity. I argue, on phenomenological rather than experimental grounds, that for-me-ness names the limit-condition within which any such spatial or temporal articulation can be experienced at all. The paper bridges operational Presence research with Husserlian givenness, Leibhaftigkeit, and image consciousness; rereads Bodyless Presence as exposing the resilience of here; rereads Bodyless Presentness as exposing the resilience of now; and develops a stratified account of Presence through Zahavi's pre-reflective self-awareness while taking Derrida's critique of self-presence seriously. It concludes by proposing immersive media as dissociation apparatuses for loosening conditions ordinarily coupled within experiential there-ness.

---


### 210. [Physics-Informed Method of Group Data Handling: Adaptive Construction of Functional Representations with an Application to the Navier-Stokes Equations](https://arxiv.org/abs/2609.39291)

**<font color=#1a73e8>作者：</font>** Mykhailo Minin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed computational methods usually optimize parameters within a functional representation whose structure is fixed in advance. This work proposes a Physics-Informed Method of Group Data Handling (PI-GMDH), in which representations of coupled physical fields are progressively constructed during solution. Candidate functional directions are evaluated through the first variation of the complete physical and observational objective, introduced in packages, and followed by block-coordinate damped Gauss-Newton coefficient optimization. The framework is demonstrated with tensor-product Chebyshev functions on the incompressible Navier-Stokes equations using a two-dimensional time-dependent Taylor-Green benchmark. Under the tested configuration, adaptive PI-GMDH reached validation and held-out test losses of 5.299e-19 and 5.296e-19 with 204, 201, and 175 active functions for u, v, and p. Complete degree-by-degree and all-terms PI-GMDH variants, together with selected PINN and KAN reference configurations, are used to examine the effect of structural construction policy. The results show that, for this controlled synthetic benchmark, selective progressive construction can provide a favorable combination of accuracy, representation size, and wall-clock time. The comparison is illustrative rather than a claim of universal superiority over alternative physics-informed approaches.

---


### 211. [Semantic-Aware Joint Source-Channel Optimization for Encoder-Agnostic Digital Video Communication](https://arxiv.org/abs/2609.39296)

**<font color=#1a73e8>作者：</font>** Xiangben Zhu, Caili Guo, Yang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video semantic communication has attracted increasing attention as a promising approach to improving video transmission efficiency. However, most existing approaches rely on computationally intensive deep learning-based video encoders and decoders, which hinders their deployment in resource-constrained scenarios. To address this issue, we propose a lightweight semantic-aware joint source-channel optimization (SAJSCO) scheme that can be integrated into existing digital video communication systems as a plug-in module. Specifically, we develop a video communication system model in which the transmitter jointly optimizes source and channel coding parameters based on the inter-frame semantic importance of the input video and estimated channel state information. On this basis, we formulate an optimization problem that maximizes semantic importance weighted video reconstruction quality under a maximum bitrate constraint. To solve it, we first quantify inter-frame semantic importance using a cosine similarity-based metric with a shifted window mechanism. We then develop a multi-actor proximal policy optimization (MPPO) algorithm to solve the formulated problem by jointly adapting the source compression rate and channel coding rate. The learned policy can be directly applied to different video encoders without encoder-specific retraining or fine-tuning. SAJSCO achieves Bjøntegaard Delta rate reductions of 34.86\% and 18.01\% when integrated with H.265, a conventional video encoder, and DCVC-RT, a deep learning-based video encoder. Over-the-air experiments on a hardware testbed further demonstrate a PSNR gain of up to 1.448 dB with H.265 and an LPIPS reduction of up to 0.033 with DCVC-RT compared with the respective best-performing fixed-parameter baselines.

---


### 212. [BMASH: Ball-Motion-Aware Soccer Header Spotting](https://arxiv.org/abs/2609.39300)

**<font color=#1a73e8>作者：</font>** Ahmed Endris Hasen, Muhammad Shahzad Khan, Nikolaos Passalis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in computer vision have made broadcast sports videos increasingly useful for event analysis, performance assessment, and player-safety applications. In soccer, however, header spotting remains a challenging problem due to the subtle and short-lived nature of header events. This paper focuses on soccer header spotting: identifying moments in broadcast videos where the ball contacts a player's head. We first adapt and evaluate Video Swin as a strong action-recognition baseline for this task, and then introduce BMASH, a ball-motion-aware fusion framework that integrates detector-derived ball features. BMASH combines Video Swin action representations with ball-presence and motion features from frame-level soccer-ball detection, integrating player-action context with ball dynamics to distinguish headers from visually similar events. We evaluate BMASH using game-level splits with separate test matches and rotating validation folds, considering both centered-window classification and continuous full-video spotting. Results show that Video Swin provides a strong baseline for header spotting, while BMASH improves clip-level AP and ROC-AUC over the corresponding Video Swin baseline. In continuous full-video spotting, BMASH achieves a comparable event-level F1-performance with a different precision--recall trade-off.

---


### 213. [XIM: The XDC Interledger Messaging Protocol](https://arxiv.org/abs/2609.39310)

**<font color=#1a73e8>作者：</font>** Atul Khekade, Ritesh Kakkad, Wanwiset Peerapatanapokin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed ledgers, privacy-preserving institutional networks, and conventional payment systems increasingly need to exchange authenticated messages and settle assets across heterogeneous trust domains. Existing interoperability systems typically optimize for one of three concerns: application-level abstraction, cross-chain message transport, or synchronized execution within a related ledger family. This paper proposes XIM, the XDC Interledger Messaging Protocol, a chain-agnostic protocol for transporting canonical messages across heterogeneous networks while allowing each communication lane to select an explicit verification policy. XIM separates message semantics from transport, verification, execution, routing, asset identity, and compliance metadata. Its cryptographic state is represented by deterministic message identifiers and commitment roots, while an append-only transition log provides auditability and replay protection. XIM introduces a Universal Asset Identifier (UAID), a pluggable adapter interface, lane-scoped security policies, and an optional policy-aware route graph for multi-hop settlement. XDC Network can serve as a coordination and settlement domain without requiring every XIM message or route to transact through XDC. We specify the protocol model, state machine, message encoding, commitment structure, verification modes, failure semantics, security assumptions, threat model, implementation architecture, and an incremental deployment plan. The design targets public blockchains, permissioned ledgers, institutional networks, and authenticated financial-system gateways, with particular attention to stablecoins, tokenized assets, trade finance, and ISO 20022-compatible payment workflows.

---


### 214. [When Data Becomes Judgment: Misaligned Interpretations and Accountability in Food Delivery Platforms](https://arxiv.org/abs/2609.39311)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Shuoning Shi, Bingyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Food delivery platforms mediate service encounters through real-time tracking data. While presented as objective, such data often obscures the situational constraints shaping delivery work, producing systematic misalignments between user perception and courier experience. This study presents a socio-technical analysis of real-time mobile tracking systems in the wild. Through semi-structured interviews with 23 users and 17 couriers on Chinese food delivery platforms, we identify two interrelated dynamics. First, users operate within a data-as-behavior interpretive framework, translating spatial and temporal anomalies into moralized judgments of courier negligence. Second, couriers engage in anticipatory data management, a form of hidden digital labor in which they reshape their physical behavior to produce interface-legible trajectories rather than physically optimal ones. Together, these findings expose a burden-shifting mechanism---characterizing the systemic outcomes of decontextualized interface design rather than explicit designer intent---in current tracking architectures, demonstrating how current tracking architectures leave gig workers bearing much of the explanatory burden. We propose design directions toward contextual transparency, redistributing this explanatory burden from individual workers to the platforms that possess the logistical context to bear it.

---


### 215. [NarrativeSteward: Coordinating Delegation, Guidance, and Verification in Agent-Assisted Interactive Narrative Authoring](https://arxiv.org/abs/2609.39333)

**<font color=#1a73e8>作者：</font>** Wenjin Wang, Jiazhen Lei, Yuxin Sha 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents can turn authors' goals into interactive narratives by independently organizing and carrying out generation and revision. As agents generate and revise extensive content, authors struggle to grasp its overall structure, local details, and relationships, complicating continued guidance. We present NarrativeSteward, an authoring environment that organizes outlines, worldbuilding, and narrative graphs as linked artifacts for agent implementation and author guidance. Agent dialogue and project-wide structural review help authors understand the evolving work and guide local and cross-layer revisions, while change records and execution verification help authors assess the resulting work. Technical tests validated the system's change records, recovery mechanisms, and execution diagnostics. In a 12-participant within-subject study, NarrativeSteward supported easier formulation of revision requests and inspection of changes, and greater perceived understanding of changes and story structure, than general-purpose agents. Qualitative findings show how reviewing the work and feedback helps authors develop requirements and guide subsequent delegation. We open-source NarrativeSteward at this https URL.

---


### 216. [TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335)

**<font color=#1a73e8>作者：</font>** Zijing Qin, Jun Zhou, Ruicheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video virtual try-on has attracted increasing attention due to its broad potential in digital fashion and intelligent e-commerce. However, existing methods primarily focus on low-resolution settings and still face substantial challenges when extended to high-resolution scenarios. These limitations can be attributed to two main factors: (1) the insufficient utilization of rich garment reference information, and (2) the lack of explicit positional modeling between garment and video representations during cross-modal interaction, which weakens fine-grained local correspondence. To address these issues, we propose TexTailor, a high-fidelity video virtual try-on framework built upon a pretrained video Diffusion Transformer. Specifically, we introduce a timestep-adaptive modulation mechanism to dynamically adjust garment visual representations throughout denoising. We further develop a frame-aligned positional encoding strategy to strengthen garment-to-video correspondence, together with a multi-source injection design that reduces interference among heterogeneous conditions. Extensive experiments on multiple video virtual try-on benchmarks, including the high-resolution Eevee dataset, demonstrate that TexTailor achieves competitive performance in garment detail preservation, temporal consistency, and overall video quality.

---


### 217. [How Many Samples Are Enough for Learning Across Domains?](https://arxiv.org/abs/2609.39336)

**<font color=#1a73e8>作者：</font>** Hong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the fundamental mechanisms of learning is essential for designing systems with strong generalization. Recent studies have shown that increasing the number of training domains, or enlarging the distribution shift among them, improves generalization when each domain contains sufficiently many data samples. However, the conditions under which the data samples can be considered sufficient remain unexplored. In this work, we fill this gap by establishing criteria for per-domain sample requirements based on the presented learning bounds. These criteria not only reveal an inverse linear scaling law between the number of training domains and the number of samples required per domain, but also explain the fundamental rationale behind the assumption of data sufficiency, thereby providing theoretical guidance for assessing the adequacy of existing datasets and constructing datasets. This differs from classical learning theory, as the number of samples required is highly dependent on the number of training domains. Additionally, we prove the close relationship between in-domain learning and out-of-domain generalization through the presented generalization bounds, and lastly discuss some key arguments.

---


### 218. [Learning Beyond Full Imitation: Task-Preserving Knowledge Distillation](https://arxiv.org/abs/2609.39338)

**<font color=#1a73e8>作者：</font>** Qianfeng Yuan, Wenbing Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers knowledge by encouraging a student to match a teacher's predicted class probabilities. These probabilities express not only confidence in the correct class, but also relations among incorrect alternatives. Yet closer imitation does not necessarily yield a better student. A student may already distinguish the correct class more sharply than its teacher, so further imitation can require giving back discrimination it has acquired. Our main result is an exact separation between full imitation and conditional learning. When the correct class's score advantage over each alternative must be preserved, full teacher-to-student KL minimization is blocked exactly when the student assigns no more probability than the teacher to every incorrect class. Crucially, the teacher's relative probabilities among incorrect classes remain fully learnable. We characterize the exact price of this transfer: a minimum increase in correct-class log-odds that compensates for the largest conditional-probability mismatch. Label fitting and conditional matching can therefore be completed even as full teacher KL diverges. This separation motivates task-preserving knowledge distillation (TPKD), which keeps the label gradient intact and minimally corrects the conditional gradient so that its output update preserves the label step's gains against every incorrect alternative. The corrected conditional direction retains more than half of the original first-order conditional descent at the same step size, with a tight bound. For a fixed positive conditional target and sufficiently small constant output steps, label and conditional errors vanish together. Experiments trace this learning from exact head updates to ordinary network training. TPKD reaches 88.05% accuracy on CIFAR-100 and 93.81% on CLINC150, improving over standard distillation by 0.47 and 0.35 percentage points across three seeds.

---


### 219. [ElectrolyteFM: Unifying Electrolyte Property Prediction through Cross-Property Knowledge Learning](https://arxiv.org/abs/2609.39340)

**<font color=#1a73e8>作者：</font>** Jiaxin Yu, Shuo Wang, Peng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrolyte formulation design requires balancing multiple physicochemical properties, yet existing models often focus on a limited subset. Learning each property in isolation can overlook transferable chemical information, whereas indiscriminate sharing can introduce cross-property interference. Our directed transfer analysis shows that jointly learning two property prediction tasks can improve or degrade prediction relative to separate training, with asymmetric transfer effects between the tasks. We propose ElectrolyteFM, a unified multi-property prediction model which can more accurately predict multiple properties of each electrolyte by effectively identifying and utilizing property-specific features and knowledge shared across properties. More specifically, ElectrolyteFM learns property-specific representations independently and captures cross-property knowledge through a separately trained expert pool. A router selects relevant shared information for each formulation and target property, and property-specific residual adapters convert this information into corrections to the corresponding representation for prediction. Experiments on Electrolyte12 show that ElectrolyteFM reduces normalized mean absolute error averaged across 12 electrolyte properties by 14.8% relative to the strongest electrolyte-specific baseline. On an independent sodium-electrolyte dataset unseen during training, it reduces conductivity mean absolute error by 6.7% relative to the best-performing baseline.

---


### 220. [The Golden Path Hypothesis: Reusable Schedules in Diffusion Caching](https://arxiv.org/abs/2609.39343)

**<font color=#1a73e8>作者：</font>** Dong Wang, Wenwu Tang, Francesco Corti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion caching accelerates generation by replacing transformer computation with cached or predicted features at selected denoising steps. We introduce the Golden Path Hypothesis (GPH): under fixed inference conditions, prompt-independent cache schedules can achieve final-output quality comparable to the best prompt-specific schedules across prompts. We investigate the GPH across ten caching methods, four image and video models, and three cache ratios. Prompt-adaptive methods repeatedly select a small number of schedules, and reusing their most frequent schedules on new prompts closely matches the quality of prompt-specific choices. Exhaustive evaluation of 1.4 million schedules on four examples further identifies prompt-independent schedules that remain competitive on unseen prompts. To explain this transfer, we analyze denoising trajectories and the accumulation of caching errors. Latent-state trajectories exhibit similar structures across datasets and seeds, while an exact error decomposition shows that accumulated effects of earlier errors predict final latent-state error better than local approximation errors. This motivates searching for end-to-end schedules using final-output quality. With only a small set of examples, the resulting golden paths transfer across prompts and datasets, and can be tuned to the desired quality objective, including reconstruction fidelity or perceptual similarity.

---


### 221. [On the Complexity of Preference-Based Bandits](https://arxiv.org/abs/2609.39351)

**<font color=#1a73e8>作者：</font>** Ahmed Ben Yahmed, Marc Abeille, Clément Calauzènes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study preference-based bandits with general reward function classes, where a learner sequentially selects pairs of arms and observes binary preference feedback governed by the Bradley--Terry model. This setting naturally arises in applications such as recommender systems, tournament ranking, and learning from human feedback, where relative preferences are easier to elicit than absolute rewards. The observation model inherits the logistic bandit challenge of handling the problem-dependent constant $\kappa$, which accounts for the non-linearity of the link function and can grow arbitrarily large. Moreover, prior work has predominantly focused on linear or kernelized reward models, precluding the use of richer function classes. To address these limitations, we consider general reward function classes and introduce the \emph{locally sensitive eluder dimension}, a novel complexity measure tailored to the logistic structure of preference feedback that yields fine-grained regret guarantees without unfavorable dependence on $\kappa$. Building on this notion, we propose \textbf{GINOP} (Generic INformative OPtimism), an algorithm that constructs log-loss confidence sets and jointly selects arm pairs to balance optimism and informative exploration. We establish a first-order regret bound that, in contrast with what previous results suggest, demonstrates that learning with preference feedback is as statistically efficient as learning from direct reward observation. Finally, we corroborate our theoretical findings with empirical evaluations against competitive baselines.

---


### 222. [Robustifying Asynchronous SGD via Soft Throttling](https://arxiv.org/abs/2609.39357)

**<font color=#1a73e8>作者：</font>** Kaoru Otsuka, Maxime Meyer, Yuki Takezawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous SGD is a popular algorithm for distributed learning where each client's gradient update is applied on arrival. This leads to a speed-up, but also an increased vulnerability to attacks, as fast clients can dominate the total update. We introduce Throttle, a Byzantine-robust generalization of asynchronous SGD where the key idea is to exponentially down-weight updates from faster clients by a factor $q$. Both asynchronous SGD ($q=1$) and synchronous Byzantine-robust SGD ($q\to\infty$) correspond to specific settings of Throttle. We provide a theoretical analysis of the convergence rate and validate the robustness to attacks both theoretically and empirically. Remarkably, our experiments show that this down-weighting mechanism can also improve performance over standard asynchronous SGD even in the non-Byzantine setting.

---


### 223. [Link Inference Attack on Privacy-Preserving Knowledge Graphs](https://arxiv.org/abs/2609.39362)

**<font color=#1a73e8>作者：</font>** Emna Bouguerra, Ibtissam Harrouche, Ferran Alborch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are widely used to store and share structured information across sensitive domains such as healthcare, fi- nance, and social networks. A common privacy practice is to delete sen- sitive relations before publishing the graph, under the assumption that removing edges is sufficient to prevent their recovery. In this paper, we challenge this assumption and show that even when a relation is fully or partially hidden, its existence leaves structural traces in the public graph that can be exploited to recover it with high accuracy. To this end, we propose a link inference attack that operates on the topology of the public graph, and evaluate it under two privacy scenarios that differ in how the adversary exploits the knowledge available to him. In the first setting where the adversary exploits all topological information, the attack achieves near-perfect discrimination (AP = 0.949, ROC-AUC = 0.999), while in the more realistic one where the adversary makes use of some semantic information, it recovers up to 74% of hidden edges. Build- ing on these results, we further conduct a structural analysis to identify which topological properties of the graph drive the attack success, re- vealing that privacy risk is not uniform across entities and that certain structural patterns make specific relations significantly more vulnerable to inference than others.

---


### 224. [COBICount: Separating Object and Background Responses for Remote Sensing Object Counting Without Training on Target Data](https://arxiv.org/abs/2609.39366)

**<font color=#1a73e8>作者：</font>** Junjing Zheng, Zhiyi Zhou, Ningrui Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing object counting estimates how many buildings, vehicles, or ships appear in overhead images. Most supervised counters predict a density map, whose sum gives the object count, and assume similar categories, sizes, and backgrounds. Applying them across regions, sensors, or categories often requires target data or further training, which may be costly or unavailable. We study source-only counting. Training for the counting task and model selection use one group of images that shares an object category and similar imaging conditions, with one point marking each object. Target images and information remain unavailable until the model is fixed. This reduces data preparation but makes transfer harder. A model trained on one source may place high density values, called responses, on real objects and repeated background structures. Road edges, parking grids, roof boundaries, and water boundaries may then be counted as objects, creating candidate origin ambiguity. COBICount separates response generation, acceptance, and background suppression. Candidate Evidence (CE) generates possible responses. Candidate Acceptance (CA) keeps compact responses centered on objects. Bias Isolation (BI) reduces responses associated with repeated background structures. Their outputs form the final density map. Trained on RSOC Building and evaluated directly on DOTA Large Vehicle, Small Vehicle, and Ship, COBICount achieves the lowest mean absolute error (MAE) averaged over the target domains among the compared methods, 174.132. It uses 5.07 million parameters and 17.41 billion floating point operations for a 512x512 input. COBICount improves transfer without target data or training for each target. The code will be available at: this https URL.

---


### 225. [Making Grid Beam Search Less Greedy](https://arxiv.org/abs/2609.39368)

**<font color=#1a73e8>作者：</font>** Sean Papay, Roman Klinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common formalism for constraining the output of autoregressive text generation models involves lexical constraints, words or phrases which are required to occur in the generated text. DFA-constrained beam search and grid beam search are two widely used paradigms for decoding from autoregressive models while enforcing lexical constraints. As the former approach requires a number of forward passes exponential in the number of constraint tokens, it is often dispreferred to the latter, which requires only linearly many forward calls. However, while grid beam search achieves an exponential speedup, it does so in a manner which does not treat all of the constraints equally. In this paper, we demonstrate that grid beam search is biased to incorporate easier-to-satisfy constraints first, leaving harder constraints to the end of the sequence. This contrasts with DFA-constrained beam search, which exhibits no such bias. To address this shortcoming, we propose fair grid beam search, a modification to grid beam search which avoids this bias while still requiring only linearly many forward passes. Experimentally, we confirm grid beam search's bias on two constrained generation tasks, finding significant differences in how it orders constraint tokens as compared to DFA-constrained beam search and fair grid beam search. Furthermore, we find that fair grid beam search not only fixes grid beam search's bias, but finds higher-probability strings in the process.

---


### 226. [Wavelet Flow Matching for Time Series](https://arxiv.org/abs/2609.39374)

**<font color=#1a73e8>作者：</font>** Lucas Poinsignon, Jorge da Silva Gonçalves, Samuel Ruipérez-Campillo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic time series are increasingly used for data augmentation, privacy-preserving data sharing, and downstream model development, yet faithfully reproducing both multi-scale temporal structure and cross-channel dependencies remains challenging. We study multivariate time-series generation through flow matching in the wavelet domain. By operating on multilevel discrete wavelet coefficients rather than directly in the time domain, the model represents coarse structure and progressively finer details at separate scales. Their naturally different variances further induce an implicit coarse-to-fine generative process without requiring an explicit multi-scale schedule. Since the transform acts independently on each channel, we pair it with a channel-token transformer whose attention directly models cross-channel dependencies. Across seven benchmark datasets and four sequence lengths, our method is best or tied on a majority of dataset-metric combinations, with the largest and most consistent improvements in Context-FID and discriminative score.

---


### 227. [InfoAgent: Traceable Generation and Repair of Evidence-Grounded Infographics](https://arxiv.org/abs/2609.39380)

**<font color=#1a73e8>作者：</font>** Yifan Li, Tong Li, Qi Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable infographic generation requires facts, symbols, and visual relations to remain consistent through rendering and revision. Correcting one element also requires tracking its supporting evidence and the dependencies affected by the change. We present \textbf{InfoAgent}, a training-free framework for \emph{evidence-bound visual-symbolic program synthesis}. Its Infographic Visual Description (IVD) records factual payloads, evidence provenance, execution routes, and verification obligations in a typed dependency graph. Retrieved design priors guide compilation, and layered execution combines raster synthesis with editable symbolic and binding objects while retaining their traces. Dependency-aware repair localizes corrections, rechecks affected dependencies, and requires protected obligations to remain satisfied under the declared checkers. Unresolved obligations remain explicit. On IGenBench, InfoAgent achieves 93.0 Q-ACC and 59.0 I-ACC. We also introduce InfoGraphicBench-Evidence, where complete-checklist pass rates on 200 test requests increase from 21.5\% for Same-IVD Prompt to 23.5\% for the initial layered output and 28.5\% after repair, using the same evidence and initial IVD. On 120 audited repair cases, localized repair edits 12.4\% of the canvas on average, compared with 67.3\% for global regeneration.

---


### 228. [TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic](https://arxiv.org/abs/2609.39385)

**<font color=#1a73e8>作者：</font>** Bhuvanesh Verma, Ali Abusaleh, Alexander Mehler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argument Mining (AM) is a critical NLP task that remains significantly under-resourced in Arabic. This paper presents $\testtt{STAR-Ar}$, a BERT-BiLSTM-CRF architecture for argument discourse detection and classification, as our system for Daleel 2026, the inaugural Arabic argument mining shared task. The task requires the identification and classification of argumentative discourse units (ADUs) in debate and editorial this http URL jointly model these two objectives as a token-level sequence labeling task using a BERT-BiLSTM-CRF architecture that combines contextual transformer embeddings with structural transition constraints to support accurate span detection. $\testtt{STAR-Ar}$ achieves an F1-score of 72.69 on validation and 73.7 on test data. Our domain-specific analysis shows that models trained exclusively on editorials underperform those trained on debates, a disparity we primarily attribute to the smaller size of the editorial dataset. The code for $\testtt{STAR-Ar}$ is available at ${\href{this https URL}{\faGithub~TTLab at Daleel 2026}}$

---


### 229. [Beyond Simulation: Retain-and-Repair Neural Operators for Real-World Adaptation](https://arxiv.org/abs/2609.39387)

**<font color=#1a73e8>作者：</font>** Woojin Cho, Junghwan Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators increasingly benefit from pretraining on numerical simulations, yet adapting them for real-world prediction remains challenging. We introduce the Retain-and-Repair Neural Operator (R$^2$NO), a framework for adapting simulation-pretrained operators to real-world data while retaining useful pretrained structure. The pretrained operator is first finetuned on real data and then frozen to provide a source prediction, and a shared repair module learns a sequence of refinements from the same observations. Using orthogonal Fourier projections, a spectral ensemble fits a small ridge regression within each cell of the Fourier domain and combines the refinements by weights fitted on a held-out split of the real data. The cells are defined jointly by radial ranges, angular sectors, and measured channels, allowing refinement depth to vary with frequency magnitude, with orientation, and across channels. Including the source prediction as a candidate makes retention available in every cell, and independently trained repair modules enter the same combination as additional candidates. On all RealPDEBench systems and six backbones, R$^2$NO consistently outperforms full finetuning and iterative refinement. The framework treats adaptation depth as a cell-specific choice learned from real data.

---


### 230. [Decoupled and Distilled: Task-Adaptive LoRA-Teachers with Ensemble Knowledge Transfer for Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2609.39390)

**<font color=#1a73e8>作者：</font>** Hongwei Zhao, Rui Liu, Yansong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-Shot Class-Incremental Learning (FSCIL) addresses the challenge of learning new classes from very limited samples while retaining knowledge of previously learned ones. Although parameter-efficient fine-tuning methods with pre-trained models show promise for class-incremental learning, strict gradient-based constraints can be unreliable under severe data scarcity, while multi-expert approaches can impose substantial inference-time costs. We propose TALON (Task-Adaptive LoRA-Teachers with Ensemble Knowledge Transfer), an inference-efficient FSCIL framework. TALON dynamically allocates an independent LoRA-Teacher to each incremental task for task-specific representation learning, then distills multiple frozen teachers into a unified LoRA-Student through Ensemble Knowledge Transfer, eliminating runtime module selection or generation. A semantic-guided distillation strategy weights teacher contributions by feature-space similarity to mitigate catastrophic forgetting and overfitting. Across three class-order runs, TALON achieves comparable or better mean average accuracy across four FSCIL benchmarks, obtaining 86.68 +/- 1.22% on CUB200, 90.39 +/- 0.27% on CIFAR100, 78.38 +/- 0.94% on ImageNet-R, and 96.34 +/- 0.33% on miniImageNet. TALON uses up to 33x fewer deployment parameters and reduces average inference time per task to 26.7 s, a 41.70% reduction relative to ASP.

---


### 231. [Experimental Experience Modeling for Autonomous Research](https://arxiv.org/abs/2609.39392)

**<font color=#1a73e8>作者：</font>** Wenda Wei, Yingchen Zhang, Ruqing Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents can generate hypotheses and conduct experiments, but experimentation remains a major source of computational cost. A fundamental challenge is deciding which experiments are worth running, particularly when prior evidence is insufficient to resolve uncertainty. Yet current research agents lack a systematic way to leverage experimental experience when making such decisions. We introduce Experimental Experience Modeling (EEM), a framework for making informed experimental decisions by acquiring, reusing, and accumulating experimental experience. EEM extracts decision-relevant records from earlier experimental trajectories, distills them into reusable experience, and organizes them in an experience library. For a new experimental decision, EEM retrieves relevant historical experience and assesses whether it provides sufficient support for deciding whether a candidate direction warrants further investment. When historical experience is insufficient, EEM conducts a targeted, low-cost pilot experiment to acquire the missing decision-relevant experience on demand. It then combines this newly acquired experience with retrieved historical experience to determine whether the direction warrants full-scale evaluation, which requires substantial resources. The resulting experimental outcomes are further distilled into reusable experience, allowing the library to continually grow through iterative accumulation. Experiments on autonomous research benchmarks show that EEM improves research performance while reducing model interaction overhead, demonstrating the value of reusing accumulated experience and acquiring additional experience only when needed.

---


### 232. [Awakening of the Buddha: Subspace Learning During Population-Loss Plateaus](https://arxiv.org/abs/2609.39408)

**<font color=#1a73e8>作者：</font>** Akash Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Population loss can remain nearly constant while a neural network learns a substantially more predictive representation. We establish this separation for two-layer ReLU and leaky-ReLU networks trained on Gaussian inputs by simultaneous fixed-step population gradient descent on all parameters. For structured additive teachers whose links are positive mixtures of Gaussian-damped cubics in $H^1(\gamma)$, we give explicit conditions under which small IID Gaussian initialization yields a high-probability guarantee: at a checkpoint during a high-loss plateau, minimum alignment between the rank-$r$ teacher subspace and the leading $r$-dimensional eigenspace of the predictor's average gradient outer product (AGOP) increases by at least $1/2$, and the minimum refit MSE under unchanged coefficient budgets decreases by more than $0.399$, both relative to initialization. The same trajectory subsequently attains a trained loss below every value in the plateau window. A complementary result treats unequal-weight cubic teachers and small additive Sobolev perturbations using projected-feature refits. For SwiGLU networks with an exactly fitted intercept, we prove leading-AGOP alignment during a loss plateau at fixed width and dimension as Gaussian initialization vanishes, for square-integrable teachers with nonzero Hermite content of degree one, two, or three. A rank-one cubic specialization also gives simultaneous unrestricted-refit gains at a prescribed width. An approximation lower bound further shows that certain interaction targets retain nonzero error when ridge neurons are restricted to shared orthogonal axes within the teacher subspace. Population-moment experiments with ReLU students across 21 teachers and 50 initializations per teacher complement the analysis.

---


### 233. [Aligning the Incomplete: Joint Distribution Calibration for Multimodal EEG-Eye Emotion Recognition](https://arxiv.org/abs/2609.39413)

**<font color=#1a73e8>作者：</font>** Yang Wu, Jinpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The success of cross-subject multimodal emotion recognition hinges on maintaining the consistency of the joint data distribution across individuals. However, real-world deployment frequently triggers the \emph{asymmetric joint distribution collapse}: EEG signals suffer from severe cross-subject distribution shifts, while eye movements sensors are susceptible to packet loss and tracking failures. Existing methods treat domain adaptation and missing-modality imputation as disjoint tasks. Consequently, they fail to resolve the compounded errors when both degradations co-occur, either propagating domain shifts through imputed signals or destroying the joint decision boundary. To tackle this unified challenge, we propose GUARD (\textbf{G}radient-guided \textbf{U}nsupervised \textbf{A}symmetric \textbf{R}ecovery of \textbf{D}istributions). First, GUARD establishes a reliable anchor manifold in the source domain by employing a theoretically grounded gradient-weighted objective, which forces the robust EEG modality to preemptively entangle task-discriminative ocular features. Next, to structurally recover the collapsed joint distribution, we constrain a generative module with downstream perceptual losses, prioritizing emotion-discriminative semantics over mere signal fidelity. Finally, we formulate target-domain adaptation as an ill-posed inverse problem. By driving a cycle-consistent flow, we achieve unsupervised calibration of the recovered joint distribution directly on the target-domain manifold. Extensive experiments demonstrate that GUARD significantly outperforms state-of-the-art methods, maintaining resilient discriminative performance even under complete auxiliary modality failure. Our code and models are made publicly available to ensure complete reproducibility.

---


### 234. [IDEAL: A Multimodal Domain Adaptation Framework for EEG-Eye Emotion Recognition](https://arxiv.org/abs/2609.39421)

**<font color=#1a73e8>作者：</font>** Yang Wu, Jinpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) emotion recognition serves as a pivotal interface for human-computer interaction, yet the physiological variability across individuals complicates the already challenging task of fusing heterogeneous physiological signals (e.g., EEG and eye movements). However, most prevalent domain adaptation paradigms are tailored for unimodal scenarios, failing to address the heterogeneity of multimodal signals. Furthermore, they predominantly rely on feature-level alignment, overlooking the fundamental data-level discrepancy, which risks compromising fine-grained discriminative information during aggressive adaptation. To bridge these coupled gaps, we propose Instance-based Domain Expansion and Adversarial Learning (IDEAL), a unified framework that synergizes instance-level curriculum expansion with feature-level hierarchical adversarial alignment. IDEAL first introduces a multi-model collaborative screening mechanism, which propagates high-confidence target samples to explicitly bridge the distributional gap at the data level via a quantity-quality equilibrium strategy. We provide a theoretical analysis that this instance expansion strategy strictly tightens the upper bound of the target risk. Subsequently, a hierarchical adversarial network, augmented with the angular-contrastive constraints, progressively aligns representations from low-level statistics to high-level semantics while preserving class separability. Extensive experiments on four benchmark datasets demonstrate that IDEAL significantly outperforms state-of-the-art methods. To facilitate reproducibility and future research, our source code is publicly available at this https URL.

---


### 235. [PCB-MC: Missing Component Analysis in Printed Circuit Boards](https://arxiv.org/abs/2609.39427)

**<font color=#1a73e8>作者：</font>** Betsy Villa Brochero, Ian Gibson, Estefania Talavera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting missing components on printed circuit boards (PCBs) differs fundamentally from conventional object detection, as the model must localize components that are not present. We introduce PCB-MC, a curated dataset for missing component detection with footprint level annotations built on top of the RF100 dataset. The dataset contains 197 distinct board types, each corresponding to a unique PCB design, with multiple augmented samples per type. We also provide benchmark results on PCB-MC by evaluating a diverse set of supervised and unsupervised methods. To ensure fair evaluation, we propose board type aware cross validation splits that prevent layout leakage between training and test sets. Supervised models showcase high false negative rates on unseen board designs, and unsupervised anomaly detection methods fail entirely due to the lack of spatial alignment with a board specific reference. These results confirm that missing component detection on diverse PCB layouts remains an open challenge. We release PCB-MC and all training protocols to support reproducible research on structural absence detection in industrial inspection.

---


### 236. [Towards Trustworthy AI for Glioma Diagnosis: A Task-Aware Evaluation of Uncertainty Quantification](https://arxiv.org/abs/2609.39429)

**<font color=#1a73e8>作者：</font>** Gonzalo Esteban Mosquera Rojas, Sebastian R. van der Voort, Carolin M. Pirkl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty Quantification (UQ) is a key requirement for trustworthy AI in high-stakes medical image analysis. In this work, we evaluate UQ in a multi-task Deep Learning framework for MRI-based glioma diagnosis that performs tumor segmentation and predicts IDH mutation status, 1p/19q co-deletion status, and tumor grade. Monte Carlo Dropout (MCD) is used for a detailed task-aware analysis of predictive, aleatoric, and epistemic uncertainty. We assess MC sample convergence, calibration, error detection, selective prediction, associations with segmentation performance, and the effect of voxel-wise uncertainty aggregation on case-level reliability. We also compare MCD with Deep Ensembles (DE) and Monte Carlo Deep Ensembles (MCDE), examine interactions between segmentation quality and classification, and evaluate a composite trust score integrating segmentation and classification uncertainty. Across tasks, uncertainty estimates supported meaningful error detection, while calibration depended on the dropout rate, with moderate rates yielding the most reliable probabilities. Uncertainty decomposition provided task-dependent interpretability but did not consistently improve error detection over predictive uncertainty alone. DE and MCDE showed comparable operational utility, with no method consistently dominating across tasks and metrics. The composite trust score did not consistently outperform classification uncertainty for selective prediction. Overall, our results provide a task-aware evaluation strategy and practical guidance for the development of trustworthy AI for glioma diagnosis.

---


### 237. [DuplexAct-Bench: Broadening Full-Duplex Speech Evaluation toward Proactive Interaction across Diverse Behavioral Requirements](https://arxiv.org/abs/2609.39446)

**<font color=#1a73e8>作者：</font>** Keyue Xing, Wentao Ding, Mengmeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing full-duplex speech benchmarks cover only subsets of real-time interaction behaviors, often under limited contextual conditions. We introduce DuplexAct-Bench, a bilingual benchmark that systematically covers six complementary behaviors, from interruption and yielding to proactive initiation, active silence, and backchanneling, across Pre-session, In-session, and No-explicit conditions. Across 1,290 English and Chinese streaming trials, we evaluate 12 full-duplex speech systems on both Timing and Content. Results reveal substantial variation across behaviors, conditions, and systems, as well as frequent mismatches between semantic quality and behavioral timing. These findings show that current systems remain far from robustly managing when, whether, and how to participate as real-time interaction unfolds. Project page: this https URL

---


### 238. [ResARC: Residual-Aware AutoRegressive Coding for Ultra-Low Bitrate Image Compression](https://arxiv.org/abs/2609.39451)

**<font color=#1a73e8>作者：</font>** Qin Yan, Ruixiao Dong, Yutao Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progressive autoregressive image codecs provide an appealing paradigm for generative compression by quantizing continuous latents into discrete tokens, transmitting coarse-to-fine prefix tokens and generating the remaining suffix tokens at the decoder. However, their reconstruction quality is fundamentally limited by two residuals introduced along this pipeline: the quantization residual, arising from information loss during discrete tokenization, and the generation residual, resulting from imperfect autoregressive generation of the suffix tokens. To address these limitations, we introduce ResARC, a residual-aware autoregressive codec that explicitly compensates for both residuals at the decoder. Specifically, we generate the quantization residual with a diffusion transformer conditioned on the autoregressive decoding context, while requiring no additional side information. In parallel, we compute the generation residual at the encoder and employ a learned Generation Residual Codec to efficiently compress and transmit it for decoder-side correction. The recovered residuals are then integrated with the reconstructed latent representation and decoded through an adapted VAE decoder. Extensive experiments demonstrate that ResARC achieves competitive perceptual similarity while substantially improving distributional fidelity over leading generative codecs across the ultra-low bitrate regime. Code and models will be released soon.

---


### 239. [Mutual Equilibrium: Multimodal Representation Learning through Reciprocal Feedback](https://arxiv.org/abs/2609.39456)

**<font color=#1a73e8>作者：</font>** Ho-min Park, Byungkon Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proposes a mutual feedback architecture, MEQ, that refines the two inputs, of possibly different modalities, into a pair of coupled embeddings such that each embedding reflects the information of the other. The core idea is to incorporate continuous interchange of information between the two inputs. This idea leads to a mutual feedback architecture consisting of two components whose outputs are fed back into the other. The final output of this model is defined as the fixed point of this interaction. We provide theoretical analysis that offers interpretation of this model as well as design choices to prevent failure cases. We show the benefits of MEQ through classification and visual grounding tasks spanning various datasets. Quantitatively, our model outperforms or shows competitive performance on concatenation-based multimodal classification problems. Qualitatively, the proposed interactive mechanism allows the model to progressively refine the visual grounding when paired with complementary modality, thus demonstrating the power of mutual feedback under such settings.

---


### 240. [Right-Wing Rock or Just Rock? A Computational Linguistic Analysis of Frei.Wild](https://arxiv.org/abs/2609.39460)

**<font color=#1a73e8>作者：</font>** Carlotta Schneeberger, Kevin Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rechtsrock is a subgenre of rock music that spreads right-wing ideology, often instrumentalized to recruit adolescents into the radical scene. Monitoring institutions counteract this by manually examining and, in some cases, banning extremist content; however, there are border cases that evade regulation. We present a study aimed at determining whether such a case, the band this http URL, should be classified as politically right-leaning or as part of the general German rock genre. We sampled a German rock dataset and created a corpus for right-wing rock to use as reference in this analysis and found that we can confirm the intuitions from previous investigations that this http URL successfully maintains an ambiguity with regard to their political affiliation. However, the tendency is towards the right-wing spectrum. Lexical analyses reveal nationalistic narratives and two high-performing classifiers (up to 97% ROC-AUC score) label more than half of their songs as right-wing extremist. Our analysis provides insight into how computational methods can improve the process of identifying right-wing extremist tendencies in music, especially in borderline cases like this http URL. The code and data are made available for future research.

---


### 241. [Understanding Head Geometry and Dynamics in Federated Regression through a Natural Solution Selection Rule: An Unconstrained Feature Model Analysis](https://arxiv.org/abs/2609.39464)

**<font color=#1a73e8>作者：</font>** Chuang Ma, Tomoyuki Obuchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In federated averaging, local objectives can admit multiple optimal heads, making the aggregate depend on which heads clients return. We study this ambiguity in federated multivariate regression with private backbones and a shared linear head, using an unconstrained feature model (UFM) that treats training-sample features as free variables. We introduce a natural selection rule: each client returns the optimal head closest to the broadcast head. We show that global minimization with a vanishing proximal penalty on the head realizes this rule. When the clients' optimal Gram matrices and the initial shared Gram matrix are positive definite, the shared Gram matrix follows a closed recursion and converges to the unique Bures-Wasserstein barycenter of the clients' optimal Gram matrices. Even with this alignment, the limit generally differs from the centralized optimal Gram matrix. We decompose this gap into three positive-semidefinite terms arising from differences in client target means, covariance heterogeneity, and averaging the aligned heads. A correction based on a one-time exchange of target means and covariances recovers the centralized optimal Gram matrix in one round under exact local optimization and the same selection rule. We verify these results numerically in the UFM and test its predictions on five tabular and five image regression datasets using deep networks with feature regularization and long local training. In these experiments, ordinary training approaches the predicted barycenter, while a weak proximal penalty improves endpoint agreement and yields trajectories that closely follow the predicted Gram dynamics. The correction moves the final Gram matrices close to the centralized UFM prediction.

---


### 242. [T-ARC: Topology-Aware Randomized Clustering via Distributionally Robust Stochastic Block Models](https://arxiv.org/abs/2609.39466)

**<font color=#1a73e8>作者：</font>** Serena Grazia De Benedictis, Andersen Ang, Nicoletta Del Buono 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce a new clustering method, namely T-ARC (Topology-Aware Randomized Clustering), that corrects the geometric bias of K-means by embedding topological information directly into the optimization objective. Building on the assumption that the data admits an underlying hidden structure modeled via a latent graph, the idea is to uncover this information through the interplay between the standard K-means data-fidelity term and a graph-cut penalty, which discourages cluster assignments inconsistent with the connectivity structure of the data.
To render this coupling tractable, the latent graph is modeled as a random realization from a Stochastic Block Model (SBM), whose scalar parameter is optimized within a Distributionally Robust Optimization (DRO) framework, yielding a closed-form proximal update. Both SBM and DRO are informed by a persistence-based similarity matrix derived from zero-dimensional persistent homology ($H_0$), which translates the multiscale connectivity structure of the data into a pairwise topological prior. The overall optimization proceeds via Block Coordinate Descent; convergence is established through a global Lyapunov functional: the deterministic blocks satisfy monotonic descent, while the stochastic graph update satisfies descent in expectation, so that the expected energy converges.
Experiments on synthetic datasets with non-convex geometries and on random subsets of Fashion-MNIST show that T-ARC recovers latent topological structures where K-means fails, achieving the highest accuracy on curved and interleaved clusters while remaining competitive, and markedly more stable than K-means, on real data.

---


### 243. [DensePed-Lite: Quality-Aware Adaptive Detection for Dense Pedestrians under Occlusion](https://arxiv.org/abs/2609.39467)

**<font color=#1a73e8>作者：</font>** ZiAn Wang, MingZhe Liu, Chaoyi Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian detection plays a crucial role in computer vision with applications in autonomous driving, surveillance, and public safety. However, real-world dense scenes bring severe challenges, including heavy occlusion, drastic scale variations, and strict real-time requirements. Existing lightweight detectors struggle to balance accuracy and efficiency while often neglecting quality-aware feature modeling and consistency between classification and localization, leading to unstable performance under crowded conditions. To address these issues, we propose DensePed-Lite, a unified framework built on a single principle: under occlusion the network should adapt its behavior to the quality of what it observes rather than assume complete information. This principle is realized at three points where occlusion does the most damage: unreliable confidence scoring (UQE), fragmented spatial coverage (MPSC), and incoherent multi-scale fusion (CTDM). The three mechanisms reinforce one another instead of acting in isolation, all without significantly increasing complexity. Experiments on CityPersons and CrowdHuman validate that DensePed-Lite achieves a superior accuracy-efficiency trade-off compared with recent state-of-the-art lightweight methods, making it suitable for real-time deployment in dense pedestrian scenarios.

---


### 244. [Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning](https://arxiv.org/abs/2609.39473)

**<font color=#1a73e8>作者：</font>** Quan M. Tran, Zhuo Huang, Zhen Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly rely on memory to generalize beyond their training environments. However, agents are bounded by what they have seen and believed, and leveraging such memories in unseen environments can introduce biases into their internal beliefs. We formalize this phenomenon as \textit{false memory}, which can arise from spurious correlations, environment shifts, and knowledge conflicts. Despite its importance, false memory is difficult to evaluate because it stems from agent internal beliefs and is easily confounded with ordinary generalization failures. Therefore, we propose FAME, a training-free framework that evaluates false memory through the evolution of agent beliefs under counterfactual reasoning. Specifically, counterfactual scenarios reveal how beliefs change as the latent concept of memory shifts under hypothetical interventions; thus, measuring the resulting concept drift provides a signal for distinguishing faithful versus false memory. Such concepts can be estimated from agent hidden states before answer generation, avoiding the need for reward design or answer sampling. Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% - 96.7% across false-memory settings, and outperforms the best baseline by 3.4% - 23.3% across realistic benchmarks, spanning math reasoning (GSM-Symbolic), code generation (GitChameleon), and complex reasoning (BigBench-Hard). We further release corresponding counterfactual templates and facilitate future research on false memory.

---


### 245. [From Wrecks to Wisdom: Recovering Crash Mechanics from Real-World Multi-View Photos](https://arxiv.org/abs/2609.39486)

**<font color=#1a73e8>作者：</font>** Ondřej Valach, Václav Diviš, Ivan Gruber  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating accident mechanics from real-world crashes is important for vehicle-safety analysis, injury modeling, crash-severity prediction, and operational workflows such as insurance claim triage. In standard crash records, key metadata such as impact configuration, principal direction of force, and change in velocity ($\Delta V$) may be missing, delayed, or corrupted, while post-crash photographs are widely available and contain rich visual evidence of deformation. We study how much crash-mechanics information can be recovered directly from vehicle photos when structured signals are absent. We formulate crash understanding as supervised prediction from per-case multi-view photo sets. Targets include six Collision Deformation Classification (CDC) descriptors and the longitudinal and lateral components of reconstructed $\Delta V$. Each photo is encoded by a shared visual backbone, and the resulting view-level features are fused into a case-level representation from which target-specific heads predict crash descriptors. Using 15.2k training cases from the Crash Investigation Sampling System, drawn from about 1.5M photos before filtering, together with 1.15k validation and 1.15k test cases, we define an evaluation protocol for vision-based crash descriptor estimation from incomplete multi-view evidence. Post-crash imagery alone provides usable signal for several non-trivial crash-mechanics descriptors, while weakly observable and long-tailed targets remain challenging. Within the compared training regimes, the selected joint-training recipe reduces mean absolute angular error for principal direction of force from 20.1 to 14.05 degrees and longitudinal $\Delta V$ MAE from 8.04 to 7.45 km/h. Our work provides a reference point for future multimodal fusion with structured crash metadata.

---


### 246. [Correcting CondOT: Exact Finite-Step Sampling in Gaussian Flow Matching](https://arxiv.org/abs/2609.39488)

**<font color=#1a73e8>作者：</font>** Ron Levy, Michael Elad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching generates samples by gradually transforming noise into data. In practice, using a finite number of sampling steps introduces a numerical error that depends on the chosen schedule. We study this dependence for Gaussian targets and the explicit midpoint sampling method, using the exact flow field. We measure sampling error by the squared Wasserstein distance between the target distribution and the final distribution produced by the midpoint sampler. We show that the standard conditional optimal transport (CondOT) schedule cancels the leading midpoint error and improves the general convergence bound, even when the sampling steps are unequally spaced. On a uniform grid of $S$ sampling steps, we fix the signal schedule at $\alpha_t=t$ and prove the existence of scalar noise schedules $\beta_t$ that approach the CondOT noise schedule $1-t$ at rate $1/S$ and yield exact Gaussian sampling for every sufficiently large $S$. Controlled Gaussian experiments illustrate the convergence rates and exact calibration.

---


### 247. [Towards Robust Time Series Learning via Capacity-Centric Modulation](https://arxiv.org/abs/2609.39489)

**<font color=#1a73e8>作者：</font>** Siru Zhong, Senzhang Wang, James T. Kwok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample-level reliability heterogeneity is common in deep time series learning. Standard training pipelines apply a uniform regularization setting to all samples, which can under-regularize corrupted samples and over-restrict clean samples. Common robustness approaches filter observations in data space or impose priors on latent representations. We propose Capacity-Centric Modulation (CCM) as a complementary, sample-adaptive regularization principle. Under this principle, we introduce SACM (Sample-Adaptive Capacity Modulation), a task-agnostic framework that exploits spectral sparsity to assign sample-wise dropout probabilities along internal activation paths. SACM integrates into existing backbones without architectural redesign and preserves the deterministic inference pipeline. Across 301 real-world dataset-backbone pairs covering 9 forecasting, 32 classification, and 4 anomaly-detection datasets, SACM reduces forecasting MSE by 6.7% on average and improves classification accuracy and point-adjusted F1 by 3.04% and 17.05%, respectively, relative to unmodified backbones, with zero test-time overhead.

---


### 248. [The Geometry of Randomized Smoothing on Feasible Sets](https://arxiv.org/abs/2609.39497)

**<font color=#1a73e8>作者：</font>** Syed Izhan Khilji, Alireza Furutanpey, Schahram Dustdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized smoothing certifies the probability of a fixed output event as the center of Gaussian noise moves. Feasibility or confidence filtering reports label probabilities only among retained proposals, producing a ratio. Its numerator is a fixed Gaussian event mass, while its denominator is the probability of retention and can change with the center. Substituting this ratio into the ordinary smoothing formula can therefore certify a ball that contains a decision boundary. We separate the problem into a geometric question and a certification question. Geometry determines when conditioning preserves Gaussian comparisons. Convex retained sets preserve the full comparison, while general sets require geometric control of the retained law as the center moves. Without such control, conditional probabilities imply no positive universal radius. Joint retention-and-label probabilities always yield a valid certificate for the same filtered predictor. A uniform covariance bound transfers divergence certificates to the retained law and can yield larger radii even when the Gaussian event comparison fails. Both methods admit finite-sample bounds. For a learned image classifier with a training-selected nonconvex filter, conditional Rényi bounds certify more images than joint-mass bounds without additional model evaluations. A released confidence filter exhibits verified label changes inside radii obtained by conditional substitution. An application of adaptive Gaussian composition covers causal finite-horizon executions with history-dependent center shifts under a pathwise energy bound.

---


### 249. [PartiCam: Camera Controlled Video Generation with Reward Guidance](https://arxiv.org/abs/2609.39504)

**<font color=#1a73e8>作者：</font>** Amine Ouasfi, Runjia Li, Junlin Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PartiCam, a training-free Particle filtering rooted method for improved Camera controlled video generation. Generating videos that follow a precisely specified camera trajectory remains challenging for large video diffusion models. Training-free approaches are backbone-agnostic and avoid the need to construct large camera-annotated datasets by steering pretrained models toward the desired camera motion at test time. This enables the generation of camera-controlled video data that can subsequently be used to train camera-conditioned video diffusion models. Existing sampling-based guidance approaches often suffer from unstable trajectories: they either explore too broadly and fail to respect the target camera motion or collapse early and lose visual diversity over time. We introduce a global-local refinement framework for diffusion reward guidance, enabling accurate and consistent camera control during video generation. Our method builds on Sequential Monte-Carlo (SMC) guidance, but introduces a local refinement stage based on particle filtered resampling. Experiments show large improvements in camera trajectory adherence, reduced drift, and better visual quality, without requiring model retraining.

---


### 250. [Can Domain Generalization be Guaranteed in Small-Sample Learning?](https://arxiv.org/abs/2609.39512)

**<font color=#1a73e8>作者：</font>** Hong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The small-sample learning problem remains a fundamental challenge in machine learning because limited training data lead to unstable model estimation and generalization. Structural Risk Minimization (SRM) has long been regarded as a principled solution under the classical i.i.d. assumption. However, domain generalization (DG) violates this assumption, leaving the theoretical role of SRM in DG largely unexplored. To bridge this gap, we establish the first theoretical guarantees for SRM in DG under mild assumptions. Specifically, based on the concept of stability, we derive learning consistency and generalization error bounds and prove that these bounds become tight when the hypotheses satisfy the stability condition. Building upon this, under a specific hypothesis space assumption, we establish stability, learning, and generalization bounds for SRM. We further discuss the applicability of these bounds to deep learning. This work establishes theoretical foundations for SRM under distribution shifts and sheds light on the design of robust DG algorithms in small-sample scenarios.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
