# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 301. [How Can One Choose the Best CAM-Based Explainability Method for a CNN Model?](https://arxiv.org/abs/2605.02007)

**<font color=#1a73e8>作者：</font>** Daniel da Silva Costa, Pedro Nuno de Souza Moura, Adriana C. F. Alvim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, several advances have been observed in Deep Learning with surprising results. Models in this area have been increasingly used in numerous applications, including those sensitive to human life, which require clear explanations and justifications. Various explainability methods have been proposed, but not many metrics to evaluate these methods. The most commonly used metric is the Intersection over Union (IoU). However, due to the characteristics of the results of the explainability methods, called saliency maps, which do not have a known shape, we hypothesise that there must be a better metric that allows one to find an explainability method that produces results that best resemble the human perception. We propose using different metrics to assess the similarity between human perception and the explanation saliency maps to find a better metric. An investigation was conducted employing a subset of the Chihuahuas images from ImageNet dataset. Several CAM-based explainability methods were used to generate saliency maps for each chihuahua image. Alignment was measured by applying distance metrics between the bounding box of human annotations and the saliency maps produced by each explainability method. Rankings of the best saliency maps were created using the results of the distance metrics and compared to the ranking obtained using people's choice, collected through crowdsourcing, of the best explanation saliency maps for each selected image. Comparison between rankings was performed using the Rank-Biased Overlap (RBO) metric. The results indicate the feasibility of our method to find the explainability method that best resembles human perception. In our experiments, the two metrics that best resemble human perception corresponded to Manhattan and Correlation. Besides, the best explainability methods regarding human perception were LayerCAM, Score-CAM, and IS-CAM.

---


### 302. [Reliable AI Needs to Externalize Implicit Knowledge: A Human-AI Collaboration Perspective](https://arxiv.org/abs/2605.02010)

**<font color=#1a73e8>作者：</font>** Hengyu Liu, Tianyi Li, Zhihong Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that reliable AI requires infrastructure for human validation of implicit knowledge. AI learns from both explicit knowledge (papers, documentation, structured databases) and implicit knowledge (reasoning patterns, debugging processes, intermediate steps). Implicit knowledge remains unexternalized because documentation cost exceeds perceived value -- yet AI learns from it indiscriminately, acquiring both beneficial patterns and harmful biases. Current reliability methods can only verify explicit knowledge against sources, creating a fundamental gap: the most valuable AI capabilities (reasoning, judgment, intuition) are precisely those we cannot verify. We propose Knowledge Objects (KOs) -- structured artifacts that externalize implicit knowledge into forms humans can inspect, verify, and endorse. KOs transform verification economics: what was previously too costly to verify becomes feasible, enabling accumulated human validation to improve reliability over time.

---


### 303. [Robust and Explainable Divide-and-Conquer Learning for Intrusion Detection](https://arxiv.org/abs/2605.02015)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Kevin Hamlen, Michael De Lucia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection requires complex models to capture patterns in high-dimensional, noisy, and class-imbalanced raw network traffic, yet deploying such models remains impractical on resource-constrained devices with limited processing power and memory. In this paper, we present a correlation-aware divide-and-conquer learning technique that decomposes a complex learning problem into smaller, more manageable subproblems. This enables lightweight models as simple as decision trees to be trained on focused subtasks, yielding up to 43.3% higher local accuracy and up to 257 times reduction in model size on real-world network intrusion detection datasets, while also improving adversarial robustness and explainability.

---


### 304. [What's on Your Mind? Exploring Privacy of Mental Health Apps](https://arxiv.org/abs/2605.02016)

**<font color=#1a73e8>作者：</font>** Chloe Georgiou, Hans Lu, Emiliano De Cristofaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Therapy and life-coaching apps have been rapidly growing in number, flavors, and popularity. However, their users routinely share highly sensitive and personal information, such as traumas, fantasies, desires, relationship difficulties, and other mental health concerns. This prompts the need for an empirical analysis of privacy practices in this ecosystem, and particularly the alignment between these apps' privacy policies and their actual behavior. In this paper, we present a comprehensive analysis of 25 popular Android mental health and life-coaching apps, combining static analysis, dynamic network capture, and LLM-assisted privacy policy extraction validated against manual annotation.
Our findings highlight serious concerns and substantial transparency gaps. First, every app embeds at least one tracker SDK that its privacy policy does not name, and 68% of apps fail to disclose at least half of the trackers detected in their APKs; Talkie alone embeds 20 while naming none. Second, we identify 16 permission-policy contradictions across 13 apps, i.e., a dangerous permission is declared in the manifest but omitted from the policy, including 6 apps that request camera or microphone access without disclosing photo, video, or audio collection. Third, 48% of apps disclose third-party AI processing (e.g., via OpenAI, Anthropic, Groq), with one app sending journal entries to all three simultaneously, while 7 apps use only generic language that leaves recipients unidentified. Taken together, our findings demonstrate that current disclosure practices fall short of the transparency required for meaningful informed consent. We argue for a significantly updated regulatory framework governing therapy apps in the spirit of the professional and ethical standards that bind licensed human therapists.

---


### 305. [Tenability and Weak Semantics: Modeling Non-uniform Defense -- Extended Version](https://arxiv.org/abs/2605.02024)

**<font color=#1a73e8>作者：</font>** Uri Andrews, Luca San Mauro, John Spoerl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Dung-style abstract argumentation, various semantics capture notions of acceptability of arguments. The admissibility semantics capture the notion that an argument can be consistently defended from any potential counterargument. Weak semantics often relax the demands of admissibility by restricting which counterarguments must be taken seriously (e.g., discounting self-defeating or otherwise incoherent attacks). Many prominent proposals for weak semantics remain extension-based in a stronger sense. While these semantics discount attacks from arguments which are considered unreasonable, they still require a uniform defense against all reasonable arguments, even if they are collectively inconsistent. This uniformity can be too demanding when defensibility is inherently strategic, and thus the appropriate reply depends on the opponent's line of attack.
We introduce tenability, a family of dialogue-based semantics that formalize when a designated argument (or a set of arguments) can be maintained in debate by a proponent against any conflict-free attack which the opponent may present. The approach is motivated by three natural benchmark patterns: self-defeating attack, floating assignment, and disjunctive reinstatement, on which tenability behaves differently from all weak semantics previously considered in the literature. We define three variants -- static tenability, tenability, and strong tenability -- via monotone commitment games over finite conflict-free moves, differing in the obligations imposed on the disputants. We establish the relative strength of these notions, prove implications and separations with previously studied weak semantics, and we analyze computational complexity on finite frameworks: deciding static tenability is $\Pi^P_2$-complete, while deciding tenability and strong tenability is PSPACE-complete.

---


### 306. [Towards Systematic Generalization for Power Grid Optimization Problems](https://arxiv.org/abs/2605.02026)

**<font color=#1a73e8>作者：</font>** Zeeshan Memon, Yijiang Li, Hongwei Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AC Optimal Power Flow (ACOPF) and Security-Constrained Unit Commitment (SCUC) are fundamental optimization problems in power system operations. ACOPF serves as the physical backbone of grid simulation and real-time operation, enforcing nonlinear power flow feasibility and network limits, while SCUC represents a core market-level decision process that schedules generation under operational and security constraints. Although these problems share the same underlying transmission network and physical laws, they differ in decision variables and temporal coupling, and prior learning-based approaches address them in isolation, resulting in disjoint models and this http URL propose a learning framework that jointly models ACOPF and SCUC through a shared graph-based backbone that captures grid topology and physical interactions, coupled with task-specific decoders for static and temporal decision-making. Training includes solver supervision with physics-informed objectives to enforce AC feasibility and inter-temporal operational constraints. To evaluate generalization, we assess cross-case transfer on unseen grid topologies for ACOPF and SCUC without retraining, and systematic generalization on the UC-ACOPF problem using unsupervised, physics-based objectives and a power-dispatch consensus mechanism. Experiments across multiple grid scales demonstrate improved performance and transferability relative to existing learning-based baselines, indicating that the model can support learning across heterogeneous power system optimization problems.

---


### 307. [Large margin classifier with graph-based adaptive regularization](https://arxiv.org/abs/2605.02027)

