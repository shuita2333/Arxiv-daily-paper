# 🧠 大模型相关研究 | 2026年09月22日

> 本类共 **148** 篇论文：已确认 **139** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-148](./part-03.md)

---

### 51. [X-SPUR: Explainable Surprisal-Based Protocol-Aware Unsupervised Reasoning for Automotive Ethernet Intrusion Detection](https://arxiv.org/abs/2609.21217)

**<font color=#1a73e8>作者：</font>** Jisoo Kim, Seonghoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automotive Ethernet carries heterogeneous multi-protocol traffic in modern in-vehicle networks, where labeled attack data are rarely available and the strongest prior unsupervised detector still relies on handcrafted traffic features. This article presents X-SPUR, an explainable, surprisal-based, protocol-aware unsupervised reasoning framework that instead represents raw packet fields as token sequences, learns benign traffic patterns through causal language modeling, and detects anomalies from per-token cross-entropy surprisal. To incorporate temporal context, we introduce a bimodal fusion architecture that combines payload-token embeddings with inter-packet timing through additive fusion and a Hadamard interaction. To handle the heterogeneous score distributions of different protocol families, we further propose a dual top-$k$% per-protocol $Z$-score calibration that jointly captures moderately distributed and sparse anomaly signatures. On the TOW-IDS dataset, X-SPUR achieves an AUC of 0.9987. This is marginally higher than the 0.9969 reported for AERO. X-SPUR also eliminates handcrafted feature engineering. We train a separate CarDS model using the same architecture and training hyperparameters. This model retains strong performance on the second automotive Ethernet dataset. Beyond detection, per-token surprisal provides fine-grained explainability by attributing anomaly scores to specific protocol fields, supporting interpretable security analysis in heterogeneous in-vehicle networks.

---


### 52. [CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition](https://arxiv.org/abs/2609.21259)

**<font color=#1a73e8>作者：</font>** Lance Ying, Jinzhou Wu, Yingshan Susan Wang 等 56 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding and modeling human intelligence are parallel goals shared by artificial intelligence (AI) and cognitive science. As AI systems grow increasingly capable, in what ways do model responses resemble human responses, and where do they systematically diverge? The sheer breadth and diversity of the tasks humans can perform and think about pose a challenge for scalable and rigorous comparison between humans and models. We introduce CogGym, a scalable, unified framework grounded in cognitive science for systematically comparing model and human behavior on matched experimental trials. CogGym uses a semi-automated, human-in-the-loop pipeline to standardize diverse experimental paradigms into a task-agnostic Experiment Markup Language (EML), enabling reproducible and faithful comparison at scale. For initial release, we curate and standardize 258 cognitive experiments from 100 papers that focuses on human commonsense reasoning, and evaluate 50 large language models against human responses. We find a clear scaling trend where larger and more recent AI models better reproduce human judgments. Yet AI models' improvement on such common reasoning tasks is considerably slower than the gains observed on formal-reasoning benchmarks like math and coding, and model--human fit remains well below human splithalf reliability ($R^2 = 0.93$ on text, $0.95$ on image, and $0.92$ on video) with the best models achieving $R^2 = 0.59$ on text, $0.58$ on image, and $0.43$ on video experiments. We intend for CogGym to provide a living evaluation framework that continually incorporates new cognitive science experiments to characterize where model behavior resembles human behavior, where it systematically diverges, and how those patterns change as models and experiments evolve.

---


### 53. [PlaceReasoner-Beta: Reasoning-Driven Macro Placement and Benchmarking](https://arxiv.org/abs/2609.21263)

**<font color=#1a73e8>作者：</font>** Qiufeng Li, Chengxuan Wang, Rongqian Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated macro placement remains a fundamental challenge in VLSI physical design. Despite decades of research, existing approaches predominantly optimize hand-crafted proxy objectives, such as estimated wirelength, and typically produce placements through one-shot numerical optimization, limiting their ability to incorporate visual layout context, codified design expertise, and downstream physical-design feedback in a unified loop. We present PlaceReasoner-Beta, a verifier-guided multi-agent framework that reformulates macro placement as a closed-loop reasoning problem rather than black-box optimization. A vision-language model (VLM) planner generates candidate placements from the floorplan image, macro specifications, and connectivity structure; a geometric verifier enforces physical legality and expert placement principles; a physical verifier refines candidates using early implementation feedback; and a post-route optimizer further improves promising layouts using final PPA. To enable reproducible evaluation, we introduce PlaceReasoner-Bench, a fully open end-to-end benchmark built from open RTL designs, EDA tools, and technology libraries. It comprises 8 designs at two aspect ratios, yielding 16 tasks with fixed floorplans and I/O assignments, so methods differ only in macro positions and orientations and are evaluated using routed PPA and DRC rather than pre-route proxies. Across the benchmark, PlaceReasoner-Beta achieves the best timing among DRC-clean methods on all square tasks, reducing post-route TNS by 61.2% at 1:1 and 53.0% at 2:1 relative to the classical baseline field. It also shortens routed wirelength on most designs despite never explicitly optimizing it, demonstrating that reasoning over spatial structure under physical-design feedback can improve end-to-end layout quality beyond proxy-objective optimization.

---


### 54. [Efficient Benchmarking in Production: A Study of an Evolving LLM Agent](https://arxiv.org/abs/2609.21267)

**<font color=#1a73e8>作者：</font>** Yining She, Lei Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production LLM agents are evaluated repeatedly as they evolve, but full agent benchmarks are costly to rerun. We study efficient recurring evaluation for a production analytics agent serving tens of thousands of monthly active users and report first-hand deployment experience. Using 574 historical runs of the production benchmark, split chronologically into calibration and held-out periods, we compare random sampling, historical caching, fixed representative subsets, and IRT-based adaptive testing. The results show that multidimensional 2PL adaptive testing achieves the best overall score fidelity: executing 200 questions, 38.5% of a full run, yields 1.03 pp of MAE. We nevertheless deployed difficulty-stratified fixed subsets because of their operational simplicity, and show they transfer without recalibration to five other agent families and remain stable across calibration windows as short as one day. Drawing on this deployment experience, we report practical recommendations for recurring production-agent evaluation.

---


### 55. [Beyond Exact Match: Task-Aware GRPO for Cross-Domain PCBA Visual Question Answering](https://arxiv.org/abs/2609.21276)

**<font color=#1a73e8>作者：</font>** Jia Li, Li Dai, Peng Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In automated Printed Circuit Board Assembly (PCBA) inspection, standards-guided decisions require systems to jointly reason over fine-grained visual cues, component semantics, and manufacturing knowledge. Although large vision-language models (VLMs) provide a promising foundation, their deployment is hindered by the domain shift between standards-derived samples and real-world production-line imagery, together with heterogeneous output spaces spanning choice-based and numerical counting tasks. To address these challenges, we propose a multimodal reasoning framework for cross-domain PCBA visual question answering. The framework converts standards-derived, real-world, and auxiliary PCB-domain data into a unified instruction format and constructs verified reasoning traces aligned with visual evidence, question semantics, candidate options, and ground-truth answers. We further introduce Task-Aware Group Relative Policy Optimization (GRPO), which moves beyond exact-match supervision by integrating multi-component semantic rewards for choice-based questions, distance-aware rewards for counting questions, and an auxiliary format reward for valid outputs. During inference, answer-option semantic consistency correction, self-consistency voting, and multi-model arbitration are combined to improve prediction robustness. The proposed system achieves an Overall Score of 83.24 on the official PCBA Standard-to-Real Grand Challenge leaderboard, demonstrating the effectiveness of task-aware reward design and robust inference for cross-domain PCBA visual question answering.

---


### 56. [How Many Humans Is a Judge Panel Worth?](https://arxiv.org/abs/2609.21277)

