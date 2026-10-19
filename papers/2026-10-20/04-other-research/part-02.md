# 📦 其他研究 | 2026年10月20日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

---

### 51. [OrderFlowDiT: Transport-Regularized Diffusion Transformer for Probabilistic Limit-Order Supply Forecasting](https://arxiv.org/abs/2610.22727)

**<font color=#1a73e8>作者：</font>** Jung Hun Phee, Tucker Balch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the conditional distribution of limit-order volume submitted over the next five minutes, given the current order book and recent order flow. The task requires capturing price placement, total volume, and predictive uncertainty jointly. Coordinate-wise diffusion losses do not explicitly account for price displacement, while normalizing fields to unit mass removes information about total volume. Agreement on selected summary statistics also does not establish fidelity to the joint field distribution. We introduce OrderFlowDiT, a conditional Diffusion Transformer for unnormalized bid and ask volume-at-price fields, trained with an unbalanced optimal-transport (UOT) auxiliary loss. We also develop a full-field evaluation framework that combines a transport cost sensitive to price placement and total volume with proper scoring rules and calibration diagnostics. In the primary comparison on 1950 validation conditions across 30 U.S. equities, adding UOT reduces full-field transport cost by 45.8% and the transport energy score by 26.1% relative to training with mean squared error alone. Both measures improve for every stock. These findings support incorporating price geometry and volume into generative modeling, with field accuracy and predictive uncertainty evaluated together.

---


### 52. [Thunder-DeID+: Boundary-Aware Korean De-identification from Court Judgments to Broader Sensitive Documents](https://arxiv.org/abs/2610.22733)

**<font color=#1a73e8>作者：</font>** Gyuseong Lee, Gyeongje Cho, Jongmin Kim 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the transferability of a de-identification model developed for Korean court judgments to a broader range of sensitive documents, focusing on boundary precision, label granularity, and recall. The agglutinative structure of Korean causes Byte Pair Encoding (BPE) tokenizers to frequently merge Personally Identifiable Information (PII) with adjacent particles, which complicates accurate span recovery. Furthermore, current PII taxonomies lack sufficient granularity for legal texts. To address these issues, this study introduces Thunder-DeID+, which integrates a refined three-tier PII taxonomy with a boundary-aware tokenizer. The tokenizer enhances a pretrained BPE vocabulary by incorporating N-gram and boundary-scoring components to better align token and PII span boundaries. The proposed approach is evaluated using a tokenizer-independent word-segment-level protocol. On full-length judgments, the tokenizer consistently improves W. Strict Typed F1-score from 0.76-0.77 to 0.87-0.88 across four model sizes (150M, 395M, 750M, and 1B), mainly by increasing precision rather than model scale. With fine-tuning on 1,000 broader sensitive documents, the judgment-trained model further achieves 0.93 W. Strict Typed F1-score, indicating effective transfer beyond court judgments.

---


### 53. [R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop](https://arxiv.org/abs/2610.22740)

**<font color=#1a73e8>作者：</font>** Mingda Zhang, Yun Huang, Qiang Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each skill by one noisy score. To address these challenges, we propose R$^2$Orch, a new paradigm of Recursive Self-Play Orchestration: an inner loop of self-play that improves the orchestrator on self-chosen tasks, and an outer loop that improves how the inner loop improves. To support this paradigm, we introduce Recursive Learnability, a training objective that rewards a Proposer for choosing tasks whose rollouts keep reaching different outcomes as skills are withdrawn. Built on this objective, we further propose Skill Withdrawal, in which the outer loop withdraws each skill once a controlled evaluation within self-play shows that the orchestrator performs as well without it. Moreover, the two loops form one cycle: failures are distilled into skills, skills into parameters, and withdrawals lead the Proposer to new failures, so the orchestrator moves toward zero-skill deployment. Experimental results on twelve datasets show that R$^2$Orch consistently outperforms baselines across question answering, math, code, and interactive tasks.

---


### 54. [Cross-Person Identity Change Under Source-Coupled Multi-Human Generation: A Controlled UniPortrait Study](https://arxiv.org/abs/2610.22746)

**<font color=#1a73e8>作者：</font>** Edrees Al-Edreesi, Ghaleb Al-Gaphari, Muneer Alsurori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-human personalization must account for identity changes in people outside the nominal target of a generative operation. We characterize this behavior in UniPortrait, without introducing a new preservation algorithm. Two sequential studies use 119 accepted two-person baseline scenes and three fixed output seeds, measuring continuous reference-based facial similarity with InsightFace \buffalo. In Study~1, source-coupled single-ID target-only generation (A1) produces negative mean transitions for both the protected person ($-0.567904$) and target ($-0.236904$), indicating broad perturbation rather than established successful repair with collateral loss. In Study~2, native dual-ID generation (A2) yields more positive paired contrasts: protected $+0.512918$ (95\% case-cluster CI $[0.471434,0.550259]$) and target $+0.158853$ ($[0.118903,0.197523]$), across 287 jointly measurable pairs from 111 cases. Shared baseline similarity cancels algebraically in these paired contrasts, leaving a matched POST comparison. Validation designed after the primary result freeze finds directional agreement with an independent identity evaluator and blinded human judgments; within-\buffalo\ nuisance models provide supportive sensitivity evidence. The findings characterize intact native regimes, whose references, routing, adapters, and token counts co-vary. They do not establish component causality, categorical identity preservation, successful localized editing, or generalization beyond the evaluated implementation and measurable cohort.

---


### 55. [ElectroCalm: Investigating User Experience and Physiological Responses to Multi-Node Transcutaneous Electrical Stimulation for Stress Modulation](https://arxiv.org/abs/2610.22748)

**<font color=#1a73e8>作者：</font>** Yoon Kyung Shon, Pablo E. Paredes  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Transcutaneous Electrical Stimulation (TES) for stress modulation has largely focused on vagus nerve stimulation at the neck, yet two questions remain underexplored: how users experience electrotactile sensations at this sensitive site, and whether electrotactile feedback itself can function as a haptic stress intervention. To investigate this gap, we applied an 8-node TES array to two body sites during a cognitively demanding 2-back task: the neck, a site used in prior vagal TES research for its anatomical proximity to the cervical vagus nerve, and the arm, the most common haptic wearable site, which primarily provides cutaneous electrotactile sensation without vagal access. In a usability study, both sites were rated as comparably comfortable without disrupting task performance, though the same stimulation was interpreted differently across sites. A second study assessing the physiological effects of active versus inactive stimulation under identical electrode attachment revealed that only neck TES produced cortical and autonomic changes consistent with stress modulation, while arm TES did not differ from inactive conditions. These findings suggest that neck TES can be acceptable despite the site's sensitivity, and that both the physiological effects and the sensory experience of TES depend on placement.

---


### 56. [Native Geometry vs. Linear Recoverability: How Alignment Changes Platonic Scaling](https://arxiv.org/abs/2610.22749)

**<font color=#1a73e8>作者：</font>** Angus Hoy, Austin Lutterbach, Jasper Chong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Do larger models learn increasingly similar representations of the same world? The Platonic Representation Hypothesis (PRH) predicts that they should, but similar can mean native cosine geometry---nearest-neighbour structure induced by cosine similarity before any learned alignment---or linear recoverability: correspondence revealed by a supervised linear map. Using matched Legacy Survey and Hyper Suprime-Cam (HSC) embeddings across five model families, we find that Ridge alignment strengthens the relationship between model size and cross-dataset neighbourhood correspondence relative to native cosine geometry. The effect appears in all five families and persists when both representations are reduced to dimension, so it is not simply that wider embeddings give alignment more dimensions to work with. The learned maps remain far from rotations or uniform scaling, and Sparse Autoencoder (SAE) and Block-Sparse Featuriser (BSF) features give no advantage over the same alignment applied to dense embeddings. Model scale thus improves linear recoverability more clearly than native cosine-neighbourhood correspondence, without establishing convergence toward a shared native metric geometry.

---


### 57. [Input- and Feature-Space Correction for Cross-Hospital IHC Grading](https://arxiv.org/abs/2610.22756)