**<font color=#1a73e8>作者：</font>** Vítor M. Hanriot, Turíbio T. Salis, Luiz C.B. Torres 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces the use of per-class regularization hyperparameters in Gabriel graph-based binary classifiers. We demonstrate how the quality index used for regularization behaves both in the margin region and in the presence of outliers, and how incorporating this regularization flexibility can lead to solutions that effectively eliminate outliers while training the classifier. We also show how it can address class imbalance by generating higher and lower thresholds for the majority and minority classes, respectively. Thus, rather than having a single solution based on fixed thresholds, flexible thresholds expand the solution space and can be optimized through hyperparameter tuning algorithms. Friedman test shows that flexible thresholds are capable of improving Gabriel graph-based classifiers.

---


### 308. [TIJERE: A Novel Threat Intelligence Joint Extraction Model Based on Analyst Expert Knowledge](https://arxiv.org/abs/2605.02041)

**<font color=#1a73e8>作者：</font>** Inoussa Mouiche, Sherif Saad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The extraction of entities and relationships from threat intelligence reports into structured formats, such as cybersecurity knowledge graphs, is essential for automated threat analysis, detection, and mitigation. However, existing joint extraction methods struggle with feature confusion, language ambiguity, noise propagation, and overlapping relations, resulting in low accuracy and poor model performance. This paper presents TIJERE, an innovative joint entity and relation extraction framework that formulates joint extraction as a multisequence labeling representation (MSLR) problem. Specifically, separate sequences are generated for each entity pair. Unlike prior tagging schemes, MSLR integrates expert domain features to enrich positional, contextual, and semantic representations of entities, thereby enhancing feature distinction and classification accuracy. Additionally, TIJERE reduces language ambiguity and enhances domain-specific generalization by leveraging SecureBERT+, a contextual language model fine-tuned on cybersecurity text. This improves both named entity recognition (NER) and relation extraction (RE). This paper also introduces DNRTI-JE, the first publicly available jointly labeled dataset for cybersecurity entity and RE, filling a crucial gap in cyber threat intelligence automation. Empirical evaluations on the curated DNRTI-JE dataset demonstrate that TIJERE achieves state-of-the-art performance, with F1-scores exceeding 0.93 for NER and 0.98 for RE, outperforming existing methods. Together, TIJERE and the standardized benchmarking DNRTI-JE dataset enable high-performance cybersecurity intelligence extraction, with transferable applications in healthcare, finance, and bioinformatics.

---


### 309. [Bringing Order to Asynchronous SGD: Towards Optimality under Data-Dependent Delays with Momentum](https://arxiv.org/abs/2605.02043)

**<font color=#1a73e8>作者：</font>** Tehila Dahan, Roie Reshef, Sharon Goldstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous stochastic gradient descent (SGD) enables scalable distributed training but suffers from gradient staleness. Existing mitigation strategies, such as delay-adaptive learning rates and staleness-aware filtering, typically attenuate or discard delayed gradients, introducing systematic bias: updates from simpler or faster-to-process samples are overrepresented, while gradients from more complex samples are delayed or suppressed. In contrast, prior approaches to data-dependent delays rely on a Lipschitz assumption that yields suboptimal rates or leave the smooth, convex case unaddressed. We propose a momentum-based asynchronous framework designed to preserve information from delayed gradients while mitigating the effects of staleness. We establish the first optimal convergence rates for data-dependent delays in both convex and non-convex smooth setups, providing a new result for asynchronous optimization under standard assumptions. Additionally, we derive robust learning-rate schedules that simplify hyperparameter tuning in practice.

---


### 310. [NeuroViz: Real-time Interactive Visualization of Forward and Backward Passes in Neural Network Training](https://arxiv.org/abs/2605.02044)

**<font color=#1a73e8>作者：</font>** Reza Rawassizadeh, Tanvi Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training neural networks is difficult to interpret, particularly for newcomers. We introduce NeuroViz, an interactive visualization tool that supports real-time exploration of fully connected neural network training. Users can configure network architecture, activation functions, learning rates, and datasets, then observe activations, weight updates, and loss progression. NeuroViz visualizes weight changes in direct correspondence with activation signals in both forward and backward passes, enabling users to distinguish pre- and post-update states within individual epochs and view dynamically updating per-neuron equations. We conduct a comparative user study with 31 participants against six established visualization tools and we achieved the highest usability score (SUS 80.97, in the 'excellent' range), with mean rankings of 2.47 for clarity and 2.23 for usefulness (lower is better). Over 70% of participants reported that the visualizations substantially increased their perception of neural network training transparency. The implemented instance is accessible at this https URL.

---


### 311. [Methods, Data, and Conceptual Change: Reflections from Two Quantitative Diachronic Case Studies](https://arxiv.org/abs/2605.02052)

**<font color=#1a73e8>作者：</font>** Catherine Wong, Bach Phan-Tat, Susan Fitzmaurice  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This discussion paper reflects on how quantitative approaches to historical linguistics interact with dataset properties. Drawing on two worked examples, we examine English data using quad-based concept modelling of Early Modern English discourse in EEBO-TCP (c. 1470s-1690s; 765M words) alongside SynFlow analysis of scientific writing in Royal Society Corpus 6.0.4 (1750-1799; drawn from a 78.6M-token open corpus). Through parallel comparison, the paper explores how each approach operationalises concepts, the data assumptions they entail, and the diachronic interpretations they support. We argue that comparative methodological reflection clarifies the limits of purely lexical, frequency-based approaches and highlights how dataset structure shapes the kinds of semantic change that quantitative methods can reliably detect.

---


### 312. [DR-SNE: Density-Regularized Stochastic Neighbor Embedding](https://arxiv.org/abs/2605.02060)

**<font color=#1a73e8>作者：</font>** Maksim Kazanskii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction methods such as t-SNE are designed to preserve local neighborhood structure but do not explicitly account for how probability mass is distributed, often leading to distortions of data density. We reformulate dimensionality reduction as the joint alignment of two components: (i) conditional structure, capturing local relationships, and (ii) relative density structure, captured via local density statistics. Based on this perspective, we introduce Density-Regularized SNE (DR-SNE), which augments the stochastic neighbor embedding objective with a density regularization term derived from normalized log-density estimates. Unlike prior approaches such as DensMAP and DenSNE, which rely on local scale consistency, DR-SNE directly aligns normalized density estimates, providing a simple and scale-invariant mechanism for preserving relative density variations. Empirically, DR-SNE improves density preservation while maintaining competitive neighborhood fidelity, and yields gains on density-sensitive tasks such as anomaly detection across multiple datasets. These results suggest that incorporating density information complements geometry-focused objectives in dimensionality reduction.

---


### 313. [Coopetition-Gym v1: A Formally Grounded Platform for Mixed-Motive Multi-Agent Reinforcement Learning under Strategic Coopetition](https://arxiv.org/abs/2605.02063)

**<font color=#1a73e8>作者：</font>** Vik Pant, Eric Yu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present Coopetition-Gym v1, a benchmark platform for mixed-motive multi-agent reinforcement learning under strategic coopetition. The platform comprises twenty environments organized into four mechanism classes that correspond to four foundational technical reports: interdependence and complementarity (arXiv:2510.18802), trust and reputation dynamics (arXiv:2510.24909), collective action and loyalty (arXiv:2601.16237), and sequential interaction and reciprocity (arXiv:2604.01240). Each environment carries a closed-form payoff structure and a calibrated interdependence matrix derived from the corresponding report.
Every environment exposes a parameterized reward layer configurable across three structurally distinct modes (private, integrated, cooperative). This separation of payoff from reward enables reward-type ablation, the platform's principal methodological apparatus. Four of the twenty environments are calibrated against historically documented coopetitive relationships and reproduce their outcomes at 98.3, 81.7, 86.7, and 87.3 percent on the validation rubric (Samsung-Sony LCD, Renault-Nissan Alliance, Apache HTTP Server, Apple iOS App Store).
The platform exposes Gymnasium, PettingZoo Parallel, and PettingZoo AEC interfaces and ships 126 reference algorithms: 16 learning algorithms, 7 game-theoretic oracles, 2 heuristic baselines, and 101 constant-action policies. A reference experimental study trained the 16 learning algorithms on every environment under every reward configuration with seven random seeds, producing a 25,708-run training corpus and a 1,116-run behavioral audit corpus, both released under CC-BY-4.0 with Croissant 1.0 metadata. Coopetition-Gym v1 is the first platform to combine continuous-action mixed-motive environments, parameterized reward mutuality, calibrated interdependence coefficients, game-theoretic oracle baselines, and validated case studies.

