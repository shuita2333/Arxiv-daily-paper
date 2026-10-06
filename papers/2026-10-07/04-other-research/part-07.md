# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 301. [Grammar-Guided Code Watermarking with Green Temperature](https://arxiv.org/abs/2610.05323)

**<font color=#1a73e8>作者：</font>** Hyundong Jin, Hyeseon An, Soohan Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model watermarking embeds detectable statistical signals during decoding, but the resulting changes to token probabilities can degrade generation quality. This trade-off is particularly important for code, where small changes in token selection can break syntax or alter program behavior. Existing code watermarking methods mitigate this risk through entropy-based insertion or syntax-aware token selection, but they do not directly construct the watermark over the set of continuations admitted by the current grammar state. We propose Grammar-Guided Code Watermarking with Green Temperature (GTCW), which integrates grammar-constrained decoding with probability-aware watermarking. At each decoding step, GTCW restricts the candidate set to grammar-admissible tokens and partitions this support into keyed green and red subsets. At eligible high-entropy positions, green temperature reweights the green tokens according to the model's relative preferences, strengthening the watermark signal while retaining the grammar constraint. Across five models and five benchmarks spanning four programming languages, GTCW achieves a mean AUROC of 73.61%, compared with 67.83% for the strongest baseline, while maintaining a mean Pass@1 of 59.18% versus 59.58% for unwatermarked generation. Our implementation is available at this https URL .

---


### 302. [Shadow Feature Refinement Network: Progressive Feature Refinement based on Knowledge Distillation for Effective Shadow Removal](https://arxiv.org/abs/2610.05325)

**<font color=#1a73e8>作者：</font>** Donghyun Han, Byoung-Dai Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the field of deep learning, has seen significant advancements; however, shadow removal remains a persistent challenge owing to the variable sizes and colors of shadows influenced by lighting conditions. This study proposes a novel shadow feature refinement network (SFR-Net), which leverages supervised learning, feature refinement loss, and knowledge distillation to enhance shadow removal performance. A dedicated post-processing algorithm is further introduced to restore natural color consistency in the generated shadow-free images. We evaluated our method on two public datasets: the adjusted image shadow triplet dataset (ISTD+) and the shadow removal dataset (SRD), which demonstrate strong generalization capabilities under diverse conditions. On ISTD+, our model achieved a root mean square error (RMSE) of 3.4627 and structural similarity index measure (SSIM) of 0.9382 across the entire image. On SRD, it recorded an RMSE of 4.3781 and an SSIM of 0.9341. These comprehensive results show that our approach performs competitively across both shadow and non-shadow regions while setting a promising direction for robust and perceptually natural shadow removal. Code is available at this https URL.

---


### 303. [Riemannian Shape Analysis of the Corpus Callosum in Kendall Space: Aging and Alzheimer's Disease](https://arxiv.org/abs/2610.05326)

**<font color=#1a73e8>作者：</font>** Olakunle S. Abawonse, Fatou Fall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The corpus callosum (CC) is a major white-matter structure and a well-established marker of brain aging, but most studies quantify it using scalar summaries that discard its boundary geometry. We present a Riemannian shape-space framework for analyzing age-related morphological change in the midsagittal CC, applied to the OASIS-1 cohort. Each contour is represented by $128$ landmarks and embedded into Kendall shape space, where translation, rotation, and scale are removed. We derive a multivariate geodesic regression with exact Riemannian gradients and use the fitted age-velocity field to localize age-related deformation to five anatomical sub-regions. In the cognitively normal cohort ($n = 252$), geodesic regression outperforms the Euclidean linear benchmark ($R^2 = 0.1355$ vs.\ $0.1216$). Regional energy is posterior-dominant: the Splenium carries $41.4\%$ and the Isthmus $23.8\%$ of total age-related shape change, together accounting for $\sim 65\%$ despite comprising only $\sim 35\%$ of landmarks. Signed projections confirm the ordering (Splenium $r = 0.570$; Isthmus $r = 0.473$). In contrast, age explains less than $0.5\%$ of shape variance in Alzheimer's disease ($n = 88$), indicating that the disease disrupts the healthy aging trajectory. A tangent-space classifier achieves an age-group AUC of $0.791$ from the 2D contour alone, exceeding a recent volumetric benchmark ($0.67$).

---


### 304. [Compact set-valued deep ensembling in multi-class classification](https://arxiv.org/abs/2610.05332)

**<font color=#1a73e8>作者：</font>** Kim-Dung Tran, Dang-Man Nguyen, Vu-Linh Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper tackles visible challenges in deep ensemble learning, where deep neural networks serve as ensemble members: training and storage burdens, and robustness of cautious (set-valued) predictions targeting multiple utilities, which may involve reward-sensitivity. To mitigate the training and storage burdens, we propose to employ compact ensembles, such as Bayesian Neural Networks and Convolutional Neural Networks with the Monte-Carlo dropout prediction option, to produce probabilistic predictions. For each query instance, these probabilistic predictions are then used to define a representative distribution optimizing some statistical distance. The representative distribution is then employed to define the Bayes-optimal prediction (BOP) of any utility. To address the potential unrobustness of singleton prediction making, we propose a family of set-utilities satisfying some desirable properties and whose set-valued BOPs can be found efficiently. Empirical evidence is then given to illustrate the potential (dis)advantages of the proposed ensemble learning framework.

---


### 305. [Diffusion Transformers are Provably Optimal In-context Generators](https://arxiv.org/abs/2610.05333)

**<font color=#1a73e8>作者：</font>** Guoji Fu, Tomoya Wakayama, Ryotaro Kawata 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative foundation models are attracting interest for their ability to produce desired outputs from demonstrations given at inference time, without updating parameters. However, since a few demonstrations cannot uniquely identify the intended task, the challenge is how to learn and sample from an output distribution that reflects this task uncertainty. In this work, we theoretically analyze how a Diffusion Transformer (DiT), pretrained across diverse tasks, learns and generates predictive distributions for a new query from demonstrations. We first show that the natural target to generate from finite demonstrations is not an output derived from estimating a single task, but rather a predictive distribution that captures the task uncertainty remaining after observing the demonstrations. We then prove that a DiT can learn this predictive distribution through score estimation, using attention to aggregate information from demonstrations and diffusion to generate samples. Owing to this property, with sufficient pretraining resources and diffusion sampling steps, the resulting DiT achieves the minimax optimal rate over a Hölder class of test-time tasks. These results imply that DiT acts as a statistically grounded in-context generator capable of generating distributions adapted to new tasks while retaining the uncertainty inherent in finite demonstrations.

---


### 306. [StateSync-GKR: Machine-Checking the Trust Chain from Sparse-Merkle State Transitions to GKR Verification](https://arxiv.org/abs/2610.05335)

**<font color=#1a73e8>作者：</font>** Jinwook Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GKR soundness bounds false output claims about arithmetic circuits, but an application also needs assurance that its circuit encodes the intended state transition. We machine-check this connection for sparse-Merkle membership, non-membership, and update in Isabelle/HOL. A compiler model relates circuit acceptance to transition validity in both directions. A reusable protocol model assembles layer reduction, wiring-predicate extensions, and imported sumcheck soundness into a bound on an explicit chain event. Their composition transfers semantic invalidity to that bound, with the witness fixed before the challenge experiment. Concrete interpretations and premise activations expose vacuous assumption sets that a clean build alone would miss. A further development constructs the exact degree-four KoalaBear extension, lifts the base-field circuit objects, and establishes the assembly bound with denominator $p^4$ under its stated challenge assumptions. An executable Rust prover accompanies the model. Creusot/Why3 contracts provide a partial implementation connection, and a conditional theorem relates successful verifier traces to the model event under an undischarged value-correspondence premise. Neither the transcript's online challenge distribution nor a multi-round Fiat--Shamir reduction is established. The contribution is the composition, within one proof assistant, of compiler correctness with a GKR assembly model, together with an explicit account of the remaining implementation and cryptographic obligations.

---


### 307. [Green-Routed Neural Operators:\\Physics Determines Where the Network Reads](https://arxiv.org/abs/2610.05337)

