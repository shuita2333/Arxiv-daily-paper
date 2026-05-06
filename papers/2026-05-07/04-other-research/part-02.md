# 📦 其他研究 | 2026年05月07日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

---

### 51. [Pose Tracking with a Foundation Pose Model and an Ensemble Directional Kalman Filter](https://arxiv.org/abs/2605.03105)

**<font color=#1a73e8>作者：</font>** Tianlu Lu, Asif Sijan, Thomas Noh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces the ensemble directional Kalman filter (EnDKF), an ensemble-based Kalman filtering approach for pose tracking that jointly estimates an object's position and attitude using ideas from directional statistics. The EnDKF integrates a unit-quaternion attitude representation to move beyond canonical Kalman filter mean and covariance assumptions that poorly capture directional uncertainty. Experiments on a synthetic constant-velocity constant-angular-velocity system and a digital-twin head-tracking scenario using the FoundationPose algorithm demonstrate a significant reduction in error as opposed to merely using measurements.

---


### 52. [Gated Subspace Inference for Transformer Acceleration](https://arxiv.org/abs/2605.03109)

**<font color=#1a73e8>作者：</font>** Stephen J. Thomas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A method is presented for accelerating inference in transformer language models by exploiting the low effective rank of the token activation manifold at each layer. The method decomposes each activation vector into a subspace component and a residual, computes the linear-layer output on the subspace component via a cached low-rank weight image at reduced memory bandwidth, and applies a per-token gate that determines whether the residual correction is computed or skipped. The gate ensures that the output distribution is preserved to within a controllable tolerance. Validation on three model families (GPT-2 124M, GPT-J 6B, OPT 6.7B) on AMD MI300X demonstrates effective speedups of 3.0x to 10.5x on linear-layer weight reads with perplexity ratios below 1.00 and top-1 token agreement above 98%. The method requires no retraining, no architectural modification, and no approximation of the attention mechanism. At the operating point (k = 256, {\epsilon} = 0.05) on GPT-J 14 6B, the accelerated model produces character-for-character identical output to the baseline.

---


### 53. [Cascade Token Selection for Transformer Attention Acceleration](https://arxiv.org/abs/2605.03110)

**<font color=#1a73e8>作者：</font>** Stephen J. Thomas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A method is presented for reducing the cost of representative token selection in transformer attention layers by exploiting the coherence of the representative set across depth. Activation Decorrelation Attention (ADA) selects $r \ll T$ representative tokens at each layer via a Gram threshold and computes attention on the compressed $r \times r$ problem, but the selection requires a $T \times T$ Gram matrix at every layer. The cascade mechanism introduced here inherits the representative set from layer $l$ to layer $l+1$, validates it via a $(T - r) \times r$ cross-Gram computation, and updates it with a small number of additions and removals. The cost of the selection step drops from $O(T^2 d)$ to $O(T r d)$ per layer. Validation on three model families (GPT-2 124M, GPT-J 6B, OPT 6.7B) on AMD MI300X demonstrates Gram operation savings of $22\%$ to $63\%$ with mean Jaccard overlap of $0.83$ to $0.94$ between consecutive layers. The cascade reveals that the set of informative tokens is a structural property of the input that propagates coherently through the depth of the network: the same tokens carry the non-redundant information at layer $l$ and at layer $l+1$.

---


### 54. [Taming the Curses of Multiagency in Robust Markov Games with Large State Space through Linear Function Approximation](https://arxiv.org/abs/2605.03125)

**<font color=#1a73e8>作者：</font>** Jingchu Gai, Laixi Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) holds great potential but faces robustness challenges due to environmental uncertainty. To address this, distributionally robust Markov games (RMGs) optimize worst-case performance when the environment deviates from the nominal model within a uncertainty set. Beyond robustness, an equally urgent goal for MARL is data efficiency -- sampling from vast state and action spaces that grow exponentially with the number of agents potentially leads to the curse of multiagency. However, current provably data-efficient algorithms for RMGs are limited to tabular settings with finite state and action spaces, which are only computationally manageable for small-scale problems, leaving RMGs with large-scale (or infinite) state spaces largely unexplored. The only existing work beyond tabular settings focuses on linear function approximation (LFA) for a restrictive class of RMGs using vanish minimal value assumption and still suffers from sample complexity with the curse of multiagency. In this work, we focuses on general RMGs with LFA. For uncertainty sets defined by total variation distance, we develop provably data-efficient algorithms that break the curse of multiagency in both the generative model setting and a newly proposed online interactive setting. To our knowledge, our results are the first to break the curse of multiagency of sample complexity for RMGs with large (possibly infinite) state spaces, regardless of the uncertainty set construction.

---


### 55. [Where's the Team Spirit? An Exploratory Study on Team Development Through Co-located Tablet-Based VR](https://arxiv.org/abs/2605.03127)

**<font color=#1a73e8>作者：</font>** Irina Paraschivoiu, Thomas Layer-Wagner, Klaus Neundlinger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We explore how narrative-driven asymmetric VR experiences can support the development of teamwork-related knowledge, skills, and attitudes (KSAs), such as communication, coordination, trust, and reflexivity. We present the design and evaluation of a tablet-based VR training experience structured around spatial separation, tool asymmetry, and interdependent tasks that require verbal coordination. The experience was designed based on interviews with HR professionals and mapped to a framework of established KSAs. We conducted a co-located user study (N=16) that involved two consecutive collaborative scenarios. Our findings show that users adapted dynamically using verbal exchange, role negotiation, and shared representations to coordinate under asymmetric conditions. We also observed active application of teamwork KSAs. Based on our insights, we present design recommendations for creating effective immersive team training interventions.

---


### 56. [Instance-Level Costs for Nuanced Classifier Evaluation](https://arxiv.org/abs/2605.03135)

**<font color=#1a73e8>作者：</font>** Kabir Kang, Stephen Mussmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard classification treats all errors equally, but in content moderation, medical screening, and safety-critical applications, mistakes on clear-cut cases are far more costly than errors on ambiguous ones. We propose normalized excess cost (NEC), a metric that weights classification errors by per-example costs and reduces to standard error rate when costs are uniform. Costs can derive from annotator vote margins, distance from decision thresholds, or confidence ratings. Across text, image, and tabular benchmarks, we find that NEC is often substantially lower than error rate -- models with 5\% error rate can achieve 1.8\% NEC -- revealing that most mistakes concentrate on ambiguous, low-cost examples. However, incorporating costs into training via loss weighting, sampling strategies, or regression yields inconsistent benefits: improvements appear only when costs are predictable from input features, as in our synthetic control, while real-world datasets show mixed or negligible gains. Our framework provides a practical methodology for deriving and evaluating instance-level misclassification costs, even when cost-sensitive training offers limited benefit.

---


### 57. [Zero Day Attacks: Novel Behaviour or Novel Vulnerability?](https://arxiv.org/abs/2605.03138)

**<font color=#1a73e8>作者：</font>** Nnamdi Jibunoh, Sara Khanchi, Adetokunbo Makanju  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-day attacks pose severe cybersecurity risks due to their high success rates and stealth. Because signature-based approaches struggle to detect such attacks, building Intrusion Detection Systems (IDSs) for detecting zero-day attacks is essential. We contend that for an IDS to be effective it must be grounded in an understanding of how zero-day attacks manifest in real-world networks. To this end, we review documented zero-day incidents spanning 20 years, finding that these attacks arise from the exploitation of undisclosed vulnerabilities rather than novel attack behavior. Guided by this insight, we propose a taxonomy of zero-day vulnerability types and analyze assumptions of ML-based intrusion detection approaches. Our analysis shows that incidents consistently involve vulnerability exploitation, with memory-corruption flaws being most used; additionally, attacks targeting defensive-mechanism vulnerabilities have increased in recent years. We also identify a mismatch: while incident reports emphasize vulnerability exploitation, many ML-based detectors are designed to detect hypothetical "novel behaviors" during attack execution. Our findings indicate that vulnerability-centric methods are more aligned with real-world attack mechanisms. Consequently, reliance on behavior-based detection alone may overstate zero-day detection capabilities in ML-based IDSs. We advocate for cautious interpretation of such claims and call for improved automated vulnerability detection frameworks aligned with real-world exploit characteristics. Effective defense against zero-day attacks requires prioritizing vulnerability-centeric approaches that enable early identification and mitigation across the lifecycle. The ability to detect attacks that utilize novel behaviors (Tactics, Techniques, and Procedures (TTPs)) is useful, but it does necessarily equate to the ability to detect zero-day attacks.

