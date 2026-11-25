# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

---

### 1. [Local subspace encoding for spectral prediction: from TabPFN to operator-adaptive calibration](https://arxiv.org/abs/2611.31245)

**<font color=#1a73e8>作者：</font>** Gregory Beurier, Robin Reiter, Denis Cornet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TabPFN has already shown useful predictive performance on near-infrared spectra. RamanPFN subsequently proposed two spectral representations for tabular inference: Global Compositional Unmixing (GCU) and Local Vibrational Subspace Encoding (LVSE). We assess whether these representations also help on datasets assembled through the nirs4all ecosystem, and whether their value extends to classical calibration. We reanalyse completed experiments from a public spectral dataset catalogue. On a post-hoc subset of 61 matched numerical prediction tasks, after excluding ten class-code, metadata or semantically ambiguous targets, LVSE reduces RMSE relative to raw-spectrum TabPFN by 10.22%, 12.80% and 14.52% on average for checkpoints 2.5, 3 and 3.5, respectively, with median reductions of 4.99%, 4.74% and 7.82%. Across 76 classification datasets, weighted F1 increases by 2.22, 2.56 and 3.81 percentage points. The 2.5 classification procedure uses output coding on 15 datasets exceeding the checkpoint's native class limit. GCU alone is less reliable in this implementation. LVSE also improves PLS and Ridge in many cases, with median RMSE reductions of 4.75% and 1.89%. Adding LVSE candidates to an operator-adaptive model is feasible, but a separate 35-task panel derived from the public AOM benchmark shows only small median gains. These results motivate evaluating LVSE alongside existing representation choices. They do not establish that a selector choosing between raw and LVSE inputs will improve every task.

---


### 2. [Actionwave: A Systematic Benchmark for Waveform-Centric Clinical Prediction Across Care Scenarios](https://arxiv.org/abs/2611.31249)

**<font color=#1a73e8>作者：</font>** Jie Peng, Davis Hobley, Song Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous bedside waveforms record rapid physiological changes that can inform clinical decisions. Existing benchmarks examine selected prediction conditions, but it remains unclear how model advantages depend on signal duration, warning time, and available inputs across care settings. We introduce Actionwave, a benchmark for waveform-centric clinical prediction across intensive-care, operating-room, and emergency-department settings. Actionwave uses a common decision-time prediction interface and groups clinically grounded tasks by what is inferred and when. It varies conditions relevant to clinical use, including the warning required before an intervention. We compare diverse architectures and pretrained biosignal encoders under specified model-size and compute budgets. The protocol requires patient-level splits, strict information cutoffs, and comparisons that isolate individual modeling factors. Across 20 tasks and 1.4M task-labelled windows from source datasets, the experimental grids account for over 87,000 model fits. These comparisons identify task-specific choices and show why matched cohorts, unimodal controls, and explicit timing are necessary when interpreting waveform model performance.

---


### 3. [Instantiation of Human Values in Image Generation](https://arxiv.org/abs/2611.31253)

**<font color=#1a73e8>作者：</font>** Maria-Teresa De Rosa Palmini, Piera Riccio, Noa Garcia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models are increasingly embedded in everyday visual culture, yet little is known about how they translate abstract human values into visual scenes. We address this gap by introducing a framework, grounded in Schwartz's theory of basic human values, for studying value instantiation: the process by which ideals such as success, care, or freedom are visually realized. Using person-centered prompts from 70 positive and negative value items, we generate 28,000 images across four state-of-the-art T2I models. We identify visual prototypes, recurring combinations of subjects, actions, and settings, and use them to quantify how narrowly models instantiate these values and how this breadth compares with human descriptions of the same items. We then map these prototypes onto a taxonomy of social configurations spanning setting, sociality, mode of engagement, and social register, revealing what is systematically foregrounded or omitted. Our results show that T2I models produce far more concentrated representations than humans do when describing the same values. They default to a hyper-individualistic, adult-centric worldview, reproducing value-specific associations, such as achievement tied to formal institutional settings or hedonism rendered as affluent consumption, while marginalizing everyday labor, relational care, and non-adult perspectives. As a proof of concept, we show that these structural gaps can guide a steering method that diversifies outputs without modifying the original prompt.

---


### 4. [Capability and Interpretability of Transformers on Multi-task Recurrence](https://arxiv.org/abs/2611.31260)

**<font color=#1a73e8>作者：</font>** Xiamin Chen, Linyu Liu, Jiachen Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers are widely used in various language tasks, with limited understanding of their internal mechanisms. Motivated by the recurrent structure of many linguistic rules, we study the capability and interpretability of Transformers through a controlled family of linear recurrence tasks over finite cyclic groups. These tasks range from executing a single fixed rule to identifying a latent rule from context and switching between explicitly specified rules, with and without input masking. Through extensive experiments across different configurations, we find that switching specified rules is simpler than identifying latent rules for Transformers in general. We also identify how several key factors affect the generalization capability of Transformers, including the depth, width, and the algebraic structure of the linear recurrence. Curriculum training is extremely useful when the number of rules is large. With standard tools in mechanistic interpretability like linear probing and input patching, our study reveals how Transformers represent, identify, and execute multiple rules.

---


### 5. [ToneMamaba: Learning Contextualized Tonal Contours with Boundary-Reset State Space Models](https://arxiv.org/abs/2611.31267)

**<font color=#1a73e8>作者：</font>** Po-Yu Chiu, Yi-Fen Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mandarin tone recognition in connected speech is challenging because contextual and durational variation reshapes F0 contours. We propose ToneMamba, a boundary-aware state space model that replaces static boundary embeddings with bidirectional state resets at syllable, word, and IPU levels. Fixed weights fuse multi-level representations, while shared-weight bidirectional scans use channel-wise directional fusion to reduce parameters. Dynamic syllable pooling forms tonal contours, and rhythm-conditioned gating incorporates durational information. ToneMamba achieves 97.9% and 74.8% accuracy on FCU-VOICE-360 read and MCDC-8 conversational speech, outperforming the baseline (ToneNet) by 0.9 and 15.9 percentage points, respectively. Ablations show that word-level resets are particularly effective, while rhythm conditioning provides greater gains in conversational speech, underscoring the role of durational variation in spontaneous speech.

---


### 6. [Lexical Tone and Word Order Matter in Translation: Prosodic Correspondence Across Languages](https://arxiv.org/abs/2611.31276)

**<font color=#1a73e8>作者：</font>** Haopeng Xie, Ismail Rasim Ulgen, Shengying Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prosody conveys emphasis, emotion, and intent, yet its correspondence across translation remains underexplored, especially when languages differ in lexical tone and word order. To our knowledge, we present the first systematic word-level analysis of prosodic correspondence in translated speech spanning tonal and non-tonal Asian languages, with comparisons to European-language findings and explicit analyses of lexical tone and word reordering. Building on prior evidence of fine-grained prosody correspondence in European-language pairs, we investigate how these linguistic factors relate to word-level pitch and energy correspondence between English and five languages: Mandarin Chinese, Thai, and Vietnamese, which have lexical tone, and Japanese and Korean as additional comparisons. Correspondence is generally lower than previously reported European-language estimates. Adjusting for lexical tone increases pitch correspondence for English-Mandarin Chinese, English-Thai, and English-Vietnamese. However, English-Japanese and English-Korean also exhibit lower correspondence than the European-language estimates, indicating that tonal status alone does not explain the observed pattern. Greater word reordering is associated with weaker local correspondence even under semantic alignment, suggesting that semantic alignment does not fully account for differences in prosodic organization. These findings characterize the limits of fine-grained acoustic correspondence across translation and motivate prosody modeling that accounts for lexical pitch constraints and the structural context of translated content.

---


### 7. [Irreducible Governance Structure for Autonomous Agent Systems: Fair Allocation, Strategy-Proofness, and Multi-Scale Composition](https://arxiv.org/abs/2611.31284)

**<font color=#1a73e8>作者：</font>** Marcelo Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agent governance is commonly framed as a problem of enforcing correct execution. However, in multi-agent systems, an equally fundamental question precedes execution: which agents are allowed to act.
In this paper, we show that allocation is not an auxiliary concern but a structural component of governance. When multiple agents compete for execution under constrained resources, any allocation mechanism introduces unavoidable trade-offs between fairness, efficiency, and resistance to strategic manipulation. We formalize this through a set of impossibility results, including Sybil amplification and the incompatibility of desirable allocation properties.
We then show that these allocation constraints cannot be resolved within a single layer of control. Instead, they propagate across the system, interacting with execution atomicity, state enforcement, and behavioral drift. This leads to a multi-scale governance structure composed of four orthogonal dimensions: temporal (atomicity), state (enforcement), behavioral (drift monitoring), and population (allocation).
Our main result is an irreducibility theorem: under finite observability, no governance architecture can collapse these dimensions without loss of correctness or stability. Allocation, in particular, acts as a first-class constraint that prevents simplification of the governance stack.
We validate these results through a series of analytical constructions and empirical ablations, showing that removing or approximating any layer leads to systematic failure modes.
This work reframes agent governance as a structural problem: not only how actions are executed, but how access to execution is determined, and why these decisions impose irreducible architectural requirements.