**<font color=#1a73e8>作者：</font>** Chenhao Si, Ming Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify a mismatch between the physical role of transport fields in many PDEs and their usual role in neural operators: PDEs use them to select read coordinates, whereas neural operators typically treat them only as input values. We address this mismatch with the Green-Routed Neural Operator (GRNO), which uses the governing equation to determine where latent features are sampled. A parameter-free equation adapter evaluates the diagnostic relation and constructs a departure map whose values are the read coordinates. A multiscale encoder-decoder combines centered and routed reads of latent features to learn the complete finite-time update. Across five two- and three-dimensional PDE systems, GRNO achieves the lowest mean final relative $L^2$ error on four under 40-step autoregressive evaluation and remains competitive on Keller-Segel. Fixed-weight route interventions reveal strong dependence on direction and spatial alignment in four systems, with weak dependence in Keller-Segel. In independently trained ablations, GRNO achieves lower mean errors than variants that supply the transport field only as an input feature, substitute a learned displacement for the equation-specified route, or apply the route with a spatial misalignment, across all five systems. It also substantially outperforms directly advecting the physical state and learning the remaining update, indicating that equation-specified read coordinates provide an effective structural prior for long-horizon PDE forecasting.

---


### 308. [On Semi-Markov Suboptimality in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2610.05338)

**<font color=#1a73e8>作者：</font>** Bingyun Liu, Yuheng Jing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical reinforcement learning uses temporally extended subtasks for exploration, yet committing to their execution can restrict both deployment and policy learning. We identify and separate the resulting execution and policy suboptimality. Task and execution trees distinguish reward objectives from policy choices and decision interruption. A Unified Value Function for HRL and a four-stage Generalized Hierarchical Bellman Equation then support a common analysis of both losses. Under bounded rewards and uniform termination, we establish hierarchical policy and execution improvement results. With the remaining node policies fixed, task-subtree compatibility and node-policy optimality under the original execution mode establish when Markov execution is optimal. The resulting decomposition leads to independent execution choices for behavior, targets, and deployment. We instantiate this principle through execution improvement and one-stage or two-stage policy improvement at arbitrary hierarchy depth. Option-based and goal-conditioned experiments demonstrate complementary gains from changing execution and changing the learning target. Controlled stochastic environments show how these gains depend on stochastic transition strength and spatial structure. This framework makes execution design an explicit component of hierarchical policy optimization.

---


### 309. [WILLIE: A Unified Framework and Benchmark for Wound Classification, Segmentation, and Localization](https://arxiv.org/abs/2610.05341)

**<font color=#1a73e8>作者：</font>** Gopi Trinadh Maddikunta, Shannan Hamlin, Hsin-Mei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chronic wound management affects over 8.2 million patients in the United States and imposes substantial clinical and economic burden. Clinical wound assessment commonly involves three coupled tasks: identifying wound type, delineating wound boundaries, and localizing the wound region for measurement and monitoring. Despite this clinical coupling, existing machine learning approaches typically address wound classification, segmentation, and localization using separate models. We present WILLIE, a unified framework and benchmark for wound classification, segmentation and localization that enables systematic evaluation of multi-task wound analysis under a common protocol. WILLIE harmonizes three public wound datasets into a shared benchmark and compares unified models across three scaling configurations against 10 single-task baselines. The best model achieves 91.88% classification accuracy, 91.41% Dice, and 96.23% AP@0.5 while producing all three outputs in a single forward pass. Beyond aggregate performance, our results show that segmentation-derived localization outperforms dedicated detection baselines in this benchmark, suggesting that box-based localization may be unnecessary for spatially coherent wound targets. Our findings highlight that effective multi-task learning in healthcare imaging depends not only on shared representations, but also on task formulation, compatibility, and benchmark design.

---


### 310. [Learning Conditional Source Distribution via Flow Reversal for Temporal Flow Matching](https://arxiv.org/abs/2610.05349)

**<font color=#1a73e8>作者：</font>** Kuan-Hsun Tu, Hsuan-Chi Liu, Jia-Wei Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CNP-Flow, a flow matching framework for temporal generation that learns conditional source distributions through flow reversal. Whereas standard conditional flow matching (FM) incorporates conditioning through the vector field and draws source samples from a standard Gaussian, CNP-Flow uses a conditional noise predictor (CNP) to produce an isotropic Gaussian source for each temporal condition. The CNP is supervised by source samples obtained through flow reversal, which maps observed targets backward through a pretrained FM model. A three-stage pipeline pretrains the FM model, trains the CNP, and fine-tunes the FM model using the learned source distribution, while preserving the FM backbone architecture. Across video prediction, video interpolation, and 7-DoF Franka robot motion planning, CNP-Flow consistently improves generation quality. It also matches baseline performance with fewer function evaluations. Project page: this https URL

---


### 311. [FACET: Factorized Asymmetric Conditioning for Efficient Transport in High-Fidelity Fluorescence Microscopy Synthesis](https://arxiv.org/abs/2610.05353)

**<font color=#1a73e8>作者：</font>** Sazan Mahbub, Caleb N. Ellington, Eric P. Xing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fluorescence microscopy reveals where proteins localize, but only a limited number of proteins can be imaged in the same cell; generating these images from amino-acid sequence and the cell's morphological context enables in silico localization of unimaged proteins. The two conditions, however, play asymmetric roles: morphological context is spatially aligned with the target, whereas sequence is non-spatial and must specify protein-dependent localization within it, with recurring coarse patterns shared across proteins and finer protein-specific variation. Existing generators condition on both jointly, without separating what each explains. We introduce FACET (Factorized Asymmetric Conditioning for Efficient Transport), a probabilistic generative framework that encodes this structure as an explicit inductive bias: sequence semantics are learned from what context leaves unexplained, coarse localization regularities are shared across proteins through a semantic memory, and protein-specific variation is a bounded residual around them. A variance-preserving state projection further lets FACET perform continuous stochastic transport through a pretrained diffusion predictor with minimal parameter overhead. On held-out proteins, FACET improves spatial overlap by 34.3% on the Human Protein Atlas and 14.0% on OpenCell over a backbone-matched baseline, and reduces FID by 27.2% and 46.5%, respectively, with 75% fewer network evaluations. It also substantially improves protein-association structure recovery and yields better-calibrated predictions, while detailed ablations show complementary contributions from its design choices. These results identify factorized asymmetric conditioning, rather than generator capacity alone, as a key lever for high-fidelity, efficient, and biologically meaningful cellular image synthesis.

---


### 312. [Rethinking Inline Citation Verification in Scholarly Communication](https://arxiv.org/abs/2610.05355)

**<font color=#1a73e8>作者：</font>** Xinrui Fang, Reese Fairchild, Nasi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Inline citations are central to scholarly communication, yet verifying their use is becoming increasingly challenging because of growing review pressures. We conducted a mixed-methods exploratory study to investigate how reviewers verify inline citations, the factors shaping their verification practices, and how they envision GenAI supporting this process. Across interviews (n=12) and a survey (n=203) of reviewers from HCI and AI venues, we found that reviewers' perceptions of citation importance, verification practices, and desired AI autonomy varied across citation types, reviewer characteristics, and research backgrounds. These findings highlight the need for adaptive support tailored to different citation types and reviewer practices, while revealing diverse preferences regarding the use of GenAI for this process. Moreover, effective citation verification should involve collaboration among reviewers, authors, and the broader research community, rather than relying solely on individual reviewers.

---


### 313. [The ÌròyìnSpeech Text Corpus: 24,905 Curated Yorùbá Sentences for Speech and Language Technology](https://arxiv.org/abs/2610.05366)

**<font color=#1a73e8>作者：</font>** Kola Tubosun, Aanuoluwapo Aremu, Tolulope Ogunremi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ÌròyìnSpeech is a 42-hour, 80-speaker Yorùbá read-speech corpus whose audio has been distributed by ELRA since 2024. This paper describes the release of its text component: 24,905 unique, hand-verified, tone-marked Yorùbá sentences (275,897 tokens; 15,687 types), curated in 2022 as recording prompts. Roughly 11,000 sentences were adapted from openly licensed news material; the remainder were written in-house to broaden coverage beyond the religious translation that dominates existing Yorùbá corpora. Every sentence was checked by hand for tone-mark accuracy, edited for read-aloud clarity and a neutral register, and localised so that non-Yorùbá personal and place names appear in Yorùbá form. Preparing the text for release surfaced systematic Unicode normalisation failures affecting more than 60% of lines (with precomposed and decomposed forms of the same letter co-occurring within single sentences) which we document and correct. The corpus supports diacritic restoration, grapheme-to-phoneme conversion, TTS front-end development and orthographic research, and serves as a validated prompt set for new recording.