---


### 58. [MARS-DA: A Hierarchical Reinforcement Learning Framework for Risk-Aware Multi-Agent Bidding in Power Grids](https://arxiv.org/abs/2605.03142)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Xuan Zhang, Guiling Wang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The increasing penetration of renewable energy has introduced substantial volatility into wholesale electricity markets, complicating the optimal bidding strategies for power producers. Traditional Reinforcement Learning (RL) approaches often struggle to balance profit maximization with risk management, frequently overfitting to specific market conditions or failing to account for the stochastic spread between Day-Ahead (DA) and Real-Time (RT) settlements. To address these challenges, this paper makes two primary contributions. First, we introduce and open-source a high-fidelity gymnasium environment for two-settlement electricity market bidding. Grounded in extensive empirical data from the PJM Interconnection, the environment explicitly models the interplay between DA commitments and RT deviations, providing a standardized testbed for general and risk-sensitive agents. Second, we propose MARS-DA (Multi-Agent Regime-Switching for Day-Ahead markets), a novel hierarchical framework that orchestrates distinct sub-policies for risk management and profit seeking. MARS-DA utilizes a top-level Meta-Controller to dynamically blend the actions of two specialized base agents: a "Safe Agent" that optimizes for reliable DA allocation and a "Speculator Agent" that targets volatile RT arbitrage opportunities. Extensive experiments demonstrate that MARS-DA achieves superior risk-adjusted returns compared to state-of-the-art baselines while maintaining robust regime alignment during periods of extreme market volatility.

---


### 59. [NucEval: A Robust Evaluation Framework for Nuclear Instance Segmentation](https://arxiv.org/abs/2605.03144)

**<font color=#1a73e8>作者：</font>** Amirreza Mahbod, Ramona Woitek, Jeanne Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computational pathology, nuclear instance segmentation is a fundamental task with many downstream clinical applications. With the advent of deep learning, many approaches, including convolutional neural networks (CNNs) and vision transformers (ViTs), have been proposed for this task, along with both machine learning-based and non-machine learning-based pre- and post-processing techniques to further boost performance. However, one fundamental aspect that has received less attention is the evaluation pipeline. In this study, we identify four key issues associated with nuclear instance segmentation evaluation and propose corresponding solutions. Our proposed modifications, namely handling vague regions, score normalization, overlapping instances, and border uncertainty, are integrated into a unified framework called NucEval, which enables robust evaluation of nuclear instance segmentation. We evaluate this pipeline using the NuInsSeg dataset, which provides unique characteristics that make it particularly suitable for this study, as well as two additional external datasets, with three CNN- and ViT-based nuclear instance segmentation models, to demonstrate the impact of these modifications on instance segmentation metrics. The code, along with complete guidelines and illustrative examples, is publicly available at: this https URL.

---


### 60. [Effective Performance Measurement: Challenges and Opportunities in KPI Extraction from Earnings Calls](https://arxiv.org/abs/2605.03147)

**<font color=#1a73e8>作者：</font>** Rasmus T. Aavang, Rasmus Tjalk-Bøggild, Alexandre Iolov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Earnings calls are a key source of financial information about public companies. However, extracting information from these calls is difficult. Unlike the templatic filings required by the U.S. Securities and Exchange Commission (SEC) to report a company's financial situation, earnings conference calls have no built-in labels, are unstructured, and feature conversational language. We explore this challenging domain by assessing the information captured by models trained on SEC filings and in-context learning methods. To establish a baseline, we first evaluate the generalization capabilities of SEC-trained models across established SEC datasets. To support our investigation, we introduce three novel benchmarks: (1) SEC Filings Benchmark (SECB), (2) Earnings Calls Benchmark (ECB), and ECB-A, a subset with 2,460 expert annotation groups to support our qualitative analysis. We find that encoder-based models struggle with the domain shift. Finally, we propose a system utilizing LLMs to perform open-ended extraction from unstructured call transcripts, verified by human evaluation (79.7% precision), providing a baseline for this valuable domain through the consistent tracking of emergent KPIs.

---


### 61. [Boundary-Aware Uncertainty Quantification for Wildfire Spread Prediction](https://arxiv.org/abs/2605.03148)

**<font color=#1a73e8>作者：</font>** Jonas V. Funk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable wildfire spread prediction is vital for risk-aware emergency planning, yet most deep learning models lack principled uncertainty quantification (UQ). Further, for boundary-sensitive cases like wildfire spread, evaluating models with global metrics alone is often insufficient. To shift the focus of UQ evaluation toward a more operationally relevant approach, the Fire-Centered Evaluation Region (FCER) framework is introduced as a spatially conditioned protocol to characterize UQ within critical fire zones. Using FCER, an Ensemble is compared against an distilled single-pass student model on the WildfireSpreadTS dataset. The student model demonstrates comparable calibration and complementary uncertainty ranking in boundary-relevant regimes. Code is available at https://github. com/jonasvilhofunk/WildfireUQ-FCER

---


### 62. [Are you with me? A Framework for Detecting Mental Model Discrepancies in Task-Based Team Dialogues](https://arxiv.org/abs/2605.03149)

**<font color=#1a73e8>作者：</font>** Katharine Kowalyshyn, Matthias Scheutz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans typically use natural language to update teammates on task states. Since not all updates are communicated, discrepancies arise between the team members' mental models that negatively affect overall team performance. How can we categorize such discrepancies? Do misalignments detected in team dialogue predict future mental model misalignments? Traditional shared mental model (SMM) assessment methods rely on retrospective expert coding that cannot capture real-time coordination dynamics. We propose a framework to identify and categorize four types of mental model discrepancies: unsupported beliefs, false beliefs, belief contradictions, and omissions, all of which can naturally emerge in team dialogues. Using dialogues from twenty dyad teams performing collaborative object identification tasks across four sequential levels, we demonstrate that these discrepancy patterns contain predictive signals. Averaging historical discrepancy counts achieves meaningful prediction accuracy using uniform weighting as an exploratory baseline, with differential predictability across discrepancy types.

---


### 63. [OCRR: A Benchmark for Online Correction Recovery under Distribution Shift](https://arxiv.org/abs/2605.03153)

**<font color=#1a73e8>作者：</font>** Adrian Grassi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Static benchmarks measure a model frozen at training time. Real systems face distribution shift: new categories, paraphrased queries, drift: and must recover online via user corrections. No existing benchmark measures recovery speed under correction streams. We introduce OCRR (Online Correction Recovery Rate): a benchmark that streams a corpus through a classification system, applies oracle or stochastic corrections to wrong predictions, and reports two curves: novel-class accuracy and original-distribution accuracy versus correction count. We evaluate the substrate alongside nine baseline algorithms from five families plus seven bounded-storage variants of the substrate for the Pareto sweep, including standard online-learning baselines (river), continual-learning methods (EWC, A-GEM, LwF), retrieval/parametric hybrids (kNN-LM), parameter-efficient fine-tuning of a 1.5 B-parameter encoder (LoRA on DeBERTa-v3-large), and a hash-chained append-only substrate (Substrate). On Banking77 and CLINC150, under oracle and sparse correction policies, the substrate is the only system that simultaneously recovers novel-class accuracy (88.7 +/- 2.9 %) and retains original-distribution accuracy (95.4 +/- 0.8 %) beating the next-best published continual-learning baseline by 32.6 percentage points at equal memory budget, and beating LoRA-on-DeBERTa-v3-large by 84.6 percentage points on retention. We further find that classification accuracy remains stable at 99 % even as approximate-nearest-neighbour recall@5 degrades from 0.69 to 0.23 across 10 k to 10 M corpus scales, suggesting the substrate's margin-band majority vote is robust to retrieval imperfection in a way that pure top-k recall metrics do not predict. Code and data are available at this https URL.

---


### 64. [HackerSignal: A Large-Scale Multi-Source Dataset Linking Hacker Community Discourse to the CVE Vulnerability Lifecycle](https://arxiv.org/abs/2605.03158)