---


### 314. [Weight Clipping for Robust Conformal Inference under Unbounded Covariate Shifts](https://arxiv.org/abs/2605.02072)

**<font color=#1a73e8>作者：</font>** James Wang, Surbhi Goel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) provides powerful, distribution-free prediction sets, but its guarantees rely on the exchangeability of training and test data, which is often violated in practice due to covariate shifts. While weighted conformal prediction (WCP) is designed to handle such shifts, it can suffer from significant undercoverage when the density ratio between the distributions is unbounded and/or must be learned. This is because of both overfitting in learning the density ratio, and high variance in estimating the nonconformity score threshold. To address this, we introduce clipped least-squares importance fitting (CLISF) as a reduced-variance method for density ratio estimation. Specifically, we show that density ratios learned using CLISF, when plugged into WCP, have bounded expected undercoverage. Furthermore, we show that the undercoverage can be corrected by running WCP with a slightly inflated coverage target; crucially, we are able to estimate the required level of inflation from the data. We provide the first theoretical guarantees for weight clipping in conformal inference, achieving dataset-conditional coverage with a sample complexity that does not blow up with the higher moments of the true density ratio -- a key limitation of prior work. We verify our results on real-world benchmarks and synthetic data.

---


### 315. [Obscura: Privacy-Preserving Protocol for the Algorand Blockchain Using LSAG Ring Signatures](https://arxiv.org/abs/2605.02077)

**<font color=#1a73e8>作者：</font>** Navid Azimi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While public blockchains provide transparent and auditable transaction histories, they inherently compromise user privacy. Existing privacy-enhancing protocols, such as those deployed on Ethereum, typically rely on succinct zero-knowledge proofs (zk-SNARKs) to obscure the transaction graph. However, implementing comparable cryptographic guarantees on high-throughput blockchains like Algorand is challenging due to strict per-call execution budgets and the state contention introduced by global Merkle accumulators. This paper presents Obscura, a decentralized, non-custodial privacy protocol tailored for constrained smart contract environments. Obscura achieves transaction anonymity using Linkable Spontaneous Anonymous Group (LSAG) signatures over the BN254 elliptic curve, verified entirely on-chain. To overcome limitations of the Algorand Virtual Machine (AVM), we introduce a novel state model that leverages Algorand's Box Storage for $O(1)$ commitment membership checks, eliminating the need for global Merkle accumulators, and a dynamic opcode-budget expansion mechanism via pooled inner application calls. Our implementation demonstrates that signer-ambiguous privacy is practical and efficient on Algorand without relying on trusted setups or succinct proofs. Obscura provides a robust privacy layer for transparent ledgers, bridging the gap between high-throughput blockchain architectures and the dual requirements of cryptographic privacy and selective auditability.

---


### 316. [Cripping AI: Reimagining AI Through Lived Disability Experiences](https://arxiv.org/abs/2605.02080)

**<font color=#1a73e8>作者：</font>** Xinru Tang, Ting-an Lin, Jingjin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Drawing on crip theory, this paper proposes cripping AI as a guiding framework to center lived disability experiences in AI research and development. Moving beyond calls to make AI "accessible" to people with disabilities, cripping AI seeks to: (1) reveal and dismantle ableist assumptions embedded in how AI is imagined, designed, and evaluated; (2) center disabled ways of knowing (i.e., cripistemologies); (3) respect disabled labor in co-creating accessible practices. We demonstrate how to apply our framework with three cases: deafness and sign language AI, blindness and visual assistive AI, and stuttering and speech AI. We end by outlining three directions for future work, including cripping AI with diverse human bodyminds, across the entire AI pipeline and ecosystem, and in collaboration with other justice-oriented AI efforts.

---


### 317. [EditPropBench: Measuring Factual Edit Propagation in Scientific Manuscripts](https://arxiv.org/abs/2605.02083)

**<font color=#1a73e8>作者：</font>** Garvin Kruthof  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Local factual edits in scientific manuscripts often create non-local revision obligations. If a dataset changes from 215 to 80 documents, claims such as 'medium-scale' or 'a few hundred items' may also become stale, even though they do not repeat the edited number. We introduce EditPropBench, a benchmark for measuring whether LLM editors propagate factual edits through dependent manuscript claims. Each item contains an ML/NLP-style synthetic manuscript, a targeted edit, and a controlled fact graph with sentence-level labels for direct targets, required downstream updates, and protected unrelated text. EditPropBench provides a controlled manuscript-level benchmark with sentence-level dependency supervision, three editing protocols, adversarial metric probes, stress-test variants, and a metric suite centered on Edit-Ripple Adherence (ERA). On the hard implicit/free-form stratum, five LLM editing systems span ERA 0.148--0.705; even the strongest misses roughly 30% of required cascade updates. A mixed-stratum stress test shows that LLMs retain a positive advantage over deterministic substitution baselines when easy substitution-solvable cases are included. Finally, an audit of recent arXiv cs.CL benchmark and dataset papers finds fact-dependent qualitative claims in 37.2% of papers. EditPropBench shows that current LLM editors can repair many implicit consequences of factual edits, but reliable scientific revision still requires cascade-aware checking.

---


### 318. [GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086)

**<font color=#1a73e8>作者：</font>** Baobing Zhang, Wanxin Sui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian splatting (3DGS) is a state-of-the-art representation for real-time photorealistic novel-view synthesis, yet a single high-fidelity scene typically occupies hundreds of megabytes to several gigabytes, exceeding the budgets of mobile, immersive, and volumetric video platforms. Existing 3DGS compression methods (e.g., HAC++, FlexGaussian, LP-3DGS) treat pruning, quantization, and entropy coding as separate stages and rely on hand-tuned heuristics (opacity thresholds, fixed bit-widths, SH truncation), limiting cross-scene generalization and preventing users from specifying a target rate or quality budget. We propose GETA-3DGS, to our knowledge the first end-to-end automatic joint structured pruning and quantization framework for 3DGS. Building on GETA for joint pruning-quantization of deep networks, we contribute: (i) a 3DGS-aware quantization-aware dependency graph (QADG) treating each Gaussian primitive as a group with five attribute sub-nodes and degree-aware SH sub-nodes; (ii) a render-aware saliency fusing transmittance-weighted contribution, screen-space gradient, and pixel coverage into a Gaussian-level importance score; and (iii) a heterogeneous per-attribute mixed-precision scheme co-optimized with structural sparsity under a projected partial saliency-guided (PPSG) descent guarantee. On Mip-NeRF 360, Tanks and Temples, and Deep Blending, GETA-3DGS operates directly on raw Gaussian primitives rather than a post-hoc anchor representation, delivering ~5x storage reduction over Vanilla 3DGS with no per-scene thresholds. Bit-width policy is the dominant rate-distortion lever: a uniform 6-bit cap costs up to -6.74 dB on view-dependent scenes versus our heterogeneous allocation, matching an information-theoretic reverse-water-filling analysis we develop. GETA-3DGS is complementary to existing codecs: entropy coding (HAC++, CompGS) is downstream, so the two can be composed.

---


### 319. [Cross-Language Learning within Arabic Script for Low-Resource HTR](https://arxiv.org/abs/2605.02089)

**<font color=#1a73e8>作者：</font>** Sana Al-azzawi, Elisa Barney, Marcus Liwicki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten Text Recognition (HTR) under limited labeled data remains a challenging problem, particularly for Arabic-script languages. Although modern sequence-based recognizers perform well in high-resource settings, their accuracy degrades sharply as training data becomes scarce. Arabic-script languages share a common writing system with substantial character overlap, motivating cross-script training as a strategy to mitigate data scarcity. We performed experiments on Arabic, Urdu, and Persian scripts and achieved improvements over single-script baselines (new SotA especially for low-resource settings). A key finding of our experiments is that cross-script transfer is largely driven by script-level overlap rather than uniform accuracy improvements. Through a statistical character-level analysis we show that gains are structurally concentrated on characters shared across scripts, while language-specific characters exhibit limited or negative transfer. These findings provide insight into transfer dynamics in low-resource script families. Detailed results include: We conduct a controlled line-level study of cross-script joint training for Arabic-script HTR under low-resource regimes (number of samples K \in 100, 500, 1000 labeled lines) on Arabic (KHATT), Urdu (NUST-UHWR), and Persian (PHTD). A CRNN model is trained on the union of multiple related Arabic-script datasets and evaluated on individual target languages. On Persian (PHTD), joint training achieves a Character Error Rate (CER) of 9.99, surpassing previously reported results despite not using the full available training data. On an Urdu dataset (UNHD), joint training reduces CER from 17.20 to 14.45. Code and data splits are released to ensure reproducibility.1