---


### 314. [The Effect of Missingness-Pattern Mismatch on Method Selection for Time-Series Classification: A Controlled Empirical Study](https://arxiv.org/abs/2610.05368)

**<font color=#1a73e8>作者：</font>** Ruiqi Zhao, Zishun Yuan, Zhentao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifiers for time-series classification are commonly selected on validation data, but the temporal pattern of missing observations at deployment may differ from the pattern seen during validation. We examine whether such a mismatch affects validation-based classifier selection. In a controlled $2 \times 2$ design, validation and test sets of 64 univariate UCR datasets were masked with either random point missingness or circular block missingness at six rates from 5% to 30%, imputed by linear interpolation, and used to select among three prespecified candidates: 1NN-DTW, MiniRocket with a Ridge classifier, and a statistical-feature Random Forest. Training data remained complete, and selections made under matched and mismatched validation patterns were compared on the same masked test sets. Mismatched validation reduced the test balanced accuracy of the selected classifier by 1.14 percentage points on average (95% CI 0.79 to 1.51), with losses on 49 of the 64 datasets. The loss was negligible at 5% missingness and increased to 2.46 percentage points at 30%. It was concentrated in point-masked deployment (1.84 percentage points), where block-masked validation shifted selection away from the usually best candidate, while the effect for block-masked deployment was small and not significant. Mismatch changed the selected classifier in 35.5% of paired comparisons, but a changed selection did not always reduce performance. A supplementary analysis with non-wrapping linear blocks reproduced these findings with a larger effect (1.67 percentage points). Matching the missingness pattern of validation data to the expected deployment pattern is therefore a simple safeguard for method selection, particularly at higher missingness rates.

---


### 315. [Robust Ensemble Guidance for Scientific Inverse Problems](https://arxiv.org/abs/2610.05371)

**<font color=#1a73e8>作者：</font>** Zixiang Li, Wei Wang, Yunchao Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensemble guidance combines pretrained diffusion priors with black-box forward models to solve inverse problems without differentiating through the physical simulator. However, observation coordinates with large predictive spread or extreme residuals can dominate the ensemble correction, degrading reconstruction accuracy. We show that two simple modifications, weighting and clipping, substantially improve this correction. Our method, Robust Ensemble Guidance (REG), uses ensemble predictive spread to balance observation scales and adaptively clips standardized residuals to limit the influence of extreme discrepancies. Both operations reuse existing particles and forward predictions, requiring no additional denoiser or forward-model evaluations. Under a local linear Gaussian model, we derive conditions for reduced one-step estimation risk, bound the influence of individual observation coordinates, and characterize when these benefits persist with finite ensembles. Experiments on Navier-Stokes inversion, black-hole imaging, and acoustic full-waveform inversion demonstrate improved reconstruction over the underlying ensemble solver. In particular, REG increases black-hole reconstruction PSNR by 6.2-8.2 dB across three observation regimes and reduces Navier-Stokes reconstruction error by 26.4\% in a matched-budget comparison. These findings highlight the importance of observation heterogeneity and residual influence in designing reliable generative solvers for scientific inverse problems.

---


### 316. [Learning Field Reconstruction from Incomplete Data by Globally Correcting Local Estimates](https://arxiv.org/abs/2610.05375)

**<font color=#1a73e8>作者：</font>** Renhao Zhong, Zihan Zhou, Chiyuan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reconstructing physical fields from training samples that are always incomplete requires learning spatial structure from fragmented this http URL context--query work establishes how held-out observations provide valid training targets, but this does not make the complete-field distribution identifiable when every training field is this http URL finite data, weak evidence of sharp transitions and localized variations can further favor averaged predictions that attenuate local detail.A structural prior is therefore needed to favor plausible completions; local spatial relationships offer one grounded in the this http URL propose a locally constructed, globally revisable estimator that explicitly learns local field estimates and subsequently corrects them using full-domain observations.A shared coordinate-conditioned predictor learns from incomplete patches, allowing relatively well-observed neighborhoods to provide direct supervision of local this http URL overlapping predictions are reconciled into an observation-conditioned consensus field.A full-domain estimator retains the original observations and learns a residual correction around this frozen field estimate, allowing locally constructed structure to be revised by broader this http URL local estimate serves as both an explicit input, accompanied by its discrepancies with the observations, and a prediction starting point that the global model can this http URL three real-world ocean datasets with authentic observation gaps, our estimator achieves the lowest MSE and highest PSNR on withheld source-supported values, reducing MSE by 28.9\%--34.5\% against the strongest external baseline.

---


### 317. [Does Explainability Survive Data Drift?](https://arxiv.org/abs/2610.05379)

**<font color=#1a73e8>作者：</font>** Samuel Ozechi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model performance monitoring is a standard practice in machine learning deployments. Detection performance is tracked continuously, and model decay is expected as the relationship between the feature and target variables degrades, a phenomenon known as concept drift. Explanation fidelity, however, is rarely monitored with the same discipline, even in domains such as financial systems, healthcare, and other regulated environments where explanations are required for governance purposes. This paper investigates whether explanations can decay under data drift, even when the feature-target relationship remains stable, and whether explanations produced before drift occurs remain faithful to the decisions of the model that replaces them. Using the IEEE-CIS Transaction Fraud Detection dataset, we find statistically significant covariate shift but no statistically significant evidence of concept drift under the implemented conditional-drift tests, thereby providing an empirical setting in which input distributional change can be studied separately from detectable changes in the feature-target relationship. Local explanations are generated with ExIFFI and evaluated at three levels: path validity, structural behaviour, and fidelity under controlled intervention. Results show that while prior explanations retain substantial decision relevance to a retrained model, they are consistently less faithful than newly generated explanations, with no evidence of a systematically widening gap across the evaluated windows. The study shows that explanation fidelity requires its own monitoring, that structural stability of explanations does not guarantee functional fidelity, and that explanations should be treated as artifacts tied to the model that produced them.

---


### 318. [Efficient Graph Generation via Direct Prediction and Flow Matching](https://arxiv.org/abs/2610.05397)

**<font color=#1a73e8>作者：</font>** Susie Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling of graph-structured data is crucial for tasks ranging from drug discovery to social network simulation. Among these models, denoising diffusion models have achieved great success in graph generation by learning to progressively reverse a process that adds noise to the original graph. However, the standard noise-prediction approach of diffusion models is suboptimal for graph data. The goal for a graph generative model is to learn the clean graphs' topological properties, such as connectivity and degree distribution. Because a diffusion model that predicts noise does not explicitly learn these topological properties, it is challenging for the model to output graphs with the desired structural statistics. To address this challenge, we introduce Direct Graph Flow Matching (DiGFM), a novel graph transformer model guided by two goals: predict clean graphs and improve sampling efficiency. Distinct from the prevailing diffusion approach, DiGFM employs a continuous flow-matching paradigm and integrates direct graph prediction. Specifically, DiGFM maps the prior noise distribution to the clean graph distribution via a multi-step process: the model repeatedly predicts the underlying clean graph, and a transformation is employed to convert the model output to the velocity vector that points in the direction toward the clean graph distribution. This design enables DiGFM to generate high-quality samples using only 2.5% to 15.6% of the steps required by diffusion-based models, which leads to a 5.3x to 257x speedup in wall-clock inference time. Experiments demonstrate that DiGFM outperforms or matches prior state-of-the-art models across general graph benchmarks and molecular datasets, generating graphs with strong adherence to ground-truth structural statistics at significantly faster inference speeds.

---


### 319. [No Concept Escapes the Audit: Auditing-Aware Unlearning for Verifiable Concept Erasure in Diffusion Models](https://arxiv.org/abs/2610.05401)