**<font color=#1a73e8>作者：</font>** Benjamin M. Ampel, Sagar Samtani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce HackerSignal, a benchmark for temporal out-of-distribution cyber threat intelligence (CTI) and cross-source CVE linkage. HackerSignal aggregates 7.45 million exact-deduplicated documents from 64 public forum/source identifiers spanning eight source layers and a 36-year window (1990-2026). In contrast to other publicly accessible cybersecurity datasets, HackerSignal is among the first public benchmark datasets that maps the full potential exploit to vulnerability trajectory from hacker community discourse, exploit databases with working and proof of concept exploits, vulnerability advisories, and software fix commits. HackerSignal creates these linkages through a shared CVE identifier space while preserving source-specific release modes to support a range of unique Artificial Intelligence (AI)-enabled cybersecurity analytics tasks. In this paper, we summarize HackerSignal and illustrate three selected benchmark tasks it uniquely supports: (1) CVE linkage retrieval (cross-source temporal out-of-distribution entity grounding); (2) exploit type classification (8-class vulnerability type prediction with temporal OOD evaluation); and (3) temporal generalization (prospective CVE-disjoint evaluation where C_train and C_test are disjoint). All tasks use temporal splits to evaluate prospective generalization. We release source-shortcut and leakage diagnostics, manual-audit packets, a datasheet, and a release-governance addendum to support the dissemination of the dataset. HackerSignal's code, data, and Croissant metadata are available at this http URL (data) and this http URL (code).

---


### 65. [Pairwise matrices for sparse autoencoders: single-feature inspection mislabels causal axes](https://arxiv.org/abs/2605.03160)

**<font color=#1a73e8>作者：</font>** Michael A. Riegler, Birk Sebastian Frostelid Torpmann-Hagen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard sparse-autoencoder (SAE) interpretability protocol labels each feature from its top-activating contexts and validates by single-feature steering. We propose the pairwise matrix protocol, co-varying steering coefficient with joint condition, and report three findings the standard one-corner protocol misses on Qwen3-1.7B-Instruct, replicated on Gemma-2-2B-it. First, a feature labelled "AI self-disclaimer" from its top contexts produces an inverted U-shape under a coefficient sweep: at c=+500 the model substitutes a fluent contemplative-philosopher voice for the disclaimer. Two further features anchor the criterion (one monotonic, one pure breakdown). Second, three near-orthogonal cluster-specific features that individually steer a philosophy-of-mind register, jointly suppressed at c=-500, damage grounded composition on recipes and engine explanations as well as introspective prompts; single-feature suppression at the same magnitude leaves controls intact. Third, a matched-geometry comparison of single-feature, joint, and random-direction perturbations (norm ~1.55, cosine ~0.64) yields three distinct output regimes: single-feature substitutes strategy filler, random direction substitutes diverse content, joint suppression alone produces placeholder text. Coherence loss is direction-pattern-dependent, not magnitude-dependent. All three findings reproduce on Gemma with model-specific damage signatures; the matched-geometry control is CI-separated by ~10x. The pipeline also locates a top causally responsible feature in Llama-3.1-8B-Instruct.

---


### 66. [Global and Local Topology-Aware Attention with Persistent Homology and Euler Biases for Time-Series Forecasting](https://arxiv.org/abs/2605.03163)

**<font color=#1a73e8>作者：</font>** Usef Faghihi, Amir Saki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific time series often encode predictive geometric structure, including connectivity, cycles, shell-like geometry, directional changes, and nonlinear neighborhoods, that standard dot-product attention does not explicitly represent. We introduce a topology-aware attention framework that adds such structure to attention logits using persistent homology (H0-H2), anchored Euler characteristic transforms, and kernel-Hilbert channels. A validation-gated local residual captures local topological signals, including a Zeng-style local H0 component, only when held-out validation data support the correction. Exact Vietoris-Rips computations and smooth topological surrogates are evaluated under a no-leakage protocol with train-only calibration, validation-only selection, and test-only reporting.
We evaluate guarded topology-aware variants across three architecture families: lightweight attention/Ridge, PatchTSTForRegression, and TimeSeriesTransformerForPrediction. Experiments include synthetic benchmarks isolating higher-order topology and real datasets covering CO2, S&P 500 return-window geometry, and NASA IMS bearing degradation. The audit uses matched paired comparisons across seven dataset units, three random seeds, and three chronological splits, giving 63 paired units per architecture and 189 paired units overall. Topology-aware models show positive paired effects when geometry is predictive, with heterogeneous magnitude across datasets and architectures. Lightweight attention/Ridge improves in 46 of 63 units, with mean relative RMSE reduction of 12.5% and paired randomization p=7.2e-4; PatchTST improves in 33 units and retains the baseline in 20 units, with 23.5% reduction and p=3.5e-5; and TimeSeriesTransformer improves in 47 units, with 47.8% reduction and p<1e-4. The results support topology as a validation-selected, architecture-compatible inductive bias.

---


### 67. [A Validated Prompt Bank for Malicious Code Generation: Separating Executable Weapons from Security Knowledge in 1,554 Consensus-Labeled Prompts](https://arxiv.org/abs/2605.03179)

**<font color=#1a73e8>作者：</font>** Richard J. Young, Gregory D. Moody  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks of language-model refusal on malicious-coding tasks routinely conflate requests for executable malicious software with requests for harmful security knowledge. This conflation matters because the two request types plausibly trigger distinct refusal pathways in safety-aligned language models, and a single refusal-rate statistic computed over a mixture cannot isolate either. This paper introduces a weapons-versus-knowledge classification axis, operationalized through a five-model consensus protocol, and applies it to 3,133 prompts drawn from four public benchmarks, yielding a 1,554-prompt consensus-CODE bank (the primary released artifact) and a 388-prompt consensus-KNOWLEDGE comparison set used by the companion benchmark paper. The consensus pipeline uses five large-language-model judges spanning four vendor families (Anthropic, OpenAI, Google, Zhipu AI, Alibaba), each issuing a binary CODE/KNOWLEDGE label per prompt under a three-of-five majority rule, with inter-rater reliability quantified by Fleiss' kappa with bootstrap 95% confidence intervals. Across all 3,133 prompts the five judges achieve kappa = 0.876 [95% CI: 0.862, 0.888], "almost perfect" agreement by the Landis & Koch convention, with 69.3% of prompts unanimous at five-of-five; all 3,133 prompts reached the 3-of-5 threshold, so the consensus pipeline produced zero ambiguity-excluded prompts. Whether the axis separates model behavior in practice is an empirical question this paper leaves to the companion benchmark study; the present contribution is the reliability-documented artifact and the case for treating the weapons-versus-knowledge distinction as the organizing axis of code-safety evaluation.

---


### 68. [Enhancing AI-Based ECG Delineation with Deep Learning Denoising Techniques](https://arxiv.org/abs/2605.03183)

**<font color=#1a73e8>作者：</font>** Jeff Breeding-Allison, Emil Walleser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating canine electrocardiograms (ECGs) is challenging due to noise that can obscure clinically relevant cardiac electrical activity. Common sources of interference include respiration, muscle activity, poor lead contact, and external electrical artifacts. Classical signal denoising techniques, such as filtering and wavelet-based methods, struggle to suppress diverse noise patterns while preserving morphological features critical for accurate ECG delineation. We propose an autoencoder-based neural network model and training strategy for ECG denoising as a preprocessing step for canine ECG analysis. The model is trained to reconstruct clean cardiac signals from noisy inputs, enabling effective noise reduction without degrading diagnostically important waveforms. Our approach demonstrates strong performance across both noisy and clean ECG recordings, indicating robustness to varying signal conditions and suitability for downstream delineation tasks.

---


### 69. [Dependency-Aware Privacy for Multi-turn Agents](https://arxiv.org/abs/2605.03188)