---


### 320. [NORA: A Harness-Engineered Autonomous Research Agent for End-to-End Spatial Data Science](https://arxiv.org/abs/2605.02092)

**<font color=#1a73e8>作者：</font>** Bing Zhou, Xiao Huang, Huan Ning 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The automation of scientific research workflows has emerged as a transformative frontier in artificial intelligence, yet existing autonomous research agents remain largely domain-agnostic, lacking the specialized reasoning, method selection, and data acquisition capabilities required for rigorous spatial data science. This paper introduces NORA (Night Owl Research Agent), a harness-engineered, multi-agent autonomous research system purpose-built for GIScience and spatial data science. NORA orchestrates the complete research lifecycle through a skills-first architecture comprising 21 domain-specialized workflow skills, 9 specialist sub-agents, and custom Model Context Protocol (MCP) servers. Central to the system's design are two novel domain-specialized skills: a spatial analysis skill unit that encodes decision frameworks for exploratory spatial data analysis, spatial regression, and diagnostics; and a spatial data download skill that supports reproducible acquisition from authoritative geospatial data sources. We formalize the concept of harness engineering for scientific research agents, demonstrating how lifecycle hooks, safety gates, generator-evaluator separation, human-in-the-loop, and state persistence ensure reliable and reproducible autonomous research. We evaluate NORA through case studies by 6 domain specialists and 3 LLM reviewers across seven dimensions (novelty, quality, rigor, etc). Results demonstrate that domain-specialized harness engineering substantially improves the efficiency and quality of research output compared to general-purpose agent configurations.

---


### 321. [SignMAE: Segmentation-Driven Self-Supervised Learning for Sign Language Recognition](https://arxiv.org/abs/2605.02094)

**<font color=#1a73e8>作者：</font>** Kunyuan Xie, Zhixi Cai, Kalin Stefanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subtle hand differences make sign language recognition challenging, yet many existing methods rely on encoders pretrained on generic action datasets that poorly capture such fine-grained cues. We propose a self-supervised pretraining method for sign language recognition that uses segmentation-based masking to adapt to the presence and motion of key body parts, rather than treating hand poses as static visual tokens. The resulting mask-and-reconstruct objective improves fine-grained sign representation learning. On WLASL, NMFs-CSL, and Slovo, our encoder achieves state-of-the-art performance, improving per-instance and per-class Top-1 accuracy while using fewer input frames and modalities than comparable encoders.

---


### 322. [From Spherical to Gaussian: A Comparative Analysis of Point Cloud Cropping Strategies in Large-Scale 3D Environments](https://arxiv.org/abs/2605.02098)

**<font color=#1a73e8>作者：</font>** Maximilian Kellner, Dominik Merkle, Michael Brunklaus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale 3D point clouds can consist of billions of points. Even after downsampling, these point clouds are too large for modern 3D neural networks. In order to develop a semantic understanding of the scene, the point clouds are divided into smaller subclouds that can be processed. Typically, this division is done using spherical crops, resulting in a loss of surrounding geometric context. To address this issue, we propose alternative methods that produce subclouds with larger crop sizes while maintaining a similar number of points. Specifically, we compare exponential, Gaussian, and linear cropping methods with the spherical method. We evaluated two 3D deep learning model architectures using multiple indoor and outdoor environment datasets. Our results demonstrate that altering the cropping strategy can enhance model performance, especially for large-scale outdoor scenes, yielding new state-of-the-art results. Code is available at this https URL

---


### 323. [Stochastic Modeling of Human-Machine Authentication Channels under Partial Information Leakage](https://arxiv.org/abs/2605.02102)

**<font color=#1a73e8>作者：</font>** Nilesh Chakraborty, Mohammad Zulkernine, Burak Kantarci  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable and secure human-machine communication is fundamental to IoT and cyber-physical ecosystems, where smartphones and wearables commonly serve as authentication controllers. PIN-based authentication can be viewed as a low-bandwidth communication channel through which users transmit numeric credentials under practical constraints. However, conventional evaluations adopt a binary view of security-treating such channels as either fully secure or fully compromised-thereby overlooking the progressive reliability degradation caused by partial information leakage in real-world IoT settings. In this paper, we model the PIN entry process as a stochastic human-IoT communication system and propose a context-conditioned probabilistic inference framework to quantify reliability loss and Quality-of-Service degradation under partial symbol exposure. The proposed approach treats missing digits as latent variables and estimates them using smoothed conditional probability distributions with fallback priors. Unlike traditional sequential models that assume contiguous positional dependencies, the method does not explicitly parameterize hidden-state transitions or emissions; instead, it performs context-driven probabilistic inference to approximate latent dependencies across digit positions. Using over one million real-world four-digit PIN samples, we evaluate single-, double-, and triple-digit leakage scenarios and derive position-dependent reliability metrics. The proposed model achieves up to 55.31% prediction accuracy for one missing digit and 12.12% for three missing digits, while consistently outperforming a standard sequence-model baseline and classical machine learning models in terms of precision, recall, and F1-score. These results formalize PIN entry as a noisy human--IoT communication channel and demonstrate substantial reliability degradation under realistic partial exposure conditions.

---


### 324. [Sharpness-Aware Pretraining Mitigates Catastrophic Forgetting](https://arxiv.org/abs/2605.02105)

**<font color=#1a73e8>作者：</font>** Ishaan Watts, Catherine Li, Sachin Goyal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining optimizers are tuned to produce the strongest possible base model, on the assumption that a stronger starting point yields a stronger model after subsequent changes like post-training and quantization. This overlooks the geometry of the base model which controls how much of the base model's capabilities survive subsequent parameter updates. We study three pretraining optimization approaches that bias optimization toward flatter minima: Sharpness-Aware Minimization (SAM), large learning rates, and shortened learning rate annealing periods. Across model sizes ranging from 20M to 150M parameters, we find that these interventions consistently improve downstream performance after post-training on five common datasets with up to 80% less forgetting. These principles hold at scale: a short SAM mid-training phase applied to an existing OLMo-2-1B checkpoint reduces forgetting by 31% after MetaMath post-training and by 40% after 4-bit quantization.

---


### 325. [The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence](https://arxiv.org/abs/2605.02106)

**<font color=#1a73e8>作者：</font>** Terry Dorsey, Kevin Huggins  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemporary artificial intelligence systems achieve strong performance through large-scale parameterization, retrieval augmentation, and training on extensive static corpora. Despite these advances, they continue to face limitations in persistent memory, temporal grounding, provenance, and interpretability. These challenges are especially pronounced in large language models, where experience is encoded implicitly in fixed parameters, limiting the ability to preserve, inspect, and reinterpret past interactions over time.
This paper establishes a memory-centric architectural foundation for artificial intelligence in which experience is represented explicitly and persistently to support temporal grounding, provenance, and interpretability. It proposes an alternative to parameter-centric approaches by treating memory as a first-class, structured substrate for reasoning.
We introduce the Dynamic Gist-Based Memory Model (DGMM), an architecture in which experience is represented as an evolving, graph-structured episodic-semantic memory. DGMM encodes experience as interconnected conceptual structures grounded in time, source, and interaction context, and defines selective, cue-conditioned recall as the mechanism for constructing working memory. A formal schema and architectural invariants are provided based on additive memory growth and recall-conditioned interpretation.
The results specify properties of DGMM, including episodic persistence, locality of cue-conditioned surprise, and contextual variability without structural modification of stored memory. DGMM provides a coherent architectural theory in which memory is explicit and persistent, supporting evolving interpretation without retraining and enabling interpretable, context-aware, and temporally grounded AI systems.

---


### 326. [Geometric and Spectral Alignment for Deep Neural Network I](https://arxiv.org/abs/2605.02108)