**<font color=#1a73e8>作者：</font>** Chao Li, Yingying Yu, Yunfeng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How many human judgments does a panel of language models represent? The answer depends on what is matched. We audit categorical judge panels against empirical human label distributions, retaining disagreement that binary errors relative to one gold label collapse. We measure spectral residual diversity by matching the participation ratio of a normalized residual Gram matrix to conditionally independent human-reference draws, giving nu_H. We separately match distributional squared error, giving nu_MSE. Across three ChaosNLI tasks, the same 32-judge panels have nu_H=4.24--6.50 but nu_MSE=2.30--3.75. A spectral identity separates the eigenvalues, member energies, and averaging-direction weights that determine error. Realizable hard-label panels show that greater spectral diversity can accompany worse distribution recovery even with equal member energies and nonnegative correlations. In the observed panels, within-size ranking agreement varies sharply by task; some member additions produce conflicting changes that persist across two item halves. The consensus-direction share of centered residual variance is gamma_co=43.8% on MNLI-m and 33.7% on SNLI, quantifying shared variation retained by averaging. We provide aligned votes and analysis protocols for auditing these distinctions. Effective size is therefore a target-specific measurement: spectral diversity and distribution recovery should not be treated as interchangeable measures of panel quality or as general human-replacement rates.

---


### 57. [GUIDE: Designer-in-the-loop Authoring of Conformant Generative User Interfaces](https://arxiv.org/abs/2609.21285)

**<font color=#1a73e8>作者：</font>** Hyewon Lee, Ziying Wang, Aiden Moy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative User Interfaces (GenUIs) enable applications to generate interfaces on demand from user needs and context. Like conventional UIs, they must still reflect designers' intent and conform to requirements such as brand identity. Unlike conventional UIs, designers cannot directly specify or see every interface a GenUI may produce, making design intent harder to enforce. We introduce GUIDE (GenUI Development Environment), a system that lets designers continuously inspect and refine GenUI behavior as they create and edit interfaces. GUIDE uses designers' modifications and interactions to adapt GenUIs through prompt optimization and a novel adaptive conformance scoring model. We validate GUIDE's scoring model and system. The scoring model matched or outperformed proprietary LLM baselines on held-out comparisons of real and synthetic application screens. In a study with 12 UI/UX practitioners, participants found GUIDE effective and usable and significantly preferred aligned outputs over a strong baseline using exemplars and a model-generated this http URL.

---


### 58. [GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development](https://arxiv.org/abs/2609.21293)

**<font color=#1a73e8>作者：</font>** Xiuhui Zhang, Yi Chen, Shusheng Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous software generation (ASG) aims to turn human requirements into executable applications, but delivering these applications does not necessarily establish that their interacting components satisfy the specified behavioral requirements. We introduce GameASG-Bench, a benchmark that makes behavioral testability part of the generation task for game development. Our design declares an evaluation interface specification before generation, fixing legal starting scenarios, player-level actions, stable snapshots, rejection behavior, and invariants while leaving private implementations open. Concretely, we include: (i) static L1 checks that assess source-level compliance; and (ii) browser-executed L2 checks that combine semantic observations with real input and runtime evidence. We implement this protocol as 47 browser-native game-generation tasks spanning 12 primary genres and both 2D and 3D interaction, each with executable checks and an independently verified reference implementation. Our experiments answer four key questions about end-to-end agent performance, tool access and nominal turn budget, reasoning effort, and harness choice. Across nine agent stacks, the highest observed mean L2 check pass rate is 93.2%, yet the highest observed strict task success rate, requiring all L1 and applicable L2 prerequisite and core requirement checks, is only 55.3% (26/47 tasks). For DeepSeek-V4-Flash, full tool access and larger nominal turn budgets yield more strict task successes, while the strict task success rate is not monotonic in reasoning effort. Both tested harnesses achieve 18 strict task successes, but only ten tasks succeed under both. These results expose task-level compliance gaps that high average check pass rates actually obscure.

---


### 59. [FairLMs: A Turnkey Library for Fairness in Language Models](https://arxiv.org/abs/2609.21296)

**<font color=#1a73e8>作者：</font>** Jiale Zhang, Michael Larionov, Zichong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness research on language models involves measuring bias, applying mitigation methods, and examining the evidence on which an evaluation rests. Existing tools offer complementary functionality through different interfaces, so combining them requires reconciling model interfaces, evidence formats, access constraints, and result types before applicability can be checked or methods compared. We introduce \textbf{FairLMs}, a Python library that connects these activities through explicit declarations of model capabilities and input requirements. It provides 33 intrinsic and extrinsic metrics, 14 mitigation components spanning four intervention categories, 14 dataset and scoring-instrument diagnostics, adapters for the three Transformer architectures and supported hosted completion APIs, and benchmark loaders. Declarations are checked before execution and results carry the configuration under which they were obtained, so that compatible components can be combined, methods compared under a common protocol, and workflows extended to new models and datasets. The source code is available at: this https URL.

---


### 60. [VeriFuse: Bounded Vision-Language Arbitration and Reason-Guided Refinement for Cooperative 3D Perception](https://arxiv.org/abs/2609.21323)

**<font color=#1a73e8>作者：</font>** Hongyi Lin, Yiyao Liu, Qi Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated strong scene understanding and semantic judgment across diverse tasks, but their appropriate role in cooperative perception remains unclear. Directly asking a VLM to regress 3D detections is unreliable and computationally expensive, whereas using it to select the output of a single source discards useful information from other agents. We introduce VeriFuse, a bounded arbitration framework for vehicle-infrastructure cooperative 3D detection. Each agent first produces detections independently. Around each vehicle and roadside proposal, VeriFuse generates source-conditioned geometric candidates and combines the original detections, their perturbations, and cross-source hypotheses into a unified candidate pool. A frozen VLM then chooses among three admissible actions: SELECT an adequate candidate; REFINE an existing anchor when an object is supported but all candidates are geometrically inadequate; or REJECT an unsupported infrastructure-only proposal. Experiments on the DAIR-V2X dataset show that VeriFuse achieves 0.494/0.357 cooperative 3D AP50/AP70 and limits the relative vehicle-side BEV AP50 drop under a 300 ms delay to 1.7%. Overall, VeriFuse assigns the VLM a clear and constrained role in cooperative perception: semantic reasoning resolves ambiguity among cross-agent hypotheses, while deterministic constraints determine the final 3D geometry.

---


### 61. [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/abs/2609.21340)

**<font color=#1a73e8>作者：</font>** Shuo Huang, Gholamreza Haffari, Xingliang Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Empirical identity leakage from released text is increasingly driven by attackers that combine large language models (LLMs) with auxiliary knowledge to link documents to individuals. Existing audits typically report success rates for specific attack pipelines but lack finite-sample statistical guarantees, while training-time protections such as differential privacy are difficult to translate into release-time decisions for individual natural-language documents. We introduce Conformal Privacy Auditing(CPA), a distribution-free calibration framework that provides a statistical certificate of re-identification risk for each released document against LLM-empowered adversaries. CPA outputs a conformal ambiguity set of candidate identities that is guaranteed to contain the true identity with user-chosen confidence under exchangeability, together with an interpretable leakage proxy derived from set size. CPA supports both logit-access and sampling-only attackers, enabling audits of open-source models and proprietary API models in a unified framework. Across multiple release benchmarks and attacker configurations, CPA achieves calibrated coverage and reveals sharp shifts in certified identifiability as auxiliary knowledge, LLM augmentation, and release mechanisms vary, providing a statistically grounded basis for reporting and comparing release-time linkage risk across attacker configurations, datasets, and release mechanisms alike.

---


### 62. [CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices](https://arxiv.org/abs/2609.21344)

**<font color=#1a73e8>作者：</font>** Wenquan Zhou, An Wang, Jing Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For Internet of Things (IoT) devices, a secure algorithm alone is not enough: an attacker with physical access can attack the implementation directly, and its flaws are hard to fix once deployed. Large language models (LLMs) are now used to build and analyze such implementations. LLM benchmarks exist for cryptography and general cybersecurity, but none covers cryptographic engineering. In this paper, we present CESBench, 380 expert-written items across six sub-domains of cryptographic engineering security for IoT devices: side-channel, fault injection, implementation, countermeasures, evaluation, and integration. Four task types target different competences: 209 multiple-choice items test recall, 67 judgment items require a security verdict and its justification, 63 scenario items require an engineering diagnosis, and 41 code tasks are graded by 572 test cases. To validate the benchmark, 11 open-weight and proprietary LLMs answer every item. Multiple-choice and code responses are scored automatically, and judgment and scenario responses by an LLM judge, whose scores are checked against a second judge from another model family and human re-scoring. Composite scores range from 54.4% to 83.6%. The top score on each task type is 98.6% for multiple choice, 95.1% for code, and 88.4% for scenario diagnosis, but only 58.8% for judgment. Across models, 88.5% of verdicts are correct, yet their justifications earn only 53.4% of the rubric marks. Multiple choice is near its ceiling for the strongest models and most code tasks are solved, whereas justifying a security verdict remains the weakest competence. The benchmark, prompts, and per-item results are public.