**<font color=#1a73e8>作者：</font>** Jongwoon Lee, Jhair Gallardo, Christopher Kanan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (FMs) are trained predominantly on hematoxylin and eosin (H&E) images but are increasingly used as frozen feature extractors for immunohistochemistry (IHC), where cross-hospital differences can impair grading. However, systematic comparisons of correction methods for cross-hospital IHC grading remain limited. To address this gap, we benchmark label-free transformations applied to input images before frozen-FM encoding and to features after frozen-FM encoding using UNI and Virchow2, three IHC markers, and six directed cross-hospital transfers, yielding 12 settings. Among the evaluated input-space methods, our proposed method FIX achieved the largest macro-F1 improvement over no correction, outperforming well-known stain normalization techniques. Among feature-space methods, a simple feature-wise standardization achieved the best improvement over no correction, outperforming CORAL. Under patient-averaged tile-level evaluation, combining FIX with feature-wise standardization improved macro-F1 and quadratic weighted kappa (QWK) by 0.181 and 0.208, respectively, and reduced ordinal error by 0.209 relative to no correction. These results show that input- and feature-space transformations can provide complementary benefits for cross-hospital IHC grading with frozen pathology FMs.

---


### 58. [Between Spoilers and Guesswork: Avoiding Over-Specification in Coding Benchmarks](https://arxiv.org/abs/2610.22760)

**<font color=#1a73e8>作者：</font>** Yuanzhe Liu, Bastian Lipka, Avraham Shinnar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks drive AI progress, but are hampered by task under-specification and over-specification. Task under-specification causes guesswork, where solutions have to make things up, or worse, resort to contamination or reward hacking. Task over-specification causes spoilers, where solutions can bypass some of the harder steps the benchmark was supposed to measure. Since future-looking benchmarks should be difficult, over-specification reduces a benchmark's shelflife of community adoption. Repository-level coding benchmarks have helped the field progress but experience unnecessary churn due to both over- and under-specification. For instance, SWE-bench Pro, FEA-bench, Doc2Feat-bench, and Multi-SWE-bench all tackle under-specification by augmenting task statements with hints derived from ground truth. We show that leaking ground-truth information into the task statement causes over-specification in some of these benchmarks. We experiment with various specification levels, trying to thread the needle between spoilers and guesswork. Based on these results, we recommend techniques for deriving parsimonious hints. We will release our hints so the community can obtain more reliable signals from popular benchmarks.

---


### 59. [Acquisition Function-Guided Generation for Bayesian Optimization over Discrete Spaces](https://arxiv.org/abs/2610.22763)

**<font color=#1a73e8>作者：</font>** Tommaso Ancilli, Thomas Wedenig, Henry Moss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) over discrete spaces is challenging due to missing gradients and the sparsity of valid solutions. Latent-space BO sidesteps both issues by fitting a surrogate in the latent space of a generative model, which however substantially complicates the direct incorporation of domain knowledge that is naturally expressed in the original discrete space. In this work, we instead combine a pretrained generative model with a surrogate defined directly in data space, where inductive biases such as domain-specific kernels can be readily incorporated. Rather than maximizing the acquisition function over the discrete design space, our method samples candidates from the generative model under a distribution tilted by the acquisition function. To recover useful gradients for sampling, we embed this tilted distribution into a diffusion bridge that yields a smooth, posterior-averaged acquisition function. This leads to \emph{acquisition function guided generation} (AFGG), which we instantiate with a categorical diffusion model and an autoregressive normalizing flow. Across a broad suite of molecular benchmarks, the diffusion model variant performs on par with leading BO methods, while the flow model variant outperforms state-of-the-art methods in most cases and remains highly competitive otherwise. Our implementation is available at this https URL.

---


### 60. [StoBasket: Joint Upsell and Cross-Sell Optimization for Contribution Margin](https://arxiv.org/abs/2610.22768)

**<font color=#1a73e8>作者：</font>** Xin Heng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retail recommenders rank relevance, but retailers earn contribution margin: an upsell earns the margin difference over the item it replaces, whereas a cross-sell earns its full margin. We introduce joint stochastic basket editing, a formulation in which one policy selects replacement and addition offers for an existing basket, values them by expected incremental contribution margin, and couples them through displayed-offer, accepted-offer, and joint-acceptance response channels. To our knowledge, it is the first formulation in which upsell and cross-sell responses are coupled; prior separable treatments are its zero-coupling special case. In real-data-calibrated simulations on five public basket datasets, StoBasket captures essentially all attainable offer margin: within 0.5% in every default-price setting and within 0.7% when the true response lies outside its model family. Correct economic accounting is the broadest gain: margin-weighted popularity leaves up to 11% of attainable margin unrealized, and a published next-basket recommender leaves 11-52%. Joint selection adds 10.2% of attainable margin on Instacart, where premium tiers and add-ons are strongly linked. When offers pay only together, the best heuristics lose 64% while exact search stays within 0.5%. For a structured subclass, we characterize when staged policies fail and give an exact optimizer that solves every tested real basket in 0.13 ms median and at most 111 ms. Profit saturates long before prediction accuracy: a correctly structured predictor trained on 5,000 randomized sessions comes within 0.06% of perfect prediction, while a signal-free one loses 38%. The same estimates yield a decision-aware market-basket analysis whose cost does not grow with association order.

---


### 61. [Direct Conditional Parameterization for N-Dimensional Splatting](https://arxiv.org/abs/2610.22778)

**<font color=#1a73e8>作者：</font>** Zhongpai Gao, Benjamin Planche, Van Nguyen Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> N-dimensional splatting extends 3D Gaussian Splatting with view direction and time to model view-dependent and dynamic effects. Each primitive is lifted into a joint distribution over position and conditioning variables, then conditionally sliced at each rendering query. N-DGS and UBS share this step across Gaussian and Beta kernels: recovering the conditional mean, opacity, and covariance requires per-primitive matrix inversions and regression products in every forward pass. We introduce direct conditional parameterization, replacing this covariance-derived readout with explicit per-effect parameters: a Cholesky precision factor for opacity and a factorized query-to-position regression operator with learnable per-dimension coupling. Unrestricted conditional coordinates recover a valid joint covariance; our factorization adds spatial-scale and coupling priors. Applied to both kernels, the parameterization yields dGS (Gaussian) and dBS (Beta). Across five static and dynamic benchmarks, they match or exceed their covariance-derived counterparts on quality, with gains up to +1.26 dB in the main MCMC evaluation. Production slicing is 6.9-7.7 times faster than on-the-fly covariance-derived conditioning; complete-render profiling gives 1.25-1.91 times speedups on four trained scenes. Direct conditioning provides a structured, kernel-agnostic alternative for N-dimensional splatting. Project page: this https URL.

---


### 62. [Causal Latent Workspaces for Looped Transformers](https://arxiv.org/abs/2610.22796)

**<font color=#1a73e8>作者：</font>** Ilia Zaznov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reusing a Transformer block across depth increases computation without replicating its parameters, but successive passes have no dedicated state through which positions can exchange compact summaries of their causal prefix. We introduce the causal latent workspace Transformer: an anchored, four-round shared-depth architecture in which each position writes gated vectors into prefix-specific latent slots and retrieves a content-addressed summary before the next shared block application. This path complements causal self-attention while the original input embedding remains accessible at every round. Across three byte-level corpora, three seeds, and two matched parameter budgets, the proposed model achieves the best mean held-out perplexity in five of six settings against five Transformer controls. At 101.71M parameters it leads on WikiText-103 raw, enwik8, and TinyStories, reaching perplexities 2.7820, 2.7843, and 1.6823; these improve upon the strongest non-workspace control on each corpus by 1.06%, 0.73%, and 1.01%. All nine seed-labelled comparisons at this budget favor the workspace. At 0.918M parameters it leads on WikiText-103 and TinyStories, whereas a conditioned loop is stronger on enwik8. Architectural ablations show that adding the workspace improves upon the anchored loop in all six settings and support refreshing its causal summaries at each round. Together, these results identify a causal, content-addressable prefix workspace as an effective structural augmentation of looped Transformers.

---


### 63. [Replay Pruning and Few-Bit Integer Inference for Hardware-Efficient Speed-Sign Recognition](https://arxiv.org/abs/2610.22811)

**<font color=#1a73e8>作者：</font>** Se Un Park, Kyungkeon Chung, Huigeol Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speed-limit sign recognition on an automotive camera system-on-chip (SoC) must fit a detector and a classifier (the reader) into the memory, arithmetic, and energy budgets of the device. In our two-stage recognizer, the detector, a YOLO-family network with ReLU and hard-sigmoid operators, is compressed by channel replay: an iterative pruning cascade identifies the channels to remove, the recorded deletions are replayed on the original task-trained network, the parent, and one continuous knowledge-distillation recovery follows. On a YOLOv5n, replay removes 60.3% of the parameters at the accuracy of the parent and, in validation mAP50-95 over five matched seeds, outperforms iterative pruning and training from scratch, and its per-step variant (per-step replay) is the most accurate pruning method. On a YOLOv8n, replay and per-step replay outperform every other method and the unpruned parent. The reader, a five-layer CNN with 18k parameters, and the post-processing of the YOLOv5n and YOLOv8n heads use integer arithmetic only. With 4-bit weights and 8-bit activations (W4A8), the reader matches FP32 accuracy in 12.1 KB of on-chip memory, and an executable streaming model reproduces the INT8 class predictions of its runtime on all 9,850 test crops. On a Jetson AGX Orin, INT8 is faster than FP16 only in the implicit formulation of TensorRT, and the replay detector runs fastest on the deep-learning accelerator (DLA). Trained on public data only, the combined system of 0.72 M parameters recognizes 95.2% of the signs of a held-out automotive camera at 90% precision and 94 frames per second.