---


### 8. [The Industrialization of Noise: Why Automated Proof-Solving is the Same Old Dead End](https://arxiv.org/abs/2611.31286)

**<font color=#1a73e8>作者：</font>** Richard DeMillo, Richard Lipton  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nearly fifty years ago, DeMillo, Lipton, and Perlis argued that mathematical proofs are not static, isolated structures of formal logic, but the products of a vibrant, evolving social process of human critique, internalization, and shared intuition. In October 2026, OpenAI challenged this thesis by releasing a massive repository of 722 automated mathematical manuscripts, claiming full or partial solutions to 372 longstanding open problems. This paper examines the immediate crisis through the lens of the original DLP framework. We argue that the sudden, automated overproduction of dense, unreadable proofs represents an industrial pollution of the mathematical ecosystem. By examining the three fatal structural pillars of this automated approach (Specification, Regress, and Utility), we demonstrate that decoupling the act of mechanical solving from the human social process of understanding produces a sterile repository of dead logical artifacts.
The resulting industrialization of unexamined manuscripts is self-fulfilling. Flooding the literature guarantees that the finite supply of human attention will lose the race to separate signal from noise. In this sense, posting a result is not the same act as submitting it to the community processes by which mathematics is vetted, digested, and incorporated into shared knowledge.

---


### 9. [Hidden Clues in WM-811K: Uncovering the Spatial Signals Behind Wafer Map Prediction](https://arxiv.org/abs/2611.31292)

**<font color=#1a73e8>作者：</font>** Kabir Tolani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> WM-811K (also known as LSWMD) is a wafer map dataset first made publicly available in a 2015 paper by Wu et al. Convolutional neural networks have been used to achieve high classification accuracy on this dataset, yet it's not easy to decipher which features of the dataset are driving that performance. This study attempts to answer this specifically for WM-811K: how much of the predictive performance results from the wafer layout, the count of failed dies, their distance from the center and their exact 2-D location. After analyzing duplicate wafer maps, removing same wafer maps with conflicting labels and ensuring that the same manufacturing lot or exact same map doesn't appear in training, validation and test data, we were left with 25,513 defect-labeled wafer maps from eight classes. We then constructed four variations of each wafer map. The Original was the actual wafer map present in the dataset. The Layout-only kept only the layout of the non-background dies. The Global-shuffle kept the count of failed dies while shuffling them around. The Radial-shuffle randomized the locations of failed dies only in their radial bin, which was chosen out of 8 radial bins based on distance from the center. The data split, preprocessing and CNN architecture remained the same for all four of them. Macro-F1 progressed like this: 0.3829 (Layout-only), 0.5803 (Global-shuffle), 0.7439 (Radial-shuffle) and 0.8563 (Original). These results show that WM-811K contains useful information at several levels: wafer layout, number of failures, distribution of failed dies in a given radius, and exact 2-D locations of the failed dies. Therefore, high classification performance on this benchmark does not come only from learning the exact defect configuration.

---


### 10. [Information Security Risk Preparedness in Electronic Data Interchange: A Comparative Assessment of General IT and Healthcare Environments](https://arxiv.org/abs/2611.31294)

**<font color=#1a73e8>作者：</font>** Naresh Kshetri, Bishwo Prakash Pokharel, Arati Bastakoti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electronic Data Interchange (EDI) supports the exchange of structured information across business and healthcare environments, making information security and organizational risk management critical to reliable digital transactions. This study empirically assesses security-control preparedness and organizational risk-taking ability in EDI-related environments through a comparative analysis of General IT Professionals (GIT) and Healthcare EDI Professionals (HEP). A quantitative, cross-sectional survey was conducted with 100 respondents, equally divided between the two groups. Security Control Preparedness (SCP) and Threat Perception (TP) were validated using reliability and exploratory factor analyses, followed by group comparisons, correlation analysis, and multiple linear regression. HEP respondents reported significantly higher SCP than GIT respondents (M = 4.70 vs. 3.89, p < 0.001, d = 1.06) and higher Organizational Risk-Taking Ability (ORTA) (M = 6.14 vs. 5.28, p = 0.001, d = 0.66). In contrast, GIT respondents reported higher threat perception (M = 2.95 vs. 2.04, p < 0.001, d = 0.72). SCP was positively associated with ORTA (r = 0.479, p < 0.001), whereas TP showed a significant negative association (r = -0.610, p < 0.001). A parsimonious regression model incorporating SCP and TP explained 41.6% of the variance in ORTA (R^2 = 0.416, adjusted R^2 = 0.404, p < 0.001). Based on these empirical findings, an EDI Risk Management Framework (EDI-RMF) is proposed integrating governance, human and organizational security, technical safeguards, physical protection, and continuous monitoring. The findings provide empirical evidence for strengthening information-security risk management in EDI-enabled environments, particularly within developing-economy contexts.

---


### 11. [Towards Efficient Attack Tree Generation from Attack Graphs for Unobservable Target Analysis](https://arxiv.org/abs/2611.31302)

**<font color=#1a73e8>作者：</font>** Chijioke Eze, Aliyu Tanko Ali, Leonard Chidiebere Eze 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attack trees provide a structured approach to security analysis but traditionally require prior knowledge of the attacker's objective. In practice, this objective often remains hidden, even when some attacker actions are partially detected. This paper presents a methodology for generating attack trees without assuming a predefined target by modeling the threat environment as a constraint-weighted graph and applying temporal reachability analysis. The approach identifies probable attacker locations from partial observations and a time budget, carrying traversal cost as an attack-tree attribute. It then extracts target-oriented subgraphs that preserve feasible attack paths while eliminating irrelevant nodes. We demonstrate the framework across three scenarios: a single office building, a multi-building industrial complex, and a real IoT device-communication network recovered from the CICIoT2023 attack dataset. Compared with the baselines, our approach achieves a lower reduction factor while maintaining complete target preservation, substantially outperforming topology-only methods that ignore temporal constraints. We further perform a sensitivity analysis across 66 weight configurations, showing that target identification is stable when strategic value receives at least 20\% of the weight in the single building and at least 50\% in the multi-building complex, while additional experiments reveal sensitivity to perturbations of the underlying strategic-value prior.

---


### 12. [Evolutionary AI Control: Population-Level Safety Under Reproduction, Heredity, and Selection](https://arxiv.org/abs/2611.31312)

**<font color=#1a73e8>作者：</font>** Andrew T. Cadotte  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An AI agent can satisfy every individual safety check and still give rise to a population that violates a collective safety limit. This risk arises in open multi-agent systems, where agents copy themselves, modify their successors, and change system membership during a run. Selection then shifts the population toward traits outside the developers' optimization targets. We prove conditions under which safety guarantees persist through reproduction, inheritance, and selection, and we characterize how they fail.
Four counterexamples illustrate these failures. Unauthorized copies, which violate a specified reproductive restriction, can each leave fewer than one successor on average while their expected number grows without bound under continued production from an expanding authorized population. Two lineages can each decline in isolation yet grow exponentially when they interact. Alternating between reproductive rules can drive growth even when each rule, applied alone, suppresses it. Selection can raise the population's average rate of unauthorized reproduction above a certified limit even though every agent's rate remains fixed.
Whereas existing verification methods assume fixed or registered membership, we prove safety certificates, under stated assumptions, for populations whose agents create successors during a run. The main result bounds the expected cumulative harm over a run, including when a scheduler adapts the reproductive rules to the observed history. Further conditions cover every population state reachable through evolution and preserve reproductive restrictions as descendants inherit modifications. Drawing on the mechanisms by which multicellular organisms control cell reproduction, the framework enables developers to specify and verify these controls before deployment.

---


### 13. [Conformalized Tree-Based Gradient Ensembles for Out-of-Distribution Detection and Plausible Recourse](https://arxiv.org/abs/2611.31319)