**<font color=#1a73e8>作者：</font>** Ziran Liu, Wei Wang, Jinhao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep residual architectures are modeled as products of near-identity Jacobians. This paper proves deterministic quotient-geometric estimates for singular spectra of Frobenius-normalized layer factors, emphasizing a normalized top-radial Cartan coordinate and fitted power-law chart.
Full-rank factors are mapped from $\mathrm{GL}(d)$ to the positive cone by $A\mapsto A^\top A$, then to ordered eigenvalue data. Under Frobenius normalization, exact power-law spectra form a trace-normalized Cartan orbit. This orbit is a Gibbs family on ranks, a Fisher information line, and a Bures--Wasserstein curve with line element $d/4$ times Fisher information.
The main rigidity theorem is a slack-aware margin inequality: interface radial amplitude, non-backtracking slack, and signed residual variation control displacement of the fitted Cartan coordinate. In the exact-chart zero-slack case, a depth-$L$ budget gives exponent drift of order $(\log M)/L$; generally, slack and residual increments augment the bound.
We separate scalar top-radial from full-Cartan spectral control, which also needs Bures/Hellinger residual variation. We prove approximate-power-law and metric-chart versions, converse lower bounds, Fisher--KL/Bures action estimates, and near-identity expansions for normalized residual chains.
Near-identity results verify transport budgets; chart quality remains measurable. Effective rank is a spectral-energy quantile, giving finite-width power-law tail bounds and robust rank-window transition estimates. Empirical static-weight exponent profiles serve as diagnostics; full verification also requires interface budgets, slacks, and residuals for the same operator chain.

---


### 327. [Detecting Adversarial Data via Provable Adversarial Noise Amplification](https://arxiv.org/abs/2605.02109)

**<font color=#1a73e8>作者：</font>** Furkan Mumcu, Yasin Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The nonuniform and growing impact of adversarial noise across the layers of deep neural networks has been used in the literature, without a formal mathematical justification, to detect adversarial inputs and improve robustness. In this work, we study this phenomenon in detail and present a formal adversarial noise amplification theorem. We specify a set of sufficient conditions under which the adversarial noise amplification is mathematically guaranteed. Based on theoretical observations, we propose a novel training methodology with a custom spectral loss function and a specific architectural design to enhance the amplification signal for detecting adversarial data. Finally, we introduce a new, lightweight detection mechanism that leverages the enhanced amplification signal and operates entirely at inference time. To validate our approach, we demonstrate the detector's efficacy against both state-of-the-art attacks and a purpose-built adaptive attack, confirming that enhanced amplification can serve as a robust and reliable signal for adversarial defense.

---


### 328. [Adversarial Update-Based Federated Unlearning for Poisoned Model Recovery](https://arxiv.org/abs/2605.02110)

**<font color=#1a73e8>作者：</font>** Wenwei Zhao, Xiaowen Li, Yao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is vulnerable to poisoning attacks, where malicious clients upload manipulated updates to degrade the performance of the global model. Although detection methods can identify and remove malicious clients, the model remains affected. Retraining from scratch is effective but costly, and existing unlearning methods remain unsatisfactory in both effectiveness and efficiency. We propose Federated Adversarial Unlearning (FAUN), a lightweight framework that retains only a short window of malicious clients' updates and employs adversarial optimization on a proxy dataset to derive updates that eliminate malicious directions. Applying these updates for a few unlearning rounds, followed by benign fine-tuning, enables fast removal of malicious effects and stable recovery. Experiments on three canonical datasets show that FAUN achieves recovery comparable to retraining while requiring far fewer rounds and reduces attack success rates to near zero, confirming FAUN successfully eliminates the contributions of unlearned clients.

---


### 329. [Statistical Consistency and Generalization of Contrastive Representation Learning](https://arxiv.org/abs/2605.02116)

**<font color=#1a73e8>作者：</font>** Yuanfan Li, Xiyuan Wei, Tianbao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive representation learning (CRL) underpins many modern foundation models. Despite recent theoretical progress, existing analyses suffer from several key limitations: (i) the statistical consistency of CRL remains poorly understood; (ii) available generalization bounds deteriorate as the number of negative samples increases, contradicting the empirical benefits of large negative sets; and (iii) the retrieval performance of CRL has received limited theoretical attention.
In this paper, we develop a unified statistical learning theory for CRL. For downstream tasks, we evaluate retrieval quality using an AUC-type population criterion and show that the contrastive loss is \emph{statistically consistent} with optimal ranking. We further establish a \emph{calibration-style inequality} that quantitatively relates excess contrastive risk to excess retrieval suboptimality. For upstream training, we study both supervised and self-supervised contrastive objectives and derive generalization bounds of order $O(1/m + 1/\sqrt{n})$ and $O(1/\sqrt{m} + 1/\sqrt{n})$, respectively, where $m$ denotes the number of negative samples and $n$ the number of anchor points. These bounds not only explain the empirical advantages of large negative sets but also reveal an explicit trade-off between $m$ and $n$. Extensive experiments on large-scale vision--language models corroborate our theoretical predictions.

---


### 330. [Reinforcement Learning Trained Observer Control for Bearings-Only Tracking](https://arxiv.org/abs/2605.02120)

**<font color=#1a73e8>作者：</font>** Branko Ristic, Sanjeev Arulampalam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops a deep reinforcement learning based observer control policy for autonomous bearings-only tracking of a moving target. The observer manoeuvre problem is formulated as a belief Markov decision process, where the belief state is represented by the posterior of a cubature Kalman filter (CKF). The reward function is designed to address two conflicting objectives: minimising the absolute target position estimation error (Euclidean distance) and maintaining CKF estimation consistency (Mahalanobis distance). The reward is formulated as a geometric interpolation between the two objectives on the Pareto front, parametrised by a weighting factor $\beta \in [0,1]$. The policy is implemented as a deep Q-network (DQN) trained over 50,000 episodes. Performance is evaluated over 5,000 Monte Carlo episodes and compared against two baselines: the perpendicular-to-bearing heuristic and the D-optimal Fisher information maximisation criterion. The results show that the DQN policy at $\beta = 0.7$ achieves the best trade-off between accuracy and robustness: it matches the information-theoretic baseline on mean tracking accuracy while reducing the worst-case error by nearly a factor of ten, owing to the implicit filter-consistency regularisation provided by the Mahalanobis term in the reward.

---


### 331. [SCRIBE: Practical Static Binary Patching via Binary-Aware Recompilation of Decompiled Code](https://arxiv.org/abs/2605.02121)

**<font color=#1a73e8>作者：</font>** Han Dai, Soumyakant Priyadarshan, Abdullah Imran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When source code or the original toolchain is unavailable, patching binaries is difficult because it requires editing low-level assembly code directly. As an alternative, one can decompile the binary, apply the patch at the source level, and then recompile the modified code. However, as this paper demonstrates, this workflow is hindered by pervasive syntactic and semantic inaccuracies in the output of modern decompilers, many of which prior work has overlooked. To address these challenges, we present SCRIBE, a patching framework that handles syntactic and semantic issues in decompiled code, improving both recompilation success and correctness. SCRIBE's novel "binary-aware" recompilation approach repairs semantic inaccuracies in decompiler output by leveraging information extracted directly from the original binary. In our evaluation, SCRIBE resolved approximately 81% of previously incorrect functions produced by the Hex-Rays decompiler, demonstrating the effectiveness of its approach. Moreover, we show that, using SCRIBE, it is possible to patch 13 of 14 real-world CVEs without access to the original source code and without performing any manual binary editing. To further validate our findings, we conducted a user study with 18 participants. Using SCRIBE, participants achieved 100% patching success, compared to 3.7% without it. Finally, we asked three large language models to generate source-level patches via SCRIBE; all three achieved 100% success when using the framework, demonstrating its potential to enable fully automated patching. Overall, these results indicate that SCRIBE makes source-level patching of binaries accessible and reliable, even without access to the original source.

---


### 332. [STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems](https://arxiv.org/abs/2605.02122)