---


### 64. [World Action Critic (WAC) Model: Joint Foresight and Criticism for Policy Learning](https://arxiv.org/abs/2610.22825)

**<font color=#1a73e8>作者：</font>** Xiangteng Zhang, Haoyuan Liu, Yang Guan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have shown considerable promise in sequential decision-making by anticipating the consequences of actions and providing predictive foresight for policy learning. However, learning to reason about counterfactual actions remains challenging, since predictive objectives may underemphasize information critical for action evaluation, while unexecuted actions lack observed futures for direct supervision. To address these challenges, we propose the World Action Critic (WAC) Model, which proposes multimodal action candidates and jointly learns candidate-conditioned future prediction and consequence evaluation. In our proposed framework, critic supervision directly shapes intermediate predictive representations during rollout, encouraging them to retain information needed to distinguish action quality. Observed futures supervise prediction for executed actions, while external task-quality targets provide evaluation signals for counterfactual candidates. Through joint optimization, critic signals from these candidates propagate into predictive representations without requiring their observed futures. Our theoretical analysis characterizes critic-guided feature retention and bounds candidate-selection regret. Applied to autonomous driving, WAC achieves 93.4 PDMS on NAVSIM-v1, demonstrating the effectiveness of jointly learning predictive foresight and consequence evaluation.

---


### 65. [Partial-Revelation Panel Forecasting: Predictive Information Gain, Allocation, and Coarsening-Consistent Operators](https://arxiv.org/abs/2610.22831)

**<font color=#1a73e8>作者：</font>** Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study partial-revelation panel forecasting: given $k$ of $n$ annotator votes on the previous dialogue turn, predict the full count distribution of the next turn's panel. This cross-turn predictive information differs from same-item annotation value. Under any nested revelation mechanism, the population decrement satisfies $V(k)-V(k+1)=I(Y;R_{k+1}\mid X_k)$; a fitted model also contributes adjacent excess-risk differences. Coarsened-completely-at-random (CCAR) masking supplies the exchangeable random-rater interpretation used in our operators. We define coarsening-consistent panel operators with a closed-form Dirichlet-multinomial realization, learned completion, and rater-count transfer. Against per-level lookup, cold-start count negative log-likelihood differences are -0.422/-0.166/-0.014 nats on IEMOCAP/M3ED/EmoWOZ. A held-out rater experiment measures same-item value: first and second additional votes reduce NLL by 0.583/0.221, 0.578/0.184, and 0.180/0.069 nats, respectively. Cross-turn and same-item gains are not interchangeable, and CCAR masks are controlled interventions rather than observed arrival processes. Consistency is auditable but does not guarantee predictive improvement; per-level marginalization can outperform a shared table. Target-free allocation beats uniform only where row-level signal is predictable: at budget one it recovers 83--93% of retrospective feature class headroom on IEMOCAP/M3ED but does not improve EmoWOZ. Gains are modest and corpus-dependent, with several small or null partial-revelation differences. Code and aggregate result artifacts accompany the preprint.

---


### 66. [Variational and Decomposed method for Mitigating Bimodal Bias in Robust Visual Question Answering](https://arxiv.org/abs/2610.22845)

**<font color=#1a73e8>作者：</font>** Yihan Zhao, Yuncheng Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual question answering (VQA) models are known to suffer from the bias issue, which refers to overfitting the regularities of frequent patterns. Previously, researchers only consider the language bias. Recently, the multimodal bias is noticed. However, what multimodal bias is remains unclear. In this paper, we investigate the multimodal bias in counting and non-counting questions. We find that they have distinct underlying mechanism, so their biases come from distinct reasons. We provide valuable interpretations of VQA counting mechanism: \textbf{quantity information stems from the magnitude of the multimodal features in specific dimensions.} Thus, counting bias stems from the vision side and propagates to multimodal features through modality fusion, while the non-counting bias stems from primarily language bias and slightly vision bias. Thus, we propose a method to deal with them differently: Variational and Decomposed method for mitigating Bimodal Bias (VDB). It extracts bimodal bias affected by different proportion of vision and language sides. We introduce variational bias models utilizing the principle of Variational Auto-Encoder to learn mainly language bias with slight vision effect, and a bimodal bias model for bimodal bias combining language and vision sides. Extensive experiments on VQACPv2, VQACPv1, and GQAOOD datasets demonstrate the rationality of our claim and the effectiveness of our method. We also provide explanation for the compromised performance on VQAv2.

---


### 67. [Look Back, Correct Forward: Error Feedback Calibration for Time Series Forecasting](https://arxiv.org/abs/2610.22872)

**<font color=#1a73e8>作者：</font>** Haonan Yang, Yulin He, Zhuo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting models are increasingly deployed in continuously evolving environments. After a forecast is issued, future observations gradually arrive and reveal how the model has failed. Existing methods mainly treat such observations as supervision for parameter updates. However, it remains unclear whether verified forecasting errors can themselves provide causal feedback for correcting future predictions. To address this, we introduce Error Feedback Calibration (EFC), a fully test-time framework for deterministic post-hoc correction of time series forecasting. EFC constructs a Causal Error Diagonal (CED) from revealed errors of overlapping historical forecasts, providing a fresh view of the frozen forecaster's recent failure behavior. Then Cumulative Error Transport (CET) maps this error state to future residuals using cumulative estimation, while temporal out-of-sample validation controls the correction strength. Temporal Residual Learning (TRL) further predicts only the residual structure left after CET from recent CED trajectories, rather than relearning the entire forecasting error. Extensive experiments across forecasting backbones and datasets show that EFC broadly improves forecasting performance while substantially controlling harmful over correction.

---


### 68. [Immersive Focus+Context Techniques to Assist in Interpretation of High Density Forest Point Clouds](https://arxiv.org/abs/2610.22878)

**<font color=#1a73e8>作者：</font>** Spencer O'Keeffe, Jan Rombouts, Bruce H Thomas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual Reality (VR) is changing how we interact with complex spatial datasets. VR has the potential within forestry to help analyse remotely sensed spatial data for inventory management. However, challenges of scale and legibility of dense forest point clouds must be addressed. To do so, we present three VR Focus+Context (F+C) techniques: Wedgelight, Remote Lantern, and Ray Lantern. These techniques present point cloud data using a constrained highdetail focus within a broader abstracted context representation, manipulated using egocentric and exocentric interactions. We conducted two user studies. The first informed the design of the F+C techniques. The results from the first study indicate that VR significantly outperforms desktop displays in basic analysis of forestry point clouds, with improvements to both time and accuracy. The second study evaluated the performance of the resulting F+C techniques in a task analogous to real-world forestry operations. Our F+C techniques significantly outperformed current approaches, confirming their viability for facilitating detailed and effective forest assessments. These findings indicate that VR has significant advantages for spatial data analysis tasks in forestry, making a strong argument for its adoption in future analytical frameworks. The F+C visualisation techniques we introduced show considerable promise for analysis of high density point clouds, opening new avenues for development in immersive analytics. Supplemental materials (code, scans, results) are available at this https URL.

---


### 69. [RAMP: Toward Ubiquitous Quantum-Safe Key Distribution as a Service](https://arxiv.org/abs/2610.22879)

**<font color=#1a73e8>作者：</font>** Jiafan Wang, Sebastian Kish, Dongxi Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum key distribution (QKD) offers a security foundation independent of computational hardness assumptions. However, its reliance on specialized hardware limits access by ordinary users. Turning QKD into a service poses a fundamental trust challenge, as the providers that supply QKD-derived material themselves could retain knowledge of the keying inputs of users. This makes end-to-end confidentiality solely depend on the trustworthiness of the service infrastructure.
We present RAMP, a service-oriented framework that decouples QKD material generation from key consumption. Providers operate QKD infrastructure and supply raw-key materials, while users securely acquire, mask, and locally process them into final keys without operating QKD devices. RAMP employs reconciliation-preserving masking compatible with both DV- and CV-QKD. It mitigates the trust dependence by separating the QKD-service and user-side masking domains. We formalize complementary confidentiality guarantees: RAMP protects the final key even if colluding providers expose their complete raw-key views, provided the masking domain remains secure; conversely, exposing the complete masking state does not break final-key secrecy as long as the QKD source and acquisition paths remain protected. The results establish the dual-domain security boundary of RAMP.
We implement RAMP using experimentally acquired QKD data and standardized quantum-safe cryptography. After acquiring service-provisioned keying material, commodity endpoints complete user-side QKD post-processing with an average key-distillation throughput of 2.1Kb/s on an M4 Pro CPU. To our knowledge, we demonstrate the first experimental realization of such service-provisioned, user-side QKD processing, presenting a viable path toward QKD as a service.