---


### 63. [IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/abs/2609.21346)

**<font color=#1a73e8>作者：</font>** Ran Cheng, Longfei Xu, Zheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) scales capacity, but existing designs cannot set three quantities independently. For a single token, participation is how many experts contribute knowledge to its output, execution is how many are actually computed (compute cost), and materialization is how many expert-sized parameter sets must be built and stored (memory cost). Sparse routing keeps execution and materialization low, but shrinks participation: for each token, only a few experts contribute. Dense output-mixing restores full participation, but its execution grows with the number of experts. Parameter-merging keeps execution at one expert, but its materialization grows with the number of routing decisions. We propose IntBMoE, a block-conditioned MoE that decouples all three by pairing dense expert composition with sparse block execution. Its blocks come from a small learned codebook, one per entry. At each internal layer, a lightweight hypernetwork merges all expert bases in that layer's pool into one composed expert. Participation is full, because every composed expert draws on the entire pool. Execution stays sparse, because a router sends each token to only a few blocks. Materialization is bounded, because the codebook, not the input, fixes how many blocks exist. Dual-Path Residual Gating (DPRG) further couples two independently composed paths through multiplicative gating. Experiments on image classification show consistent gains over representative sparse and dense MoE baselines. Additional experiments on language modeling and sequential recommendation validate its generalization beyond vision. IntBMoE is fully deployed in AMap's generative recommendation system, serving hundreds of millions of users under a 60ms latency budget, with a 2.4% relative UVCTR gain in online A/B testing. Our code is available at this https URL.

---


### 64. [From Memory to Behavior: A Behavior-Aware Role-Playing Framework for Social Media Influencers](https://arxiv.org/abs/2609.21349)

**<font color=#1a73e8>作者：</font>** Ji-Lun Peng, Yi-Zhen Zhang, Chun-Nan Chou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have shown strong potential as role-playing agents for real individuals, yet faithful impersonating remains challenging. Existing in-context learning-based methods fail to capture how individuals react under different situations. In addition, LLM-based evaluation is difficult for obscure individuals. To address these challenges, we propose Situation--Internal state--Behavior Persona method to incorporate situation-dependent behavioral strategies. We further design an evaluation protocol that provides LLM evaluators with references about the impersonated individual. We evaluate our approach on a newly constructed dataset for the task of generating replies on social media. Experimental results show that our proposed method outperforms state-of-the-art ICL-based baselines, while our evaluation protocol achieves moderate correlation with human judgment. Besides, experiments on fictional-character benchmarks demonstrate that our proposed method is applicable beyond the social media setting. These findings suggest that incorporating behavioral information broadly improves the fidelity of role-playing for real individuals on social media or fictional characters.

---


### 65. [PrismAlign: Prior-Steered Multi-View VLM Alignment for Hallucination-Robust Table OCR](https://arxiv.org/abs/2609.21351)

**<font color=#1a73e8>作者：</font>** Guangyi Liu, Qianjun Huang, Boyu Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table extraction suffers from frequent structural errors and semantic hallucinations. We propose PrismAlign, a multi-VLM framework aligning diverse visual perspectives to resolve ambiguity. It integrates priors of table logic to assess output plausibility, decoupling structural alignment from cell content alignment. A Bayesian decision strategy maximizes alignment accuracy by exploiting the correlation between extraction errors and computable rule violations. Evaluated on open-source and custom VLMs, PrismAlign reduces hallucinations and achieves state-of-the-art performance on OmniDocBench 1.5, as well as on the table category of CC-OCR and PureDocBench.

---


### 66. [Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining](https://arxiv.org/abs/2609.21362)

**<font color=#1a73e8>作者：</font>** Nghia Hieu Nguyen, Thai Bao Huynh, Binh-An Dinh-Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conventional tokenizers represent text as characters or statistically derived subwords, overlooking the internal phonological structure of syllables and often requiring large vocabularies. We introduce \textbf{Phonemic Tokenizer}, a linguistically motivated tokenizer for Vietnamese and Chinese that converts each syllable into IPA and factorizes it into three phonological components: onset, rime, and tone. The three components jointly occupy one contextual position, preserving syllable-level sequence length while enabling representation sharing across phonologically related syllables. Non-phonological and unsupported units are handled through character-level fallback. This deterministic design requires no corpus-dependent vocabulary learning and yields vocabularies of only 112 entries for Chinese and 256 for Vietnamese. Intrinsic evaluation shows that the tokenizer achieves substantially higher Rényi efficiency in both languages, represents every entry in a standard Vietnamese syllable dictionary with a Fertility of exactly one, and generally produces shorter Vietnamese sequences than existing pretrained tokenizers. We further instantiate the tokenizer in \textbf{PhonemicBERT}, which combines factorized component embeddings and reconstructs complete masked syllables using three prediction heads. Under a controlled Chinese pretraining setup, PhonemicBERT-Zh is competitive with or outperforms character, subword, and SubChar alternatives across diverse language-understanding tasks. PhonemicBERT-Vi also achieves competitive or superior results to established Vietnamese and multilingual pretrained models. These results establish phonemic factorization as a compact, efficient, and interpretable alternative to atomic and statistically segmented text representations.

---


### 67. [ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](https://arxiv.org/abs/2609.21378)

**<font color=#1a73e8>作者：</font>** Qiang Zhang, Ruixue Ding, Fanrui Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain. Recent pairwise evaluation methods alleviate reward discrimination collapse by replacing pointwise scoring with relative preferences. However, they still compress rich comparative feedback into a single trajectory-level reward, obscuring decisive intermediate steps and preventing successful behaviors from being consolidated into reusable skills. We propose ArenaFlow, a hierarchical credit propagation framework for open-ended agent reinforcement learning. ArenaFlow leverages tournament-based relative ranking to derive trajectory-level reward signals. Each comparison is further equipped with structured reflective evaluation, which reveals three types of supervision: pivotal success steps, reusable strategy skills, and usage attribution of retrieved skills. At the step level, ArenaFlow propagates trajectory-level advantages to high-confidence pivotal steps according to tournament survival depth, enabling more targeted optimization of local reasoning behaviors. At the skill level, ArenaFlow estimates skill utility from group-level usage attribution and maintains a global skill memory through utility-aware updating, pruning, and retrieval. The resulting high-utility skills further serve as policy priors for future exploration. Extensive experiments validate ArenaFlow's effectiveness on open-ended agent tasks.

---


### 68. [Prediction Dynamics in Depth-Recurrent Language Models](https://arxiv.org/abs/2609.21383)

**<font color=#1a73e8>作者：</font>** Xinyue Luo, Fei Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depth-recurrent language models refine predictions through repeated latent updates. Why can intermediate answers agree with the endpoint while their scores continue to change? We derive a sharp margin characterization that decomposes the conservatism of a magnitude bound into common translation, direction relative to the winner, and the pairing of each competitor's update with its score gap. Across Huginn-3.5B and Ouro-1.4B, accounting for update direction and competitor pairing reduces the mean earliest qualifying depth by a further 22.5-34.4% of the total depth beyond translation removal under full answer-text scoring. This retrospective comparison uses completed trajectories. Substantial contributions also occur under label scoring. For shared predictive distributions, we separate common and contrast motion orthogonally and express the common component through candidate-set mass and within-set concentration. Common and contrast energies can attenuate at different rates, allowing a growing preference-change share to coexist with shrinking absolute updates. These findings explain finite-depth answer preservation through the geometry and composition of observed score changes.

---


### 69. [AgentVidBench: A Multi-Hop Video Question Answering Benchmark for Evaluating MLLM Agents](https://arxiv.org/abs/2609.21386)