**<font color=#1a73e8>作者：</font>** Akash Bonagiri, Gerard Janno Anderias, Saee Patil 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human evaluation remains the primary standard for assessing modern AI systems, yet annotator disagreement, bias, and variability make system rankings fragile under standard majority vote aggregation. Majority vote discards annotator reliability and item-level ambiguity, often yielding unstable comparisons across annotator subsets. We introduce STABLEVAL, a disagreement-aware evaluation framework that models latent item correctness and annotator-specific confusion patterns to produce posterior expected item credit and calibrated agent-level scores. Unlike label-denoising approaches such as Dawid-Skene, STABLEVAL is explicitly designed for stable and uncertainty-aware system evaluation rather than hard label recovery. We formalize ranking stability as a first-class evaluation objective and analyze how aggregation methods preserve or distort underlying annotator behavior. Across controlled synthetic experiments and multiple real-world human-annotated benchmarks, majority vote exhibits increasing score error and ranking instability under annotator heterogeneity and adversarial noise, while STABLEVAL yields more stable and statistically grounded system rankings. These results demonstrate that modeling disagreement is essential for robust and reproducible AI evaluation.

---


### 333. [Boundary Mass and the Soft-to-Hard Limit in Mixture-of-Experts](https://arxiv.org/abs/2605.02124)

**<font color=#1a73e8>作者：</font>** Reza Rastegar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax-routed mixture-of-experts models approach hard routing as the temperature tends to zero, but this limit is singular near routing ties. This paper studies that singularity at the population level for squared-loss MoE regression. The central object is the \emph{boundary mass}, namely the probability that the top two router scores are separated by only a small margin. Under smoothness and transversality assumptions on the router and input law, we prove coarea/tube estimates showing that this mass is linear in the slab width, with leading constant given by a surface integral over the routing interface in the binary case. These estimates yield quantitative soft-to-hard risk bounds and, under compactness and uniform margin control, $\Gamma$-convergence of the soft objectives to the hard-routing objective. The main conclusion is that the zero-temperature limit is controlled by a thin geometric layer around routing interfaces, not by the full input space. We then use this geometric core in two more model-dependent directions. In a teacher--student setting, we prove a conditional landscape-transfer principle showing that, when the profiled hard-routing problem has favorable identifiability and curvature and the relevant derivatives transfer at boundary-layer scale, small-temperature soft routing inherits approximate teacher recovery and strict-saddle behavior away from teacher-equivalent partitions. We also give a reduced two-expert Gaussian calculation that illustrates a local symmetry-breaking mechanism aligned with the teacher separator.

---


### 334. [Video Generation with Predictive Latents](https://arxiv.org/abs/2605.02134)

**<font color=#1a73e8>作者：</font>** Yian Zhao, Feng Wang, Qiushan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Variational Autoencoder (VAE) enables latent video generative modeling by mapping the visual world into compact spatiotemporal latent spaces, improving training efficiency and stability. While existing video VAEs achieve commendable reconstruction quality, continued optimization of reconstruction does not necessarily translate into improved generative performance. How to enhance the diffusability of video latents remains a critical and unresolved challenge. In this work, inspired by principles of predictive world modeling, we investigate the potential of predictive learning to improve the video generative modeling. To this end, we introduce a simple and effective predictive reconstruction objective that unifies predictive learning with video reconstruction. Specifically, we randomly discard future frames and encode only partial past observations, while training the decoder to reconstruct the observed frames and predict future ones simultaneously. This design encourages the latent space to encode temporally predictive structures and build a more coherent understanding of video dynamics, thereby improving generation quality. Our model, termed Predictive Video VAE (PV-VAE), achieves superior performance on video generation, with 52% faster convergence and a 34.42 FVD improvement over the Wan2.2 VAE on UCF101. Furthermore, comprehensive analyses demonstrate that PV-VAE not only exhibits favorable scalability, with generative performance improving alongside VAE training, but also yields consistent gains in downstream video understanding, underscoring a latent space that effectively captures temporal coherence and motion priors.

---


### 335. [FLoRA: Fusion-Latent for Optical Reconstruction and Flood Area Segmentation via Cross-Modal Multi-Task Distillation Network](https://arxiv.org/abs/2605.02137)

**<font color=#1a73e8>作者：</font>** Jagrati Talreja, Tewodros Syum Gebre, Leila Hashemi-Beni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate flood water mapping is critical for disaster management, yet current methods struggle to fully exploit the potential of spaceborne imagery. Optical data offers high interpretability but is limited by environmental conditions, whereas SAR provides reliable all-weather coverage with reduced visual interpretability. FLoRA (Fusion Latent for Optical Reconstruction and Area Segmentation) is a cross-modal multi-task framework that jointly reconstructs high-fidelity optical imagery and segments flood water regions from Sentinel 1 SAR by fusing the complementary strengths of optical and SAR data. During training, a lightweight optical teacher (driven by RGB and NDVI priors) provides pyramidal features that guide SAR representations into a fusion latent space via multiscale windowed cross attention and FiLM conditioning, with gated residuals preventing overcorrection. This design enables multi-task learning across two complementary objectives: (a) SAR-to-optical translation for fine-grained RGB reconstruction and (b) flood water region segmentation for hydrologic interpretation. The dual decoders are optimized using Charbonnier SSIM for structural fidelity, edge FFT magnitude losses for spectral realism, and Dice BCE hydrology-aware edge alignment for precise flood water delineation. A feature distillation constraint further aligns fused SAR features with the optical teacher's manifold. Evaluations on SEN1FLOODS11, DEEPFLOOD, and SEN12MS demonstrate that FLoRA surpasses fusion baselines in PSNR, SSIM, and LPIPS, demonstrating that multi-modal fusion within a teacher-guided latent space yields semantically faithful and physically consistent flood-water intelligence from spaceborne observations.

---


### 336. [On the Optimal Sample Complexity of Offline Multi-Armed Bandits with KL Regularization](https://arxiv.org/abs/2605.02141)

**<font color=#1a73e8>作者：</font>** Kaixuan Ji, Qiwei Di, Heyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kullback-Leibler (KL) regularization is widely used in offline decision-making and offers several benefits, motivating recent work on the sample complexity of offline learning with respect to KL-regularized performance metrics. Nevertheless, the exact sample complexity of KL-regularized offline learning remains largely from fully characterized. In this paper, we study this question in the setting of multi-armed bandits (MABs). We provide a sharp analysis of KL-PCB (Zhao et al., 2026), showing that it achieves a sample complexity of $\tilde{O}(\eta SAC^{\pi^*}/\epsilon)$ under large regularization $\eta = \tilde{O}(\epsilon^{-1})$, and a sample complexity of $\tilde{\Omega}(SAC^{\pi^*}/\epsilon^2)$ under small regularization $\eta = \tilde{\Omega}(\epsilon^{-1})$, where $\eta$ is the regularization parameter, $S$ is the number of contexts, $A$ is the number of arms, $C^{\pi^*}$ policy coverage coefficient at the optimal policy $\pi^*$, $\epsilon$ is the desired sub-optimality, and $\tilde{O}$ and $\tilde{\Omega}$ hide all poly-logarithmic factors. We further provide a pair of sharper sample complexity lower bounds, which matches the upper bounds over the entire range of regularization strengths. Overall, our results provide a nearly complete characterization of offline multi-armed bandits with KL regularization.

---


### 337. [Personalized Federated Learning for Gradient Alignment](https://arxiv.org/abs/2605.02143)

**<font color=#1a73e8>作者：</font>** Dongwon Kim, Gyuejeong Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning (pFL) aims to adapt models to client specific data distributions, yet it often fails to reliably preserve personalized information. Local training is hindered by high variance gradients induced by limited and heterogeneous client data, while aggregation further distorts client specific optimization directions. To address these challenges, we propose pFLAlign, a gradient alignment framework to maintain client specific information during both local training and aggregation. pFLAlign consists of two complementary mechanisms: one adapts local gradient directions to reduce variance during client side optimization, and the other mitigates aggregation induced distortion by realigning the global model with each client's personalized direction. Theoretically, we derive pFLAlign from a PAC Bayesian analysis, which reveals how personalized gradient alignment preserves client specific information. Our experiments and ablation studies show that pFLAlign consistently improves personalization performance and training stability, achieving state of the art results.

---


### 338. [Projection-Free Transformers via Gaussian Kernel Attention](https://arxiv.org/abs/2605.02144)