---


### 70. [ToPA: Block-wise Toeplitz Adaptation for Expressive and Efficient Fine-Tuning](https://arxiv.org/abs/2610.22883)

**<font color=#1a73e8>作者：</font>** Sicong Li, Qianqian Xu, Zhiyong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) has emerged as a prevalent strategy for adapting large pre-trained models. Among PEFT techniques, reparameterization-based methods, particularly those that employ low-rank or sparsity structures, have attracted significant attention. However, these approaches often underperform full fine-tuning. Specifically, low-rank methods constrain the update rank, which is misaligned with the inherently high-rank nature of full fine-tuning. In contrast, sparsity-based techniques limit the flexibility of the parameter space and compromise connectivity across weights. To overcome these limitations, we explore the use of Toeplitz matrices, whose entries are constant along each diagonal, therefore providing a compact parameterization without imposing explicit rank or sparsity constraints. A straightforward approach is to update weights via a product of Toeplitz matrices. However, similar to RNNs, long multiplicative chains often lead to gradient instability. To address this issue, we propose \textbf{ToPA}, a more refined version of this idea that replaces standard Toeplitz matrices with block-wise Toeplitz, greatly increasing each factor's capacity and shortening the chain, thereby stabilizing training and improving expressiveness. We theoretically show that products of block-wise Toeplitz matrices can approximate arbitrary matrices under shorter chain length, justifying the structural design of ToPA. Furthermore, we demonstrate that ToPA offers greater expressivity than existing low-rank and sparse parameterizations. Empirical evaluations across 21 NLP and CV datasets, spanning 5 model architectures, consistently validate the effectiveness of ToPA.

---


### 71. [Learning to Be Guided: Shaping Latent Geometry for Classifier-Free Guidance](https://arxiv.org/abs/2610.22885)

**<font color=#1a73e8>作者：</font>** Haoming Liu, Junhao Zhu, Shaoyi Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is a standard component of conditional diffusion models, and guided generation performance has become the \textit{de facto} measure of state-of-the-art models. Recent work on latent diffusion models seeks to learn latent spaces that are easier to model with diffusion. However, under CFG, generation additionally depends on how conditions are arranged in the latent space. We study this arrangement under discrete class conditions, termed \emph{class geometry}, and investigate what class geometry allows a latent space to work well with CFG. Under a Gaussian class model, we show that shifting variance from intra- to inter-class at fixed total variance makes classes more distinguishable under noise, and derive a noisy posterior objective whose per-sample descent direction is proportional to the oracle CFG correction. Based on the analysis, we propose Prototype Regularization (PR), a lightweight surrogate for the intractable noisy posterior objective, which applies a cosine prototype classifier to spatially pooled latents. With a controlled training budget (20 epochs for VAE, 80 epochs for DiT), adding PR to an LDM baseline reduces guided gFID on ImageNet from 3.31 to 2.28, surpassing a DINOv3-aligned VA-VAE (2.44) with negligible overhead. We further demonstrate that PR generalizes to pseudo-labels derived from clustering, continuous text-embedding conditions, and video latents. Together, our findings highlight class geometry as a critical factor in guided generation and take a first step toward CFG-compatible representation learning. Our project page is available at: this https URL.

---


### 72. [What Accuracy Hides In Learned Transformer Programs](https://arxiv.org/abs/2610.22891)

**<font color=#1a73e8>作者：</font>** Jonathan Lee, Narmeen Oozeer, Philip Quirke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer Programs (TP) (Friedman et al., 2023) constrain a Transformer's architecture so that its learned computation can be extracted as readable Python code. TP expose learned computations, but token accuracy can hide incorrect complete answers. In this work, we examine how program inspection provides insights beyond accuracy scores and helps guide training. We first evaluated TP on nine algorithmic tasks. We compared token accuracy with accuracy on complete output sequences and checked for failures missed by sampled tests. Further, we assessed training data improvements informed by program inspection and failure analysis, finding gains in sequence accuracy on several tasks. We examined a counting task where a program achieved 100% accuracy on sampled test sequences but failed on another input using the symbols and lengths allowed during training. The program counted correctly, but the required answer was missing from its output labels. After adding training examples with larger counts, the retrained models passed exhaustive evaluation over the bounded domain. In the frequency ranking task, inspection showed how correct counts contributed to incorrect answers in programs trained before and after changes to the training data. Finally, we studied constraints imposed by TP training and operations. The TP training process can lead to accuracy losses late in training. Our reference constructions also show how composing the restricted TP operations can use many layers or large lookup tables.

---


### 73. [HAPACT: A Benchmark For Human-Centric Physical Impact Localization in Movies](https://arxiv.org/abs/2610.22895)

**<font color=#1a73e8>作者：</font>** Youngrae Kim, Yejin Jang, Eunho Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical reasoning about humans in videos has largely focused on everyday interactions, where contact, pressure, pose, and motion support embodied perception and contact-aware applications. Still, short and forceful properties like impact events remain relatively underexplored, despite their relevance to broader understanding of how abrupt physical events affect the human body. To fill this gap, we introduce human-centric impact localization, a new task that localizes target physical impacts temporally within a video and spatially on the human body. We further present HAPACT, a HumAn-centric imPACT dataset and benchmark built from movie clips, containing over 2.8K video-query pairs with more than 20K fine-grained human-annotated frames. We built HAPACT around viewer-grounded annotation, text-conditioned localization, and supervision at frame-level temporal and SMPL-X-based spatial granularity. To demonstrate the effectiveness of our benchmark, we conduct extensive evaluations of existing methods, employing video moment retrieval models for temporal localization and human-scene contact models for spatial localization. For the spatial task, we propose a text-conditioned baseline by reformulating localization as query-guided body-region selection. Benchmark results show that physical impact localization remains challenging for existing methods, motivating HAPACT as a dedicated benchmark to support physical impact reasoning in videos.

---


### 74. [When to Forget: Risk-Controlled Context Adaptation for Long-Horizon Agents](https://arxiv.org/abs/2610.22897)

**<font color=#1a73e8>作者：</font>** Chenle Chen, Yangbo Wei, Zhijie Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents learn from failure, but the value of a failure record can change as execution progresses. We study when retaining, compressing, or removing the same history block improves subsequent execution relative to full-history KEEP. We introduce RECAP, a framework that combines matched context interventions, execution-relational prediction, and independent policy certification. Matched environment states and rollout seeds measure success and continuation prompt-cost differences; prefix-only relations between a failure block and the current execution propose promising edits. Independent task bundles then select a policy subject to harmful-intervention and non-positive-benefit risk constraints under a fixed measurement protocol. A five-seed longitudinal case holds both the failure block and its summary fixed: compression fails at an early state and becomes a cost-saving intervention at a later state. Across five backbones, RECAP produces positive paired-success saving estimates with backbone-specific reliability-efficiency tradeoffs. On Hunyuan-A13B, it edits 43.24% of retained checkpoints while matching KEEP's observed 91.89% continuation success and reducing unconditional mean continuation prompt cost by 4,619.8 tokens (2.13%). The framework provides an execution-level reference for deciding when to forget: retain history by its value to what comes next.

---


### 75. [A Feature Selection Layer Approach for Multi-Class Classification on Neural Networks](https://arxiv.org/abs/2610.22898)

**<font color=#1a73e8>作者：</font>** João Pedro Silveira e Silva, Márcio Dorn, Bruno Iochins Grisci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the age of data-driven decision-making, deep learning models have become powerful tools for uncovering patterns and making predictions that influence many aspects of society. However, their broader adoption in scientific and business applications is often limited by a lack of interpretability. Feature weighting methods, which assess the relevance of individual features, are among the most widely studied approaches for improving interpretability. While post hoc techniques have advanced significantly, especially in modeling nuanced relationships between features and labels in multiclass problems, embedded methods typically fall short in this regard. Embedded techniques integrate feature relevance learning directly into the model training process, but they are often unable to capture label-specific relationships. To address the limitation, we propose multiple extensions to the Feature Selection Layer, an embedded feature weighting mechanism for neural networks. Through extensive experimentation, we identify the most effective extension and benchmark it against established feature weighting methods. Our results show that the proposed method matches existing techniques in identifying globally relevant features and outperforms them in capturing label-specific relevance. By leveraging the internal dynamics of the trained neural network, it reveals how individual features contribute to the prediction of specific labels, requiring no post-processing beyond the training process.