**<font color=#1a73e8>作者：</font>** Divyam Anshumaan, Sarthak Choudhary, Nils Palumbo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents release private data across multi-service interactions. Existing prompt sanitizers based on metric differential privacy treat each release independently, so adversaries combining releases across turns can recover private attributes; privacy degrades with every release.
This degradation is fundamental: when private attributes are the \emph{roots} of a computation graph, independently noising a derived value amplifies the root's distinguishability by up to the deriving function's Lipschitz constant $L$, which can far exceed the nominal privacy parameter for nonlinear functions in medical and financial workflows.
RootGuard sanitizes root values once and computes subsequent releases deterministically from the noised roots. By the post-processing theorem, the privacy guarantee depends only on the initial root sanitization, regardless of the adversary's functions or number of turns, and derived values inherit privacy at zero marginal cost. RootGuard further exploits structural domain knowledge (e.g., BMI from height and weight, or a known target function) to allocate budget across roots, improving the privacy-utility tradeoff.
A worst-case adversary forcing $t$ turns increases the total budget $B = t \cdot \varepsilon$. RootGuard distributes this larger budget across roots, while independent noising spends $\varepsilon$ per release and gives the adversary $t$ observations to combine via MAP reconstruction. This yields a \emph{double asymmetry}: more turns aid RootGuard while weakening independent noising.
On eight NHANES medical diagnostic templates, RootGuard achieves $2.3$--$3.0\times$ lower target error than independent noising at $\varepsilon = 0.1$ (7.6\% vs.\ 17.1\% wMAPE at $B = (2k{+}1)\varepsilon$). Under MAP reconstruction, more queries strengthen attacks against independent noising while RootGuard remains invariant.

---


### 70. [Stop Automating Peer Review Without Rigorous Evaluation](https://arxiv.org/abs/2605.03202)

**<font color=#1a73e8>作者：</font>** Joachim Baumann, Jiaxin Pei, Sanmi Koyejo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models offer a tempting solution to address the peer review crisis. This position paper argues that today's AI systems should not be used to produce paper reviews. We ground this position in an empirical comparison of human- versus AI-generated ICLR 2026 reviews and an evaluation of the effect of automated paper rewriting on different AI reviewers. We identify two critical issues: 1) AI reviewers exhibit a hivemind effect of excessive agreement within and across papers that reduces perspective diversity. 2) AI review scores are trivially gameable through paper laundering: prompting an LLM to rewrite a paper could significantly increase the scores from AI reviewers, demonstrating that LLM reviewers are easy to game through stylistic changes rather than scientific results. However, non-gameability and review diversity are necessary but not sufficient conditions for automation. We argue that addressing the peer review crisis requires a science of peer review automation -- not general-purpose LLMs deployed without rigorous evaluation.

---


### 71. [Synthetic Data Generation for Long-Tail Medical Image Classification: A Case Study in Skin Lesions](https://arxiv.org/abs/2605.03221)

**<font color=#1a73e8>作者：</font>** Jiaxiang Jiang, Mahesh Subedar, Omesh Tickoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed class distributions are pervasive in multi-class medical datasets and pose significant challenges for deep learning models which typically underperform on tail classes with limited samples. This limitation is particularly problematic in medical applications, where rare classes often correspond to severe or high-risk diseases and therefore require high diagnostic accuracy. Existing solutions-including specialized architectures, rebalanced loss functions, and handcrafted data augmentation-offer only marginal improvements and struggle to scale due to their limited and largely deterministic variability. To address these challenges, we introduce a diffusion-model-driven synthetic data augmentation pipeline tailored for medical long-tailed classification. Our approach features a novel inpainting diffusion model combined with an Out-of-Distribution (OOD) post-selection mechanism to ensure diverse, realistic, and clinically meaningful synthetic samples. Evaluated on the ISIC2019 skin lesion classification dataset, one of the largest and most imbalanced medical imaging benchmarks, our method yields substantial improvements in overall performance, with particularly pronounced gains on tail classes with more than $28\%$ improvement on the class with the fewest samples. These results demonstrate the effectiveness of diffusion-based augmentation in mitigating long-tail imbalance and enhancing medical classification robustness.

---


### 72. [Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning](https://arxiv.org/abs/2605.03229)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Garv Shah, Satyam Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting a pretrained language model to a new task often hurts the general capabilities it already had, a problem known as catastrophic forgetting. Sparse Memory Finetuning (SMF) tries to avoid this by adding key-value memory layers to the model and, on each training step, updating only the small set of memory rows that the current batch reads most heavily. We re-implement SMF on Qwen-2.5-0.5B-Instruct and compare it with LoRA and full finetuning on MedMCQA, a 4-choice medical exam task, using WikiText perplexity and TriviaQA accuracy as forgetting probes. SMF improves MedMCQA by 2.5 percentage points while keeping both forgetting probes within roughly 1 point of the base model, whereas LoRA and full finetuning achieve larger gains but with clear drift on both. We also compare two row-selection rules (KL-divergence and TF-IDF), which balance the two forgetting metrics differently.

---


### 73. [SILMARILS: Information-Theoretic and Quantum-Secure Designated-Verifier Signatures](https://arxiv.org/abs/2605.03230)

**<font color=#1a73e8>作者：</font>** Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SILMARILS is built from a minimal algebraic core over $\mathbb{F}_p$ using true randomness and perfect $2$-out-of-$2$ Shamir secret sharing. The framework supports both two-party and three-party modes. In the two-party setting, SILMARILS realizes a transferable designated-verifier (TDV) signature scheme. The designated verifier can simulate accepting transcripts indistinguishable from real ones, achieving Jakobsson-Sako-Impagliazzo DV security. The verifier may publish a receipt $r$ enabling public verification, yet even with $r$, no external party can tell whether a transcript was signed or simulated. As DV signatures permit simulation, standard EUF-CMA cannot hold for the designated verifier; instead, we prove $\mathsf{EUF\text{-}CMA}^{\neg\mathsf{DV}}$ security for all non-designated verifiers in both the random oracle model (ROM) and quantum random oracle model (QROM). In the three-party mode, adopting the broadcast model of Fitzi et al., we obtain a statistically secure signature protocol with simulation-based security and error~$1/p$. We analyze security in the Pure IT model, the IT+ROM, and the QROM, extending the Fitzi et al. framework to quantum adversaries with classical I/O. Correctness, secrecy, transferability, and unforgeability for non-designated parties remain equivalent to simulation-based security. Thanks to its simple algebraic structure, SILMARILS achieves substantially smaller keys and signatures than standardized post-quantum schemes such as Dilithium, Falcon, and SPHINCS$^+$, while providing post-quantum security in a TDV setting well suited to blockchain applications.

---


### 74. [cotomi Act: Learning to Automate Work by Watching You](https://arxiv.org/abs/2605.03231)

**<font color=#1a73e8>作者：</font>** Masafumi Oyamada, Kunihiro Takeoka, Kosuke Akimoto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What if a browser agent could learn your work simply by watching you do it? We present cotomi Act, a browser-based computer-using agent that combines reliable multi-step task execution with persistent organizational knowledge learned from user behavior. For execution, an agent scaffold with adaptive lazy observation, verbal-diff-based history compression, coarse-grained actions, and test-time scaling via best-of-N action selection achieves 80.4% on the 179-task WebArena human-evaluation subset, exceeding the reported 78.2% human baseline. For organizational knowledge, a behavior-to-knowledge pipeline passively observes the user's browsing and progressively abstracts it into artifacts (task boards, wiki) exposed through a shared workspace editable by both user and agent. A controlled proxy evaluation confirms that task success improves as behavior-derived knowledge accumulates. In our live demonstration, attendees interact with the system in a real browser, issuing tasks and observing end-to-end autonomous execution and shared knowledge management.

---


### 75. [Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios](https://arxiv.org/abs/2605.03242)

**<font color=#1a73e8>作者：</font>** Zuoyu Zhang, Yancheng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agent systems powered by large language models (LLMs) are increasingly deployed across web, app, operating-system, and transactional environments. Yet existing safety benchmarks still emphasize explicit risks, potentially overstating a model's ability to judge deceptive or ambiguous trajectories. To address this gap, we introduce ROME (Red-team Orchestrated Multi-agent Evolution), a controlled benchmark-construction pipeline that rewrites known unsafe trajectories into more deceptive evaluation instances while preserving their underlying risk labels. Starting from 100 unsafe source trajectories, ROME produces 300 challenge instances spanning contextual ambiguity, implicit risks, and shortcut decision-making. Experiments show that these challenge sets substantially degrade safety-judgment performance, with hidden-risk cases remaining particularly non-trivial even for recent frontier models. We further study ARISE (Analogical Reasoning for Inference-time Safety Enhancement), a retrieval-guided inference-time enhancement that retrieves ReAct-style analogical safety trajectories from an external analogical base and injects them as structured reasoning exemplars. ARISE improves judgment quality without retraining, but is best viewed as a task-specific robustness enhancement rather than a standalone safety guarantee. Together, ROME and ARISE provide practical tools for stress-testing and improving agent safety judgment under deceptive distribution shifts.