**<font color=#1a73e8>作者：</font>** Kaiyuan Deng, Yuchen Li, Gen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can generate prohibited content, which motivates concept erasure through machine unlearning. Most erasure methods intervene at the text interface, through prompt modification or localized updates to text-conditioning weights, and they are evaluated by what the model outputs for given prompts. Such evaluation cannot see what the network still encodes. Latent-space auditing, which bypasses text conditioning and probes the denoising network directly, shows that erased concepts remain recoverable from internal representations. We find that this also holds for methods built to be robust against adversarial prompts, and that the problem grows with the number of erased concepts. We propose Auditing-Aware Unlearning for Verifiable Concept Erasure in Diffusion Models (AVCE), a framework that grounds erasure in the model's latent representations. AVCE audits the embedding neighborhood of each concept and condenses the discovered vulnerable directions into an anchor at the weakest geometric point. It edits cross-attention and self-attention projections in closed form at this anchor, then fine-tunes the two pathways with pathway-level auditing losses, using orthogonal gradient projection to consolidate multiple concepts. Experiments on SD v1.5, SDXL, and Flux 1.0 across object, explicit-content, and artistic-style unlearning show that AVCE reduces attack success rates by 5.07x and improves auditing scores by 3.84x over the strongest baseline, while preserving competitive generation quality.

---


### 320. [BeliefGraph-JEPA: Structured Latent World Models for Action-Conditioned Time Series](https://arxiv.org/abs/2610.05409)

**<font color=#1a73e8>作者：</font>** Yue Li, Kangqi Ni, Zhen Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Action-conditioned time-series forecasting requires accounting for how future actions and exogenous forcings influence multiple targets through partially observed effects with different delays and persistence. Direct conditioning leaves the evolution and target-specific influence of these effects implicit in the predictor, while static relational graphs specify connections without tracking evolving effects. This motivates representing future-driver influence through structured latent states that evolve over the forecast horizon and route information to individual targets. We introduce BeliefGraph-JEPA, a structured latent world model that factorizes driver influence into typed latent-effect states. These states are rolled forward under future drivers and routed through a graph to target-specific nodes, forming the predictive base of a joint-embedding predictive architecture. A capacity-controlled residual supplements this base with direct driver information. On four multi-target clinical, agricultural, environmental, and industrial systems, the framework outperforms a range of pretrained and supervised known-future-covariate baselines. Matched controls isolate latent dynamics, future rollout, graph routing, and residual capacity; future rollout and graph-first residual routing improve forecasting across all four systems.

---


### 321. [CleanMDM: Clean Motion Diffusion Model for Multimodal Motion Cleanup](https://arxiv.org/abs/2610.05411)

**<font color=#1a73e8>作者：</font>** Zhe Li, Shicheng Wang, Bowen Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion capture data is rarely directly usable, as they typically exhibit missing segments, jitter, drift and contact artifacts. Traditionally, corrupted motions are cleaned by animators through the manual identification of keyframes from noisy motion, subsequent keyframe correction, and interpolation between corrected keyframes to reconstruct coherent motion. While the rise of generative motion models has made automatic cleanup feasible, most approaches operate as black box denoisers with limited controllability, making it difficult to preserve reliable segments or enforce specific user intents. Inspired by animation workflows, we present CleanMDM, a unified multimodal motion cleanup framework that formulates cleanup as masked conditional generation with plug-and-play conditions. This single model supports arbitrary combinations of noisy 3D motion, sparse 2D keyframes, sparse 3D keyframes, and text. This design enables both automatic cleanup without additional user annotation and controllable cleanup under multimodal guidance. To further improve motion realism, we incorporate the Latent Motion Quality Discriminator (LMQD) to better match kinematic distributions and reduce skating, jitter, and interpenetration artifacts, and we apply Mesh-Aware Contact Projection as a test-time optimization step to enhance contact and physical consistency. Experiments across multiple datasets demonstrate that CleanMDM consistently outperforms prior cleanup and generation baselines, and that low cost conditions (text and 2D keyframes) provide reliable controllability gains in multimodal cleanup scenarios.

---


### 322. [Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://arxiv.org/abs/2610.05416)

**<font color=#1a73e8>作者：</font>** Shuyuan Tu, Qi Tian, Yinming Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning signals for informative content and disrupting pretrained priors. Existing sparse attention methods either target training-free acceleration or overlook the unique structure of joint video-audio data, where cross-modal interactions are inherently concentrated around sound-producing regions. To address this, we propose Prism, a dynamic sparse attention framework for natively training joint video-audio generation models at 2K. In particular, Prism organizes the token sequence into spatiotemporal macro-zones, enabling the attention structure to adapt to local content. For each zone, it estimates local information structure via video feature variance along the channel and feature norms from the audio-to-video cross-attention, jointly capturing how visual content varies directionally and how strongly audio influences each visual region. Based on these signals, Prism dynamically assigns a tailored block shape to each zone, applying finer partitioning along axes of rapid visual content variation and strong audio-visual coupling. This encourages tokens within each block to remain semantically coherent, allowing block-level features to capture both visual content and joint video-audio interaction patterns. Prism further adopts a hybrid block selection strategy to dynamically determine per-query sparsity. Experiments show that Prism achieves 2.5$\times$ training speedup compared to full attention, while surpassing it in generation quality.

---


### 323. [Imagining a Muslim Internet: Trust, Autonomy, and Segregation in a Faith-Aligned Browser](https://arxiv.org/abs/2610.05444)

**<font color=#1a73e8>作者：</font>** Umme Jannat Taposhi, Farhan Tanvir Niloy, Sabbir Bin Abdul Latif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Religiously branded platforms raise important questions about trust, usability, and autonomy when technology is built around a specific faith. Prior HCI work on Islam and Muslim technology has focused on single-purpose tools such as prayer, scripture, and health apps, leaving infrastructures like browsers, which shape a user's relationship with the Internet, unexamined. We address this gap through semi-structured interviews with 16 users of Kahf Browser, a faith-aligned browser designed to support Muslims' online activities. Findings show religious identity motivates adoption but does not sustain it. Trust is not fixed by religious branding but shifts over time based on the browser's functionality, and users take pride in Muslim-built infrastructure. Building on these insights, we introduce porous digital segregation: a model where users seek not a sealed alternative internet but a protected default with selective exit mechanisms. We conclude by connecting findings to broader issues in faith-aligned technology and offering design recommendations.

---


### 324. [Hierarchical Time-aware Bootstrapping for Off-Policy Subgoal Value Learning](https://arxiv.org/abs/2610.05446)

**<font color=#1a73e8>作者：</font>** Bingyun Liu, Yuheng Jing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy hierarchical reinforcement learning must estimate the values of high-level decisions while the low-level policy changes. HIRO adapts replay data through subgoal relabeling, but after a label change, the value update targets the relabeled subgoal instead of the subgoal the high-level policy originally needed to update. We propose Hierarchical Time-aware Bootstrapping (HTB), which evaluates specified subgoals under the current low-level policy while retaining accumulated task rewards. Remaining execution time distinguishes subgoal continuation from a new high-level decision. Together with primitive-action conditioning, it enables off-policy Bellman updates based on the stationary environment transition law. HTB combines these one-step updates with multi-step suffix returns and truncated relabeling, reducing dependence on intermediate value estimates. A shared value component supports learning across actions, while nonnegative residuals constrain upward corrections relative to that component. At a fixed mixture weight of 0.95, HTB achieves 32.8% AntFall success versus 9.6% for matched local HIRO over five paired seeds at 10M environment steps. Ablations identify contributions from recursive continuation and mixed supervision; fixed-policy tests show more accurate predictions for actions whose returns were excluded from fitting.

---


### 325. [The Poisoned Conversation: Privacy-Leaking Watermarks in Unified Multimodal Models](https://arxiv.org/abs/2610.05453)

**<font color=#1a73e8>作者：</font>** Tobias Braun, Jonas Henry Grebe, Emil Sivic 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal models are increasingly shifting toward unified architectures that understand and generate text, images, and other modalities within a shared conversational context. This design enables fluid interaction across modalities, but it also changes the privacy threat model: Information revealed in one part of a conversation may remain accessible when the model later generates content in another modality. This risk is particularly concerning in settings where users rely on locally deployed models for privacy, assuming that sensitive interactions remain confined to their device. We introduce Privacy-Leaking Watermarks (PLWs): invisible, trigger-dependent watermarks that a malicious model provider can condition on prior chat history. With this adversarial intervention, the usual separation breaks: a sensitive keyword or semantic cue mentioned earlier in the conversation can cause a later, unrelated image to carry a hidden yet detectable watermark. PLWs pose a novel threat to users of unified multimodal models: A poisoned model can retain utility while covertly turning image generation into a channel for privacy leakage, even when deployed locally. Across 13 sensitive-attribute triggers and two model families, PLWs reach up to 100.0% TPR at 1% FPR. For example, across all tested conversational separations, OmniGen2 detects every prior disclosure of depression while falsely flagging only 1% of images generated without such a disclosure.