---


### 76. [Provable Authority: A Protocol for Verifiable Authority Resolution and Control Across Human, Organizational, and Agentic Transactions](https://arxiv.org/abs/2610.22899)

**<font color=#1a73e8>作者：</font>** Jeremy Blackburn, Tim Hines, Matthew Koepp 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Payment systems authenticate users, devices, accounts, and cryptographic credentials, but a relying party, such as a counterparty, payment rail, marketplace, or autonomous agent runtime, generally cannot obtain compact, independently verifiable evidence that the party presenting one exact transaction holds current organizational authority to execute it under the applicable evidence, policy, budget, and approval state. Agentic commerce makes this gap operationally urgent: a software agent can produce a valid signature while acting outside its delegated purpose, after its sponsor's authority has changed, or on transaction details that differ from those a human approved. We describe the ChainIT Authority Protocol, a subject-neutral and rail-neutral pre-execution authority and evidence control plane. The protocol separates durable identity, a versioned organizational authority record (the Authority Resolution Pactvera), sourced evidence assertions, deterministic reason-coded policy predicates, and organization-configured dispositions; binds each decision and human approval to a canonical transaction digest; reserves capacity atomically so that limits hold under concurrency; and authorizes commit only through a single-use, sender-constrained Execution Authorization Credential consumed at the rail adapter, with append-only lifecycle evidence sealed after the terminal outcome. An Agent Subject Profile adds the workload registration, attested key hierarchy, and sovereignty boundary required when the acting subject is an AI agent, without introducing a separate authority concept. We specify the commit-time execution predicate and bounded-freshness status rules, give enforcement profiles for fiat (ACH, wire, card, instant payment) and stablecoin rails, and state residual risks and non-goals.

---


### 77. [Provable Compliance: A Protocol for Runtime Compliance Evidence and Transaction-Specific Decisioning](https://arxiv.org/abs/2610.22913)

**<font color=#1a73e8>作者：</font>** Jeremy Blackburn, Tim Hines, Matthew Koepp 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Regulated institutions already perform onboarding, screening, monitoring, and review, but compliance evidence ages, and whether it supports a decision depends on the institution, product, subject, counterparty, transaction, jurisdiction, risk tier, and purpose. A relying party therefore often cannot obtain compact, attributable proof of which evidence, policy, authority, and transaction context were current when a decision was made, a gap that grows as authority is delegated to software agents and scheduled workflows. We describe ChainIT Provable Compliance, the compliance-side layer of the ChainIT Authority Protocol. Each sourced or institution-generated fact is represented as a separate Evidence Assertion VDT with provenance, freshness, confidence, permitted purpose, and privacy classification; a versioned Compliance Policy Profile selects the applicable rules; a Business Rules Engine returns deterministic, reason-coded predicate results; and the organization's configured Workflow Engine composes them into a signed, time-bounded Compliance Decision VDT for one reliance event. The decision contributes a single predicate, Compliance Decision Permits, to session-eligibility and transaction-policy decisions. It never independently authorizes payment: only a final Allow together with an exact transaction digest, atomic capacity reservation, and a single-use execution credential can commit value. The paper specifies point-of-reliance freshness, scoped propagation of evidence changes, decision states, evidence domains (AML, sanctions, PEP, background, identity, and licensing), the U.S. and FATF regulatory context as of August 2026, privacy and disclosure controls, and residual risks.

---


### 78. [Reward Engine: Reward-Centric Self-Evolution for Open-Ended Tool Agents](https://arxiv.org/abs/2610.22915)

**<font color=#1a73e8>作者：</font>** Litong Feng, Ji Qi, Yiran Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended tool agents can complete the same objective through different tool paths, and their quality depends jointly on the interaction trace, environment state, and final artifacts, so such tasks rarely admit an executable ground-truth reward. The central challenge is therefore to construct a reward from existing experience that exposes the current policy's failures while remaining stationary during optimization. We introduce Reward Engine, which, like a self-motivated student, first works out what success requires and then optimizes toward it. From the task and initial trajectories, it builds a RewardPack of testcases for required correctness and rubrics for graded quality, each executed as a check that returns a judgment with evidence. The frozen RewardPack then guides the agent to revise and select its outputs, and can also serve as a reward for reinforcement learning. On WorkBuddy Bench Office and Claw-Eval, the constructed reward largely agrees with the benchmark graders, not reversing their ordering on 82.3\% and 80.5\% of candidate pairs. Used to revise executions, it raises three-run consistency ($\mathrm{Pass}^{3}$) over Baseline from 45.0\% to 54.0\% and from 78.4\% to 83.7\%.

---


### 79. [MaskMerge: Structure-aware Token Merging for Efficient Instance Segmentation](https://arxiv.org/abs/2610.22921)

**<font color=#1a73e8>作者：</font>** Bavesh Balaji, Letian Jiang, Alexander Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token merging improves the efficiency of Vision Transformers by combining redundant tokens, but existing methods largely rely on feature similarity to determine which tokens to merge. This criterion is effective for semantic segmentation, yet can fail in instance segmentation, where adjacent objects of the same class often have highly similar features. We identify this failure mode as cross-instance token fusion. We introduce MaskMerge, an instance-aware token merging method that uses coarse intermediate mask predictions to constrain feature-based merging and preserve instance boundaries. We evaluate MaskMerge on two diverse instance segmentation domains characterized by high inter-instance visual similarity: PanNuke and iSAID. Against the SOTA token merging method ALGM, MaskMerge improves mAP from 30.1 to 32.1 on PanNuke while reducing computation from 229 to 153 GFLOPs and running 1.18x faster, and from 33.1 to 36.2 on iSAID while reducing computation from 198 to 182 GFLOPs and running 1.23x faster. Additionally, we also test it on Cityscapes and match ALGM's performance while using fewer FLOPs. The gains also transfer to an MAE pretrained backbone, demonstrating that instance-aware merging enables more aggressive compression when appearance similarity alone cannot reliably preserve object identity.

---


### 80. [Scalable Levenberg-Marquardt Training Framework for Deep Learning](https://arxiv.org/abs/2610.22925)

**<font color=#1a73e8>作者：</font>** Xianghao Wang, Johan Barthélemy, John Taylor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Levenberg-Marquardt (LMA) algorithm is a widely used nonlinear least-squares solver known for its rapid convergence. For small-scale neural networks, LMA provides better convergence and architectural robustness than first-order optimizers like Adam. However, LMA imposes prohibitive memory and computational costs. These costs are primarily from the Jacobian matrix, whose dimensions scale with both the number of samples and parameters. This bottleneck prevents its use in large-scale neural networks. Recent efforts scale LMA using preconditioned conjugate gradient (PCG) solvers to avoid materializing the Jacobian. However, PCG only approximates the solution, requiring many network propagations and a task-specific preconditioner. Other studies optimize LMA to reduce costs, but they restrict their methods to specific tasks or network architectures. As a result, LMA remains impractical for training general large-scale neural networks. In this paper, we propose LeMA, a distributed LMA algorithm for large-scale neural network training on multi-GPU platforms. Our contributions are twofold: First, an exact dual formulation of LMA removes the memory dependence on the parameter dimension. Second, a Jacobian sharding strategy computes Jacobian shards on the fly and in parallel to avoid materializing the full Jacobian. For large-scale neural networks, LeMA reduces the memory footprint of LMA from quadratic in the number of parameters to quadratic in the batch size. This makes exact LMA steps feasible for billion-parameter models without approximate PCG solves. Furthermore, for a convolutional neural network with 1,000,022,632 parameters on an 8-GPU node, LeMA achieves a 7.97x speedup over a single GPU, corresponding to a 99.7% strong scaling efficiency.

---


### 81. [SwitchTube: A Proof-of-Concept System Introducing "Adaptable Commitment Interfaces" as a Tool for Digital Wellbeing](https://arxiv.org/abs/2610.22947)