**<font color=#1a73e8>作者：</font>** Debarshi Kundu, Archisman Ghosh, Swaroop Ghosh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention in Transformers is typically implemented as $\mathrm{softmax}(QK^\top/\sqrt{d})V$, where $Q=XW_Q$, $K=XW_K$, and $V=XW_V$ are learned linear projections of the input $X$. We ask whether these learned projections are necessary, or whether they can be replaced by a simpler similarity-based diffusion operator. We introduce \textbf{Gaussian Kernel Attention} (GKA), a drop-in replacement for dot-product attention that computes token affinities directly using a Gaussian radial basis function (RBF) kernel applied to per-head token features. Each head learns only a bandwidth parameter $\sigma_h$, while a single output projection $W_O$ preserves compatibility with the standard Transformer interface. GKA can be interpreted as normalized kernel regression over tokens, linking modern Transformer architectures to classical non-local filtering and kernel smoothing methods. We evaluate GKA in both vision and language modeling settings. For autoregressive language modeling within the \texttt{nanochat} framework, we implement causal masking and sliding-window constraints by masking and renormalizing the Gaussian kernel. At depth 20, a GKA model with $0.42\times$ the parameters and $0.49\times$ the total training FLOPs of a standard attention baseline trains stably, exhibits a near-zero train-validation gap, and demonstrates competitive behavior on standard benchmarks, albeit with higher bits-per-byte (BPB) at this compute scale. Overall, GKA provides a minimal, interpretable attention mechanism with an explicit locality scale, offering a dimension in the accuracy-efficiency trade-off for Transformer design.

---


### 339. [SpecEdit: Training-Free Acceleration for Diffusion based Image Editing via Semantic Locking](https://arxiv.org/abs/2605.02152)

**<font color=#1a73e8>作者：</font>** Zhengan Yan, Shikang Zheng, Haoran Qin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image editing offers strong semantic controllability, but remains computationally expensive due to iterative high-resolution denoising over all spatial tokens. Dynamic-resolution sampling reduces this cost by performing early steps at reduced resolution. However, existing approaches prioritize upsampling using low-level heuristics such as edge detection or channel variance, which are weakly aligned with editing semantics and may lead to structural inconsistency. Moreover, spatial regions are often upsampled without verifying whether semantic modification is actually required, resulting in redundant high-resolution computation and accumulated errors. Therefore, we propose SpecEdit, a training-free dynamic-resolution framework tailored for diffusion-based image editing. SpecEdit follows a draft-and-verify scheme: a low-resolution draft first estimates the semantic outcome, after which token-level discrepancies are used to identify edit-relevant tokens for high-resolution denoising, while the remaining tokens stay at a coarse resolution. Experiments on Qwen-Image-Edit and FLUX.1-Kontext-dev demonstrate up to 10x and 7x acceleration, while maintaining strong quality. SpecEdit is complementary to step distillation and other acceleration techniques, achieving up to 13x speedup when combined with existing methods. Our code is in supplementary material and will be released on GitHub.

---


### 340. [Cross-Polarization Fusion of VV AND VH SAR Observations for Improved Flood Mapping](https://arxiv.org/abs/2605.02153)

**<font color=#1a73e8>作者：</font>** Jagrati Talreja, Tewodros Syum Gebre, Leila Hashemi Beni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Radar (SAR) imagery is widely used for flood monitoring due to its all-weather and day-night imaging capability. However, flood mapping using single-polarization SAR data remains challenging in complex environments where surface and volume scattering coexist. In this paper, we investigate the effectiveness of cross-polarization fusion of VV and VH SAR observations for improved flood mapping. A deep learning-based segmentation framework is employed to jointly exploit complementary information from VV and VH polarizations. To ensure a fair evaluation, three configurations are compared under identical training conditions: VV only, VH only, and fused VV-VH input. Performance is assessed using standard flood mapping metrics, including Intersection over Union (IoU) and F1-score, along with qualitative visual analysis. Experimental results demonstrate that VV-VH fusion consistently outperforms single-polarization models, particularly in vegetated and heterogeneous flood regions, leading to more accurate flood boundary delineation. The findings highlight the importance of cross-polarization SAR fusion for enhancing the reliability of SAR-based flood mapping in disaster monitoring applications.

---


### 341. [Combining Trained Models in Reinforcement Learning](https://arxiv.org/abs/2605.02159)

**<font color=#1a73e8>作者：</font>** Ujjwal Patil, Javad Ghofrani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) has delivered strong results in domains such as Atari and Go, but it still suffers from high sample cost and weak transfer beyond the training setting. A common response is to reuse information from previously trained models through transfer, distillation, ensemble methods, or federated training instead of learning each target task from random initialization. The literature on these mechanisms is fragmented, and published comparisons are hard to interpret because tasks, baselines, and compute budgets differ.
This paper presents a PRISMA-guided systematic review of empirical studies on pretrained knowledge reuse in DRL. Starting from 589 records retrieved from IEEE Xplore, the ACM Digital Library, and citation tracing, we screened 570 unique records and assessed 89 full texts. After applying the final eligibility criteria, 15 empirical studies remained in the main synthesis. We analyzed them qualitatively across three factors: source-target similarity, diversity among reused models, and the fairness of comparisons against from-scratch baselines.
Three patterns recur across the surviving corpus. First, positive results are concentrated in settings where source and target tasks share substantial structure or where the method includes an explicit gating or alignment mechanism. Second, evidence for ensembles and federated aggregation is promising but sparse and mostly limited to narrow settings. Third, compute-matched comparisons are rare, which weakens claims about efficiency gains over stronger single-agent baselines. The paper contributes a narrower and internally consistent review scope, a study-level synthesis of empirical evidence, and a provisional independence spectrum that should be treated as a hypothesis for future benchmarking rather than a validated metric.

---


### 342. [Experience Constrained Hierarchical Federated Reinforcement Learning for Large-scale UAV Teams in Hazardous Environments](https://arxiv.org/abs/2605.02165)

**<font color=#1a73e8>作者：</font>** Qinwei Huang, Rui Zuo, Simon Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional federated learning assumes that greater learner participation improves training performance, by leveraging abundant, independently generated local data. However, in federated reinforcement learning (FRL) for unmanned aerial vehicle (UAV) teams in hazardous environments where experience generation is severely constrained by safety considerations, energy limitations, and mission duration, this assumption may break. This work introduces Experience-Constrained Hierarchical Federated Reinforcement Learning (EC-HFRL), a framework in which clusters act as federated learning agents, while multiple intra-cluster learners represent parallel learning resources that reuse a shared experience pool. We show that increasing participation does not necessarily improve learning performance. Instead, learning performance is strongly associated with experience reuse strategy and the dominance of key analytically identified gradient transition experiences within a cluster. In particular, minibatch size primarily determines effective replay exposure, while higher intra-cluster participation increases reuse level. Empirical results demonstrate that the performance regimes are strongly associated with the structure of the learning signal, rather than federated aggregation effects, clarifying the limited and secondary role of learner participation in experience-constrained FRL.

---


### 343. [Manifold-Aligned Guided Integrated Gradients for Reliable Feature Attribution](https://arxiv.org/abs/2605.02167)

**<font color=#1a73e8>作者：</font>** Soyeon Kim, Seongwoo Lim, Kyowoon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature attribution is central to diagnosing and trusting deep neural networks, and Integrated Gradients (IG) is widely used due to its axiomatic properties. However, IG can yield unreliable explanations when the integration path between a baseline and the input passes through regions with noisy gradients. While Guided Integrated Gradients reduces this sensitivity by adaptively updating low-gradient-magnitude features, input-space guidance still produces intermediate inputs that deviate from the data manifold. To address this limitation, we propose \emph{Manifold-Aligned Guided Integrated Gradients} (MA-GIG), which constructs attribution paths in the latent space of a pre-trained variational autoencoder. By decoding intermediate latent states, MA-GIG biases the path toward the learned generative manifold and reduces exposure to implausible input-space regions. Through qualitative and quantitative evaluations, we demonstrate that MA-GIG produces faithful explanations by aggregating gradients on path features proximal to the input. Consequently, our method reduces off-manifold noise and outperforms prior path-based attribution methods across multiple datasets and classifiers. Our code is available at this https URL.

---


### 344. [Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/abs/2605.02168)