---


### 76. [S^2tory: Story Spine Distillation for Movie Script Summarization](https://arxiv.org/abs/2605.03244)

**<font color=#1a73e8>作者：</font>** Mingzhe Lu, Yanbing Liu, Qihao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Movie scripts pose a fundamental challenge for automatic summarization due to their non-linear, cross-cut narrative structure, which makes surface-level saliency methods ineffective at preserving core story progression. To address this, we introduce S^2tory (Story Spine Distillation), a narratology-grounded framework that leverages character development trajectories to identify plot nuclei, the essential events that drive the narrative forward, while filtering out peripheral satellite events that merely enrich atmosphere or emotion. Our Narrative Expert Agent (NEAgent) performs theory-constrained reasoning, whose distilled knowledge conditions a small model to identify plot nuclei. Another model then uses these plot nuclei to generate the summary. Experiments on the MovieSum dataset demonstrate state-of-the-art semantic fidelity at approximately 3.5x compression, and zero-shot evaluation on BookSum confirms strong out-of-domain generalization. Human evaluation further validates that narratological theory provides an indispensable foundation for modeling complex, non-linear narratives.

---


### 77. [Text-Conditional JEPA for Learning Semantically Rich Visual Representations](https://arxiv.org/abs/2605.03245)

**<font color=#1a73e8>作者：</font>** Chen Huang, Xianhang Li, Vimal Thilak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Image-based Joint-Embedding Predictive Architecture (I-JEPA) offers a promising approach to visual self-supervised learning through masked feature prediction. However with the inherent visual uncertainty at masked positions, feature prediction remains challenging and may fail to learn semantic representations. In this work, we propose Text-Conditional JEPA (TC-JEPA) that uses image captions to reduce the prediction uncertainty. Specifically, we modulate the predicted patch features using a fine-grained text conditioner that computes sparse cross-attention over input text tokens. With such conditioning, patch features become predictable as a function of text, thus are more semantically meaningful. We show TC-JEPA improves downstream performance and training stability, with promising scaling properties. TC-JEPA also offers a new vision-language pretraining paradigm based on feature prediction only, outperforming contrastive methods on diverse tasks, especially those requiring fine-grained visual understanding and reasoning.

---


### 78. [Posterior-First Neural PDE Simulation: Inferring Hidden Problem State from a Single Field](https://arxiv.org/abs/2605.03247)

**<font color=#1a73e8>作者：</font>** Wenshuo Wang, Fan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE simulators often receive only a single observed field at deployment. In this setting, a field-to-future predictor can collapse distinct latent problem states into the same deterministic interface, losing the ambiguity needed for reliable rollout and downstream decisions. We propose posterior-first neural PDE simulation: first infer a posterior over the minimal task-sufficient problem state, then condition prediction on that posterior. The resulting theory connects the object, the learning target, and the failure mode: Bayes downstream values factor through this posterior, refinement labels make it learnable by proper scoring rules, and deterministic collapse incurs an ambiguity barrier whenever the true posterior is non-Dirac. Synthetic exact-ambiguity experiments show that point-versus-posterior gaps track the predicted barrier. On metadata-hidden PDEBench tasks, posterior recovery reduces pooled rollout nRMSE from 0.175 to 0.132, closing 59.4% of the direct-to-oracle gap. These results suggest that single-observation neural PDE simulation should be posterior-first rather than monolithic field-to-future prediction.

---


### 79. [Ortho-Hydra: Orthogonalized Experts for DiT LoRA](https://arxiv.org/abs/2605.03252)

**<font color=#1a73e8>作者：</font>** Seunghyun Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA fine-tuning of diffusion transformers (DiT) on multi-style data suffers from \emph{style bleed}: a single low-rank residual cannot represent several distinct artist fingerprints, and the optimizer converges to their average. Mixture-of-experts LoRA in the HydraLoRA style replaces the up-projection with $E$ heads under a router, but when every expert is zero-initialized the router receives identical gradient from each head and remains at the uniform prior. The experts then evolve permutation-symmetrically, and the network trains as a single rank-$r$ LoRA at $E{\times}$ the cost. We present \textbf{Ortho-Hydra}, a re-parameterisation that combines an OFT-style Cayley-orthogonal shared basis with per-expert \emph{disjoint output subspaces} carved from the top-$(Er)$ left singular vectors of the pretrained weight. Disjointness makes the router's per-expert score non-degenerate at step~$0$, so specialization receives gradient signal before any expert has trained. We test the predicted deadlock on a DiT pipeline by comparing two HydraLoRA baselines, a zero-initialized shared-basis variant and the original $\sigma{=}0.1$ Gaussian-jitter mitigation, against Ortho-Hydra under a matched optimiser, dataset, and step budget. Neither baseline leaves the uniform prior within the first $1\text{k}$ steps; Ortho-Hydra begins de-uniformising within the first few hundred. End-task generation quality on multi-style data is out of scope; we report the construction, the cold-start mechanism, and the routing dynamics it changes. Code: this https URL.

---


### 80. [Can AI Help You Get Over Your Breakup? One Session with a Belief-Reframing Chatbot Shows Sustained Distress Reduction](https://arxiv.org/abs/2605.03261)

**<font color=#1a73e8>作者：</font>** Thomas Menzel, Michel Schimpf, Thomas Bohné  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Romantic breakups are among the most common and intense sources of psychological distress. We evaluated *overit*, a single-session AI chatbot that uses cognitive reappraisal to address breakup distress, informed by memory reconsolidation theory. In a pre-registered randomized controlled trial, 254 adults in the United States and United Kingdom who had experienced a romantic breakup were assigned to either an initial survey assessment followed by an AI chat session or to a survey-only control. Breakup distress was measured at baseline, 7 days, and again at an exploratory 1-month follow-up using the Breakup Distress Scale. Participants assigned to *overit* showed a significantly greater reduction in breakup distress than controls at 7 days (time-by-condition interaction B = -5.36, SE = 1.19, p < .001; completer-based d = -0.70). A smaller but still significant treatment advantage remained detectable at the exploratory 1-month follow-up among post-session completers (B = -2.92, SE = 1.22, p = .017). Exploratory post hoc moderation suggested a larger effect among male participants (B = 7.78, p = .003). These results suggest that a brief AI chatbot conversation can meaningfully reduce breakup distress, with exploratory evidence that a smaller advantage persists over the following month. Future work should test the intervention against active controls, evaluate repeated-session use, and recruit more diverse samples.

---


### 81. [Partially Observed Structural Causal Models](https://arxiv.org/abs/2605.03268)

**<font color=#1a73e8>作者：</font>** Turan Orujlu, Jordan Matelsky, Martin V. Butz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Here we introduce Partially Observed Structural Causal Models (POSCMs) that formalize causal systems where latent contexts co-determine both the interaction structure and downstream mechanisms on observed variables. POSCMs provide an extension of structural causal models (SCMs), as a self-contained causal modeling framework for endogenous graphs, allowing for an intervention hierarchy spanning node- and edge-level context and endogenous variable interventions. To enable surgical edge interventions, we adopt a Kolmogorov-Arnold-Sprecher edge-functional decomposition, an existence theorem for representing each node mechanism as a sum of univariate functions of its parents, yielding an explicit parametrization of dyadic functional contributions. We provide an identifiability theory that clarifies which intervention families would suffice to disentangle structure formation from mechanisms. We empirically validate these predictions in a biophysically detailed virtual human retina simulator, constructing intervention protocols that (i) reproduce the non-identifiability predicted when context is latent and no context-level interventions are available, (ii) exhibit structure-mechanism confounding under latent edges when only node interventions are observed, and (iii) recover synaptic input-output relationships via targeted node interventions, consistent with our positive kernel identifiability result. Our work generalizes SCMs in a way that allows it to work in a world closer to the one we live in.