**<font color=#1a73e8>作者：</font>** Kai Lukoff, Ulrik Lyngs, Karina Shirokova 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> YouTube has many features, such as homepage recommendations, that encourage users to explore its vast library of videos. However, when users visit YouTube with a specific intention, e.g., learning how to program in Python, these features to encourage exploration are often distracting. Prior work has innovated 'commitment interfaces' that restrict social media but finds that they often indiscriminately block needed content. In this paper, we describe the design, development, and evaluation of an 'adaptable commitment interface,' the SwitchTube mobile app, in which users can toggle between two interfaces when watching YouTube videos: Focus Mode (search-first) and Explore Mode (recommendations-first). In a three-week field deployment with 46 US participants, we evaluate how the ability to switch between interfaces affects user experience, finding that it provides users with a greater sense of agency, satisfaction, and goal alignment. We conclude with design implications for how adaptable commitment interfaces can support digital wellbeing.

---


### 82. [Designing Human-AI Collaborative Science: The 9A Framework](https://arxiv.org/abs/2610.22948)

**<font color=#1a73e8>作者：</font>** Zihan Zheng, Linyue Pan, Xin Lan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) for Science is often described as a progression from human-directed assistance toward increasingly autonomous AI scientists. Human-AI collaboration offers a further mode in which human and AI contributions substantively shape scientific reasoning, judgments, and the course of inquiry. Existing research addresses work allocation, human-AI coordination, and system evaluation, but how these aspects interact to shape collaborative scientific systems remains insufficiently articulated. We develop the 9A Framework for Human-AI Collaborative Science (HACS) to connect these considerations across three layers. The organization layer specifies what scientific activities are required (Activity), who performs them (Actor), and who holds authority over consequential decisions (Authority). The coordination layer addresses how participants access relevant research information (Awareness), how scientific work advances through iterative proposal, execution, examination, revision, and resolution (Accountability), and when collaborative arrangements should be adjusted (Adaptability). The evaluation layer establishes what constitutes effective system performance (Achievement), how comparisons can be designed to identify the effects of organizational and coordination choices (Attribution), and what evidence supports the resulting conclusions (Assurance). Together, these layers frame HACS as a system-design problem, providing a basis for designing collaborative scientific workflows and for empirically comparing their effectiveness.

---


### 83. [On the tradeoff between robustness and geometric accuracy in adversarial training](https://arxiv.org/abs/2610.22955)

**<font color=#1a73e8>作者：</font>** Rachel Morris, Ryan Murray, Kerrek Stinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For non-parametric binary classification in the presence of an adversary, we prove an optimal quantitative estimate for adversarial classifiers controlling geometric accuracy, as measured by the Hausdorff distance to the Bayes classifier, in terms or their robustness, as encoded by the adversarial budget $\varepsilon$. This rigorously shows that robust classifiers sacrifice at most $O(\sqrt{\varepsilon})$ or $O(\varepsilon)$ in accuracy, depending on the regularity of the underlying Bayes classifier. In contrast to prior work on the incompatibility of robustness and accuracy over low-complexity hypothesis classes, our work shows that high-complexity hypothesis classes allow for robust classifiers with precisely quantified accuracy. Our results apply for adversaries determined by any norm on Euclidean space and in both the infinite and finite data settings.

---


### 84. [DiffusionRVGE: Reinforcement Learning via Regression-Based Value Gradient Estimation](https://arxiv.org/abs/2610.22973)

**<font color=#1a73e8>作者：</font>** Jiayuan Wang, Tongyao Pang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning improves diffusion models using rewards on generated images, but repeated denoising and gradient estimation make training expensive. We introduce \method, an efficient method that constructs useful update directions by regressing centered rewards on centered final denoised images. It requires neither reward derivatives nor adjoint backpropagation through the sampling trajectory. A unified first-variation formulation identifies the value-gradient target with or without a trajectory-KL penalty. A population analysis under Gaussian noising explains the regression geometry, while a subspace analysis motivates clean-image coordinates. The implementation adapts rollout bandwidth and query weights to reward continuity: local rollouts suit smooth rewards, whereas broader groups provide informative contrasts for discrete rewards. Trained jointly on five rewards, one SD3.5-Medium model matches or exceeds DiffusionNFT's joint model on seven of eight metrics, reaching GenEval $0.94$, OCR $0.92$, and PickScore $23.82$ at about one fifth of its estimated training compute. In single-reward training, \method reaches matched reward thresholds $2.1$--$6.7\times$ faster than reproduced DiffusionNFT on identical hardware. Ablations support the clean-image estimator, direct direction transfer, and reward-dependent rollout choices. Code is available at this https URL.

---


### 85. [Sink-Sparse Hybrid Attention for Efficient Inference in T2I/T2V Diffusion Transformers](https://arxiv.org/abs/2610.22975)

**<font color=#1a73e8>作者：</font>** Bingxin Xing, Yu Zhang, Jiatong Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have become a common backbone for high-quality text-to-image and text-to-video generation, but repeated dense self-attention remains a major inference bottleneck as token sequences grow and the same operator is invoked across many denoising steps. Our study suggests that dense attention in pretrained DiTs contains reusable layer/head-specific high-mass structure that can be identified from a small offline calibration set and reused across future generations. This leads to Sink-Sparse Hybrid Attention, a train-free attention replacement that reuses static sink masks and supplements them with a lightweight pooled-KV branch, while leaving model weights and sampling schedules unchanged. On Wan2.1-T2V-1.3B, the method attains 1.54$\times$ end-to-end speedup while maintaining generation quality. On Z-Image-Turbo, it attains 1.57$\times$ end-to-end speedup with competitive GenEval2 performance. These results indicate that reusable importance-aware sparse support can provide an effective train-free acceleration path for both T2V and T2I DiTs.

---


### 86. [GOLD: Geometric Optimized Latent Diffusion for Structure-Aware RNA Inverse Folding](https://arxiv.org/abs/2610.22992)

**<font color=#1a73e8>作者：</font>** Qi Si, Xuyang Liu, Penglei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing RNA sequences that fold into specific 3D structures is a fundamental challenge in therapeutics. Current RNA inverse folding methods typically condition on 3D backbone coordinates but the generation is limited to 1D discrete sequences. This ignores the continuous side-chain orientations, which are essential for overall structural stability. To address this issue, we explicitly introduce side-chain geometry into the RNA generative process. Unlike co-design frameworks that diffuse across separate raw spaces, we propose Geometric Optimized Latent Diffusion (\textbf{GOLD}), which project sequence and structure into a unified latent manifold. GOLD employs a novel GeoVAE to elegantly integrate discrete RNA sequences with continuous side-chain angles. By mapping these modalities into a single, smooth latent manifold, GOLD naturally facilitates a synergistic co-diffusion process. To enhance structural validity, we further introduce a training-free, gradient-guided sampling mechanism. By decoding the generated sequence probabilities and side-chain geometries into structures during the sampling process, we compute analytical gradients from physical constraints. This dynamic feedback actively guides the generated sequence to a physically stable state. Extensive experiments validate the superiority of GOLD, achieving state-of-the-art performance across sequence recovery, secondary structure validity, and 3D foldability metrics. Our code and data are publicly available at this https URL.

---


### 87. [TALLOP: Joint Optimization of Local Training and Communication Compression for Time-Constrained Federated Learning](https://arxiv.org/abs/2610.22996)

**<font color=#1a73e8>作者：</font>** Honoka Anada, Yafei Ou, Shinya Takamaeda-Yamazaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimizing the wall-clock time required to reach a target accuracy is crucial in federated learning (FL), where many applications require frequent model updates as data distributions evolve over time. Nevertheless, in heterogeneous environments, slow clients with limited computational and communication capabilities can delay global synchronization, forcing faster clients to wait and increasing the overall training time. To mitigate this straggler effect, recent studies have introduced per-round time constraints and adapted client workloads within the available time. However, these approaches primarily focus on local computation, whereas communication can become a major bottleneck in communication-limited environments, motivating the joint optimization of training workload and communication compression. Although previous studies have explored such joint optimization, determining an effective training--communication balance under a fixed per-round time budget remains challenging, as the resulting model performance depends on both training progress and compression-induced degradation. We therefore propose TALLOP, which jointly optimizes the local training workload and communication compression under per-round time constraints. TALLOP predicts the training loss achievable under different computation budgets from the early-stage mini-batch loss trajectory (LENS), and estimates the degradation caused by communication compression using a compression-error model (CLEN). TALLOP combines these predictions to select the training-communication allocation that minimizes the post-compression loss under the given round time constraint. Experiments in heterogeneous FL environments show that TALLOP generally achieves competitive or improved time-to-accuracy compared with approaches that optimize only local training or neither, although the benefit over training-only adaptation depends on the setting.

---


### 88. [A Label Noise Robust Algorithm for Graph Data using Neighborhood Label Distribution](https://arxiv.org/abs/2610.22998)