**<font color=#1a73e8>作者：</font>** Seoyeon An, Hyeonseo Jang, Minsu Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive video understanding is crucial for advancing artificial intelligence toward the intricate dynamics of the physical world. While recent advances in Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in video understanding, existing benchmarks remain confined to simple scene-level queries or global summaries that require only single-step inference. Real-world video understanding involves more challenging tasks that require multi-hop multimodal reasoning, and there is a critical absence of video benchmarks equipped to rigorously evaluate these agentic capabilities. To bridge this gap, we introduce AgentVidBench, a multi-hop video question answering benchmark focused on evaluating the spatial, temporal, and causal reasoning capabilities of MLLM agents. Beyond standard question-answer pairs, AgentVidBench provides step-by-step solution traces to support trajectory evaluation that assesses whether agents explicitly acquire the evidence needed to justify their answers. Experiments with 12 proprietary and open-source MLLMs show that single-turn performance remains limited on AgentVidBench, while integrating these models into state-of-the-art agentic workflows generally improves performance with respect to both accuracy and trajectory scores. We further present a simple yet effective agentic strategy that serves as a competitive baseline on AgentVidBench, establishing our benchmark as a holistic testbed for future research on agentic video understanding. Code and datasets are available at this https URL and this https URL.

---


### 70. [Consistent Relexicalization of Clinical Documents using Graph-Based Approach](https://arxiv.org/abs/2609.21387)

**<font color=#1a73e8>作者：</font>** Dipankar Das, Atri Mandal, Sandeep Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relexicalization is a pivotal technique in clinical NLP, as it facilitates robust masking of sensitive information while synthesizing datasets that retain high-fidelity, real-world characteristics. However, preserving structural integrity, relational coherence, and temporal consistency during transformation remains a significant challenge. Existing approaches frequently rely on independent entity replacement, which results in clinical inconsistencies across longitudinal records. This reduces the value of such relexicalized datasets for downstream scientific analysis. To address these limitations, we introduce G-RELIC (Graph Based Contextual Relexicalization with Improved Consistency) which combines the power of LLMs with graphs. G-RELIC implements a graph-based mapping mechanism which optimizes for one-to-one correspondence between original and surrogate entities. It also introduces a deterministic temporal repositioning algorithm to preserve temporal consistency. Empirical evaluations on diverse, real-world clinical datasets validate that G-RELIC significantly outperforms state-of-the-art baselines. G-RELIC yields a 30.4 percentage point improvement in relational integrity (62.1% to 92.5%) and 45.9 percentage point improvement in temporal coherence (46% to 91.9%) without compromising on the recognized privacy benchmarks for clinical datasets. This maximizes the analytical utility of relexicalized datasets while minimizing re-identification risk.

---


### 71. [Offline Multimodal Large Language Models for Decision Support in Air Operations](https://arxiv.org/abs/2609.21390)

**<font color=#1a73e8>作者：</font>** Joao P. A. Dantas, Jelton A. Cunha, Gabriel Dietzsch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Air operations rely on complex rules, established procedures, and time-critical analysis under limited connectivity and strict security constraints. In such environments, analysts must combine written doctrine with images, often without access to external computing resources. This paper studies offline large language models as decision support tools, deployed in isolated and restricted environments to give analysts access to doctrinal knowledge that remains traceable to its original sources through natural language interaction. We describe a modular retrieval-augmented architecture suitable for operation without Internet connectivity, supporting both text and image input from technical manuals. As a first step toward evaluating this architecture, we report a pilot study with four image analysts of the Brazilian Air Force, combining (i) a doctrinal knowledge assessment based on their electronic-target identification doctrine, comparing human and proposed system performance on the same test, and (ii) a measurement of the cognitive workload involved in manually producing a reconnaissance target report (Relatório de Missão de Reconhecimento - REMIR) without AI assistance. The results show a demanding manual task, especially in terms of mental demand (6.0/7) and effort (5.0/7), while the proposed system matches the human score (8/10) and completes the assessment in 7.1 minutes (compared to a human average of 26.5 minutes), establishing a baseline for future AI-assisted evaluation. Finally, we describe a future evaluation protocol to systematically compare manual and AI-assisted workflows.

---


### 72. [Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction](https://arxiv.org/abs/2609.21392)

**<font color=#1a73e8>作者：</font>** Qi Chen, Yunfei Chu, Haolin He 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural audio-visual interaction is emerging as an important interface for AI assistants, allowing users to communicate through speech and vision rather than carefully composed text prompts. However, existing benchmarks of interactive capabilities still focus primarily on response quality, leaving a more fundamental question underexplored: can a model correctly infer the user's underlying demand from complex multimodal interaction? Real-world user demands are often underspecified in speech and must be inferred from multimodal cues and dialogue history. This inference is further complicated by ambiguous or disfluent expression and noisy acoustic environments. Conversely, request-like speech may not constitute a demand to the assistant, leading to false triggers. We establish Omni Demand Understanding (ODU) as a distinct multimodal contextual inference problem: given an interaction stream, a model must detect whether a user demand is present and infer intent from multimodal and conversational context. ODU evaluates this capability along five dimensions, covering both single-turn and multi-turn interactions. We construct ODU-Bench using a challenge-driven taxonomy, taxonomy-guided agentic video generation, and human-recorded interactions, followed by media-grounded annotation and human verification. We evaluate 14 native MLLMs. Even the strongest, Gemini 3.1 Pro, recovers only 44.7% of key information that must be inferred from visual, acoustic, or conversational context. Moreover, 11 of the 14 models exhibit false-trigger rates above 50% on non-demand scenarios. These results reveal a systematic capability gap in current MLLMs' ability to infer contextual user demands. We hope ODU can establish the evaluation of a previously underexplored yet essential capability in multimodal interaction: correctly understanding user demands before generating an appropriate response.

---


### 73. [A Scene Language Model for Open-Vocabulary Scene Mapping](https://arxiv.org/abs/2609.21400)

**<font color=#1a73e8>作者：</font>** Adam Lilja, Fabio Hübel, Siming He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene mapping aims to build a persistent representation of the objects in an environment. Existing systems typically rely on engineered mapping pipelines to associate observations, merge information across views, and maintain a consistent scene representation over time. Many additionally store feature-rich object representations, such as embeddings or image crops, increasing the size and complexity of the persistent memory. We introduce SceneLM, a Scene-Language Model that directly maintains a textual scene map. The full scene is represented as a structured text list of objects, which serves as the model's only persistent memory. For each input image, the model reads the current scene state and updates the map by adding, editing, and removing objects. To learn this behavior, we introduce supervision tasks for iterative scene map maintenance together with an automatic annotation pipeline that generates training data from images without human labels. We evaluate SceneLM on both a language-grounded retrieval benchmark and a localization benchmark. Across both benchmarks, the model produces a scene map that achieves competitive performance with complete mapping systems built from dedicated perception and geometric modules while producing a scene representation that is 6-12x more compact. We further show that SceneLM can be run online on an edge device through experiments on a quadruped. These results show that a persistent open-vocabulary 3D scene map can be maintained directly by a single vision-language model using only a lightweight text representation. Training and inference code is available on this https URL.

---


### 74. [Talking Past the Machine: Morality, Politeness, and Alignment in Human-AI Dialogue](https://arxiv.org/abs/2609.21401)

**<font color=#1a73e8>作者：</font>** Marina Mitiaeva, Lu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems produce fluent, socially appropriate responses, yet whether they participate in cooperative communication or merely simulate its surface forms remains unclear - a question central to how these systems are evaluated, trusted, and designed. This study investigates how morality, politeness, and alignment - three dimensions central to cooperative dialogue - function in human-AI interaction compared to human-human conversation. We analyze 15,881 human-ChatGPT and 10,784 human-human multi-turn dialogues, using mixed-effects models to identify which features predict turn-to-turn alignment. We observe a consistent dissociation: AI produces the surface features of cooperative communication without the underlying social architecture. Moral output appears preconfigured rather than negotiated; warmth is generated without face sensitivity; linguistic convergence declines persistently. Most strikingly, the cooperative mechanisms themselves reverse direction: hedging and softening associated with greater accommodation between humans are associated with reduced alignment when produced by AI, and purity framing associated with human divergence coincides with users converging toward the AI. Agency - giving users room to shape the exchange - is the most consistent predictor of alignment across both interaction types, while lower moral assertiveness in more recent models is not accompanied by better cooperation. Together these patterns suggest that AI reproduces the surface of cooperation without the mutual adaptation that grounds it between humans - and, more surprisingly, that mechanisms sustaining human accommodation can run in reverse with AI, suggesting a turn-level view may be insufficient for interaction-level success.

---


### 75. [DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement](https://arxiv.org/abs/2609.21423)