**<font color=#1a73e8>作者：</font>** Wenyi Wu, Sibo Zhu, Kun Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model (LM)-based agents have demonstrated promising capabilities in automating complex tasks from natural language instructions, yet they continue to struggle with long-horizon planning and reasoning. To address this, we propose an enhanced multi-agent framework that decomposes automation into three roles: a planner for high-level decision-making, an actor for task execution, and a memory manager for contextual reasoning. While this modular decomposition aligns with established design patterns, our core contribution lies in a systematic compute-allocation analysis, revealing that planning is the dominant factor influencing task performance. Execution and memory management require significantly less compute and model capacity to achieve competitive results. Building on these insights, we introduce a planner-centric reinforcement learning approach, which exclusively optimizes the planner using trajectory-level rewards from a VLM-as-judge, while freezing the other components. Extensive experiments on benchmarks spanning web navigation, OS control, and tool use demonstrate that concentrating model capacity and learning on high-level planning yields robust and compute-efficient improvements in long-horizon agent automation. Our code is publicly released.

---


### 345. [Heterogeneous Model Fusion for Privacy-Aware Multi-Camera Surveillance via Synthetic Domain Adaptation](https://arxiv.org/abs/2605.02169)

**<font color=#1a73e8>作者：</font>** Peggy Joy Lu, Wei-Yu Chen, Yao-Tsung Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose HeroCrystal, a novel privacy-preserving framework for multi-camera domain-adaptive object detection, addressing challenges such as data privacy, class imbalance, and heterogeneous architectures. Our framework consists of three key stages. In the Generated Stage, we introduce a one-shot, target-aware diffusion-based generation module that learns visual style from a single target-domain image while leveraging prompt-based control to synthesize specific object instances. Unlike conventional style transfer-based methods that require large target datasets and ignore semantic-level discrepancies, our approach enables privacy-preserving augmentation to reduce ethical concerns, and introduces controllable rare object generation to mitigate long-tailed category degradation. In the Federated Stage, we employ probabilistic Faster R-CNN on the client side to improve localization accuracy, and a dynamic model contrastive strategy to suppress domain-specific bias. The server side performs model fusion across heterogeneous architectures without accessing raw data. Finally, in the Distilled Stage, we propose an inconsistent categories integration algorithm to resolve label inconsistency and architecture heterogeneity across clients. Extensive experiments on multiple cross-domain detection benchmarks demonstrate that our method outperforms existing multi-source domain adaptation and federated learning baselines under multi-class, privacy-preserving settings. Our method improves mAP by +2.1% over prior privacy-preserving approaches and achieves a new state-of-the-art mAP of 33.4%, highlighting the effectiveness of HeroCrystal in enabling practical multi-camera AI surveillance systems.

---


### 346. [CLaC at SemEval-2026 Task 6: Response Clarity Detection in Political Discourse](https://arxiv.org/abs/2605.02170)

**<font color=#1a73e8>作者：</font>** Nawar Turk, Lucas Miquet-Westphal, Leila Kosseim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present our system for SemEval-2026 Task 6 (CLARITY) on response clarity and evasion detection in question-answer pairs from U.S. presidential interviews, comparing fine-tuned encoders with prompt-based LLMs. Our LLM ensemble achieves 80 macro-F1 on the 3-class Task 1 (9th/41) and 59 on the 9-class Task 2 (3rd/33). Across 8 transformer encoders optimized through a four-stage pipeline, partial encoder layer unfreezing outperforms full fine-tuning by a wide margin. Combining English and multilingual encoders further improves ensemble performance over either family alone, despite multilingual models being individually weaker. Prompt-based LLMs, without any task-specific parameter updates, outperform fine-tuned encoders, particularly on minority classes; among open-weight LLMs, parameter count does not predict performance. Enriched input, concatenating the full interviewer turn, improves LLM performance but not that of encoders, an effect that persists with Longformer's extended context window, suggesting the divergence is not attributable to sequence-length capacity alone in our settings. The Clear Reply/Ambivalent boundary remains the dominant failure mode, mirroring the disagreement among human annotators. Our code, prompts, model configurations, and results are publicly available.

---


### 347. [Intervention Complexity as a Canonical Reward and a Measure of Intelligence](https://arxiv.org/abs/2605.02175)

**<font color=#1a73e8>作者：</font>** Brendan McCane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Legg--Hutter universal intelligence measure provides a rigorous scalar assessment of general intelligence as expected reward across all computable environments, weighted by simplicity. However, the measure presupposes an externally specified reward function, raising the question of whether the reward primitive is inherently arbitrary or whether a canonical choice exists. We propose a new measure, called intervention complexity, that has five natural properties: environment-derivedness, universality, minimality, sensitivity, and achievement preference. Given a resource function rho encoding an inductive bias (such as program length, execution time, or energy), rho-intervention complexity is a universal reward. The result yields a family of canonical rewards indexed by resource bias, providing a principled completion of the Legg--Hutter framework that does not require external normative input. We further propose a two-dimensional characterisation of intelligence: agent competence (how well the agent performs relative to the oracle optimum) and learning efficiency (how quickly this competence improves with experience). A separation theorem establishes that the choice of resource bias determines the computability of the resulting measure: action-count IC is computable in polynomial time, while program-length IC without oracle access is uncomputable, with the gap between oracle and bare IC precisely quantifying the information-theoretic content of learning. We discuss implications for superintelligence and for pre-training universal agents.

---


### 348. [Manifold-Constrained Adversarial Training for Long-Tailed Robustness via Geometric Alignment](https://arxiv.org/abs/2605.02183)

**<font color=#1a73e8>作者：</font>** Guanmeng Xian, Ning Yang, Philip S. Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial training is effective on balanced datasets, but its robustness degrades under longtailed class distributions, where tail classes suffer high robust error and unstable decision boundaries. We propose Manifold-Constrained Adversarial Training (MCAT), a unified framework that enforces the semantic validity of adversarial examples by penalizing deviations from class-conditional manifolds in feature space, while promoting balanced geometric separation across classes via an ETF-inspired regularization. We provide theoretical results that link geometric separation to lower bounds on adversarially robust margins, and show that manifold-constrained adversarial risk upperbounds robust risk on high-density semantic regions. Extensive experiments on standard longtailed benchmarks demonstrate consistent improvements in overall, balanced, and tail-class adversarial robustness.

---


### 349. [RAFNet: Region-Aware Fusion Network for Pansharpening](https://arxiv.org/abs/2605.02184)

**<font color=#1a73e8>作者：</font>** Jianing Zhang, Zijian Zhou, Kai Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and high-resolution panchromatic (PAN) images. Although deep learning has advanced this field, mainstream frequency-based methods relying on standard scaled dot-product attention suffer from quadratic computational complexity and fail to exploit the inherent regional sparsity of remote sensing imagery. Furthermore, existing spatial enhancement strategies typically employ static convolution kernels, which struggle to adapt to the complex frequency and regional variations of PAN and MS images. To address these bottlenecks, we propose a Region-Aware Fusion (RAFNet) Network that synergistically models spatial and frequency information. Specifically, we design a Spatial Adaptive Refinement (SAR) module that leverages the discrete wavelet transform (DWT) for directional frequency separation and K-means clustering for regional partitioning, which enables the dynamic construction of region-specific adaptive convolution kernels, achieving spatially and frequency-adaptive feature enhancement. Moreover, we introduce a Clustered Frequency Aggregation (CFA) module based on a sparse attention mechanism guided by the semantic clusters, which executes a region-aware sparse attention strategy that drastically reduces computational redundancy while ensuring high-quality frequency feature extraction. In addition we integrated these modules into a progressive, multi-level spatial-frequency network architecture to facilitate robust interaction and accurate image reconstruction. Extensive experiments on multiple benchmark datasets demonstrate that the proposed RAFNet significantly outperforms state-of-the-art pansharpening methods in both reduced- and full-resolution assessments. The code is available at this https URL.

---


### 350. [KANs need curvature: penalties for compositional smoothness](https://arxiv.org/abs/2605.02190)

**<font color=#1a73e8>作者：</font>** James Bagrow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold networks (KANs) offer a potent combination of accuracy and interpretability, thanks to their compositions of learnable univariate activation functions. However, the activations of well-fitting KANs tend to exhibit pathologically high-curvature oscillations, making them difficult to interpret, and standard regularization penalties do not prevent this. Here we derive a basis-agnostic curvature penalty and show that penalized models can maintain accuracy while achieving substantially smoother activations. Accounting for how function composition shapes curvature, we prove an upper bound on the full model's curvature relative to the curvature penalty, and use this to motivate richer forms of penalties. Scientific machine learning is increasingly bottlenecked by the trade-off between accuracy and interpretability. Results such as ours that improve interpretability without sacrificing accuracy will further strengthen KANs as a practical tool for both prediction and insight.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