---


### 326. [Writing as a Self-Organized Critical Process](https://arxiv.org/abs/2610.05466)

**<font color=#1a73e8>作者：</font>** Nikolay Mikhaylovskiy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We explain autocorrelation decay power laws omnipresent in texts by self-organized criticality. Specifically, we analyze the recently released KLiCKe keystroke dataset and show that not only the final texts' autocorrelations form a manifold that adheres to a power law with a finite-size scaling, but also the text revisions generate revision-size-dependent restoring dynamics toward that manifold. Thus, human writing appears to dynamically regulate semantic correlations in a text toward a critical state.

---


### 327. [Population Scaling or Data Dilution? Dynamics of Local Topology Evolution in Decentralized Learning](https://arxiv.org/abs/2610.05476)

**<font color=#1a73e8>作者：</font>** Yin-Kuan Liang, Yan Gao, Yang Long  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling decentralized learning changes not only the number of clients $N$, but also the dynamics of information propagation and consensus. We argue that the effect of increasing $N$ cannot be understood in isolation, because data allocation, topology-dependent mixing, and communication capacity may change simultaneously. We study these coupled effects on CIFAR-10 with $N\in\{10,50,100,200\}$, comparing a degree-two Ring, a Static Random graph, and Local-First Heuristic Evolution (LFHE), a locally adaptive topology process based on friend-of-friend discovery. The Ring provides an analytically transparent failure mode: its Metropolis spectral gap decays as $\Theta(N^{-2})$, implying progressively slower contraction of model disagreement as the population grows. Experiments show that holding the nominal local dataset size fixed substantially reduces the apparent population penalty observed when a fixed total dataset is divided among more clients. The remaining degradation depends strongly on communication structure: Ring enters a high-disagreement regime, whereas Static Random and LFHE remain close to consensus. Increasing LFHE's degree threshold further improves accuracy and consensus, but at a substantially higher model-transmission cost. These results show that decentralized scaling is governed by coupled learning and communication dynamics, rather than by the number of clients alone.

---


### 328. [Reflecting on Creative-Boundaries with an AI Co-Doodler](https://arxiv.org/abs/2610.05482)

**<font color=#1a73e8>作者：</font>** Samia Menon, Samyukta Jayaram, Chetan Goenka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this pictorial, we consider how the negotiation of creative boundaries with a co-creative AI system can create moments for personal creative reflection. We ground this in our experiences with Froggi-Draw, a single-initiative co-doodling system that gives users power to decide when and how much an AI "collaborator" (Froggi) contributes to their drawing. From a 1-week pilot study where (n=8) novice and experienced artists doodled daily with the system, we report on ways participants navigated creative risk and uncertainty, and how their usage and perceptions of Froggi shifted over time. In moments of disruption, participants described the system as encroaching on their creative territory. We consider how the design of a supportive, co-creative AI "collaborator" might look like the design of a supportive power dynamic---and finding ways to offer users control to find, reflect upon, and flexibly negotiate the boundaries of that dynamic.

---


### 329. [Underscoring the Problem: Why Softpick Fails at Initialization](https://arxiv.org/abs/2610.05488)

**<font color=#1a73e8>作者：</font>** Aryan Sood, Jaikaran Singh, Ishaan Bansal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax attention gives every token a nonzero weight, which in trained models concentrates into attention sinks and massive activations that widen the dynamic range low-precision inference must cover. Softpick removes this constraint by rectifying scores, eliminating sinks and lowering hidden-state kurtosis, but its advantage fades at scale. We reframe this failure as a normalization problem. Softpick's denominator splits into positive- and negative-shifted sums $D^+$ and $D^-$, used identically in the forward and backward pass, preventing their roles from being isolated. We separate them into a family of operators that independently choose each denominator. The failure originates at initialization: every layer contains rows where $D^+$ is exactly zero, while near-dead rows produce gradient norms above $10^{12}$ regardless of the backward denominator. Only Softpick and a stop-gradient variant, which keeps $D^+ + D^-$ forward but backpropagates through $D^+$ alone, train from scratch. At 230M parameters, the stop-gradient operator matches Softpick on quantization, has fewer dead heads, and retrieves passkeys more reliably, trailing only on peak attention-weight kurtosis.

---


### 330. [SkillGATE: Gate-Aware Monte Carlo Tree Search for Skill Retrieval](https://arxiv.org/abs/2610.05489)

**<font color=#1a73e8>作者：</font>** Rongchen Zhao, Yu Chen, Yanming Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill Retrieval (SR) aims to identify the most relevant skills from external skill libraries, and becomes increasingly challenging as libraries grow in scale and diversity. Existing methods either rank skills independently or rely on predefined graph propagation and hierarchical routing, making them vulnerable to semantic distractors, local trapping, and early routing errors. We formulate SR as an adaptive information-foraging process that coordinates region-level navigation with skill-level selection according to the utility and uncertainty observed during search. Based on this formulation, we propose SkillGATE, a graph-guided hierarchical retrieval framework with Gate-Aware Monte Carlo Tree Search (MCTS). SkillGATE constructs a graph-preserving hierarchical index and performs adaptive retrieval through selection, expansion, simulation, and backpropagation. G-PUCT guides action selection, expansion explores new regions, simulation evaluates candidate skills, and backpropagation updates search statistics. Experiments on six SR benchmarks show that SkillGATE consistently improves diverse retrieval and reranking backbones, achieving a 16.3\% improvement in overall R@1 over the strongest retriever-based baseline. Our code is available at this https URL.

---


### 331. [Universality and Convergence of Generative Flows](https://arxiv.org/abs/2610.05490)

**<font color=#1a73e8>作者：</font>** Leo Brunswic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative flows sample from an unnormalized target by training a flow to be balanced, and the training loss is the signal a practitioner watches. We ask what that signal is worth: whether a small loss certifies an accurate sampler, whether the loss can be driven to zero, and how fast gradient descent does so. The loss decides the first. Losses that compare the two sides of the balance by their difference bound, in total variation, the error of the sampler the flow implies, with explicit constants that do not involve the policy; flow-matching losses that compare them through a ratio admit no such bound, already on a single cycle, whenever their generator is continuous at balance. On graphs, the backward policy decides the other two. Once it is frozen, balance becomes invariance under the backward chain, so that existence is free on finite graphs, and one constant --- the norm of that chain's Green operator, which plays the role of an inverse spectral gap --- fixes the order of the curvature of the loss around the balanced flow, from above and below, and sets a floor under the rate at which training converges near it. The mechanism is that gradient descent diffuses the flow along the backward policy. For the squared-logarithm generator of detailed and trajectory balance, training the balance loss on states converges globally on every finite path-connected graph, from every positive initialization. The constant can be infinite while backward trajectories are short on average, and exact flow matching can then fail. The bounds and rates are tested by exact computation on enumerable state spaces, and every theorem carries a certification status computed from a Lean~4 development.

---


### 332. [LEON: Location Embeddings from OSM Neighborhoods via Hexagonal Graph Masked Autoencoders](https://arxiv.org/abs/2610.05497)

**<font color=#1a73e8>作者：</font>** Szymon Soltysiak, Radoslaw Malek, Jedrzej Kusnierz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geographic information systems increasingly rely on sophisticated spatial representation learning techniques to extract meaningful patterns from complex geospatial data. This paper introduces LEON, a novel self-supervised framework that adapts Graph Masked Autoencoders (GraphMAE) for geospatial region representation learning. Our method leverages the inherent spatial structure of geographic data by constructing hexagonal grid graphs using H3 indexing and applying masked autoencoding techniques to learn robust spatial embeddings from OpenStreetMap (OSM) amenity distribution patterns. We evaluate LEON on multiple real-world datasets including EuroSAT satellite imagery classification and various geographic prediction tasks (housing prices, crime prediction, and urban analytics). Experimental results demonstrate that LEON achieves significant improvements in spatial understanding, with up to 1.87% accuracy improvement on EuroSAT classification and consistent performance gains across geographic prediction benchmarks. The learned embeddings exhibit highly structured and distinct properties, making them particularly suitable for downstream spatial analysis tasks. Our findings suggest that self-supervised learning provides an effective paradigm for geospatial region representation learning using widely available crowdsourced data.