**<font color=#1a73e8>作者：</font>** Mariam Zakaria Moussa Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual recourse provides actionable feature adjustments that reverse unfavourable predictions made by automated decision models. However, when recourse search optimizes purely against classifier confidence or narrow proxy scores over gradient-boosted decision trees (GBDT), search procedures can exploit boundary artifacts and low-density regions---an instance of Goodhart's law---yielding out-of-distribution (OOD) recommendations that appear favourable nominally while lacking manifold plausibility. In this paper, we study conformalized OOD gating coupled with actionability-constrained counterfactual search across two tabular benchmarks: Adult and Give Me Some Credit (GMSC). Calibrating finite-sample anomaly gates (gate_IF, gate_LOF, and the conjunctive gate_ALL) at significance level delta = 0.05 over isolation forest, local outlier factor, and k-nearest-neighbor signals, we audit generated counterfactuals against held-out GMM and OCSVM detectors alongside ablation studies (gen10, gen100, and relax). Across matched recourse pairs where both constrained and unconstrained searches succeed, gate_ALL significantly reduces held-out OCSVM flags on Adult (N=541, Delta flag_OCSVM = -0.0296, p_Holm = 4.0e-4) and lowers both held-out flags on GMSC (N=540, Delta flag_OCSVM = -0.0346, p = 1.0751e-4; Delta flag_GMM = -0.1663, p = 3.5679e-16) while increasing matched recourse cost (Delta cost = +0.3035, p = 1.3365e-5) and narrowing overall feasibility. Our findings formalize the cost--feasibility--plausibility trade-off and demonstrate how conformal OOD gating audits recourse reliability on tabular ensembles.

---


### 14. [Flagging Batch Shift in Flow Cytometry using Jeffreys Divergence between Gaussian Mixtures](https://arxiv.org/abs/2611.31321)

**<font color=#1a73e8>作者：</font>** Jonathan Legrand, Aguirre Mimoun, Audrey Bidet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for clinical flow cytometry are usually evaluated on data drawn from their training distribution. In routine practice, however, acquisition conditions and reagents may change, potentially making predictions unreliable without warning. We propose a model agnostic criterion for prediction reliability based on a notion of distance from the training distribution: each patient sample is represented by a Gaussian mixture model, and its Jeffreys divergence to a reference fitted on the training data is estimated using Monte Carlo integration. We illustrate our approach on real-life shifted cohorts of acute myeloid leukaemia patients, using a classifier trained to predict NPM1 mutation status. First, we show graphically and statistically that pairwise divergences capture acquisition cohort structure. We then calibrate a rejection threshold on a subset of shifted cohort samples and evaluate it on held-out subjects. Across 20 runs, the misclassification rate of rejected samples was 2.5 times larger than for retained samples. These results suggest that input divergence can help identify unreliable predictions, providing a strong candidate component for abstention frameworks, along with quality control measures and classifier confidence.

---


### 15. [Conservative Overlap Fuzzy Rough Sets for Incomplete Data](https://arxiv.org/abs/2611.31329)

**<font color=#1a73e8>作者：</font>** Trung Hieu Vuong, Van Thien Nguyen, Nhu Son Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attribute reduction in incomplete information systems is difficult because missing values break the equivalence-class structure of rough set theory. We propose the Conservative Overlap Fuzzy Rough Set (COFRS) model. Each object is described by its set of present attributes. The similarity of two objects is a weighted overlap on the attributes present in both, divided by the fixed number of attributes |A| instead of the size of their union, so missing values are penalised globally and are not matched as wildcards. From this similarity we define a soft dependency degree based on weighted granule consistency, and we search for reducts by greedy backward elimination in O(|U|^2 |A|^2) time. We show that the relation is symmetric and non-reflexive, that the dependency degree is not monotone, and we give a sufficient condition under which monotonicity holds. On 11 UCI benchmarks with missing rates from 0.15% to 20.46%, COFRS gives the smallest reducts on average (4.1 attributes, against 5.0-11.2 for Tolerance-RS, a range-threshold variant Tol-RS_tau, Zhou-RS and the min-aggregation variant COFRS-min). The difference is significant against Tol-RS_tau, Zhou-RS and COFRS-min (Holm-adjusted Wilcoxon p<0.01) but not against Tolerance-RS (p=0.56), and it is small against the Jensen-Shen selector (adjusted p=0.084). At equal reduct size, COFRS selects more informative attributes than random subsets. With a kNN classifier the methods do not differ significantly in accuracy, F1 or G-mean; with an RBF-SVM they do, and COFRS ranks last. The gain is therefore compactness, not predictive accuracy.

---


### 16. [Trustworthy Edge AI: Security, Privacy, and Resilience for Distributed Intelligence](https://arxiv.org/abs/2611.31331)

**<font color=#1a73e8>作者：</font>** Jaydip Sen, Subhasis Dasgupta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This chapter examines the principles and emerging research directions for building secure, privacy-preserving, and resilient Edge Artificial Intelligence (Edge AI) systems. As intelligence shifts from centralized clouds to distributed edge environments, challenges arise in ensuring data integrity, privacy, and reliable operation under adversarial and uncertain conditions. The chapter analyzes Edge AI architectures, emphasizing the expanded attack surface due to heterogeneous devices, resource constraints, and dynamic networks. It reviews core security mechanisms, including hardware-rooted trust, zero-trust models, secure communication, and attestation. Privacy-preserving approaches, such as federated learning, secure aggregation, and differential privacy, enable collaborative intelligence without centralized data sharing. Resilience strategies, including fault tolerance, adversarial robustness, and adaptive orchestration, are also explored. Case studies from smart cities, autonomous vehicles, healthcare, and industrial IoT illustrate practical trade-offs. The chapter advocates a holistic, cross-layer design integrating security, privacy, and resilience for trustworthy edge intelligence.

---


### 17. [Fusion Gains Depend on the Implementation and the Calibration Target: An 18-Task Study of Prediction Intervals with a Single-Source Fallback](https://arxiv.org/abs/2611.31333)

**<font color=#1a73e8>作者：</font>** Liwei Deng, Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fused model can benefit from an extra learning stage as well as from a second data source. We compare four fusion implementations with matched single-source learners on 18 regression tasks with prediction intervals. Across ten refits under group-wise calibration, linear stacking improved the interval score by 6.0% against a source model without a second stage and by 0.1% against its matched single source. The four implementations agreed on 3 of 18 tasks and gave opposite clear verdicts on 12, including 8 of the 10 tasks with naturally distinct sources. With pointwise calibration, they agreed on 5 tasks and gave opposite clear verdicts on 9. A development-set selector with a matched single-source fallback improved ten-refit task-averaged scores by 2.2--6.3% in every implementation under both calibrations. Adding fused arms to the pool of single-source candidates improved the mean relative score by about 5 percentage points. Under group-wise calibration, the gradient-boosted selector met the criterion frozen before evaluation on eight held-out tasks. In post-opening refits, selectors lost to the matched single source in 4.4--6.1% of task-level runs under group-wise calibration. Under signed pointwise calibration, three implementations lost in 19--23% of runs. Fusion evaluations should compare matched candidates on held-out data and report how often the selector loses alongside its average gain.

---


### 18. [High Throughput Meets Low Latency: CKKS Functional Bootstrapping on GPUs](https://arxiv.org/abs/2611.31335)

**<font color=#1a73e8>作者：</font>** Carlos Agulló-Domingo, Carlo Pascoe, Óscar Vera-López 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Functional (programmable) bootstrapping extends the bootstrapping operation of Fully Homomorphic Encryption (FHE) to evaluate an arbitrary function while refreshing a ciphertext. This capability was a unique feature of scalar CGGI/DM cryptosystems for many years until it was recently added to the toolset of vectorized FHE schemes, with CKKS being the most promising option both in terms of throughput (amortized time) and functionality. Previous work showed that CKKS functional bootstrapping outperforms CGGI/DM functional bootstrapping in terms of throughput by two to three orders of magnitude, but still loses in latency on CPU by two to three orders of magnitude. We present an optimized GPU implementation of CKKS functional bootstrapping that closes the latency gap. Our implementation supports evaluating functions over both small integers (as in CGGI/DM) and real numbers (unique to CKKS), which we call discrete-CKKS and continuous-CKKS functional bootstrapping, respectively.

---


### 19. [Look Where Camouflage Breaks: Concealment-Guided Observation for Camouflaged Object Detection](https://arxiv.org/abs/2611.31392)

**<font color=#1a73e8>作者：</font>** Dingming Zhang, Fengyang Xiao, Jingjia Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A camouflaged object can blend into its surroundings at one scale and become distinguishable at another. Yet a region's apparent ambiguity gives limited guidance on which observation would resolve it. The challenge is to connect the form and scale of concealment to the evidence that a new view can reveal. We introduce CamoBreak, an active framework for camouflaged object detection guided by a Concealment Spectrum. From the image and current predictions, the spectrum measures regional resemblance and boundary ambiguity across comparison scales, distinguishing persistent concealment from separation emerging at finer or broader scales. These measurements guide crop selection from the already-captured image and recognition against global foreground and background references. An object-conditioned spatial preference then selects where local evidence should update the prediction and feature memory, retaining target corrections while suppressing background distractions. Accepted corrections reshape the next measurement, while predicted segmentation benefit determines whether to observe again. Experiments across encoder families and related segmentation tasks show consistent improvements. Targeted analyses support improved small-target recovery, multiple-object coverage, and selective evidence integration. Code will be released.