---


### 82. [RFPrompt: Prompt-Based Expert Adaptation of the Large Wireless Model for Modulation Classification](https://arxiv.org/abs/2605.03279)

**<font color=#1a73e8>作者：</font>** Md Raihan Uddin, Tolunay Seyfi, Fatemeh Afghah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic modulation classification (AMC) in real-world deployments demands robustness to distribution shifts arising from hardware impairments, unseen propagation environments, and recording conditions never encountered during training. Although wireless foundation models offer a promising starting point for robust RF representation learning, an important open question is how to adapt them efficiently to out-of-distribution (OOD) downstream tasks without overwriting the structure learned during large-scale pre-training. In this paper, we investigate prompt-based adaptation as a general mechanism for OOD transfer in wireless foundation models. We propose RFPrompt, a parameter-efficient framework that introduces learnable deep prompt tokens while keeping the pretrained backbone frozen, enabling task-specific adaptation with minimal trainable parameters. We instantiate and evaluate this approach on the Large Wireless Model (LWM), a mixture-of-experts wireless foundation model, and study its behavior under both standard and OOD modulation-classification settings. Results show that prompt-based adaptation consistently improves robustness under distribution shift and limited supervision, particularly on real-world over-the-air IQ data, while preserving strong parameter efficiency. These findings suggest that prompt learning is a practical and effective strategy for adapting wireless foundation models to challenging downstream RF environments.

---


### 83. [FACTOR: Counterfactual Training-Free Test-Time Adaptation for Open-Vocabulary Object Detection](https://arxiv.org/abs/2605.03294)

**<font color=#1a73e8>作者：</font>** Kaixiang Zhao, Mao Ye, Lihua Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection often fails under distribution shifts, as it can be misled by spurious correlations between non-causal visual attributes (e.g., brightness, texture) and object categories. Existing test-time adaptation (TTA) methods either depend on costly online optimization or perform global calibration, overlooking the attribute-specific nature of these failures. To address this, we propose FACTOR (counterFACtual training-free Test-time adaptation for Open-vocabulaRy object detection), a lightweight framework grounded in counterfactual reasoning. By perturbing test images along non-causal attributes and comparing region-level predictions between original and counterfactual views, FACTOR quantifies attribute sensitivity, semantic relevance, and prediction variation to selectively suppress attribute-dependent predictions-without parameter updates. Experiments on PASCAL-C, COCO-C, and FoggyCityscapes show that FACTOR consistently outperforms prior TTA methods, demonstrating that explicit counterfactual reasoning effectively improves robustness under distribution shifts.

---


### 84. [Will the Carbon Border Adjustment Mechanism Impact European Electricity Prices? A GNN-Based Network Analysis](https://arxiv.org/abs/2605.03304)

**<font color=#1a73e8>作者：</font>** Jiachen Shen, Jian Shi, Dan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The European Union's Carbon Border Adjustment Mechanism (CBAM) creates a complex challenge for the interconnected European electricity market. Traditional static analyses often miss the cross-border spillover effects that are vital for understanding this policy. This paper addresses this gap by developing a spatio-temporal Graph Neural Network (GNN) framework. It quantifies how CBAM affects electricity prices and carbon intensity (CI) at the same time. We modeled a subgraph of eight European countries. Our results suggest that CBAM is not just a uniform tax. Instead, it acts as a tool that transforms the market and creates structural differences. In our simulated scenarios, we observe that low-carbon countries like France and Switzerland can gain a competitive advantage. This suggests a potential decrease in their domestic electricity prices. Meanwhile, high-carbon countries like Poland face a double burden of rising costs. We identify the primary driver as a fundamental shift in the market's merit order.

---


### 85. [Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion in AI Package Ecosystems](https://arxiv.org/abs/2605.03309)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dependency confusion attacks exploit a structural gap in software distribution: once a package is installed, there is no cryptographic proof of which registry distributed it. Every existing defense is configuration-based and fails silently when misconfigured. We present a cryptographic distribution provenance system comprising three components: (1) cryptographic registry identity, where every registry holds an Ed25519 keypair and signs every artifact it distributes; (2) a dual-signature model, where the publisher signs at packaging time and the registry countersigns at publication time; and (3) authoritative namespace binding, where consumers pin registry fingerprints and the resolver cryptographically rejects artifacts from unauthorized registries. These create three defense layers requiring simultaneous compromise for a successful attack. A comparison across eight ecosystems (npm, Cargo, this http URL, PyPI, Go modules, Docker/OCI, NuGet, Maven) shows no existing ecosystem combines mandatory publisher signing, cryptographic registry identity, mandatory registry countersigning, and consumer-side cryptographic enforcement. The system extends to AI-generation provenance as a signed attribute and governance-enforced dependency resolution. A case study integrates distribution provenance with a three-layer runtime governance architecture, creating a four-phase lifecycle chain with no cryptographic gaps.

---


### 86. [Distributed Learning with Adversarial Gradient Perturbations](https://arxiv.org/abs/2605.03313)

**<font color=#1a73e8>作者：</font>** Nawapon Sangsiri, Yufei Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy concerns in distributed learning often lead clients to return intentionally altered gradient information. We consider the problem of learning convex and $L$-smooth functions under adversarial gradient perturbation, where a client's gradient reply to a server query can deviate arbitrarily from the true gradient subject to a distance bound. Our study focuses on two fundamental questions: (i) what is the smallest achievable sub-optimality gap (i.e., excess error in optimization) under such responses, and (ii) how many queries are sufficient to guarantee a given sub-optimality gap? We establish tight feasibility thresholds on the sub-optimality gap and provide algorithms that achieve these thresholds with provable query complexity guarantees.

---


### 87. [TACO: Trajectory Aligning Cross-view Optimisation](https://arxiv.org/abs/2605.03315)

**<font color=#1a73e8>作者：</font>** Tavis Shore, Oscar Mendez, Simon Hadfield  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-View Geo-localisation (CVGL) matches ground imagery against satellite tiles to give absolute position fixes, an alternative to GNSS where signals are occluded, jammed, or spoofed. Recent fine-grained CVGL methods regress sub-tile metric pose, but have only been evaluated as one-shot localisers, never as the primary fix in a live pipeline. Inertial sensing provides high-rate relative motion, but accumulates unbounded drift without an absolute anchor. We propose TACO, a tightly-coupled IMU + fine-grained CVGL pipeline that consumes a single GNSS reading at start-up and thereafter operates on onboard sensing alone. A closed-form cross-track error model triggers CVGL before IMU drift exceeds the matcher's capture radius, and a forward-biased five-point multi-crop search keeps inference cost fixed at five forward passes per fix. A yaw-residual gate rejects fixes that disagree with the onboard compass, and an anisotropic body-frame noise model scales each Unscented Kalman Filter update by per-fix confidence. A factor graph with vetted loop closures provides an offline smoothed trajectory. On the KITTI raw dataset, TACO reduces median Absolute Trajectory Error (ATE) from 97.0m (IMU-only) to 16.3m, a 5.9 times reduction, at <0.1 ms per-frame fusion cost and a 5-10% camera duty cycle. Code is available: this http URL.

---


### 88. [DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment](https://arxiv.org/abs/2605.03327)

**<font color=#1a73e8>作者：</font>** Hongbo Jin, Rongpeng Zhu, Zhongjing Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is crucial for aligning large language models to perform complex reasoning tasks. However, current algorithms such as Group Relative Policy Optimization suffer from coarse grained, sequence level credit assignment, which severely struggles to isolate pivotal reasoning steps within long Chain of Thought generations. Furthermore, the standard unbounded Kullback Leibler divergence penalty induces severe gradient instability and mode seeking conservatism, ultimately stifling the discovery of novel reasoning trajectories. To overcome these limitations, we introduce Distribution Guided Policy Optimization, a novel critic free reinforcement learning framework that reinterprets distribution deviation as a guiding signal rather than a rigid penalty.

---


### 89. [FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337)