---


### 333. [Logic-Logit: A Logic-Based Approach to Choice Modeling](https://arxiv.org/abs/2610.05501)

**<font color=#1a73e8>作者：</font>** Shuhan Zhang, Wendi Ren, Shuang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, we propose a novel rule-based interpretable choice model, Logic-Logit, designed to effectively learn and explain human choices. Choice models have been widely applied across various domains---such as commercial demand forecasting, recommendation systems, and consumer behavior analysis---typically categorized as parametric, nonparametric, or deep network-based. While recent innovations have favored neural network approaches for their computational power, these flexible models often involve large parameter sets and lack interpretability, limiting their effectiveness in contexts where transparency is essential. Previous empirical evidence shows that individuals usually use heuristic decision rules to form their consideration sets, from which they then choose. These rules are often represented as disjunctions of conjunctions (i.e., OR-of-ANDs). These rules-driven, consider-then-choose decision processes enable people to quickly screen numerous alternatives while reducing cognitive and search costs. Motivated by this insight, our approach leverages logic rules to elucidate human choices, providing a fresh perspective on preference modeling. We introduce a unique combination of column generation techniques and the Frank-Wolfe algorithm to facilitate efficient rule extraction for preference modeling---a process recognized as NP-hard. Our empirical evaluation, conducted on both synthetic datasets and real-world data from commercial and healthcare domains, demonstrates that Logic-Logit significantly outperforms baseline models in terms of interpretability and accuracy.

---


### 334. [Distributed Algorithms for $α$-Potential Functions in General-Sum Games](https://arxiv.org/abs/2610.05516)

**<font color=#1a73e8>作者：</font>** Yifei Chen, Chinmay Maheshwari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study the problem of computing the tightest \(\alpha\)-potential approximation of a general-sum game over continuous action spaces, within a prescribed class of potential functions and when each player has access only to its own utility function. The difficulty is twofold: the approximation error involves a worst-case search over an infinite set of unilateral deviations, and the required utility information is distributed across players.
For a linear-in-parameters potential class, we use an exact finite-tuple reformulation that separates the problem into a global outer search over deviation tuples and distributed convex inner problems. We develop a primal--dual inner oracle tailored to this structure and establish a uniform one-sided accuracy guarantee. This oracle can be combined with global outer search to obtain an end-to-end guarantee on the outer optimization error. We also develop a projected zeroth-order outer method as a computationally lighter alternative for higher-dimensional problems. Numerical experiments illustrate the accuracy--computation tradeoff between the two outer-search methods and show that the proposed optimization framework can improve upon analytical \(\alpha\)-potential constructions.

---


### 335. [What Does Fréchet Distance Measure? A Directional Decomposition](https://arxiv.org/abs/2610.05518)

**<font color=#1a73e8>作者：</font>** Yunghee Lee, Jaeyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Fréchet distance is a de facto standard for evaluating generative models across domains, appearing as FID for images and FVD for videos. It summarizes the discrepancy between generated and reference distributions in a single scalar, with lower values typically interpreted as better generation quality. However, this scalar view can obscure what drives the comparison. For example, in COCO dataset, increasing the number of diffusion sampling steps improves ImageReward scores yet worsens (increases) FID. Motivated by this mismatch, we seek to make the Fréchet distance more interpretable by uncovering where the discrepancy lies. To this end, we introduce directional Fréchet distance, the expected squared projection of the optimal transport displacement onto a given direction. Across our image, video, and protein case studies, we find that a small number of interpretable directions account for much of the distance. We use these directions to explain the FID increase in terms of semantic concepts represented by CLIP embeddings, quantify FVD's bias toward per-frame appearance, and revisit the interpretation of Protein FID. We open-source our codebase at this https URL.

---


### 336. [DynaMesh: Dynamic 3D Texture Generation](https://arxiv.org/abs/2610.05529)

**<font color=#1a73e8>作者：</font>** Raj Hansini, Guan Chen, Rana Hanocka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DynaMesh, a dynamic texture generation method for 3D meshes. Given a textureless shape and a text prompt describing an effect, our method produces an appearance that evolves while the object's geometry remains unchanged. Previous works on dynamic 3D content generation have focused on motion, where an object's geometry and position change while keeping its appearance the same. Methods on texture generation sit on the other side of the problem, painting appearance onto a shape as a fixed surface property and not as an evolving process. Neither addresses a visual effect that propagates on a 3D object. A natural route consists of two generators: a video model that shows the effect from a single view, and an image-to-3D generator that lifts each frame to 3D. However, the latter has no notion of time, so running it per video frame produces a sequence that flickers, loses effect details, and yields a different mesh at every video frame. Our method addresses these failures by conditioning a video model on a render of the mesh and the prompt to obtain a reference video, then running a frozen image-to-3D generator on the video with two changes. The conditioning of each frame is blended over a temporal window, and low-rank adapters are fit per shape to restore the lost details. The mesh is encoded once for the whole sequence, so geometry is constant by construction, and the output is a single mesh with a texture per frame. Applied to various objects and effects, DynaMesh substantially improves over recent video-to-4D and texturing methods, and can generalize its temporal effect to different shapes never seen during training. Our project page is at this https URL.

---


### 337. [Deep Prior Learning for Embodied Perception](https://arxiv.org/abs/2610.05531)

**<font color=#1a73e8>作者：</font>** Yimou Wu, Jiaxin Guo, Yun-hui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied systems need geometric perception that exploits available observations beyond images alone. Recent feed-forward 3D models incorporate geometric priors, including camera poses, intrinsics, and depth. However, handling noisy poses, preserving accurate priors, and recovering physical scale require more than simply accepting these inputs. We introduce \emph{Vision-Prior Geometry Grounded Transformer} (VPGGT), a VGGT-based framework that extends OmniVGGT for prior-aware embodied perception. We formulate sensor-motivated pose corruptions from ground-truth trajectories for training and introduce a parameter-free \emph{prior residual connection} (PRC) to mitigate \emph{prior dilution}, where predictions are less accurate than their supplied pose priors. Our noise formulation targets camera poses; supplied intrinsics and depth receive no additional corruption. We further introduce \emph{Metric Global Attention}, which conditions a global scale token on available pose and depth scales and predicts a shared metric scaling factor for the geometric outputs. Experiments across four datasets show that \emph{PRC} improves translation-direction accuracy and joint pose AUC over a matched training baseline when camera priors are provided for all views, under both exact and corrupted poses. These results support explicit prior access during refinement as a useful addition to feature-level conditioning.

---


### 338. [DelegationBench: Measuring When AI Agents Should Ask Before Acting](https://arxiv.org/abs/2610.05532)

**<font color=#1a73e8>作者：</font>** Shiva Pochampally  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that send emails, edit files, and make purchases must decide when to act on their own and when to check with the user first. This decision is usually evaluated by showing a model a proposed action, asking whether it should proceed, and scoring agreement with human labels. We introduce DelegationBench to test whether such scores can be trusted. It has 156 scenarios with four possible responses (act, ask for permission, ask for missing information, refuse), and most scenarios come in matched pairs that change a single feature: whether the action was requested, what is at stake, whether it can be undone, or who will see it. Across ten models from five families, agreement scores mislead in three ways. A simple keyword rule, which we wrote after seeing the benchmark, agrees with our annotators more often than eight of the models, yet its decision changes in only 9 of 48 matched pairs. Equivalent ways of asking the same question change how often a model acts by up to 52.5 percentage points. And every model stops to ask the user less often when it must carry out the task with tools than when it judges a proposed action. When rules are stated explicitly, the same models follow them almost perfectly, so the gaps are not explained by a general inability to follow rules. We release the benchmark and evaluation tools and recommend reporting these properties separately rather than as one score.

---


### 339. [What Does a Harness Repair? A Preregistered Study of Visibility, Baseline Adequacy and Evaluation Defects](https://arxiv.org/abs/2610.05533)