---


### 20. [Enhancing Sparse-View Gaussian Splatting with Feed-Forward Priors via Spectral Fusion and Distillation](https://arxiv.org/abs/2611.31428)

**<font color=#1a73e8>作者：</font>** Weikai Lin, Jun Dai, Sheng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting from sparse training views renders high-quality images near training views, but reconstruction quality degrades at distant regions, which are undersampled by the training set. Feed-forward novel view synthesis (NVS) models use strong learned priors to resample the scene from substantially different viewpoints, but they take more than ten times as long to render and produce high-frequency artifacts on out-of-domain scenes. We propose a plug-and-play method that enhances an existing sparse-view Gaussian model with a pretrained feed-forward NVS model. We observe that the two are complementary in the frequency domain: the prior is more accurate at low frequencies, and the Gaussians at high frequencies. The reliability of the prior relative to the Gaussians is inversely proportional to the image frequency, so the optimal fusion weight is a first-order low-pass filter with one parameter that can be fitted. Our key idea is then to intelligently fuse the reliable part of each of the two methods. To remove the slow feed-forward model at render time, we use these fused images as teachers and distill them back into Gaussians, balanced with supervision from input views. Our method improves the quality of various sparse-view Gaussian methods without sacrificing rendering speed, and our analysis works on different prior models. Project page: this https URL

---


### 21. [CaLA: Causal Latent Adjustment for World Models under Adaptive Policies](https://arxiv.org/abs/2611.31431)

**<font color=#1a73e8>作者：</font>** Robert Ness, Sofiane Ennadir, Oleg Smirnov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models is answering ``imagine" answers to ``what-if'' questions via imagined rollouts. But rollouts collected by adaptive policies induce treatment-outcome confounding in imagined rollouts. We study this problem in Match-3 difficulty adjustment, where latent player skill influences both assigned difficulty and churn. We build a fully specified Match-3 SCM with sequential mechanics, adaptive assignment, and paired ground-truth interventions, on which unadjusted models fit to the logged trajectories select difficulty settings that raise churn. We then introduce Causal Latent Adjustment (CaLA), a DAG-constrained world model that infers a variational player representation from pretreatment history. Across our evaluations, CaLA provides the most reliable population-level intervention estimates and competitive individualized decisions, although rich handcrafted histories can remain advantageous for individual-level adjustment. We further find that residual correction can degrade causal decision quality despite improving predictive fit, highlighting the need to distinguish predictive accuracy, confounding adjustment and the behavior of downstream causal estimators.

---


### 22. [Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos](https://arxiv.org/abs/2611.31435)

**<font color=#1a73e8>作者：</font>** Yucheng Zhu, Maria J. Molina, Christopher Metzler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characterizing how tornadoes evolve over space and time is critically important for understanding and preparing for these highly destructive weather events. Towards this end, we develop algorithms capable of forming time-resolved 3D reconstructions of laboratory smoke tornadoes from sparse one-sided videos. Even in a controlled environment, reconstruction is severely underconstrained: appearance is view dependent, motion is non-rigid, and the unobserved volume admits many geometries. We present Tornado4D, a physics-guided 4D Gaussian framework capable of reconstructing laboratory tornadoes from sparse, one-sided videos. Tornado4D uses knowledge of the enclosure geometry to introduce rotational airflow field priors that constrain how the 3D structure evolves over time. These rotational priors allow us to reconstruct otherwise unobserved structure. We evaluate reconstruction accuracy by computing novel-view synthesis accuracy on a held out camera view: Tornado4D outperforms frame-by-frame 3DGS and video-based 4DGS by a considerable margin.

---


### 23. [Is 4 Bits Enough for EEG Sleep Staging? A Subject-Level Benchmark of MXFP4, NVFP4 and FP8](https://arxiv.org/abs/2611.31436)

**<font color=#1a73e8>作者：</font>** Emese Batizi, Hossein Valavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Staging sleep on a wearable device keeps the raw electroencephalogram (EEG) private and saves the energy needed to transmit it. It also requires small, energy-efficient neural networks. We benchmark 13 post-training quantization (PTQ) configurations, from FP16 to the block-scaled 4-bit formats MXFP4 and NVFP4, for five-stage sleep staging from single-channel Fpz-Cz EEG. We use Sleep-EDF-78 (78 subjects), subject-wise cross-validation, three training seeds, value-exact emulation, and per-subject paired statistics. All 8- and 16-bit formats stay within 0.45 percentage points (pp) of FP32 Macro-F1. With 4-bit weights and activations, an epoch-wise CNN loses 1.98 to 3.04 pp, and a temporal-context network loses at most 1.19 pp. A same-encoder ablation shows that temporal context explains little of this gap. At equal block size, NVFP4 outperforms MXFP4. The first layer, which quantizes the raw EEG, is the most sensitive layer in both networks. Keeping the first and last layers in FP8 brings both tested 4-bit formats within 0.48 pp of FP32. This recipe adds at most 2.1% weight storage, needs no retraining, and is equivalent to quantization-aware training (QAT) within an exploratory 1-pp margin. The 4-bit losses fall on the same subjects across architectures (Spearman correlation coefficient = 0.69 to 0.79), and they reduce N3 recall the most. On the nested Sleep-EDF-20 subset, NVFP4 with FP8 first and last layers again stays within 0.25 pp of FP32. Under MXFP4, however, the ranking of the architectures reverses, and FP8 first and last layers do not fully recover two of the three tested models. In our emulation, NVFP4 with FP8 first and last layers thus loses little accuracy without QAT in both cohorts.

---


### 24. [Which Ellipses Are Outlines of a Given Ellipsoid? A Ratio Test with Unknown Focal Length](https://arxiv.org/abs/2611.31437)

**<font color=#1a73e8>作者：</font>** Michael Werman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When is an image ellipse the outline of a given ellipsoid with semi-axes $a <= b <= c? For a camera with square pixels, zero skew and known principal point, we show that it is an outline at focal length $f$ exactly when a cone ratio kappa(f), computed from two eigenvalues, is at most a/c; the middle semi-axis b plays no role. With f unknown, the admissible focal lengths form an interval; whether it is empty is decided by the smallest cone ratio over $f$, which, when attained, is obtained from an explicit quartic. The interval is bounded above only when the principal point is closer to the long axis of the ellipse than to its short axis. Thus one ellipse can rule out ellipsoids that are too round, never ones that are too elongated, and none if the principal point is unknown. Simulations and 45 Cassini images of Saturn's moons support the test.

---


### 25. [Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study](https://arxiv.org/abs/2611.31442)

**<font color=#1a73e8>作者：</font>** Sayed Amir Karim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense-embedding retrievers can fail adversarially: when a query is answered by a document A and reversed by a near-copy B that differs from A by a small meaning-changing edit (a "trap"), raw cosine over E5-Large-v2 places B in the top-10 for 82-100% of queries at a pool of 5,000. We study two things. First, a small learned projection W: R^1024 -> R^d (d in {11, 32}), trained by a deterministic recipe on a declared set of cases, that suppresses the trap: for the declared cases, HN@10 = 0.0000 (no trap in the top-10) in all twelve (domain, pool-size) settings across four independent domains (legal, medical, patent, financial) and pools up to 100,000, while the correct paraphrase is retained for 93-99% of cases, under exact nearest-neighbour search. Second, a boundary-conditioned accelerator that serves the projection at that scale: an acceleration of spectral graph retrieval (SpectRAG) that replaces a dense eigendecomposition with a boundary-value solve, holding HN@10 = 0.0000 at n = 100,000 in every domain and retrieving the ~300-query suite in 0.6-1.1 s (~2-4 ms per query on average). Because the lens's output is the stored representation (a few floats per document), a hardened, specialised index per domain or tenant is ~90x smaller and dimension-proportionally faster than the full embedding, making many small declared indexes a practical alternative to one large vector store. The claim is scoped to the declared cases on the measured pools, with no probabilistic bound; the correct-answer rate drops for a reworded query against an unchanged corpus (about 0.79, trap suppression still holding). A projection transfers only partly to other domains, which we report in full. The recipe, lenses, trap sets and evaluation harness are released under AGPL-3.0; the accelerator's implementation is a reserved commercial component, and every HN number is reproducible under exact search.

---


### 26. [The Fingerprinting Paradox: Why Sensitivity Undermines Black-Box Model Integrity Verification](https://arxiv.org/abs/2611.31455)