**<font color=#1a73e8>作者：</font>** Siyuan Liu, Fan Yu, Dongyu Ru 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online agent deployments produce abundant execution traces, while task-specific verification and expert annotation are costly to scale. We study how to distill these traces into reusable feedback without post-hoc outcome labels, drawing on their evidence of local progress, recovery, and unfinished requirements. We introduce DENSE (Distilling Evidence from Nested Subtask Executions), which organizes this evidence into evidence-grounded nested shortcut trees. DENSE compresses redundant attempts, reconciles issues across levels using recovery evidence, and summarizes completed branches while expanding unresolved ones, linking reusable progress to remaining obligations. We introduce REFIT, a source-paired protocol comparing feedback from shared initial trajectories under post-hoc outcome blindness, with environments and model contexts reset for fresh attempts at the same tasks. On Terminal-Bench 2.1, DENSE achieves the highest strict pass rate among tested non-privileged feedback methods across four recipient models. Relative to initial executions, strict pass rate improves by 7.12-15.64 pp, with 19.0-43.6% fewer observed recipient tokens in reruns. GPT-5.5 ablations support combining nested subtask analysis with shortcut construction and issue reconciliation. These findings point toward agent self-refinement through evidence-grounded trajectory reuse with less reliance on external supervision.

---


### 76. [Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework](https://arxiv.org/abs/2609.21425)

**<font color=#1a73e8>作者：</font>** Delun Kong, Wanyun Ling, Chenxi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot time-series forecasting (TSF) is often described as forecasting without target-specific parameter updates, but that training-status condition does not specify what evidence the system may use. A frozen language model prompted with serialized values, a time-series model pretrained on broad forecasting corpora, and a retrieval-augmented forecaster may all satisfy the no-update condition while drawing on different transferable evidence. This paper argues that zero-shot TSF should therefore be governed as an evidence-access claim. We propose a source-first taxonomy that separates three primary evidence sources---frozen LLM prior reuse, parametric time-series pretraining, and retrieval-augmented external memory---from the architectures that implement them. After the source is identified, four additional audit questions remain: task interface, forecast object and scoring, prediction-time context, and resource budget. The resulting agenda is to make zero-shot leaderboards auditable by reporting evidence boundaries and interface assumptions alongside scores, so that benchmark progress reflects transferable forecasting capability rather than undisclosed changes in context, memory, or budget.

---


### 77. [GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/abs/2609.21432)

**<font color=#1a73e8>作者：</font>** Kaichen Zhang, Yuzhong Hong, Junwei Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs). Despite recent advances in post-training methods, such as Group Relative Policy Optimization (GRPO), their practical deployment remains impeded by training instability arising from the reliance on importance sampling.
We introduce Group Variance Policy Optimization (GVPO), a novel post-training method that integrates the analytical solution of KL-constrained reward maximization into its gradient weighting scheme. This formulation provides an intuitive interpretation: GVPO's gradient corresponds to the mean squared error between the central distance of implicit rewards and that of actual rewards. GVPO offers two key advantages: (1) it guarantees a unique optimal solution, exactly to the KL-constrained reward maximization objective, and (2) it enables flexible sampling distributions without requiring importance sampling.
Beyond general post-training, we show that GVPO naturally extends to on-policy distillation (OPD). Furthermore, GVPO enables the optimization of a broad family of extended OPD objectives, providing a principled foundation for diverse objective design. By unifying theoretical guarantees with practical adaptability, GVPO establishes a new paradigm for reliable and versatile LLM post-training and on-policy distillation.

---


### 78. [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](https://arxiv.org/abs/2609.21450)

**<font color=#1a73e8>作者：</font>** Yamato Narita, Issei Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution. Although weight optimization, channel-wise scaling, and orthogonal rotation mitigate this problem, the error components they address and their relationship remain unclear. Using an exact decomposition of local weight-activation quantization error into an activation-guided weight compensation term and an orthogonal residual, we bound the residual using persistent channel-wise outlier and regular activation quantities. This decomposition clarifies which error components can be addressed by weight compensation and which require transformation design. We then use the residual bounds to derive practical guidelines for applying randomized Hadamard rotation, sign selection, and channel scaling. In particular, the analysis explains how random signs suppress constructive interference among persistent outlier channels, how sampling multiple sign patterns can improve transformation selection, and how second-moment balancing leads to an $L_2$ scaling rule while a further relaxation recovers SmoothQuant-style $L_\infty$ scaling. We evaluate these guidelines through backpropagation-free configurations across eight Llama and Mistral models, obtaining performance competitive with gradient-trained SpinQuant.

---


### 79. [LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers](https://arxiv.org/abs/2609.21492)

**<font color=#1a73e8>作者：</font>** Jingyu Hu, Shu Yang, Weiru Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has been shown to improve the performance of large language models (LLMs), yet existing optimization methods largely rely on outcome-based feedback, leaving the logical validity of intermediate reasoning steps largely unverified. To address the gap whereby LLMs arrive at correct final answers through logically flawed intermediate reasoning chains, we propose LogicTrack, a neuro-symbolic framework that audits reasoning trajectories by auto-formalizing each reasoning step into symbolic representations and verifying it with automated theorem provers. LogicTrack introduces Solver-Based Backtracking Reward (SBR), a step-wise scoring mechanism that quantifies logical soundness and guides backtracking tree search at inference time. We further extend LogicTrack to construct supervised fine-tuning (SFT) data with backtracking traces from its trajectories, enabling fine-tuned models to internalize step-wise auditing as an intrinsic capability. Extensive experiments across 8 reasoning benchmarks and 7 LLMs demonstrate that LogicTrack effectively improves both the verifiability of reasoning chains and final answer pass rate, thereby enhancing overall CoT quality and trustworthiness in high-stakes domains.

---


### 80. [PolyBridgeBench: Benchmarking Multimodal LLMs for Physics-Grounded Bridge Design](https://arxiv.org/abs/2609.21493)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Dongyin Chen, Rui Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models, or MLLMs, perform well at visual understanding and structured generation, yet these capabilities do not establish whether an engineering design will work when executed. Existing benchmarks assess spatial reasoning, structural validity, or physics-grounded construction, but they do not determine whether MLLMs can synthesize complete load-bearing structures and repair them after simulator execution exposes a failure. We introduce PolyBridgeBench, an executable benchmark for multimodal bridge design. A model receives a visual scene and structured engineering constraints and generates a complete node--member--material topology. Deterministic legality checks gate execution in a native dynamic physics simulation. Following an execution failure, the benchmark returns temporal visual evidence from the failed rollout and evaluates repair under a fixed interaction budget. Separate measurements of deterministic validity, dynamic functional success, and post-failure recovery identify the stage at which design fails. Experiments with six representative MLLMs across 189 levels expose a substantial gap between deterministic validity and dynamic success, pronounced sensitivity to material budgets, and limited post-failure recovery under the primary strict-budget setting.

---


### 81. [The Communication Bottleneck: A Round-Trip Study of Tree-Structured Expression Serialization in Language Models](https://arxiv.org/abs/2609.21509)

**<font color=#1a73e8>作者：</font>** Xavier Suau, Alex Ferrando de las Morenas, Luca Zappella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When language models reason in chain-of-thought or exchange free-text intermediates, they serialize structured information into natural language. How much tree-structured compositional content survives this bottleneck? We propose a round-trip protocol that answers this question empirically for tree-structured expressions. A generator converts a procedurally generated arithmetic expression into a word problem, a separate extractor recovers the expression from the word problem alone, and symbolic equivalence provides an exact oracle. Evaluating all pairwise combinations of sixteen models yields a communication matrix whose marginals separate generation quality from extraction quality. Three main findings emerge. First, the channel is lossy and asymmetric: swapping which model generates and which extracts shifts accuracy by up to 60.4 points, and the best pair reaches 92.9% by combining different models on each end rather than the same model on both. Second, at least 73.6% of round-trip failures originate at generation, and difficulty is driven by tree structure (operator count, depth, right-branching) rather than model family. Third, the channel is trainable: ~3600 fine-tuning examples that share the evaluation's operators and tree shapes lift every open-weight model above untrained Gemini-3.1-Pro, an upper bound under matched semantics. A disjoint-domain regime with new operators and vocabulary also raises every open-weight model, confirming the gain is not an artifact of matched semantics, though a gap to the frontier remains. Together these results identify tree-structured expression serialization as a primary limiting factor when models communicate hierarchical structure through natural language.