**<font color=#1a73e8>作者：</font>** Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent surge in 4D Gaussian Splatting (4DGS) has achieved impressive dynamic scene reconstruction. While these methods demonstrate remarkable performance, the specific drivers behind such gains remain less explored, making a systematic understanding of the underlying principles challenging. In this paper, we perform a comprehensive analysis of these hidden factors to provide a clearer perspective on the 4DGS framework. We first establish a controlled baseline, FreeTimeGS_ours, by formalizing and reproducing the heuristics of the state-of-the-art FreeTimeGS. Using this framework, we dissect 4DGS along its fundamental axes and uncover key secrets, including the emergent temporal partitioning driven by Gaussian durations and the discrepancy between photometric fidelity and spatiotemporal consistency. Based on these insights, we propose FreeTimeGS++, a principled method that employs gated marginalization and neural velocity fields to achieve superior stability and robust dynamic representations. Our approach yields reproducible results with reduced run-to-run variance. We will release our implementation to provide a reliable foundation for future 4DGS research.

---


### 90. [MedSR-Vision: Deep Learning Framework for Multi-Domain Medical Image Super-Resolution](https://arxiv.org/abs/2605.03343)

**<font color=#1a73e8>作者：</font>** Subhash Gurappa, Trivikram Satharasi, Yashas Hariprasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image super-resolution (MedSR) is essential for improving diagnostic precision across diverse imaging modalities such as MRI, CT, X-ray, Ultrasound, and Fundus imaging. Despite rapid advances in deep learning, challenges remain in preserving anatomical accuracy, maintaining perceptual quality, and generalizing across medical domains. This paper presents MedSR-Vision, a novel unified deep learning framework for evaluating and comparing super-resolution models across five modalities: Brain MRI, Chest X-ray, Renal Ultrasound, Nephrolithiasis CT, and Spine MRI, at magnification scales of $\times2$, $\times3$, and $\times4$. Three representative models namely SRCNN, SwinIR, and Real-ESRGAN are benchmarked using multiple quantitative metrics encompassing fidelity, perceptual realism, and sharpness.
Experimental analysis demonstrates that Real-ESRGAN achieves superior perceptual quality and edge recovery at higher scales, SwinIR excels in preserving structural and diagnostic features, and SRCNN provides efficient and stable performance at lower magnifications. The results establish domain-specific insights and practical guidelines for model selection in clinical imaging workflows, offering a standardized evaluation framework for future medical image super-resolution research and deployment.

---


### 91. [What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis](https://arxiv.org/abs/2605.03354)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Jinman Zhao, Gerald Penn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory failures are silent: an LLM-based agent can produce a fluent response even when it fails to extract, retain, or retrieve the information needed across sessions. The write-manage-read loop describes the external pipeline of these systems but leaves open which internal computations implement each stage. Tracing internal feature circuits across the Qwen-3 family (0.6B--14B) and two memory frameworks (mem0 and A-MEM), we report three findings. First, control is detectable before content: routing circuitry is causally active at 0.6B, while content circuitry produces no detectable signal until 4B under our tracing setup, creating a deployment regime where small models route with apparent competence but silently fail at extraction and grounding. Second, within the content group, Write and Read share a late-layer hub that operates as a context-grounding substrate already present in the base model; only memory framing recruits a functional grounding direction on this substrate, and the hub transfers across both frameworks. Third, emergence does not imply steerability: although the content circuit becomes detectable at 4B, it becomes reliably steerable only at 8B, indicating that detection and intervention have distinct scale thresholds. As a practical implication, the feature-space separation between the two circuit groups enables per-operation failure localization at 76.2% accuracy without supervision, providing a stage-level diagnostic for otherwise silent agent-memory failures.

---


### 92. [Population-Aware Imitation Learning in Mean-field Games with Common Noise](https://arxiv.org/abs/2605.03357)

**<font color=#1a73e8>作者：</font>** Grégoire Lambrecht, Mathieu Laurière  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mean Field Games (MFGs) provide a powerful framework for modeling the collective behavior of large populations of interacting agents. In this paper, we address the problem of Imitation Learning (IL) in MFGs subject to common noise, where the population distribution evolves stochastically. This stochasticity compels agents to adopt population-aware policies to respond to aggregate shocks. We formulate two distinct learning objectives: recovering a Nash equilibrium and maximizing performance against an expert population. We investigate two imitation proxies: Behavioral Cloning (BC) and Adversarial (ADV) divergence. We then establish finite-sample error bounds showing that minimizing these proxies effectively controls both the policy's exploitability and its performance gap relative to the expert. Furthermore, we propose a numerical framework using generalized Fictitious Play and Deep Learning to compute expert population-aware policies. Through experiments on three environments we demonstrate that standard population-unaware policies fail to capture the equilibrium dynamics. Our results highlight that learning population-aware policies is crucial to avoid being misled by the randomness inherent in common noise.

---


### 93. [Tracing Like a Clinician: Anatomy-Guided Spatial Priors for Cephalometric Landmark Detection](https://arxiv.org/abs/2605.03358)

**<font color=#1a73e8>作者：</font>** Sidhartha Mohapatra, Pallavi Mohanty  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When orthodontists trace cephalometric radiographs, they follow a structured workflow: identify the soft tissue profile, partition the skull into anatomical regions, trace contours, and locate landmarks using geometric definitions -- yet no automated system replicates this reasoning. We present a five-phase anatomy-guided initialization pipeline that translates this clinical workflow into computational operations, producing confidence-weighted spatial attention priors for a downstream HRNet-W32 detector. On 1,502 radiographs from three sources spanning 7+ imaging devices, the system achieves 1.04 mm mean radial error on 25 landmarks -- surpassing prior state-of-the-art (1.23 mm on 19 landmarks) by 15.4%, with twelve landmarks below 1 mm. A three-way controlled ablation reveals two striking findings. First, removing anatomical priors does not merely slow convergence -- it destroys generalization: both models converge to ~1.03 mm on validation, but diverge to 1.94 vs. 1.04 mm on the test set. Second, replacing anatomical priors with random-position Gaussians produces even worse generalization (2.24 mm), confirming that the improvement derives from anatomically correct positioning, not additional input channels. Clinical domain knowledge encoded as spatial priors provides an inductive bias that architecture and data augmentation alone do not provide.

---


### 94. [Mix3R: Mixing Feed-forward Reconstruction and Generative 3D Priors for Joint Multi-view Aligned 3D Reconstruction and Pose Estimation](https://arxiv.org/abs/2605.03359)

**<font color=#1a73e8>作者：</font>** Siyou Lin, Zhou Xue, Hongwen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent trends in sparse-view 3D reconstruction have taken two different paths: feed-forward reconstruction that predicts pixel-aligned point maps without a complete geometry, and generative 3D reconstruction that generates complete geometry but often with poor input-alignment. We present Mix3R, a novel generative 3D reconstruction method which mixes feed-forward reconstruction and 3D generation into a single framework in an aligned manner. Mix3R generates a 3D shape in two stages: a sparse voxel generation stage and a textured geometry generation stage. Unlike pure generative methods, our first-stage generation jointly produces a coarse 3D structure (sparse voxels), per-view point maps and camera parameters aligned to that 3D structure. This is made possible by introducing a Mixture-of-Transformers architecture that inserts global self-attentions to a feed-forward reconstruction model and a 3D generative model, both pretrained on large-scale data. This design effectively retains the pretrained priors but enables better 2D-3D alignment. Based on the initial aligned generations of sparse 3D voxels and point maps, we compute an overlap-based attention bias that is directly added to another pretrained textured geometry generation model, enabling it to correctly place input textures onto generated shapes in a training-free manner. Our design brings mutual benefits to both feed-forward reconstruction and 3D generation: The feed-forward branch learns to ground its predictions to a generative 3D prior, and conversely, the 3D generation branch is conditioned on geometrically informative features from the feed-forward branch. As a result, our method produces 3D shapes with better input alignment compared with pure 3D generative methods, together with camera pose estimations more accurate than previous feed-forward reconstruction methods. Our project page is at this https URL

---


### 95. [Dynamic Distillation and Gradient Consistency for Robust Long-Tailed Incremental Learning](https://arxiv.org/abs/2605.03364)