**<font color=#1a73e8>作者：</font>** Shahinul Hoque, Farhin Farhad Riya, Jinyuan Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box integrity verification aims to detect unauthorized modifications to outsourced models using only prediction APIs. Existing frameworks seek to improve verification efficiency through sensitive fingerprints: queries whose predictions are more likely to change under tampering than those of genuine inputs. We show that this sensitivity can also help dishonest providers recognize verification queries and selectively conceal tampering. We prove that excess sensitivity relative to genuine inputs lower-bounds statistical distinguishability. We evaluate five integrity verification frameworks across three model architectures, three datasets, and three adversarial knowledge settings. When the deployed framework is known, our fingerprint detectors achieve AUCs at least 0.989, and selective filtering makes all five frameworks require significantly larger estimated query budgets than genuine inputs, reversing their intended efficiency advantage. A query-efficiency advantage remains marginally in a small subset of evaluated settings with poor detection transfer. We further design verification methods under stronger concealment constraints but find that reduced detectability comes with losses in sensitivity or fingerprint-generation success. Our results expose a sensitivity-detectability tension and show that sensitivity alone does not ensure efficient black-box verification against adaptive malicious providers.

---


### 27. [AdProducer: Towards Agentic Advertising Video Generation](https://arxiv.org/abs/2611.31466)

**<font color=#1a73e8>作者：</font>** Kunyang Li, Chaoyang Wang, Mubarak Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have made automated advertising production increasingly feasible. However, an effective advertisement must faithfully represent the product and communicate its selling points through compelling visual storytelling, which requires more than visual synthesis: it calls for deeper product understanding and strategic decisions about how to present product value. Crucially, product research and creative design are closely intertwined, as the information gathered about a product determines which features can be faithfully demonstrated and how they should be presented. In this paper, we introduce AdProducer, the first end-to-end agentic framework for advertising video creation, transforming concise creative briefs into finished advertisements. Our multimodal agent autonomously researches products through web and image search and translates its findings into selling-point-driven storyboards that guide a frozen video generator. To achieve this, we develop a dedicated data construction pipeline that yields two training datasets, AdProducer-SFT and AdProducer-RL, and train the agent through supervised fine-tuning followed by reinforcement learning with joint optimization of storyboard- and video-level rewards. We further introduce AdCreation-Bench, comprising 305 advertising briefs across eight domains, with two complementary metrics: PG-Score for product correctness and creative execution, and Ad-Score for overall advertising effectiveness assessed by an independent judge. Experiments demonstrate that AdProducer improves the PG-Score of MiniMax H3 from 17.3 to 51.3 and generalizes to Veo 3.1 without additional training, improving its score from 28.0 to 35.9, with consistent gains in Ad-Score, VideoScore2, and human evaluations. Code, models, and data are released.

---


### 28. [Symbolic Proof Compression and Fractal Universality: A Conditional Non-Constructive Refutation of the Riemann Hypothesis](https://arxiv.org/abs/2611.31469)

**<font color=#1a73e8>作者：</font>** Andreas Martin Lisewski  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Building on S.~C.~Woon's (1994) fractal and symbolic reformulation of Voronin's Universality Theorem, we construct a formal, non-constructive proof-by-contradiction architecture exploring the Riemann Hypothesis ($\mathsf{RH}$). Woon's Corollary~3 permits arbitrary finite binary strings to be encoded into nowhere-vanishing exponential waveforms on a closed disk inside the critical strip. Combining effective upper bounds for Voronin universality (Good, Garunkštis) with Cauchy-integral Taylor decoding yields an explicit finite rational grid $\mathcal{G}_{L_0}$ below an effective ceiling $H_{\mathrm{crit}}(L_0)$ within which every formal proof of bit-length at most $L_0$ is imprinted with zero flipped digits. We introduce a conjectural \emph{Zeta-Universal Symbolic Proof Compression Hypothesis} ($\mathsf{SPC}_{\mathsf{RH}}$), positing that the global regularity implied by $\mathsf{RH}$ compresses true $\Pi_1^0$ statements about $\zeta(s)$ into $\mathsf{ZFC}$ derivations of bounded length $L_0$. Assuming classical logic and $\mathsf{SPC}_{\mathsf{RH}}$, Gödel--Carnap diagonalization over bounded zeta-encoded provability yields a contradiction. The self-referential result converts a digital encoding framework with any uniform proof-compression principle for RH into an immediate non-constructive refutation of RH. Given that, with human input and computer assistance, $\mathsf{RH}$ has been formally verified in the Lean theorem prover strictly within constructive logic, this contradiction does not refute $\mathsf{RH}$. Instead, it falsifies $\mathsf{SPC}_{\mathsf{RH}}$. We conclude by isolating the exact proof-theoretic obstruction---Pudlák's lower bound on bounded reflection proofs---showing why the analytic regularity of $\mathsf{RH}$ cannot compress logical self-reference, and exposing the limits of applying the Law of Excluded Middle to uncomputably bounded searches.

---


### 29. [Transferable, Time-Parallel Graph Dynamics via Space-Time Factorization](https://arxiv.org/abs/2611.31479)

**<font color=#1a73e8>作者：</font>** Wencong Yang, Chaopeng Shen, Abdolmehdi Behroozi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-parallel neural operators (FNO and successors) have transformed PDE surrogates on regular grids. Mesh-based operators (MeshGraphNets, Transolver) extend operator learning to irregular geometries, but jointly learning across diverse topologies while retaining non-recurrent temporal evaluation remains challenging. We propose space-time factorization: partition the model into local temporal operators (learned, graph-independent) and a spatial mixer that propagates information across nodes without graph-dependent learned parameters. This structural condition lets the same parameters run on unseen graphs; non-recurrent instances also admit time-parallel evaluation. Accurate zero-shot transfer further depends on controlling three information leaks (graph-dependent weights, graph-specific features, and graph-correlated training distributions) and on suitable task physics and training coverage. The protocol applies to two distinct spatial-mixer families, fixed-spectral and learned-attention. We validate the principle in three domains. For floodwave propagation in river networks, a 27K-parameter model trained on the Yangtze transfers zero-shot to the Mississippi with median NSE 0.998 in boundary-conditioned operational evaluation, training 5.5x faster than a stabilized recurrent baseline. On cross-geometry Navier-Stokes, the three-seed SepFNO mean relative vorticity error on five unseen targets falls by about 28% from 5 to 12 training geometries, with a consistent single-run SepTransolver trend. On cross-city traffic forecasting, zero-shot transfer reaches within 12.9% of an oracle trained on the target city. Across settings, cross-geometry error decreases with both the number of training geometries and their relatedness to the test, at a rate depending on the spatial mixer. This opens the path to pooled-data, foundation-style models for graph dynamics on irregular topologies.

---


### 30. [CHORD: Learning Latent Spaces for Constrained Stellarator Design](https://arxiv.org/abs/2611.31486)

**<font color=#1a73e8>作者：</font>** Santiago A. Cadena, Andrea Merlo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In high-dimensional, PDE-constrained design, interpolating between known feasible solutions can reveal trade-offs without repeating expensive optimization campaigns. In stellarator design for fusion energy, direct interpolation of plasma boundary parameters can violate physical constraints even when both endpoints are feasible. Learned latent representations can capture nonlinear relationships among design variables, but latent interpolation can still cross infeasible regions, and conditioning on target metrics can become inconsistent with the decoded design. We introduce CHORD, a conditional variational autoencoder that penalizes predicted constraint violations along decoded latent interpolants during training, paired with self-consistent inference that aligns conditioning with the decoded design's predicted metrics. Geometric benchmarks show the benefit of regularizing latent interpolants. In stellarator interpolation between distinct geometry families, CHORD reaches up to 81% simulator-validated mid-segment feasibility, compared with 50% for an unregularized conditional VAE and 28% for direct interpolation of boundary parameters. Ablations show that both ingredients are needed for this gain. Beyond interpolation, latent-space optimization finds simulator-feasible designs, while self-consistent sampling produces more diverse feasible alternatives. On the ConStellaration benchmark, chord-regularized models with linear conditioning reuse data from five optimization campaigns and simulator-labeled rescalings to populate the Pareto front more densely. After low-fidelity screening, 93% of 1.2k generated candidates pass the benchmark's high-fidelity feasibility test. We release code and over 600k designs for stellarator generation, surrogate training, and front-filling evaluation. These results support feasibility-aware latent learning for exploring constrained design trade-offs.

---


### 31. [Trust-Region Optimization for Performative Prediction without Response Modeling](https://arxiv.org/abs/2611.31492)