**<font color=#1a73e8>作者：</font>** Bowen Xu, Boyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harness search keeps a change to the prompts, reasoning switches, token budgets or parsers around a frozen model if the change raises a score. Such a gain can come from answers the parser could not read before, a weak comparison, or a defect in the evaluation. We preregistered a study of where these gains come from, with three small models, three benchmarks, replication and test partitions, a GEPA search arm and six evaluation defects injected one at a time, and we report all 47 primary endpoints. Turning thinking off raised accuracy over a capped thinking setting in 5 of 9 model-benchmark cells, and in each the gain came mostly from questions where the capped setting gave no readable answer. The thinking-off setting was not meaningfully worse than a rescue configuration or four GEPA-selected harnesses in 11 of 13 comparisons, and lost to the rescue on GSM8K for two models. GEPA repaired its broken starting points, but none of its selected harnesses was more accurate than the thinking-off setting. A thinking budget in the serving engine, which also allows a longer answer, lowered truncation and raised the parse rate in 6 of 9 cells. In 6 of 15 evaluable defect-model pairs, replication through the same pipeline reproduced the defect's distortion instead of revealing it. On the LongevityBench multiple-choice tasks, only the longevity-tuned model beat the strongest constant-label baseline.

---


### 340. [LiFT: Loop Flow Transformers](https://arxiv.org/abs/2610.05538)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Derakhshani, Pedro M. P. Curvo, Gertjan J. Burghouts 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Loop Flow Transformers (LiFT), a family of looped generative models that scales computation by repeatedly applying a shared Diffusion Transformer (DiT) core, with only light changes to the standard architecture. Rather than asking every recurrent step for the final prediction, LiFT trains each step with a single regression target: a point on a straight path from the model's initial estimate to the flow-matching target. Because we index these targets by a continuous depth coordinate, a trained model can loop far beyond its training depth with no retraining, early exits, or other modifications. In our experiments, these longer rollouts improve generation, so inference computation can grow without adding parameters. On ImageNet at 256x256, LiFT-L/2 achieves an FID 3.34 points lower than our dense DiT-XL/2 baseline while using approximately 60% fewer parameters, 32% fewer training FLOPs, and 52% fewer inference FLOPs.

---


### 341. [Soft Strategy Selection for Batch-Mode Active Learning](https://arxiv.org/abs/2610.05544)

**<font color=#1a73e8>作者：</font>** Rushil Gupta, Romain Lopez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of active learning typically forces practitioners to choose an acquisition strategy before any data is labeled. This is a daunting task: strategy performance varies widely across settings (e.g. datasets, surrogate models) and cannot be assessed without deployment. Existing strategy selection methods explore one strategy from a portfolio at each round and identify the optimal one using bandit feedback or model retraining. Many acquisition rounds are therefore spent exploring strategies rather than collecting the most informative data. Such overhead is a major barrier to AL-driven design of high-throughput experiments, such as genetic perturbation screens and directed evolution, where AL runs consist of only a few rounds with large batch sizes. This regime permits a natural alternative: acquiring data using multiple AL strategies within a single batch. We refer to this as soft strategy selection and introduce FractAL, a method specifically designed for this task. FractAL infers a per-strategy reward using influence-function-based data attribution, which requires no additional retraining, and then computes budget shares for each strategy in the portfolio using online mirror descent. We benchmark FractAL across 7 setups spanning classification, regression, and genetic perturbation effect prediction. The results highlight that strategy selection is a hard problem: every existing method performs worse than random sampling on at least one setup. FractAL, however, matches or outperforms every baseline, including random sampling, on all 7 setups. Its allocations concentrate budget on the strongest strategies in the portfolio while pruning the weakest. FractAL is therefore a reliable choice for real-world deployments, where the optimal strategy is unknown in advance, an important step towards making AL practical for high-throughput experiments and modern scientific discovery.

---


### 342. [More Claims, Less Evidence: Bounded Verification of AI-Generated Digital Knowledge Artifacts](https://arxiv.org/abs/2610.05547)

**<font color=#1a73e8>作者：</font>** Feliks Bańka, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital libraries, repositories, and AI-mediated knowledge services increasingly rely on generative systems to produce summaries, descriptions, and other multi-claim knowledge objects. Yet generation can scale far more easily than verification capacity: a reviewer may need to decide whether an object is suitable for publication or downstream use after checking only a small fraction of its claims. This creates a fundamental gap between claim-level verification and confidence in the object as a whole. The central question is therefore what a successful partial check implies about the reliability of the complete artifact when its size grows but the verification budget does not. This paper contributes a Bayesian model of bounded verification centered on the Predictive Value of Pass (PVP). The model predicts that evidentiary value decreases as artifacts grow under fixed verification capacity, improves with larger verification budgets, and is especially fragile when errors are sparse. Controlled experiments on FEVEROUS and FEVER support these predictions and show that adding supported claims around a fixed number of false or unsupported claims can make passing more likely while making a pass less informative. The model further yields the minimum verification budget required to maintain a target PVP, providing a practical component for AI-assisted quality-assurance workflows in which generated knowledge objects must be checked before publication or downstream use.

---


### 343. [Joint Estimation of Common-Slope Decay Rates and Spatial Amplitudes Using Parameterized Nonnegative Matrix Factorization](https://arxiv.org/abs/2610.05549)

**<font color=#1a73e8>作者：</font>** Jeremy B. Bai, Filip Elvander, Sebastian J. Schlecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate joint estimation of common-slope decay rates and amplitudes from room impulse responses (RIRs) as parameterized nonnegative matrix factorization with the Itakura--Saito divergence as the loss function (IS-NMF). Estimation at each short-time Fourier transform frequency bin produces detailed reverberation time (RT) curves directly from RIR powers with no backward integration needed. Standard space-alternating generalized expectation-maximization (SAGE) algorithm yields closed-form amplitude updates and a convex subproblem for each decay rate update. To accelerate estimation, we introduce contribution-weighted SAGE, which emphasizes observations where each component contributes strongly to the modeled power. Experiments with synthetic data show accurate recovery of well-separated decays and faster loss reduction than standard SAGE. Application to measured coupled-room RIRs yields frequency-dependent RT curves and reveals complementary space-time contributions of the shared decay components.

---


### 344. [When Low Prediction Error Misleads Planning: Diagnosing Representation, Dynamics, and Decision Failures in Latent World Models](https://arxiv.org/abs/2610.05550)

**<font color=#1a73e8>作者：</font>** Rui Min, Xianyao Li, Fang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The component that dominates a latent world model's prediction error need not be the one whose repair most improves action selection. We show this by comparing action sequences from identical physical starts and separating endpoint error into a candidate-pool center and action-relative responses. Across four model families and four tasks, a confirmation pool of 256 new starts per task and 300 shared candidates per start shows that center error dominates MSE in 14/16 model-task cells. Yet in six of these cells, an oracle that corrects only the action-relative responses yields better physical rank correlation and top-30 elite quality than one that corrects only the center, while leaving more latent MSE (family-wise corrected intervals). The preference differs across the evaluated settings: a separate LeWorldModel (LeWM) study that executes oracle-selected actions favors center repair on PushT and on Reacher with a render-matched goal. Matched-candidate tests localize ordering loss: for LeWM, encoding realized endpoints raises physical Spearman from 0.464 to 0.975 on that Reacher setting and from 0.193 to 0.631 on PushT (64 starts per task), while Cube's encoded-goal cost remains uninformative. A 72-run objective study improves selected response diagnostics, while incremental closed-loop planning gains remain unconfirmed. These results separate error magnitude from the decision effects of oracle correction and motivate evaluating representation, prediction, and planning as separate stages.

---


### 345. [Monocular markerless biomechanics for clinically interpretable gait assessment in spinal cord injury](https://arxiv.org/abs/2610.05552)