---


### 82. [ServeGuard: Verifiable, Bounded-Residual Confinement of Operator-Invisible Channels Without Revealing the Certified Read Factor](https://arxiv.org/abs/2609.21515)

**<font color=#1a73e8>作者：</font>** Dominik Dahlem, Rui Vieira  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party adapters for open-weight language models ship as opaque weight matrices; a recipient cannot check whether an adapter hides a backdoor without trusting the publisher or inspecting the weights, the publisher's core asset. For one important class (payloads placed where a safety monitor is structurally blind), detection is unsound as a defense: every detector that factors through the declared monitor is invariant on its blind subspace, and honest and backdoored adapters overlap on every blind-subspace statistic we evaluate, because benign adaptation uses that subspace too. Rather than detect this channel, we make it structurally \emph{absent} and prove that we did. The publisher builds the adapter to read the input only through directions the monitor covers and proves this in zero knowledge, revealing nothing about the read factor it certifies. The certificate is cheap because the expensive part, identifying the monitor's blind spot, is a deterministic function of the \emph{public} base model, so only one linear identity is proved; the served residual is the base model's own public floor, not a prover-chosen tolerance. The result is \emph{ServeGuard}, a supply-chain primitive: the publisher ships a \emph{proof-carrying adapter} whose proof lets a consumer or regulator verify, without the certified read factor and without trusting the publisher, that the adapter carries no hidden channel of this class relative to the declared monitor; an admission-time typing guard binds the guarantee to the adapter bytes admitted at serving time. Across eight checkpoints up to 7B from four families, the monitoring budget is architectural: the measured frontier saturates at the value-path rank on grouped-query checkpoints but not on multi-head ones. On a 0.5B model confinement is nearly free for benign adaptation, making monitor quality the security lever.

---


### 83. [VidOmni-Bench: A Benchmark for Fine-Grained Video Understanding via Spatio-Temporal Event Verification across Complexity and Duration](https://arxiv.org/abs/2609.21521)

**<font color=#1a73e8>作者：</font>** Changbeen Kim, Junwon Chang, Kipyo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Video Large Language Models (Video-LLMs) have recently demonstrated strong performance, reliably evaluating their fine-grained video understanding remains challenging. Existing benchmarks often rely on question answering or ground-truth caption matching, where models may succeed through superficial cues and incomplete annotations. To this end, we introduce VidOmni-Bench, a benchmark that requires models to verify whether each event in dense video captions is supported by the video. VidOmni-Bench consists of 500 videos spanning five complexity types and diverse durations from 4 seconds to 90 minutes. After collecting videos along these axes, we use diverse Video-LLMs to generate dense captions and obtain human-verified sentence-level labels, where sentences containing incorrect events serve as hard negatives for evaluation. Our experiments on VidOmni-Bench reveal three key findings: (i) Video-LLMs frequently generate hallucinated descriptions in dense video captioning; (ii) they also struggle as verifiers, failing to reliably detect plausible but incorrect event descriptions; and (iii) model weaknesses vary across video complexity and duration, revealing diverse, model-specific bottlenecks in current Video-LLMs.

---


### 84. [OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems](https://arxiv.org/abs/2609.21527)

**<font color=#1a73e8>作者：</font>** Kairui Yang, Xunkai Li, Kaixiang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluation attribution problem, we introduce OpenMAS-GCom, a benchmark for diagnosing how these components affect G-MAS performance through controlled interventions. We represent systems through collaboration units, communication links, shared intermediate information, and execution rules. OpenMAS-GCom compares original systems with versions modified by changing one component while keeping tasks, models, prompts, and budget limits fixed. We rewire communication edges, remove specialist or critic agents, replace intermediate messages with incorrect content, and disable workers during execution. The benchmark evaluates 17 single-agent, ordinary multi-agent, and graph-enhanced configurations on 29 datasets across six domains. We add 400 G-MAS-Complex tasks requiring agents to combine information from multiple documents, resolve conflicting records, and return specified values with source identifiers. Experiments show larger mean losses after specialist removal than after critic removal, different performance degradation under incorrect messages and worker failures despite similar original scores, and different configurations achieving the highest accuracy and accuracy per token on G-MAS-Complex.

---


### 85. [MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems](https://arxiv.org/abs/2609.21533)

**<font color=#1a73e8>作者：</font>** Kairui Yang, Minghao An, Xunkai Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems generate collaboration traces that record how agents plan tasks, verify intermediate results, and repair failures. Reusing these procedures requires preserving an action's prerequisites and the outputs needed by subsequent agents. Our empirical studies show that grouping these dependencies into functional memory units improves their retention, while connecting units increases retrieval of the units and links jointly required by a task. The preferred combination of units also changes between instructions and checklists, even when each combination's content is fixed across formats. Updating choices from the outcomes of each combination and format pairing outperforms scoring combinations and formats separately. These findings motivate MACE, a memory-agent co-evolution framework that adapts memory organization and agent memory use through execution feedback. Its MemGoG structure represents functional units as subgraphs of related conditions, actions, and outputs, connecting them through support, conflict, and repair relations. MACE Loop selects task-relevant units and relations within a memory budget and provides each agent with instructions or checklists for its current operation. It records the selected units, presentation formats, agent outputs, and task outcomes to update unit scores and relations for retrieval and inform subsequent presentation choices. Across eight benchmarks, MACE outperforms ten baselines with an average score of 81.11%, compared with 78.97% for the strongest baseline, SAGE.

---


### 86. [From Retrieval to Recognition:How Vision--Language Models Become OCR Specialists](https://arxiv.org/abs/2609.21543)

**<font color=#1a73e8>作者：</font>** Yuanxiang Huangfu, Hanmeng Zhong, Linqing Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Does a general vision--language model acquire specialized OCR ability by developing a new reading circuit or by reusing an existing mechanism? We address this question in the setting of full-sequence OCR, rather than local-answer retrieval. Using an evidence-grounded protocol with held-out causal interventions, we identify sparse and stable OCR-head sets in GLM-OCR, MinerU2.5, and PaddleOCR-VL-1.6. We then investigate the mechanistic origin of these OCR heads by comparing them with independently identified textual retrieval/copy heads in general VLMs. Across two general VLMs, visual OCR heads strongly overlap independently identified textual retrieval/copy heads, yielding untuned top-20 intersections of 73.3% and all-head Spearman correlations of 0.677-0.886. The overlap and causal interventions suggest that full-sequence OCR operates as dense sequential multimodal copy-and-paste, repeatedly retrieving visual evidence and routing it to the current output position. Finally, we examine how this shared circuit changes as a general VLM becomes an OCR specialist. Matched base-to-specialized comparisons show that OCR specialization largely preserves head identity, retaining 17-20 of the top 20 heads per task with all-head rank correlations of 0.874-0.942, while redistributing their functional and causal strengths.

---


### 87. [OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios](https://arxiv.org/abs/2609.21550)

**<font color=#1a73e8>作者：</font>** Yewen Li, Peng Jiang, Yitian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding is central to computational advertising, where strategies must maximize advertisers' conversion value under economic constraints. It has evolved from rule-based controllers to reinforcement learning and generative methods such as Decision Transformer (DT). Yet these methods increasingly mismatch the prevailing optimized cost-per-X (oCPX) paradigm, which spans heterogeneous scenarios (e.g., registration, purchase), each served by a separate model, leading to fragmented pipelines and underexploring cross-scenario modeling. Inspired by foundation models like LLMs, unifying these oCPX scenarios into one model raises three challenges: multi-objective control, scalable capacity under strict latency, and safe offline policy improvement. We present OneBid, a unified auto-bidding foundation model that learns a reusable backbone from heterogeneous oCPX logs and adapts it to scenario-specific deployments via offline post-training. Building on DT, OneBid extends single Return-to-Go conditioning to two atomic signals, Return-to-Go for conversion value and Cost-to-Go for cost ratio, plus value-aware regularization on next-action prediction. To absorb distributional heterogeneity, we design a sequence-level Mixture-of-Experts architecture, where shared experts encode cross-scenario knowledge and sparsely-routed experts capture scenario-specific patterns at low latency, yielding consistent scaling with model size and data. During post-training, we align the backbone with scenario preferences via Critic-guided Relative Offline Policy optimization (CROP): a learned critic scores candidate actions group-relatively, avoiding the unsafe online exploration of GRPO-style fine-tuning while constraining policy shift to reduce OOD risk. Validated via online A/B tests and fully deployed at Kuaishou, OneBid delivers an overall +2.2% ADVV gain on oCPX Ads, peaking at +13.1% in the ROAS scenario.