**<font color=#1a73e8>作者：</font>** Pintu Kumar, Nandyala Hemachandra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Convolutional Networks (GCNs) have demonstrated exceptional performance on graph-structured data. However, their success heavily relies on the availability of clean labels, an assumption that often fails in real-world scenarios. The learnability of GCNs is intrinsically linked to the neighborhood structure of nodes, making it critical to understand how this structure changes in the presence of label noise. In this work, we investigate how the neighborhood label distribution of a node changes under label noise. We mathematically derive that label noise smooths this distribution, which inherently increases its entropy and severely decreases interclass distinguishability. To address this challenge, we propose Leave-one-out Entropy Node Screening (LENS), an end-to-end framework that identifies noisy nodes by measuring the reduction in neighborhood entropy when a specific node is removed. LENS further incorporates a relabeling mechanism to recover and preserve valuable feature information instead of entirely discarding the identified noisy nodes. Crucially, the end-to-end computational overhead of LENS is remarkably low. Extensive evaluations demonstrate that our algorithm achieves state-of-the-art node classification accuracy while executing an order of magnitude faster than existing noise-robust approaches.

---


### 89. [BRICE: Brain-inspired Recurrent Illusory Contour Encoder for Point Cloud Completion](https://arxiv.org/abs/2610.23001)

**<font color=#1a73e8>作者：</font>** Yunlei Wang, Dawei Li, Xue-song Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mainstream point cloud completion methods are unanimously based on deep learning architectures. On one hand, these methods tend to repetitively stacking attention modules to enhance network performance, which drifts away from the neat design of unified and interpret-able networks; on the other hand, nearly all existing architectures rely solely on feed-forward connections to propagate information, neglecting feedback from deeper layers. The recurrent neural architecture, formed by feedforward-feedback loops, have shown its ability to generate Illusory Contours (ICs) in the V1 brain region of mammals; and ICs are essentially a completion mechanism of the brain for visual information. Motivated by this, we design a Brain-inspired Recurrent Illusory Contour Encoder (BRICE) to "imagine" what is missing in the incomplete 3D point clouds. Building upon the foundation model of Predictive Coding (PC), the plug-and-play nature enables BRICE to be seamlessly integrated into mainstream point cloud completion baselines. Experimental results show that BRICE can enhance various completion baselines on different 3D datasets such as MVP2K, PCN, and PlantPCom. Our code: this https URL.

---


### 90. [A Minimal ReLU Classifier on Non-Linearly Separable Data: Convergence and Implicit Bias at and beyond the Edge of Stability](https://arxiv.org/abs/2610.23007)

**<font color=#1a73e8>作者：</font>** Quan Nguyen, Robin Yadav, Param Mody 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient descent (GD) with large learning rates can successfully optimize neural networks even though classical smoothness-based learning rate conditions are violated. Yet theory for this regime largely covers linear models or linearly separable data. We analyze a minimal setting outside both regimes. Specifically, a two-neuron ReLU network trained with logistic loss on 1D non-linearly separable data. The objective is nonconvex and nonsmooth, and GD exhibits edge-of-stability (EoS) behavior. We identify an active cone in parameter space that contains every perfect classifier, where the problem becomes piecewise logistic regression with a varying effective dataset. Within this cone, we prove a finite-time loss bound for constant learning rates and show that GD converges in direction to an explicit max-margin vector, while the orthogonal component converges to the unique minimizer of a non-strongly convex potential. We further establish catapult results where exponentially small loss is reached after a single loss spike. Furthermore, we propose an adaptive schedule that lets learning rates grow to infinity without leaving the active cone. We prove that this schedule achieves a loss rate of $O(1/(T\log{T})$, which is faster than the standard $O(1/T)$ rate. Our theoretical results extend to local convergence on more general network and are validated on MNIST dataset. Overall, we show that this setup provides a tractable neural-network model for studying large and adaptive step sizes beyond linear predictors and separable data.

---


### 91. ["Deep lifts": Neural networks can generalize even with the dumbest optimizer](https://arxiv.org/abs/2610.23009)

**<font color=#1a73e8>作者：</font>** Sunil Madhow, Yu-Xiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a labeled dataset $\{(x_i, y_i)\}_{i = 1}^n$, consider drawing a parameter vector $\hat{\theta}$ uniformly at random from those that interpolate the data within a width-$W$ depth-$D$ ReLU architecture with continuous weights bounded within $[-M, M]$. We study the generalization properties of $\hat{\theta}$ in the case where the dataset can, in fact, be explained by a smaller $w$-by-$d$ ReLU network. Despite the obliviousness of the selection rule for $\hat{\theta}$, it adaptively generalizes at the rate $\tilde O\left(\frac{wdWD}{n}\right)$, rather than being governed by the VC dimension of the full $W$-by-$D$ hypothesis class. The reason is due to a particular inductive bias in ReLU networks: the $w$-by-$d$ parameter *witnesses* an exponential volume of $W$-by-$D$ interpolating parameters, which dwarfs the volume of poorly generalizing parameters (conditioned on interpolation). We explicitly construct this set of near-equivalent $W$-by-$D$ parameters by a proof technique called *deep lifting*, and then tie the achievable volume to stability properties of the $w$-by-$d$ witness. Examples show that these techniques allow us to convert approximation-theoretic results into generalization guarantees for nonparametric classes. We further show that generalization of uniform-random interpolators can survive label corruptions.

---


### 92. [Semantic-Critical Regions for Video-to-Audio Generation](https://arxiv.org/abs/2610.23021)

**<font color=#1a73e8>作者：</font>** Yun Fang, Wei Guo, Zhuonan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world videos, sound events are often associated with localized and fine-grained visual cues, such as object motion, object-part dynamics, contact events, and interactions between objects. Existing video-to-audio (V2A) methods employ implicit conditioning based on global visual representations or explicit control derived from temporal and spatial cues. However, subtle sound-producing and sound-indicative interactions remain insufficiently captured, leaving room for more precise visual conditioning of sound-event semantics and temporal dynamics. Motivated by this observation, we refer to regions containing such sound-relevant visual evidence as Semantic-Critical Regions (SCRs) and introduce SCR-V2A, a V2A generation framework that explicitly localizes and encodes SCRs as fine-grained visual guidance for audio generation. Specifically, we first identify SCRs through sound-related visual localization. We then transform the localized regions into a control representation through adapter-based dual visual encoding, which jointly captures global visual context and fine-grained sound-relevant evidence. The representation is used to condition a downstream audio generation model. Experiments on both in-domain and out-of-domain benchmarks demonstrate that SCR-V2A achieves strong performance in distribution matching and audio quality while remaining competitive in cross-modal alignment and requiring few trainable parameters. These results highlight the value of prioritizing fine-grained, sound-relevant visual regions for V2A generation.

---


### 93. [ASE: Attribution-Guided Semantic Evolution for Time Series Forecasting](https://arxiv.org/abs/2610.23027)

**<font color=#1a73e8>作者：</font>** Yuxuan Zheng, Zhaoyang Li, Purui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External text can supply predictive information absent from numerical histories, but its value depends on how it is represented, combined and deployed. We present Attribution-guided Semantic Evolution (ASE), a modular framework for constructing textual factors, evaluating their conditional contribution, and deploying validation-selected numerical--textual predictors. ASE supports task-specific implementations with lexical measurements, semantic primitives or evolved event/state factors, coupled to suitable numerical experts. Its feedback-based implementation uses conditional refitting diagnostics to guide factor revision and combination search. We evaluate ASE on the four text-associated TESS datasets and dynamic CSI 300 stock ranking. The four forecasting implementations obtain test MSEs of 0.001041, 0.022439, 0.333115 and 1.8150, each below the corresponding published TESS score. On CSI 300, the frozen text-fusion implementation improves mean RankIC by 0.000642 over its numerical expert and by 0.000701 over matched shuffled text, with positive differences in all five seeds. Controlled text perturbations support functional reliance on text correspondence, while incumbent retention prevents regressions in the measured development criterion. Together, the experiments characterize ASE at two levels: forecasting performance of task-specific implementations and the conditional contributions of individual modules.

---


### 94. [Frame-Consistent Feed-Forward 3D Gaussian Splatting from Sparse Unposed Images](https://arxiv.org/abs/2610.23039)