**<font color=#1a73e8>作者：</font>** Siqi Du, Miaolan Xie, Roy Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performative prediction studies learning problems in which deployed decisions change the distribution of future data. Existing methods often impose structure on the population response, which limits their applicability when a fixed model class poorly captures that response. Generic black-box optimization avoids response modeling but does not exploit the known loss function.
We introduce Performative Trust-Region Optimization (PTRO), which bridges these two approaches by optimizing performative risk without specifying or fitting a response model while still exploiting the known loss. The key idea is sampling from the current population to evaluate the known loss at nearby decisions, and use additional deployments only to estimate the effect of population response. This gives a local approximation of performative risk without committing to a model of how the population responds. PTRO then uses a trust-region mechanism to determine and adapt how far this local information can be trusted.
Under moment-bounded losses and suitable smoothness and estimator-accuracy conditions, we establish high-probability convergence to an $\epsilon$-stationary point of the performative risk in $O(\epsilon^{-2})$ iterations, with $O(d^{3}\epsilon^{-4})$ samples per iteration, where $d$ is the decision dimension and $q\geq2$ is the loss-moment order.
Experiments illustrate methods built around a specified response model can be more sample-efficient when their structural assumptions are accurate, whereas PTRO remains effective as the population response is poorly captured by a fixed model class. Ablations further show that both exploiting the known loss and adaptive trust-region updates are important for controlling the accuracy and efficiency.

---


### 32. [ModernELECTRA: Replaced-Token Detection with Boundary-Window Reconstruction for Compact Encoders that Classify and Embed](https://arxiv.org/abs/2611.31495)

**<font color=#1a73e8>作者：</font>** Mykhailo Shtopko, Ihor Stepanov, Dmytro Vodianytskyi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ELECTRA-style replaced-token detection (RTD) is a sample-efficient objective for pre-training text encoders, and RTD-trained models such as DeBERTaV3 are strong on classification benchmarks. The same models, however, are known to be poor backbones for embedding tasks such as retrieval and semantic similarity: the binary "original vs. replaced" signal does not ask the final layer to retain the token identity and contextual content that dense representations rely on. We introduce ModernELECTRA, a pre-training recipe that keeps RTD as the main objective and adds a lightweight auxiliary task, boundary-window reconstruction. For every token, we sample a window of 3-12 tokens that strictly contains it and reconstruct the token's original identity only from the discriminator's hidden states at the two window boundaries. The task costs one small FFN at training time and is discarded afterwards, yet it forces every final-layer state to carry information about its neighbourhood. Combined with a frozen, separately pre-trained generator, a temperature curriculum for hard negatives and a 512-to-8192 length curriculum, we train two compact encoders: EdgeCoder-31M, an 8-layer English model, and EdgeCoder-Multilingual-61M, a 16-layer model covering 46 languages, each on about 1T tokens. They reach 86.0 and 85.1 on GLUE. The English model outperforms Ettin-Enc-32m (83.5) and MiniLM-L12 (84.6) on GLUE while matching them on MTEB English v2 (51.1), and the multilingual model outperforms the 2.3x larger mmBERT-small on GLUE and Multilingual MiniLM and mDistilBERT on XTREME over the languages it covers. We also describe FlashDeBERTa, our open-source fused implementation of DeBERTa's disentangled attention that stores no $n \times n$ score matrix: at 4096 tokens it is 10x faster and uses 93% less memory than the reference implementation, and it loads existing DeBERTa checkpoints unchanged.

---


### 33. [Reading Between the Layers: Where Representation Quality Lives, and What Geometry Reveals](https://arxiv.org/abs/2611.31496)

**<font color=#1a73e8>作者：</font>** Arnesh Batra, Aniket Khandelwal, Arush Gumber 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representation quality in pretrained text foundation models is not concentrated at the final layer, yet practitioners routinely probe it there because layer selection without labels has remained an open problem. We present a large-scale empirical study of where layer quality lives across 25 models spanning four architectural families and four pretraining strategies, evaluated on 13 datasets across classification, pair classification, semantic textual similarity, and multiple-choice question answering. Peak probing layers depend systematically on pretraining strategy and architecture: masked encoders peak in late-middle layers, sequence-to-sequence models shift their peak with task type, contrastive sentence encoders concentrate signal at the final layer under CLS and last-token readouts but peak early under mean pooling, and decoder-only models exhibit distinct phase structure tied to depth. We distill these findings into the Stable Geometry Index (SGI), a closed-form, fully label-free selector with no fitted coefficients combining power-law fit quality, effective-rank capacity, spectral stability, and a weak depth prior. Across 383 evaluation groups SGI improves over the last-layer baseline and lifts Hit@3 from 0.39 to 0.52, recovering 40% of the gap to the oracle without using any labels, and exceeds a supervised ELMo-style layer mix on the matched subset despite using strictly less information. Our ablations also reverse a common assumption in the spectral-decay literature: power-law fit quality is a stronger predictor of layer quality than the exponent's proximity to one.

---


### 34. [XRL4T1D: A Post-hoc Explainability Framework for Reinforcement Learning in Type 1 Diabetes Management](https://arxiv.org/abs/2611.31498)

**<font color=#1a73e8>作者：</font>** Malay Phadke, Chirath Hettiarachchi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Type 1 diabetes (T1D) requires lifelong insulin therapy, and reinforcement learning (RL) has shown promise for automated dosing in the UVA/Padova simulator. However, the decisions of RL controllers remain difficult to interpret. We present XRL4T1D, a post-hoc explainability framework for evaluating pretrained insulin-dosing policies without retraining. Each policy uses 60 minutes of continuous glucose monitor (CGM) and administered-insulin history, sampled every 5 minutes, to recommend insulin. We use SHapley Additive exPlanations (SHAP) to compare the importance of CGM and insulin-history inputs and summarize insulin-history attributions over three 20-minute windows motivated by insulin-on-board. We assess whether these attributions correspond to policy-output sensitivity through targeted input replacement and compare temporal rankings with TimeSHAP. In all 80 patient-policy-mask-size cases, replacing the highest-attribution inputs changes the normalized insulin recommendation more than replacing the lowest-attribution or random inputs. The highest-attribution insulin-history window is also the most output-sensitive in 115 of 120 patient-policy-scenario configurations, and KernelSHAP and TimeSHAP select the same top window in 111 of 120. Applying XRL4T1D to PPO and G2P2C across 20 virtual patients, we find that both controllers rely predominantly on CGM history, especially G2P2C. However, the distribution of insulin-history importance across recent, middle, and older windows varies by cohort, explainer, and analysis settings, without a consistent separation between controllers. Global feature-attribution rankings remain stable under the tested observation corruptions. These results show why attribution fidelity, temporal reproducibility, and controller-comparison robustness should be assessed separately.

---


### 35. [Measuring Counterfactual Credit in a Replayable Wildfire-Suppression Benchmark](https://arxiv.org/abs/2611.31499)

**<font color=#1a73e8>作者：</font>** Alireza Moghaddasi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In cooperative multi-agent reinforcement learning, learned critics are usually evaluated by how well they predict the team's return. Yet predicting a team's return and assigning credit to individual actions are distinct tasks. To test credit directly, we introduce FLARE (Fireline Learning Agents in a Replayable Environment), a stochastic wildfire suppression benchmark in which any moment of a fire can be replayed with different actions under the same random events. Replaying one step measures the immediate effect of each agent's suppression, which we call simulator credit and use for training. Replaying to the end of the episode measures the effect of each action, which we use for grading critics. In a comparison over eight seeds with multi-agent proximal policy optimization (MAPPO), simulator credit reduces the interquartile mean burn score (each cell's burning time, capped and averaged over the map; lower is better) from 26.6% with shared reward to 20.9%. Learned credit from a centralized COMA-style critic does no better than the shared reward. Four trained critics predict the team's return well, yet the credit they assign is 9 to 42 times larger than the credit measured by replay. The critics also give heterogeneous agents nearly identical action rankings. These results show that a good fit to the team's return is a weak test of a critic's credit.

---


### 36. [HyMTS: A Multiscale Tensor Factorization-Based Network for Hyperspectral Image Restoration](https://arxiv.org/abs/2611.31506)

**<font color=#1a73e8>作者：</font>** Lei Xu, Fahad Sohrab, Moncef Gabbouj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) restoration has been explored using deep learning techniques recently. Because hyperspectral images have strong spectral and spatial redundancy, the underlying clean signal is usually represented in a low-dimensional spectral subspace and locally low-rank spatial structures. Existing methods primarily explore dense attention or feature mixing across spectral bands. In this work, we propose HyMTS, a hyperspectral restoration network with a backbone built on the Multi-scale Tensorial Summation (MTS) factorization operator. HyMTS provides a natural architectural mechanism for exploiting a low-rank prior, embedded directly in the network operator rather than imposed via an auxiliary loss or a constraint on the reconstructed output. Specifically, HyMTS stacks a unified block that couples factorized layers with input-adaptive layers, capturing both local and global dependencies across the spectral and spatial dimensions. Extensive experiments without auxiliary data on standard benchmarks for Gaussian and real-noise denoising and single-image super-resolution show that HyMTS efficiently achieves superior or comparable performance to various state-of-the-art approaches.