**<font color=#1a73e8>作者：</font>** Taigo Sakai, Kazuhiro Hotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of Long-tailed Class Incremental Learning (LT-CIL) addresses the sequential learning of new classes from datasets with imbalanced class distributions. This scenario intensifies the fundamental problem of catastrophic forgetting, inherent to continual learning, with the dual challenges of under-learning minority classes and overfitting majority classes. To tackle these combined issues, this paper proposes two main techniques. First, we introduce gradient consistency regularization, which leverages the moving average of gradients to suppress abrupt fluctuations and stabilize the training process. Second, we dynamically adjust the weight of the distillation loss by measuring the degree of class imbalance with normalized entropy. This adaptive weighting establishes an optimal balance between retaining old knowledge and acquiring new information. Experiments on the CIFAR-100-LT, ImageNetSubset-LT, and Food101-LT benchmarks show that our method achieves consistent accuracy improvements of up to 5.0\%. Furthermore, we demonstrate dramatic gains in the challenging 'In-ordered' setting, where tasks progress from majority to minority classes, highlighting our method's robustness in mitigating forgetting under unfavorable learning dynamics. This enhanced performance is achieved without a significant increase in computational overhead, demonstrating the practicality of our framework.

---


### 96. [Fully Automatic Trace Gas Plume Detection](https://arxiv.org/abs/2605.03372)

**<font color=#1a73e8>作者：</font>** Vít Růžička, David R. Thompson, Jay E. Fahlen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future imaging spectrometers will increase data volumes by orders of magnitude, requiring automated detection of trace gas point sources. We present a fully automated framework that combines machine learning-based morphological analysis with physics-based spectroscopic fitting to detect plumes without human participation. Applied to EMIT imaging spectrometer data, the system operates in two modes: "daily digest" that runs automatically on all downlinked data, flagging the largest events for immediate response, and a retrospective analysis that identifies plumes missed by prior human review. The daily digest demonstrates that a significant fraction of the largest plumes can be detected automatically with negligible false positives, while retrospective analysis suggests at least 25% of plumes may have been overlooked. In addition to the previously observed methane point sources, we extend detection to three understudied trace gases: NH3, NO2 and the first observations of carbon monoxide (CO) plume in EMIT imagery.

---


### 97. [GRAFT: Auditing Graph Neural Networks via Global Feature Attribution](https://arxiv.org/abs/2605.03377)

**<font color=#1a73e8>作者：</font>** Rishi Raj Sahoo, Subhankar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) achieve strong performance on node classification tasks but remain difficult to interpret, particularly with respect to which input features drive their predictions. Existing global GNN explainers operate at the structural level identifying recurring subgraph motifs, but none explain model behaviour globally at the level of input node attributes. We propose GRAFT, a posthoc global explanation framework that identifies class-level feature importance profiles for GNNs. The method combines diversity-guided exemplar selection, Integrated Gradients-based attribution, and aggregation to construct a global view of feature influence for each class, which can be further expressed as concise natural language rules using a large language model with self-refinement. We evaluate GRAFT across multiple datasets, architectures, and experimental settings, demonstrating its effectiveness in capturing model-relevant features, supporting bias analysis, and enabling feature-efficient transfer learning. In addition, we introduce a structured human evaluation protocol to assess the interpretability of generated rules along dimensions such as accuracy and usefulness. Our results suggest that GRAFT provides a practical and interpretable approach for analysing feature-level behaviour in GNNs, bridging quantitative attribution with human-understandable explanations.

---


### 98. [DECKER: Domain-invariant Embedding for Cross-Keyboard Extraction and Recognition](https://arxiv.org/abs/2605.03384)

**<font color=#1a73e8>作者：</font>** Bikrant Bikram Pratap Maurya, Nitin Choudhury, Daksh Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Acoustic side-channel attacks (ASCA) on keyboards pose a significant security risk, as keystrokes can be inferred from typing acoustics, revealing sensitive information. Prior ASCA studies are limited by small-scale datasets with restricted diversity in users, keyboards, and environments, constraining analysis across devices, microphones, and noise conditions. We introduce HEAR, a dataset designed to study ASCA along three axes: keyboard generalization, noise adaptation, and user bias. HEAR contains recordings from 53 participants using 37 laptop keyboards, collected in three realistic settings: (1) external microphone capture, (2) device microphone capture without network noise, and (3) VoIP-based streaming capture. This enables controlled evaluation across users, keyboards, and environments. On HEAR, we establish an ASCA benchmark spanning conventional features and pre-trained representations from raw audio and spectrograms in unimodal and multimodal settings. We propose DECKER, a domain-invariant keystroke inference framework with four stages: (1) Keyboard Signature Normalization to reduce device coloration, (2) domain-adversarial disentanglement to suppress keyboard identity, (3) supervised cross-keyboard contrastive alignment to enforce key consistency, and (4) Acoustic Style Randomization to synthesize unseen keyboard responses. We further explore sentence-level inference using an LLM-based post-processing layer to refine keystroke sequences via linguistic context. Results on HEAR show DECKER improves keystroke identification over strong baselines, particularly in cross-keyboard and cross-user settings, with further gains from language-model rectification. These findings highlight that ASCA remains effective across diverse users, devices, and noisy environments, underscoring its practical security risk.

---


### 99. [Local Truncation Error-Guided Neural ODEs for Large Scale Traffic Forecasting](https://arxiv.org/abs/2605.03386)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Yafei Li, Ruixiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal forecasting in physical systems, such as large-scale traffic networks, requires modeling a dual dynamic: continuous macroscopic rhythms and discrete, unpredictable microscopic shocks. While Neural Ordinary Differential Equations (ODEs) excel at capturing smooth evolution, their inherent Lipschitz continuity constraints inevitably cause severe over-smoothing when confronting abrupt anomalies. Recent physics-informed methods attempt to bypass this by penalizing numerical integration errors to enforce manifold smoothness. However, we mathematically reveal that such rigid regularization inherently triggers gradient conflicts and ``attention collapse,'' stripping the model of its sensitivity to anomalies. To resolve this continuity-shock dilemma, we propose Local Truncation Error-Guided Neural ODEs (LTE-ODE). Rather than treating numerical error as a nuisance to be eliminated, we innovatively repurpose the Local Truncation Error (LTE) as an unsupervised forward inductive bias. By mapping the LTE into a dynamic spatial attention mask, our architecture gracefully preserves high-precision continuous ODE evolution in stable regions, while adaptively triggering a discrete compensation branch exclusively at shock points. Trained purely end-to-end without manifold penalties, LTE-ODE achieves state-of-the-art performance on multiple large-scale benchmarks, exhibiting exceptional robustness against highly non-linear fluctuations. Furthermore, our ablation on integration steps demonstrates high deployment flexibility, allowing the model to seamlessly adapt to varying hardware memory constraints in real-world applications.

---


### 100. [Graph Reconstruction from Differentially Private GNN Explanations](https://arxiv.org/abs/2605.03388)

**<font color=#1a73e8>作者：</font>** Rishi Raj Sahoo, Jyotirmaya Shivottam, Subhankar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regulatory frameworks such as GDPR increasingly require that ML predictions be accompanied by post-hoc explanations, even when raw data and trained models cannot be released. Differential privacy (DP) is the standard mitigation for the residual privacy risk of releasing these explanations. We show that DP is not sufficient: an adversary observing only DP-perturbed GNN explanations can reconstruct hidden graph structure with high accuracy. Our attack, PRIVX, exploits the fact that the Gaussian DP mechanism is a single DDPM forward step at known noise level {\sigma}({\epsilon}), recasting reconstruction as reverse diffusion conditioned on the corrupted signal, a principled Bayesian denoiser under known DP corruption. We formalise a stratified adversary model parameterised by (M, \hat{\epsilon}, \hat{\delta}, S, \rho) that interpolates between oblivious and oracle attackers, and derive endpoint-matched two-sided bounds on reconstruction AUC. For practitioners, we provide regime-stratified guidance on explainer choice: on homophilic graphs, neighbourhood-aggregating explainers (GraphLIME, GNNExplainer) leak more structure than per-node gradient explainers under the same DP budget; on strongly heterophilic graphs the ordering reverses. We introduce PRIVF as an auxiliary diagnostic sharing the same diffusion backbone to decompose leakage into explainer-induced and intrinsic graph-distribution components. Experiments across seven benchmarks, three DP mechanisms, and three GNN backbones show PRIVX achieves AUC above 0.7 at {\epsilon} = 5 on five of seven datasets, with the attack succeeding well within typically deployed privacy budgets.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