**<font color=#1a73e8>作者：</font>** Viruthshaan Vinasirajan, Ranga Rodrigo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian models have made novel view synthesis almost instantaneous. Feed-forward methods predict Gaussians directly, either in two stages or in a single merged pass. Using two separately trained models is attractive because each can specialize in its own objective: one for accurate pose estimation and the other for high-quality reconstruction, rather than forcing a single jointly trained network to compromise between the two. A natural instantiation pairs a frozen pose estimator, VGGT, with a frozen reconstruction backbone, TokenGS. Prior work, such as VGGT-X and 3R-GS, also adopts a two-stage design, but attributes the resulting quality degradation to noisy pose estimates and introduces learned refinement. We show that this is not the primary source of the problem. Through per-camera analysis across 107 scenes from two datasets, DL3DV and MipNeRF360, using COLMAP poses as the reference, we find that the rotation error after alignment is small (median 1.6 degrees), whereas the translation scale is offset by a large, dataset-consistent factor. Controlled ablations over 140 DL3DV scenes show that the primary obstacles are two integration failures rather than pose error: a coordinate-frame inconsistency and a translation-scale mismatch, both of which can be corrected deterministically. With these fixes, a frozen VGGT driving a frozen TokenGS achieves 22.47 PSNR, within 0.51 dB of the COLMAP reference, with no additional training, when poses are estimated from all scene views. In the sparse setting, where reconstruction uses only four context images under the standard pose-free protocol, the same pipeline matches this all-view quality, yielding a fully COLMAP-free pipeline without any refinement step.

---


### 95. [TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation](https://arxiv.org/abs/2610.23050)

**<font color=#1a73e8>作者：</font>** Yun Wang, Chiyu Wang, Fan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in 3D generation has motivated growing interest in compact generative representations of complex 3D scenes. For native 3D Gaussian scenes, however, learning such representations remains challenging due to widely varying primitive counts, nonuniform spatial density, and differences in geometry and appearance even among spatially neighboring primitives. In this work, we introduce TriFold, a native 3D Gaussian VAE that encodes Gaussian scenes into a fixed-layout triplane latent and jointly reconstructs their geometry and appearance. The key insight is to impose structural regularity on the latent space while preserving the spatial adaptivity of the underlying Gaussians. During encoding, we use cell-wise learned queries to aggregate projected Gaussians into multiple slots per cell, reducing the information loss caused by single-feature pooling. During decoding, occupancy prediction identifies active regions, where query-based set prediction and candidate selection reconstruct local Gaussian sets with spatially varying primitive counts. Building on this representation, we train a latent flow-matching model for conditional scene-level 3DGS generation, enabling point-cloud-conditioned synthesis and single-image-conditioned amodal generation. Experiments demonstrate that TriFold achieves high-fidelity reconstruction and generation from a single image that provides only a partial observation of the scene, validating its effectiveness for native 3D Gaussian representation learning. this https URL

---


### 96. [Aspire: Practical Batch Queries on Dynamic Encrypted Database with Full Leakage Suppression](https://arxiv.org/abs/2610.23057)

**<font color=#1a73e8>作者：</font>** Hao Nie, Wei Wang, Peng Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leakage-abuse attacks against encrypted database systems exploit semantic leakage and pose a severe threat to the confidentiality of plaintext data and queries. To address this problem, we propose a zero-leakage encrypted database that rules out leakage-abuse attacks, which fundamentally rely on semantic leakage. We first distinguish between two kinds of zero-leakage security. Ideal zero-leakage forbids the disclosure of any information beyond public parameters, whereas restricted zero-leakage additionally permits the leakage of metadata (such as database size and query timing). We show that restricted zero-leakage is sufficient to thwart leakage-abuse attacks and is achievable in practice. We then formally define adaptive restricted zero-leakage security and present Aspire, an encrypted database that satisfies this notion. Aspire integrates probabilistic batch code and minimal perfect hashing to support efficient batch keyword queries and dynamic updates while revealing only non-semantic metadata. Experimental results demonstrate the practicality and efficiency of Aspire, showing that Aspire can achieve an amortized query latency of less than 1.38 ms (7.53 s for a batch of 5461 keyword queries), with an amortized communication cost of approximately 2.95 KB (16.1 MB in total), on a $2^{22}$ key-value pairs database.

---


### 97. [Path to Prior-Data Fitted Relational Models via Learned Latent Multi-table Representations](https://arxiv.org/abs/2610.23073)

**<font color=#1a73e8>作者：</font>** Mohammad Sadeq Abolhasani, Viswanath Ganapathy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-data fitted networks (PFNs) show that pretraining on large populations of synthetic tasks can enable generalization to unseen datasets with little or no downstream fine-tuning. This paradigm is effective for transformer-based tabular and relational foundation models such as RDB-PFN, but remains largely unexplored for graph-based relational models built on message passing. We pretrain the graph-based relational foundation model Griffin on large collections of synthetic relational databases and ask whether curriculum learning, which benefits transformer-based relational learners, also improves message-passing representations. Rather than fine-tune on downstream tasks, we use the pretrained encoder as a general-purpose relational representation learner and pass its latent representations to a frozen in-context predictor (\ticl{}); no component is trained on the target task. On 16 real-world relational classification tasks, evaluated over five seeds against raw-feature and untrained-encoder baselines, a purely synthetic curriculum that begins with schema-guided data and continues with schema-agnostic data gives the strongest frozen in-context performance\rev{, outperforming real-data-only pretraining and every unordered single-stage mixture of the corpora; when appended after real-data pretraining, it yields the best encoders overall}. These results provide initial evidence that PFN-style synthetic pretraining transfers to graph-based relational foundation models.

---


### 98. [Where Latents Belong and How They Flow: Joint Identification of Structural Roles](https://arxiv.org/abs/2610.23074)

**<font color=#1a73e8>作者：</font>** Xintong Li, Kun Zhang, Yujia Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent factors in dynamical systems can play different roles across observations and time. For example, an idea in a group meeting may be expressed by only some participants, inherit information from earlier discussions, and shape what is said next. We formalize this notion as the structural role of a latent factor, describing where it is expressed, whether it receives influence from the past, and whether it transmits influence to the future. The main challenge is correspondence, since the three structures may be identified under different permutations, while a structural role is defined only when they are aligned to the same latent coordinate. We show that, under suitable structural and variability conditions, all three roles are jointly identifiable under a common permutation at each time point. Guided by this theory, we develop RoleTrace, a framework that traces structural roles in a shared latent coordinate system. Synthetic experiments validate structural recovery, while experiments on multiparty meetings examine the identified roles in real sequential interactions.

---


### 99. [Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems](https://arxiv.org/abs/2610.23078)

**<font color=#1a73e8>作者：</font>** Karol Budzyn, Adrian Brodzik, Mateusz Szczepkowski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) comprise AI agents that collaborate or compete to perform complex, distributed tasks. Their dynamic interactions create opportunities for threat actors to target and impersonate other agents, intercept messages, inject malicious prompts, and exfiltrate sensitive data while simultaneously complicating the detection of anomalous behavior through conventional monitoring. This paper surveys threats and cryptographic challenges in agent-to-agent communication and presents a zero-trust architecture integrating identity, transport security, message integrity, and monitoring. The architecture establishes agent identities via decentralized identifiers and task-scoped verifiable credentials backed by a permissioned ledger, enforcing least-privilege authorization. For transport security, it provides mutually authenticated, crypto-agile TLS with hybrid post-quantum key establishment, and evaluates KEMTLS with pre-distributed public keys to reduce handshake overhead. Signed CBOR envelopes preserve payload integrity across multi-hop exchanges, while zero-knowledge proofs verify declared task constraints without exposing underlying inputs. Context-aware monitoring of inter-agent messages, tool activity, and execution telemetry informs the setting of risk-based trust thresholds and supports the detection of behavioral anomalies. Together, these mechanisms provide an integrated framework for securing and auditing agent communication, with implications for other agentic protocols and prospective 6G semantic communication.

---


### 100. [Towards High Semantic Fidelity: Hyperdimensional Symbolic Messages in Multi-Agent Communication](https://arxiv.org/abs/2610.23092)

**<font color=#1a73e8>作者：</font>** Shoucheng Song, Chang Yao, Hao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Semantic fidelity is essential for multi-agent communication under non-ideal channels, comprising transmission fidelity and conversion fidelity. Yet existing numerical and neural message formats cannot simultaneously achieve both. To address this, we propose a novel message format-\textbf{H}yperdimensional \textbf{S}ymbolic \textbf{M}essages (HSM) and its corresponding communication framework \textbf{Herm}. For transmission fidelity, Herm suppresses semantic entanglement via an entity-attribute-value structured encoding pipeline. For conversion fidelity, Herm first leverages a receiver-centric ego-binding mechanism to align semantics. Then, a similarity-aware dual-branch fusion module is proposed to prevent critical semantic dilution. To realize explicit message-semantic conversion, we devise an iterative decoding scheme via algebraic inverse operations. Experiments exhibit that Herm outperforms baselines across various noisy scenarios while maintaining superior structural readability.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