---


### 88. [MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance](https://arxiv.org/abs/2609.21554)

**<font color=#1a73e8>作者：</font>** Arash Lagzian, Srinivas Anumasa, Dianbo Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have revolutionized artificial intelligence and how human interact with AIs. Despite impressive advancements, LLMs struggle with complex mathematical, scientific, and logical tasks. Inspired by human cognitive flexibility - our ability to dynamically switch mental perspectives - we propose MIRAGE (Multi-perspective Inference-time Reasoning via Agent-Guided Exploration), a novel inference-time creative thinking framework. MIRAGE includes a Selector that prioritizes effective conceptual perspectives (e.g., algebraic, probabilistic) and a Reasoner that sequentially solves tasks until a confident solution emerges, otherwise aggregating multiple perspectives. Tested on GSM8K, MATH500, MMLU-Pro, and Game-of-24 benchmarks, MIRAGE consistently outperforms methods like Chain-of-Thought and diverse prompting ensembles, significantly boosting accuracy with minimal inference overhead, providing a scalable solution for practical applications.

---


### 89. [Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel](https://arxiv.org/abs/2609.21569)

**<font color=#1a73e8>作者：</font>** Jiaji He, Yi Shi, Junfeng Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent generations of Apple MacBooks embed an inertial measurement unit (IMU) within their unibody chassis for device orientation and motion sensing. However, this IMU inadvertently captures not only intended device-level information but also subtle physical vibrations from user interactions and the surrounding environment. These signals establish a novel, previously unexplored side channel. We uncover a vulnerability allowing non-root access to IMU data via an IOKit driver, alongside two content-free system metadata interfaces (HIDIdleTime and CGEventSource) that further enrich the side-channel leakage. Through rigorous characterization of the IMU data, we reveal that the leakage spans three core dimensions: (1) keystroke identity (which key is typed), (2) desk surface (where the laptop is placed), and (3) user behavior (who is typing). Leveraging these findings, we introduce BRUTUS, the first comprehensive unprivileged side-channel attack targeting built-in IMU sensors on Apple MacBooks. BRUTUS achieves a character-level accuracy of 89.1% to 97.5% in key recovery. Furthermore, aided by language models, it can successfully reconstruct certain sentences with 100% accuracy. For user identification and environment profiling, BRUTUS correctly discovers user and environment profiles without labels and correctly assigns subsequent segments to their corresponding profiles. Ultimately, this work highlights the urgent necessity of strictly regulating access to built-in IMU sensors.

---


### 90. [Evaluating In-Context Learning and Retrieval Strategies for Devanagari Post-OCR Correction](https://arxiv.org/abs/2609.21595)

**<font color=#1a73e8>作者：</font>** Abhishek Bhandari, Gaurav Harit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning using Large Language Models (LLMs) offers a compelling path to training-free post-OCR correction, yet its effectiveness for Devanagari script remains entirely unexplored. We present the first systematic evaluation of LLMs (3B-32B) for post-OCR correction in Hindi and Marathi, comparing three in-context example retrieval strategies: domain-random selection, dense semantic retrieval, and our proposed CharBM25, which retrieves examples by character n-gram BM25 similarity over OCR inputs to target shared error patterns with the test sentence. Across a 20,000-sentence benchmark spanning five news domains, retrieval strategy is the decisive factor in correction quality: CharBM25 outperforms domain-random selection by 2.8-4.0pp absolute WER on Hindi and 2.9-3.8pp on Marathi, using character trigrams, which consistently outperform bigrams and unigrams. Scale dominates performance: Gemma-3-27B achieves WER reductions of 55.0% for Hindi and 33.3% for Marathi under CharBM25-5. Few-shot gains are capacity-gated: models below 8B do not reliably improve over the OCR baseline, and on Marathi the smallest models (3B) degrade more sentences than they improve. Marathi is persistently harder to correct than Hindi across all scales, reflecting its greater morphological complexity. These findings establish CharBM25 as an effective, GPU-free retrieval strategy that matches or exceeds dense retrieval at negligible computational cost, and show that combining it with a general-purpose LLM of 12B+ parameters delivers reliable, training-free Devanagari post-OCR correction without task-specific fine-tuning. Dataset: this https URL

---


### 91. [Reducing Barriers to Academic Support: Evaluating a Course-Specific RAG System for Addressing Help-Seeking Disparities in Higher Education](https://arxiv.org/abs/2609.21600)

**<font color=#1a73e8>作者：</font>** Andy Gray, Jake Hobbs  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Access to academic support is a key determinant of student success, yet students experience it unequally: some readily seek help from lecturers or tutors, while others hesitate due to anxiety, fear of judgement, uncertainty about expectations, or low confidence in their understanding. This may be especially evident in computing education, where programming tasks are cumulative and cognitively demanding. Although students increasingly turn to general-purpose generative AI tools, these can produce responses that are inaccurate, insufficiently contextualised, or misaligned with module expectations. This study presents and evaluates Beacon, a course-specific Retrieval-Augmented Generation (RAG) system providing private, immediate, module-aligned academic support. Grounding responses in approved teaching materials, Beacon was designed to lower barriers to help-seeking while encouraging independent learning. Using a design-based research approach, Beacon was developed iteratively and evaluated via mixed methods, combining questionnaires and semi-structured interviews with students and staff at a Higher Education institution. Students described Beacon's responses as closely aligned with module content and more trustworthy than unrestricted generative AI tools, valuing its use of pseudocode and scaffolded explanations over direct solutions. Although participants remained cautious about trusting AI-generated responses without verification, they viewed the system as a valuable first point of support before consulting lecturers or official resources. The findings suggest that carefully designed course-specific AI systems may reduce barriers to academic support by occupying an intermediary space between independent study and formal support. Rather than replacing educators, educational AI may be most valuable when it broadens access to guidance while preserving the pedagogical role of lecturers.

---


### 92. [Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/abs/2609.21619)

**<font color=#1a73e8>作者：</font>** Qiangqiang He, Jin Li, MingCai Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves reasoning models by learning the token-level discrepancy between a stronger teacher and an on-policy student. However, this discrepancy does not purely reflect the capability gap between the teacher and the student: it also contains deviations arising from the teacher itself, which are consequently mixed into the observed teacher--student discrepancy and indiscriminately learned by standard OPD during training. This issue is further exacerbated by privileged OPD, where privileged information induces larger teacher-side likelihood shifts, thereby encouraging the student to learn more of the teacher's own deviation. We introduce \textbf{Calibrated On-Policy Distillation (Cal-OPD)}, which estimates the teacher's self-deviation region through positive and negative privileged interventions and calibrates the original teacher--student discrepancy by retaining only the component that lies beyond this region. Experiments on mathematical reasoning benchmarks show that, while retaining only about 52--65\% of the original teacher--student discrepancy as the optimization signal, Cal-OPD consistently outperforms standard OPD and its variants across model scales.

---


### 93. [One Prompt Does Not Fit All: Self-Meta-Evolve for Personalized Information Extraction](https://arxiv.org/abs/2609.21626)

**<font color=#1a73e8>作者：</font>** Hongliang Li, Lu Wang, Yong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed for enterprise information extraction (IE), where the same document must be reorganized differently for each user. Existing prompt optimization methods, however, rely on a single prompt optimized against a global objective, which is misaligned with the inherent user heterogeneity of real workplaces. We formulate enterprise IE as per-user prompt adaptation under interaction feedback and propose Self-Meta-Evolve, a hierarchical framework that maintains a dedicated prompt for each user and continuously refines it through a dual-loop process: an inner loop that edits structured prompts based on persona-conditioned feedback, and an outer loop that evolves the meta-prompt itself by distilling successful editing patterns. To enable scalable training and evaluation, we release a persona-driven IE benchmark of 292 simulated enterprise users, paired with a reproducible persona-generation pipeline grounded in O*NET occupational taxonomies. On this benchmark, Self-Meta-Evolve achieves a 74.58% success rate, outperforming the strongest prompt-optimization baseline by 13.56 absolute points, and reaches 52.54\% within only two iterations. A double-blind human study with twenty real professionals further confirms that prompts adapted by our framework win against static baselines in 71% of pairwise comparisons.