---


### 37. [How to build and train your recurrent-depth model: A fixed-point perspective](https://arxiv.org/abs/2611.31513)

**<font color=#1a73e8>作者：</font>** Thomas Pethick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent-depth models are trained with truncated backpropagation, yet it remains unclear why this works. We show that input injection, commonly used in recurrent-depth models, is exactly Halpern iteration, and that a slowly vanishing stepsize provably converges with a backpropagation window polylogarithmic in the depth. The guarantees require a Lipschitz operator, which for SwiGLU leads to a weight constraint in both row and spectral norm, while only a row norm constraint for gates. Based on these constraints, we develop an optimizer tailored to each parameter group, Sparrow, which provides a drop-in replacement of Muon/MuonH with no overhead, that speeds up training even beyond recurrent models.

---


### 38. [Synthetic Augmentation for Data-Scarce Object Detection: Allocation, Dose, and Filtering Across Six Datasets](https://arxiv.org/abs/2611.31515)

**<font color=#1a73e8>作者：</font>** João Félix, Atabak Dehban, Rodrigo Ventura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic perception for capturing uncooperative orbital objects and inspecting variable industrial products must often operate with limited labelled imagery. We examine a modular synthetic-augmentation pipeline, evaluating generation planning and post-generation filtering as separate interventions, with computational cost as a design constraint. Across six object-detection datasets, FLUX.1-Fill with class-specific LoRA adaptation produced dataset-dependent dose effects; the validation-selected augmentation improved mAP@50:95 on four datasets and reduced it on two. Filtering did not yield consistent gains, and FID, KID, precision, recall, and LPIPS did not consistently track detector changes. The results do not establish that image quality alone identifies useful samples. They motivate standardised evaluation and inexpensive candidate-utility measures that could identify useful samples before detector retraining, reducing repeated training cost.

---


### 39. [InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion](https://arxiv.org/abs/2611.31516)

**<font color=#1a73e8>作者：</font>** Simon Weber, Mateo de Mayo, Je Hyeong Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Initialization-free bundle adjustment (InitFree BA) aims to jointly recover camera poses and scene structure without requiring an initial global estimate. It is a very challenging problem, especially compared to traditional BA where a good estimation is assumed. While recent methods optimize surrogate Object Space Error (OSE) objectives from random initialization, a low objective value does not necessarily yield an accurate reconstruction, revealing a gap between optimization and reconstruction. We show that existing InitFree BA pipelines struggle to produce accurate 3D reconstructions on modern SfM benchmarks, and demonstrate that incorporating learned metric depth substantially improves their practical feasibility. We introduce InitFree-SfM, a complete initialization-free SfM pipeline combining learned correspondences, metric depth, depth-consistent track construction, and joint metric refinement. Within this framework, we propose a simple depth-augmented OSE (dOSE), which complements the directional constraints of OSE by constraining landmark positions along their viewing rays. Our approach substantially outperforms existing InitFree BA methods and achieves competitive accuracy with established SfM pipelines, including on challenging low-overlap image collections. Importantly, our analysis challenges the prevailing emphasis on surrogate objectives in previous InitFree BA research, revealing that geometric constraints play a central role in accurate reconstruction, while OSE-based optimization provides further improvements.

---


### 40. [Your Codec, Your Generator: Idempotent Generative Compression without Retraining](https://arxiv.org/abs/2611.31520)

**<font color=#1a73e8>作者：</font>** Raz Haim, Assaf Shocher  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce an image compression framework with three properties: (i) adaptation of pretrained codecs without retraining or fine-tuning, (ii) cycle-consistent recompression, even of already-encoded images, and (iii) decoding with independently chosen generative priors. We wrap the frozen encoder with non-learned operations so that every continuous latent has a preimage, yielding a surjective pseudo-invertible neural network. A nonlinear right inverse built from the pretrained decoder satisfies $E'(D'(E'(x)))=E'(x)$. To extend consistency to quantized bitstreams, the receiver searches for a continuous latent that reproduces both the transmitted main symbols and entropy side information. A successful search and an exact correction preserve both streams under deterministic coding; the final reconstruction is checked through the actual coding path. The encoder's pseudo-inverse enables a nonlinear counterpart of back-projection. In the linear case, back-projection has the closed-form solution $x'=x+A^\dagger(y-Ax)$, giving the closest reconstruction to $x$ satisfying $Ax'=y$. Our nonlinear formulation enforces the transmitted code on proposals from an independently chosen generative model. Adjusting the starting noise controls the prior's influence without changing that code. Experiments show small first-pass quality changes, higher retained quality than trained consistency codecs over 50 recompressions, also under 8-bit storage, and decoder-side control of the perception-distortion trade-off. Decoupling the codec from its prior lets the receiver adopt future generators without retraining or re-encoding.

---


### 41. [One Step, Four Clocks: How GUI Agents Fall Out of Step](https://arxiv.org/abs/2611.31522)

**<font color=#1a73e8>作者：</font>** Zhanwen Chen, Tianchun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents can choose correct actions yet fail as interfaces change during deliberation. Latency alone cannot explain these failures because actions may become invalid at different interaction stages. We model four events: environment change, observation availability, decision commitment, and action receipt (EODA). We introduce ChronotopeGym to study these failures under Paused, Replay, and Live execution. Across five tasks, agents can fail in Live despite succeeding when responses remain valid, even when actions meet deadlines. On Moving Balloon, updating a pending click raises success from 0% to 100% without changing response time. Our accelerator-resident GUI controller, Chronotope, maintains compact interaction history and selectively keeps, updates, or redecides pending actions. Compared with Agent S3, Chronotope reduces median end-to-end latency by 85.5% for a 27B model, expanding its performance envelope to 100% Live success at an 8-second deadline versus 0%. Chronotope enables real-time GUI control through compact interaction history, knowing when to preserve, revise, or replace actions, and an overall efficient architectural design that obviates verbose reflection, reasoning, and grounding calls.

---


### 42. [Fast Anatomy-Aware Diffeomorphic Augmentation for Brain MRI](https://arxiv.org/abs/2611.31524)

**<font color=#1a73e8>作者：</font>** Tonmoy Hossain, Alexandra G. Roberts, Mark Olchanyi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is essential for training deep learning models that are generalizable, particularly when training data are limited. In brain MRI, augmentation methods that synthesize anatomically diverse images without relying on large cohorts are particularly attractive, especially when training supervised models for scans with a specific resolution or MRI contrast. While conventional random nonlinear fields offer a simple means of achieving such diversity, they fail to capture the underlying spatial dependencies among morphological changes across brain regions. To address this limitation, we introduce BrainAug, an anatomy-aware augmentation framework that generates diverse, anatomically coordinated deformations without relying on population imaging data. BrainAug constructs an anatomical graph encoding spatial proximity and bilateral correspondence between brain regions, then incorporates these relationships into a probabilistic model designed to sample correlated regional volume changes. These sampled variations are translated into diffeomorphic transformations, enabling substantial structural changes while preserving anatomical topology. Combined with contrast-agnostic image synthesis, BrainAug generates training images with independently varying anatomy and appearance. Evaluations across eight brain MRI datasets demonstrate stronger segmentation generalization across diverse populations, while registration experiments show improved alignment under substantial morphological differences.

---


### 43. [SOTS: Signature-based Optimal Transport Selection](https://arxiv.org/abs/2611.31525)

**<font color=#1a73e8>作者：</font>** Khalid Akhmouch, Eric Jauer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data selection for machine learning models is a critical bottleneck in industrial applications where expert annotation is costly and time-consuming. Existing coreset selection methods for time series either ignore temporal structure entirely or cannot handle variable-length, irregularly sampled, multi-channel signals, the setting most common in industrial monitoring and testing. We introduce SOTS (Signature-based Optimal Transport Selection), an unsupervised coreset selection framework for irregular multivariate time series (IMTS) classification. Each sample is mapped to a truncated path signature, capturing the joint geometric structure of its channels, and the coreset is selected by greedily minimizing the Sliced Wasserstein distance between the empirical signature distributions of the candidate subset and the full dataset, a criterion for which we establish a convergence guarantee for random coresets. We validate SOTS on a real-world, highly imbalanced industrial I&C testing dataset, where SOTS-Greedy exceeds 95% of full-dataset accuracy using only 30% of the training data, outperforming standard coreset baselines at most budgets. This advantage generalizes to public UEA regular multivariate time series benchmarks specifically when class-discriminative information is purely geometric.

---


### 44. [Diagnosing Epistemic Uncertainty in Neural Operators: Effects of Initialization, Discretization, and Function Sampling](https://arxiv.org/abs/2611.31526)