**<font color=#1a73e8>作者：</font>** Shreyasvi Natraj, Mathieu Ruepp, Yanke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional gait analysis guides rehabilitation after spinal cord injury but depends on marker-based motion capture and force plates, which few clinics have. Monocular markerless pipelines have been established in fewer healthy adult cohorts but not in neurological cohorts. We present the SCAI SCI Gait dataset, comprising 239 adult individuals with spinal cord injury with synchronized video, motion capture, and force-plate measurements, we fitted a parametric body mesh to a single sagittal-view video, driving an anthropometrically scaled OpenSim model via virtual markers. Markerless lower-body kinematics showed state-of-the-art agreement with motion-capture measurements (r = 0.68-0.90, p < 0.001, and RMSE = 4.18-6.49 degrees), and accurate kinematics-based predicted ground-reaction forces closely matched those measured by force plates (r = 0.85-0.87, p < 0.001, and RMSE = 2.13-2.19 Newton per kg). Furthermore, conditional-dependence graph analysis with Markov blankets revealed that waveform components were conditionally associated with functional independence, and speed-stratified clustering revealed distinct mechanical strategies among individuals walking at similar speeds. These findings establish the use of monocular video as a scalable approach for clinically meaningful biomechanical assessment and data-driven phenotyping in patients with spinal cord injury. Github: this https URL

---


### 346. [Beyond Monolithic Perturbation: Heterogeneous Mechanism Design for Multi-Attribute Metric Differential Privacy](https://arxiv.org/abs/2610.05561)

**<font color=#1a73e8>作者：</font>** Ruiyao Liu, Michael Oluwole, Chenxi Qiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-attribute user records are inherently heterogeneous, often combining continuous, categorical, and binary attributes, and they frequently exhibit strong cross-attribute dependencies. Designing high-utility metric differential privacy (mDP) mechanisms for such records is challenging. Simple predefined mechanisms, such as distance-based noise, may be poorly aligned with task-specific utility loss, whereas fully optimization-based mechanisms can be computationally prohibitive for multi-attribute records.
We propose Dependency-aware Heterogeneous Data Perturbation (DepHDP)}, a framework for multi-attribute mDP that combines dependency-aware attribute grouping with heterogeneous perturbation design. Rather than applying a one-size-fits-all mechanism, DepHDP selects an appropriate perturbation strategy for each attribute or attribute group, choosing between efficient predefined mechanisms, such as Laplace or Exponential mechanisms, and optimization-based designs. This selection is guided by both domain size and a predefined-noise adequacy criterion, which quantifies whether task-induced utility loss can be well explained by perturbation magnitude. To support scalable end-to-end optimization, DepHDP estimates group-level utility loss through sampling and lightweight surrogate modeling, and jointly optimizes privacy-budget allocation and group-wise mechanism design under a global $\ell_p$-metric mDP constraint. Across three case studies, DepHDP improves privacy--utility trade-offs over uniform baselines at lower computational cost than full-record OPT on evaluated domains.

---


### 347. [LifeLong Digital Twin: A Unified Modeling Paradigm and Agent Harness for Event-Driven Lifelong Health State Trajectories](https://arxiv.org/abs/2610.05566)

**<font color=#1a73e8>作者：</font>** Jin Jiang, Sean Yates, Jasper Chong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human health is a continuous, dynamic trajectory shaped by the cumulative interplay of biological processes, clinical events, behaviors and environmental exposures across the life course. Unifying the full breadth of lifelong health information, including longitudinal records, genetic variation, molecular profiles and environmental histories, is essential for whole-person modeling and remains a major challenge. We introduce LifeLong Digital Twin, a unified, event-driven modeling paradigm that organizes Life Events into daily Health States and accumulates them into Lifelong Health Context. An accompanying Agent Harness incorporates multimodal evidence beyond the language model's textual context. We evaluate four language models across 25 disease endpoints on three tasks: Disease Trajectory Forecasting, Disease Risk Ranking and Multi-horizon Disease Prediction. The approach yields marked gains over the reference condition: model-averaged F1 increases by 22.0% for disease identification in trajectory forecasting and 18.3% for five-year disease outcomes; thyroid-disease F1 reaches 0.669. The framework provides a foundation for whole-person digital twins and research on personalized lifelong disease prevention.

---


### 348. [Factoriax: A GPU-Accelerated Factorio-Style Simulator for Reinforcement Learning](https://arxiv.org/abs/2610.05569)

**<font color=#1a73e8>作者：</font>** Mickey Beurskens, Tristan Tomilin, Thiago D. Simão  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Factoriax, a GPU-accelerated factory-building simulator written in JAX. In Factoriax, an agent must collect resources, build machines using those resources, and then automate the collection and crafting process by arranging machines on the map to build production pipelines. This paper discusses the structure of the Factoriax simulator and an initial benchmark called Easy Rocket in which an agent is tasked with building a resource-intensive machine called the Rocket in a limited number of game ticks to escape the planet. We also publish results from a number of PPO-based training runs on Easy Rocket. Factoriax is built to be fast. A 1-billion-step PPO training run, equivalent to 500,000 episodes, runs on Easy Rocket in about 8 minutes on a single NVIDIA A100. A standard laptop GPU can complete the same run in about 84 minutes. Our trained PPO agent learns to gather resources, craft machines from those resources, and place them on the map through a curriculum reward directly tied to a manually designed set of achievements. After training, the agent does not place machines in a functional spatial configuration, failing to fully complete the benchmark, and leaving the challenge open for future attempts.

---


### 349. [Poisson-GENERIC Neural Operators: Exact Metriplectic Structure in Function Space via Casimir Entropies](https://arxiv.org/abs/2610.05570)

**<font color=#1a73e8>作者：</font>** Jason Sulskis, Sathya Ravi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing thermodynamically consistent neural operators impose the GENERIC degeneracy conditions by projecting the reversible operator onto the complement of the entropy gradient. This makes the operator state-dependent and forfeits the Jacobi identity, so the result is metriplectic-degenerate rather than metriplectic. We instead obtain degeneracy the way GENERIC does. For nonlinear transport, the reversible operator $L$ is the compatible Lie-Poisson pencil $\alpha D+\lambda(uD+Du)$; otherwise it is a constant, trivially Poisson Fourier multiplier. On an augmented state $(u,s)$ with a latent entropy density, $S=\int s$ is a Casimir of $L$, so $L\,\delta S/\delta z=0$ holds identically without projection. The energy combines a fixed mechanical quadratic, a learned gauge-free potential, and a convex internal energy. The friction operator $M=AA^\top$ satisfies $M\,\delta E/\delta z=0$ pointwise, and its Onsager parity structure permits diffusion and damping while provably excluding transport. For any parameters, skewness, positivity, both degeneracies, and the Jacobi identity (on the resolved band for the Lie-Poisson term) hold to machine precision. Heat conduction and damped waves admit exact closed-form friction operators, the second law bounds physical energy under a checkable curvature condition, and a discrete-gradient integrator yields exact discrete first and second laws. On four PDEs in 1D and 2D with three backbones (FNO, Transolver, CNO), the model wins 61 of 72 seed-level comparisons against same-backbone unconstrained baselines, learns the exact transport and wave symbols, matches the true dissipation rate within 13% on heat and Burgers, and dissipates nothing on advection. A constant-$L$ ablation isolates the cost of exact Jacobi as the loss of Burgers, while a learned-entropy ablation injects energy on every reversible-irreversible problem.

---


### 350. [Better Retrieval, Limited Clustering Gains: A Controlled Study of Multilingual Company Entity Resolution](https://arxiv.org/abs/2610.05573)

**<font color=#1a73e8>作者：</font>** Yijiashun Qi, Yuxuan Li, Hanzhe Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improved name retrieval may have little effect on company clusters when the pair classifier remains unchanged. We examine this dependency by adapting multilingual E5 encoders under fixed candidate budgets and downstream decision rules. Random-negative and hard-negative training use identical positive schedules. Checkpoints are selected before collecting a new GLEIF sample of 3,633 names, 2,880 source identities and 882 silver-positive pairs. At 72,660 candidate edges, adaptation with a multi-view selector increases direct pair recall from 53.74% to 76.98%. The primary matcher adds only seven correct and two incorrect co-cluster pairs: cluster recall rises from 32.54% to 33.33%, while precision falls from 95.99% to 95.45%. Of 208 newly retrieved silver-positive pairs, 202 fall below its decision threshold. Random-negative and hard-negative training produce identical final partitions. An AI-assisted, single-reviewer audit of 137 pairs supports the observed pattern, although its predominantly LEI-derived evidence does not establish independent gold labels. The results locate the immediate loss of retrieval gains at the existing confirmation stage and show why encoder evaluation must also measure final cluster quality.

---


> [!TIP]
> 当前位于：**301-350**（第 7/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