---


### 94. [Steering LLMs Responses Towards Moral Foundations on the Norwegian MFQ-30](https://arxiv.org/abs/2609.21636)

**<font color=#1a73e8>作者：</font>** Hans Andersen, David Dichas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work applies human psychometric questionnaires to large language models to elicit moral and value profiles, but it is not clear whether these instruments measure anything stable in models or whether the resulting profiles can be moved toward a target human population. We administer the Norwegian Moral Foundations Questionnaire (MFQ-30) to six open-weight LLMs and compare their foundation profiles to a sample of N = 1,282 Norwegian respondents. We test two steering interventions, prompt-level persona steering and activation-level ActAdd. Half the models engage with the questionnaire under our attention check. The other half default to flat or central-tendency outputs that look near-human on average without tracking item content. A neutral Nordic-respondent persona, written without any distributional information from the human sample, brings the engaging models 44-77% closer to the Norwegian mean in Mahalanobis $d^2$. One-pair ActAdd at a fixed mid-layer flattens the foundation profile rather than steering individual foundations. For at least one model the same persona that shifts the profile also induces engagement that was absent at baseline, a concrete instance of the cognitive phantoms that Peereboom et al. (2025) warn about.

---


### 95. [Chinese Competitive Debating Dataset and Benchmark](https://arxiv.org/abs/2609.21637)

**<font color=#1a73e8>作者：</font>** Zongrui Yang, Haoyuan Li, Zhongsheng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Debate adjudication requires tracking how arguments develop through interaction, yet existing datasets rarely combine fine-grained debate transcripts with professional judgments collected during real competitions under a shared rubric. We introduce a dataset and benchmark for evaluating large language models' understanding of competitive Chinese-language debate at the match, stage, and speaker levels. We organized 182 matches and recruited 120 professional judges, with each match independently adjudicated by three judges using a predefined rubric. After excluding matches with incomplete records, the dataset contains 148 matches, 2,698 stages, and 20,542 exchange units, with manually verified transcripts and segmentation. It preserves original stage scores, match votes, best-debater ballots, and adjudication rationales. We define three tasks: winner-tendency prediction, stage-score prediction, and best-debater prediction. Zero-shot evaluation of multiple large language models yields a highest winner-prediction accuracy of 66.2%, a highest Pearson correlation of 0.250 between model stage scores and mean human ratings, and a highest best-debater prediction accuracy of 56.8%. The dataset and benchmark provide a testbed for studying large language models' understanding of interactive argumentation and their agreement with professional judges.

---


### 96. [Configurable Multi-Stage Vision Pipeline for Crop Disease and Pest Diagnosis](https://arxiv.org/abs/2609.21651)

**<font color=#1a73e8>作者：</font>** Naga Ganesh, Chandrashekar M S, Lakshmi Pedapudi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> this http URL is Digital Green's farm advisory service for smallholder farmers. When something looks wrong with a crop, the farmer takes a photograph and sends it, and that photograph is the whole question: no symptom described, no crop named, often no text at all. The service has to determine whether the picture can be used, what crop it shows, and what is wrong with it, from images taken on cheap phones in a field, in poor light and with a moving camera. The system doing this today cannot be adjusted. It has no adjustable thresholds for photograph rejection, crops and problems cannot be added, and there is no confidence cut-off to set.
We study about 1.16 million photographs sent to this http URL from Ethiopia, India, Kenya and Nigeria. The production quality gate rejected 46.8% of the images it judged, over a quarter of those reaching diagnosis returned no crop name, and 35.8% of the labelled problems filed under "disease" are pests, identifiable without the crop. We therefore split the work into three stages: a quality gate (M0), a crop detector (M1), and a disease or pest detector (M2). Route A fills all three with one fine-tuned vision-language model (Qwen3-VL-4B) answering in a single call. Route B fills each with a small specialist model (DaViT, YOLO26).
We replace our production GPT-4o quality gate with a small MobileNetV3 gate at 86.9% F1 in 12 ms. On one test set scored the same way for every system, a hierarchical DaViT-Base achieves 95.41% crop accuracy against 91.46% for the production baseline. It also leads on diagnosis and never declines to answer, while every language model in the comparison leaves a large share of rows with no diagnosis. The fine-tuned model retains two capabilities the specialists do not have: one call for all three stages, and a request for a better photograph when the image cannot support an answer.

---


### 97. [Analysing the Linearity of Linguistic Relations in Language Model Embedding Spaces](https://arxiv.org/abs/2609.21655)

**<font color=#1a73e8>作者：</font>** Vasudevan Nedumpozhimana, Fathima Thekkekara, John Kelleher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a framework to analyse how strongly different linguistic relations are linearly encoded in language model embedding spaces. We formalise linear encoding via a constrained linear approximation over related and unrelated word pairs and apply this to an extended BATS dataset covering inflectional, derivational, lexicographic, and encyclopedic relations in GloVe, RoBERTa, and ModernBERT. Our experiments show near-perfect linear encodings for inflectional and derivational relations, but substantially higher errors for lexicographic and encyclopedic relations, especially for one-to-many and many-to-many associations. We also find that RoBERTa and ModernBERT generally encode relations more linearly than GloVe. These results indicate that our framework can reveal which relational structures are most linearly accessible in embeddings, offering a compact tool for probing and comparing relational geometry across models.

---


### 98. [When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap](https://arxiv.org/abs/2609.21662)

**<font color=#1a73e8>作者：</font>** Gaoxiang Huang, Lei Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has become a widely used approach for controlling language models during explicit chain-of-thought (CoT) reasoning, motivating its extension to latent CoT. However, we find that steering continuous thoughts produces substantially weaker effects on subsequent language generation than steering explicit CoT, even when the hidden representations are moved by comparable amounts. We first show that task information remains identifiable in continuous thoughts. Hence, we hypothesize a \textbf{latent-to-language transition gap}, in which an intervention effect in latent space fails to transfer to language generation. Two further results support this hypothesis: the output distribution changes abruptly at the transition boundary, and task-related directions exert much weaker bidirectional control in latent CoT than in explicit CoT. These findings identify the transition interface as a central target for evaluating and designing future latent-steering methods.

---


### 99. [Rethinking Human-Aligned Evaluation: An Analysis of Semantic Metrics Beyond WER](https://arxiv.org/abs/2609.21663)

**<font color=#1a73e8>作者：</font>** Hritika Sharma, Thibault Bañeras-Roux, Alessandra Pinto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word Error Rate (WER), the most commonly used metric for Automatic Speech Recognition (ASR), treats every lexical deviation from the reference as equally costly, regardless of whether it changes meaning. This raises the question: does WER actually track how humans judge ASR transcript quality? We introduce HATS-en, an English dataset for human-centered ASR evaluation. Using this dataset, we benchmark lexical metrics against several configurations of BERTScore and SemDist, varying the language model, layer, and pooling strategy. We find that WER agrees least with human judgment among all metrics tested, that the best-performing SemDist configurations achieve the highest overall agreement, ahead of CER and BERTScore, and that no single model is best across settings. CER, despite its simplicity and low cost, remains remarkably close to these best configurations. In line with prior recommendations, our results support shifting ASR evaluation toward CER both for English and for morphosyllabic writing systems as it is a more interpretable and low-cost metric for what evaluation should actually capture, and using SemDist as a complementary evaluation.

---


### 100. [Accelerating Dense LLMs via L0-regularized Mixture-of-Experts](https://arxiv.org/abs/2609.21672)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang, Jiudong Yang, Zhaowen Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance but suffer from slow and costly inference. Existing acceleration methods often lead to noticeable performance degradation, while Mixture-of-Experts (MoE) models require extensive computational resources. In this paper, we propose L0-MoE, a lightweight MoE approach using L0-regularization to accelerate dense LLMs nearly without performance loss. Our method introduces a cluster confusion matrix for domain-aware dataset curation and applies dynamic batching for efficient training. Experiments show that L0-MoE achieves up to 2.5x speedup over dense models while maintaining competitive performance, outperforming existing LLM acceleration baselines.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-148](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