**<font color=#1a73e8>作者：</font>** Tian Yu Yen, Yucheng Fu, Pratanu Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide efficient surrogates for mappings between function spaces, but their reliability cannot be characterized by the performance of a single trained model. Existing neural operator uncertainty quantification approaches often characterize predictive uncertainty without separately identifying the contributions of individual sources of epistemic uncertainty. Finite sampling of the training function space, output discretization, and model initialization can produce substantial variation among learned operators even when the underlying physical problem is deterministic. We systematically investigate these sources of epistemic uncertainty across a diverse set of operator learning architectures. Across our experiments, we train approximately 46,000 neural operator models and construct ensembles over training datasets, model initializations, and output discretizations to characterize distributions of relative $L_2$ error rather than individual trained realizations. We find substantial architecture-dependent differences in epistemic uncertainty, with model initialization often accounting for the largest proportion of variance in relative $L_2$ error. The ranked performance of neural operator architectures can invert as the number and spatial distribution of output samples change, with the best architectures under sparse or randomly sampled observations differing from those at higher-resolution or structured discretizations. Furthermore, ensembles that reliably characterize aggregate operator error can provide unreliable estimates of error quantiles for individual test functions. These results highlight the importance of distinguishing the sources of epistemic uncertainty when evaluating neural operator reliability and establishing robust benchmarking practices.

---


### 45. [JevBench: Metamorphic Coherence Testing for Typed Probabilistic Decision Models](https://arxiv.org/abs/2611.31533)

**<font color=#1a73e8>作者：</font>** Chen Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Typed probabilistic decision models return distributions over specified answers, such as yes or no, a set of options or levels on an ordered scale. We ask whether their probabilities remain coherent when questions about the same input are reworded, negated, combined, given different options or placed in different batches. JevBench tests this coherence without gold labels. Its 50 metamorphic relations each test one law of probability or choice across five dimensions: representation, batch independence, probability measure, logical order and choice-set conditioning. Each test changes the question or batch while keeping the input fixed. Every model receives the same requests, fixed in advance. JevBench-240 contains 12,000 tests across 240 synthetic cases in 12 decision domains. A fixed subset of 1,200 tests, JevBench-mini, closely reproduces the full-suite ranking (Spearman 0.983). Across 21 openly released models, coherence scores range from 56.5 to 83.9. Batch independence holds for most models. Additivity fails broadly, particularly for complements, where the probabilities of a proposition and its negation should sum to one. A uniform reference model ignores the input and scores 89.4 at chance accuracy, exceeding every evaluated model's coherence score. Among decoders, accuracy ranges from 82.4% to 89.2%, while coherence ranges from 64.2 to 83.9. These results show why both measures are needed to assess decision models. JevBench is available as an open-source Python package.

---


### 46. [Denoising Diffusion with Progressive Posterior Sampling](https://arxiv.org/abs/2611.31558)

**<font color=#1a73e8>作者：</font>** Zeyu Luo, Shuai Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models provide effective generative priors for solving noisy linear inverse problems. However, existing posterior sampling methods may require singular value decomposition (SVD) of the measurement operator or prior knowledge of the measurement noise variance, while guidance based on local gradients provides only a limited view of posterior geometry. We propose progressive posterior sampling (PPS) with manifold projection, which automatically estimates the measurement noise variance and avoids SVD. During reverse diffusion, PPS constructs a Gaussian approximation to the posterior distribution in closed form and guides a sample drawn from the local prior toward the approximate posterior mean. We then project the guided sample onto a spherical level set that approximates the local noisy image manifold, promoting consistency with the local geometry of the diffusion prior. Experiments on FFHQ and ImageNet across four restoration tasks and three measurement noise levels demonstrate competitive reconstruction accuracy and perceptual quality by PPS.

---


### 47. [Latent Channel Completion for Forecasting in Sensor Networks with Failed Detectors](https://arxiv.org/abs/2611.31575)

**<font color=#1a73e8>作者：</font>** Mehran Shabanpour, Sadaf Khademi, Maryam Hosseini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring networks for traffic and utility infrastructure lose sensors routinely, and forecasting models that couple sensors together to gain accuracy also inherit an exposure to those losses. When a detector stops reporting, the substituted value is embedded as though it were a reading and propagates through the shared representation that couples the network, degrading forecasts for sensors that are still healthy. Because these models are selected on benchmarks where every sensor reports, the exposure is absent from the numbers used to choose them. We introduce Latent Channel Completion, a channel-axis joint embedding predictive objective that reconstructs missing sensors' latent representations rather than their values, since a coupling operator consumes embeddings and never sees raw readings. Channels are masked during training and their representations predicted from surviving channels against stop-gradient targets; at inference the operator fills in whichever sensors the monitoring system reports as dark, using parameters shared with the forecaster. On three highway detector networks, after half of each network goes dark, the accuracy advantage of coupling changes by -1.0, -0.5 and +8.8 percentage points, against losses of 10.2 to 50.3 points for the unmodified forecaster, which on one network falls behind an uncoupled reference entirely. Against cross-channel ridge imputation drawing on the same surviving sensors, completing the latent lowers error by a further 13.9% and 28.6%, and on complete inputs, the method matches its backbone. The benefit tracks how much a network gains from coupling when intact, giving operators a criterion evaluable before any outage occurs.

---


### 48. [PazaBench: Large-Scale ASR Benchmark for Low-Resource Languages in Africa](https://arxiv.org/abs/2611.31578)

**<font color=#1a73e8>作者：</font>** Mercy Muchai, Nick Mumero Mwangi, Kevin Chege 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource languages remain underrepresented in ASR benchmarks, limiting the ability to reliably assess and compare model performance. We present a large-scale benchmark for automatic speech recognition (ASR) on low-resource languages in Africa. The benchmark harmonizes six public corpora into a unified, reproducible evaluation framework and evaluates 52 state-of-the-art ASR models spanning three model architectural paradigms across 39 African languages on diverse datasets. Models are evaluated using standard accuracy and efficiency metrics, word error rate (WER), character error rate (CER), and inverse real-time factor (RTFx). This benchmark introduces architecture-aware comparison that systematically analyzes both individual models and broader model families. In addition, we quantify linguistic variance across language families, revealing how these factors shape ASR performance across diverse African languages. We also provide a comprehensive accuracy and efficiency trade-off analysis directly relevant to deployment in low-resource settings. Together, the benchmark, evaluation pipeline, and results support transparent, reproducible, and deployment-aware evaluation of ASR models for low-resource languages.

---


### 49. [Provably Near-Optimal PQ in the Extended Zador Model](https://arxiv.org/abs/2611.31579)

**<font color=#1a73e8>作者：</font>** Edo Liberty, Ashwin Padaki, Amir Ingber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates Product Quantization (PQ) Optimization with Gaussian data. It offers three key contributions (i) a proof that SVD is the optimal preconditioning rotation for PQ; (ii) a new Extended Zador (EZ) estimator of the $k$-means quantization cost that is accurate in low bit rates and low dimensions; and (iii) a novel segmentation algorithm based on 1-d bin packing of global bit allocations. The result is a simple algorithm (EZPQ) with strong approximation guarantees. It matches OPQ's empirical accuracy while providing a per-instance distortion lower bound certificate under the Gaussian EZ cost model. On typical real embedding spectra, EZPQ with 2 bits per coordinate is often certifiably within 1% of the optimum in this model. It also consistently achieves a lower reconstruction error than all random-rotation-based algorithms such as EDEN, E-RaBitQ, and TurboQuant.

---


### 50. [One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning](https://arxiv.org/abs/2611.31588)

**<font color=#1a73e8>作者：</font>** John Marangola, Antonia Bronars, Younghyo Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sim-to-real reinforcement learning (RL) has enabled impressive robotic behaviors, yet deploying policies directly from vision remains challenging. A common approach first trains a teacher policy with RL using privileged state observations, then distills its behavior into a vision-based student via imitation. However, the resulting student can substantially underperform its teacher. Directly training visual policies with RL offers a promising alternative, but learning task-relevant visual representations from scratch can be sample-inefficient, making one-phase visual RL intractable. We propose DRIFT, a simple recipe for efficient one-phase visual RL using image observations available at test time. Our key insight is to use frozen, pretrained foundation vision encoders, allowing RL to focus on learning control from existing visual representations. Freezing the encoder avoids costly backpropagation through the vision backbone, while its pretrained representations enable real-world transfer from fast, rasterized simulation rendering. Under matched architectures, observations, and compute budgets, DRIFT outperforms two-phase distillation and achieves a 58.8% relative improvement in average real-world success rate across three manipulation tasks. Controlled simulation evaluations demonstrate that DRIFT's relative advantage grows from roughly 9% in-distribution to over 61% under out-of-distribution shifts, suggesting that stronger generalization contributes to superior real-world transfer. Project website: this https URL

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
