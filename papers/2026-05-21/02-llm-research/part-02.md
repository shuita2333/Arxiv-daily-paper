# 🧠 大模型相关研究 | 2026年05月21日

> 本类共 **172** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-172](./part-04.md)

---

### 51. [POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents](https://arxiv.org/abs/2605.19127)

**<font color=#1a73e8>作者：</font>** Qiaoyuan Zheng, Yiqu Yang, Qi Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly have access to private user data and act on the user's behalf when interacting with third-party systems. The user defines what may and must not be shared, and the agent must robustly follow that intent even when third-party systems behave adversarially. We introduce POLAR-Bench (Policy-aware adversarial Benchmark), in which a trusted model with a privacy policy and a task converses with a third-party model that adversarially probes for both task-relevant and protected attributes. Across 10 domains and 7,852 samples, we score privacy and utility by deterministic set-membership and vary privacy policy dimension and attack strategy along two orthogonal axes, producing a 5 times 5 diagnostic surface per model. Our results reveal a sharp split: current frontier models withhold over 99% of protected attributes, while smaller open-weight models in the 1--30B range, the class users most commonly run as their own trusted agent on-device or via private inference, score notably worse, with the weakest leaking over half. POLAR-Bench thus localizes where each model's intent-following breaks down, providing a foothold for privacy alignment where it matters most.

---


### 52. [EgoBabyVLM: Benchmarking Cross-Modal Learning from Naturalistic Egocentric Video Data](https://arxiv.org/abs/2605.19130)

**<font color=#1a73e8>作者：</font>** Dongyan Lin, Phillip Rust, Angel Villar Corrales 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Children acquire language grounding with remarkable robustness from limited visuo-linguistic input in ways that surpass today's best large multimodal models. Recent research suggests current vision-language models (VLMs) trained on curated web data fail to generalize to the sparse, weakly-aligned egocentric streams produced by wearable devices, embodied agents, and infant head-cams -- and no fixed evaluation pipeline exists for measuring progress on this regime. We train VLMs on datasets with varying degrees of semantic alignment between visual and linguistic inputs, including naturalistic infant and adult egocentric videos, and evaluate them with a comprehensive suite spanning multimodal language grounding and unimodal vision and language tasks. At the core of this suite is Machine-DevBench, a corpus-grounded benchmark of lexical and grammatical competence, automatically generated from the model's training vocabulary across logarithmic frequency bins to eliminate the train/eval mismatch and low statistical power of prior developmental benchmarks. Our results show that current VLM paradigms hinge on the tight semantic alignment of curated data and fail to exploit the weakly-aligned signal that dominates naturalistic egocentric input -- the very regime in which humans thrive. To motivate progress, we introduce the EgoBabyVLM Challenge to drive the development of models capable of grounded language learning from the kind of naturalistic data that human infants experience.

---


### 53. [Identifiable Multimodal Causal Representation Learning under Partial Latent Sharing](https://arxiv.org/abs/2605.19135)

**<font color=#1a73e8>作者：</font>** Manal Benhamza, Marianne Clausel, Myriam Tami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal representation learning (CRL) seeks to uncover meaningful latent variables and their corresponding causal structure from high-dimensional observational data. Although its significance, CRL identifiability remains a crucial property, as it ensures the recovery of the mechanisms behind the data generation process, and hence the interpretability and robustness of the representation. Proving identifiability in CRL is intrinsically difficult, and we address in this work an even more challenging setting: multimodality. We consider multimodal observed data with a latent partially shared structure. Each modality is generated, through non linear mixing functions, from a specific subset of causal latent variables. Under flexible assumptions and without imposing any parametric distribution on the latent variables, we establish component-wise identifiability guarantees for the causal latent representation. Our identifiability results, furthermore, apply to the undercomplete scenario where we have, for each modality, more observed than latent variables. To instantiate our theoretical analysis, we introduce a Wasserstein-based module to recover the partially shared latent structure. Due to its differentiability, the latter can be easily integrated into all types of architecture, only requiring minimal changes. Extensive experiments on synthetic and realistic datasets validate the superiority of our approach over SOTA methods.

---


### 54. [Towards Data-Efficient Video Pre-training with Frozen Image Foundation Models](https://arxiv.org/abs/2605.19137)

**<font color=#1a73e8>作者：</font>** Svetlana Orlova, Niccolò Cavagnero, Gijs Dubbelman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foundation models achieve strong performance across many video understanding tasks, but typically require large-scale pre-training on massive video datasets, resulting in substantial data and compute costs. In contrast, modern image foundation models already provide powerful spatial representations. This raises an important question: can competitive video models be built by reusing these spatial representations and pre-training only for temporal reasoning? We take initial steps toward exploring a lightweight training paradigm that freezes a pre-trained image foundation model and trains only a recurrent temporal module to process streaming video. By reusing an image foundation model as a spatial encoder, this approach could significantly reduce the amount of video data and compute required compared to end-to-end video pre-training. In this work, we explore the feasibility of this approach before investing in computing for video pre-training. Our empirical findings across multiple video understanding tasks suggest that strong temporal performance can emerge without large-scale video pre-training, motivating future work on recurrent video foundation models obtained by pre-training a temporal module on top of a frozen image foundation model. Code: this https URL .

---


### 55. [Progressive Autonomy as Preference Learning: A Formalization of Trust Calibration for Agentic Tool Use](https://arxiv.org/abs/2605.19151)

**<font color=#1a73e8>作者：</font>** Changkun Ou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formalize trust calibration for agentic tool use (deciding when an automated agent's proposed action may execute autonomously versus require human approval) as a preference-learning problem. A policy gateway maintains a Gaussian-process posterior over a latent human risk-tolerance function, observed through a probit likelihood on binary approve/deny feedback, and escalates to the human exactly where the approval outcome is most uncertain. We show this is structurally an instance of Preferential Bayesian Optimization, inheriting its inference machinery (approximate Gaussian-process classification) and its sample-efficiency argument (uncertainty-targeted querying), while differing in objective: classifying an action space into allow/block/ask regions rather than optimizing a design.

---


### 56. [Prompting language influences diagnostic reasoning and accuracy of large language models](https://arxiv.org/abs/2605.19173)

**<font color=#1a73e8>作者：</font>** Adrien Bazoge, Josselin Corvellec, Sofiane Djillali Sid-Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored for clinical decision support, yet most evaluations are conducted in English, leaving their reliability in other languages uncertain. Here we evaluate the impact of prompting language on diagnostic reasoning and final diagnosis accuracy by comparing English and French performance across five LLMs (o3, DeepSeek-R1, GPT-4-Turbo, Llama-3.1-405B-Instruct, and BioMistral-7B). A total of 180 clinical vignettes covering 16 medical specialties were assessed by two physicians using an 18-point scale evaluating both diagnosis accuracy and reasoning quality. Four of the five models performed better in English (mean difference 0.37-0.91, adjusted p < 0.05), with the gap spanning multiple aspects of reasoning, including differential diagnosis, logical structure, and internal validity. o3 was the only model showing no overall language effect. These findings demonstrate that prompting language remains a critical determinant of LLM clinical performance, with implications for equitable linguistico-cultural deployment worldwide.

---


### 57. [Discoverable Agent Knowledge -- A Formal Framework for Agentic KG Affordances (Extended Version)](https://arxiv.org/abs/2605.19186)

**<font color=#1a73e8>作者：</font>** Terry R. Payne, Valentina Tamma, Enrico Daga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two decades ago, the Semantic Web Services community was asked how agents with different ontological commitments could discover, compose, and invoke web services coherently. The response was OWL-S and WSMO: formally grounded capability descriptions specifying what a service could do, what the agent must already know for invocation to be epistemically sound, and how ontological mismatches could be formally bridged. Current Knowledge Graph (KG) metadata standards such as VoID and DCAT describe what a KG contains yet say nothing about what a specific agent can prove from it, what closure assumptions govern empty results, or whether the agent's task vocabulary is grounded in the schema. Furthermore, in deployed KGs the governing schema DL and the operative entailment regime can diverge: an epistemic failure mode invisible to current metadata. We revisit and extend these insights for the KG setting with a four-dimensional formal framework from which we derive the Agentic Affordance Profile (AAP): a semantic layer above VoID and DCAT enabling principled KG selection, composition, and failure diagnosis at agent planning time. A five-point research agenda identifies the formal, computational, and engineering work needed to realise AAP-based affordance matching at scale.

---


### 58. [Hallucination as Exploit: Evidence-Carrying Multimodal Agents](https://arxiv.org/abs/2605.19192)

**<font color=#1a73e8>作者：</font>** Guijia Zhang, Hao Zheng, Harry Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal agents use screenshots, documents, and webpages to choose tool calls. When a false visual claim triggers a click, email, extraction, or transfer, hallucination becomes an authorization failure rather than an answer-quality error. We formalize this failure mode as hallucination-to-action conversion: an unsupported perceptual claim supplies the precondition that makes a privileged action appear permitted. We propose evidence-carrying multimodal agents (ECA), which treat free-form model text as inadmissible evidence. ECA decomposes each tool call into action-critical predicates, obtains typed certificates from constrained DOM/OCR/AX verifiers, and lets a deterministic gate grant only the privileges those certificates support. The architecture does not hide perception error; it converts opaque model belief into named verifier, schema, and implementation residuals. Verifier red-teaming over 1,900 attacks exposes this residual directly: four targeted hardening steps reduce gate bypass from 15% to 1.3%. With content-derived certificates, ECA obtains 0% unsafe-action rate on a 200-task end-to-end pipeline (Wilson 95% upper bound 2.67%) and a 120-task browser proof-of-concept (upper bound 4.3%). A direct HACR audit on 500 stratified task keys shows that unsupported action-critical claims reach unsafe execution for naive agents (100.0%) and prompt-only defense (49.6%), but not for ECA. Oracle-certificate replay on 7,488 GPT-5.4 benchmark traces serves as a gate-correctness sanity check, and neural judge baselines remain bypassable under the same threat model. The resulting principle is simple: model language may propose actions, but external evidence must authorize them.

---


### 59. [Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection](https://arxiv.org/abs/2605.19193)

**<font color=#1a73e8>作者：</font>** Andrea Morandi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM debate improves factuality and reasoning, but most recipes pick a fixed round count, over-spending on easy items and under-spending on hard ones. We adapt Wald's Sequential Probability Ratio Test (SPRT) as a plug-in compute governor for LLM debates. After each round, an LLM judge emits a [0,1] consensus score on the latest agent positions; a Wald monitor accumulates the log-likelihood ratio of "useful convergence" vs "not yet useful" under a Beta likelihood family, and stops when either boundary is crossed or returns a capped best-effort outcome at R_max. Under i.i.d. assumptions the rule inherits SPRT type-I/type-II error guarantees; in deployment the calibration itself is the more important object, since it estimates whether the judge score actually separates useful from unhelpful convergence in a given domain. We evaluate two tracks: (i) a Monte-Carlo study under calibrated Beta models characterising working curves, error rates, capping behaviour, and sensitivity; and (ii) a real-LLM evaluation on 200 attempted MMLU and 200 attempted GSM8K items with three heterogeneous agents (gpt-5, claude-opus-4-6, gemini-2.5-pro) and a claude-opus-4-6 judge, using disjoint 40-item calibration subsets. On GSM8K the rule stops in 1.01 average rounds (4.06 LLM calls) at 97.0% accuracy vs 99.0% for fixed-5 debate at 15 calls: a 3.7x call reduction at -2pp accuracy. On MMLU the calibrated KL collapses to about 0 and the rule caps on 99.5% of items at 2.1x cost. The takeaway is not that SPRT makes debate more accurate, but that a classical sequential test serves as a cheap compute-control and failure-detection layer for multi-agent LLM systems.

---


### 60. [Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?](https://arxiv.org/abs/2605.19196)

**<font color=#1a73e8>作者：</font>** Leyao Wang, Yanan He, Peng Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents increasingly automate complex information-seeking tasks, producing evidence-grounded reports via multi-step reasoning, tool use, and synthesis. Their growing role demands scalable, reliable evaluation, positioning LLM-as-judge as a supervision paradigm for assessing factual accuracy, evidence use, and reasoning quality. Yet the reliability of these judges for deep research agents remains poorly understood, posing a critical meta-evaluation problem: before deploying LLM judges to supervise research agents, we must first evaluate the judges themselves. Existing meta-evaluations fall short in two ways: (1) reliance on coarse, subjective human-preference agreement; (2) focus on instruction-following or verifiable tasks, leaving open-ended agent executions unexplored. To address these gaps, we introduce REFLECT (REliable Fine-grained LLM judge Evaluation via Controlled inTervention), a meta-evaluation benchmark targeting fine-grained failure detection in agentic environments. REFLECT defines a detailed taxonomy of process- and outcome-level failure modes, instantiated by performing controlled and localized interventions on quality-screened agent execution traces. This yields verifiable, comprehensive, and fine-grained instances for validating the judge models. Our experiments show that current LLM judges remain unreliable: even the best-performing models achieve overall accuracies below 55% across reasoning, tool-use, and report-quality failures, with especially poor performance on evidence verification. Together, our taxonomy and findings expose systematic judge limitations, reveal tradeoffs in cost and reliability, and offer actionable guidance for building more reliable evaluation pipelines for deep research agents.

---


### 61. [Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference](https://arxiv.org/abs/2605.19218)

**<font color=#1a73e8>作者：</font>** Beomseok Kang, Dongwon Jo, Jiwon Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models suffer severe KV cache pressure at inference, as a single image often encodes into thousands of tokens. Most existing methods exploit token sparsity through token pruning, but permanently discarding visual content causes substantial degradation on fine-grained perception tasks. This motivates a complementary axis, feature sparsity: under a fixed KV cache budget, compressing the channel dimension preserves more visual tokens at the same memory cost. Prior Key channel pruning methods, however, face a structural trade-off: token-wise channel pruning is expressive but unstructured and slow, while head-wise approach is hardware-friendly but less robust. We resolve this with RotateK, a rotation-based structured Key channel pruning framework. RotateK applies an online PCA-based rotation that aligns token-dependent channel importance into a shared low-dimensional subspace, enabling accurate pruning under lightweight head-wise masks; a fused Triton attention kernel operates directly on sparse-channel Keys for efficient decoding. Experiments on two representative VLM backbones show that RotateK consistently outperforms prior Key channel pruning in both accuracy and decoding latency, while joint token-channel pruning improves over token-only baselines at matched KV cache budgets.

---


### 62. [SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents](https://arxiv.org/abs/2605.19219)

**<font color=#1a73e8>作者：</font>** Han Li, Vibhor Malik, Zahra Zanjani Foumani 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A/B testing remains the gold standard for evaluating modifications to e-commerce storefronts, yet it diverts traffic, requires weeks to reach statistical significance, and risks degrading user experience. We present SimGym, a framework for simulating A/B tests on e-commerce storefronts using vision-language model (VLM) agents operating in a live browser. The framework comprises three key components: (a) a traffic-grounded persona generation pipeline that derives per-shop buyer archetypes and intents from production clickstream data; (b) a live-browser agent architecture that combines multimodal perception over visual and browser-structured observations with episodic memory and guardrails to conduct coherent shopping sessions across control and treatment storefronts; and (c) an evaluation protocol that compares simulated outcome shifts with observed shifts in real buyer behavior. We validate SimGym on A/B tests of visually driven UI theme changes from a major e-commerce platform across diverse storefronts and product categories. Empirical results show that SimGym agents achieve strong agreement with observed outcome shifts, attaining 77% directional alignment with add-to-cart shifts observed across interface variants in real-buyer traffic. It reduces experimental cycles from weeks to under an hour, enabling rapid experimentation without exposing real buyers to candidate variants.

---


### 63. [Position: Uncertainty Quantification in LLMs is Just Unsupervised Clustering](https://arxiv.org/abs/2605.19220)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Longchao Da, Xiaoou Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty Quantification (UQ) is widely regarded as the primary safeguard for deploying Large Language Models (LLMs) in high-stakes domains. However, we argue that the field suffers from a category error: mainstream UQ methods for LLMs are just unsupervised clustering algorithms. We demonstrate that most current approaches inherently quantify the internal consistency of the model's generations rather than their external correctness. Consequently, current methods are fundamentally blind to factual reality and fail to detect ``confident hallucinations,'' where models exhibit high confidence in stable but incorrect answers. Therefore, the current UQ methods may create a deceptive sense of safety when deploying the models with uncertainty. In detail, we identify three critical pathologies resulting from this dependence on internal state: a hyperparameter sensitivity crisis that renders deployment unsafe, an internal evaluation cycle that conflates stability with truth, and a fundamental lack of ground truth that forces reliance on unstable proxy metrics to evaluate uncertainty. To resolve this impasse, we advocate for a paradigm shift to UQ and outline a roadmap for the research community to adopt better evaluation metrics and settings, implement mechanism changes for native uncertainty, and anchor verification in objective truth, ensuring that model confidence serves as a reliable proxy for reality.

---


### 64. [HAVEN: Hierarchically Aligned Multimodal Benchmark for Unified Video Understanding](https://arxiv.org/abs/2605.19223)

**<font color=#1a73e8>作者：</font>** Mengqi Shi, Haopeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) exhibit strong performance on standard video tasks, their ability to faithfully summarize and reason over complex narratives remains poorly evaluated. Existing summarization benchmarks fragment supervision across isolated granularities, such as keyframes, key shots, or disjointed text summaries, failing to capture the inherently hierarchical structure of cross-modal alignment. To address this critical gap, we introduce HAVEN, a hierarchically aligned multimodal benchmark for unified video understanding. HAVEN pioneers a fully granular (frame, shot, and video levels) and fully multimodal (video and text) dataset architecture, complete with explicit, continuous alignment between modalities. Built upon this unified annotation paradigm, we propose a comprehensive evaluation suite spanning summarization, temporal reasoning, multimodal grounding, and saliency ranking. Extensive benchmarking of state-of-the-art MLLMs exposes a persistent gap between surface-level textual fluency and grounded multimodal understanding. Ultimately, HAVEN advances the evaluation of multimodal systems beyond traditional QA formats, offering a rigorous, standardized testbed to drive future research in interpretable, hierarchical video understanding. We publicly release the dataset, benchmark suite, and evaluation protocols.

---


### 65. [Fine-tuning language encoding models on slow fMRI improves prediction for fast ECoG](https://arxiv.org/abs/2605.19224)

**<font color=#1a73e8>作者：</font>** Aditya R. Vaidya, Richard J. Antonello, Alexander G. Huth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neuroscientists have recently turned to intracranial brain recording methods, like electrocorticography (ECoG), for human experiments because of the fine spatial and temporal resolution that they afford. Models trained on this data, however, are fundamentally restricted by the patient populations that can receive the implants necessary for recording. We propose using non-invasive fMRI to bridge the gap in training data. Using spoken language representations fine-tuned on fMRI, we build encoding models of ECoG. These representations showed improved prediction performance in ECoG, even though the temporal resolution of fMRI is two orders of magnitude worse. Prediction improved in frequency bands well beyond what is directly measured in fMRI. Next, to test the procedure's generalization ability, we fine-tuned models on fMRI responses that were temporally downsampled by a factor of 2. Despite the loss in resolution, these models were able to predict fMRI and ECoG responses at levels comparable to the original fMRI-tuned models. Finally, we showed that ECoG performance steadily scales with the amount of fMRI-tuning data. Our results show that "slow" data like fMRI can be a valuable resource for building better models of "fast" brain data like ECoG. In the future, integrating across multiple recording methods may further improve performance in other applications, like decoding.

---


### 66. [Diagnosing Multi-step Reasoning Failures in Black-box LLMs via Stepwise Confidence Attribution](https://arxiv.org/abs/2605.19228)

**<font color=#1a73e8>作者：</font>** Xiaoou Liu, Tiejin Chen, Dengjia Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models have achieved strong performance on reasoning tasks with objective answers by generating step-by-step solutions, but diagnosing where a multi-step reasoning trace might fail remains difficult. Confidence estimation offers a diagnostic signal, yet existing methods are restricted to final answers or require internal model access. In this paper, we introduce Stepwise Confidence Attribution (SCA), a framework for closed-source LLMs that assigns step-level confidence based only on generated reasoning traces. SCA applies the Information Bottleneck principle: steps aligning with consensus structures across correct solutions receive high confidence, while deviations are flagged as potentially erroneous. We propose two complementary methods: (1) NIBS, a non-parametric IB approach measuring consistency without graph structures, and (2) GIBS, a graph-based IB model that learns subgraphs through a differentiable mask to capture logical variability. Extensive experiments on mathematical reasoning and multi-hop question answering show that SCA reliably identifies low-confidence steps strongly correlated with reasoning errors. Moreover, using step-level confidence to guide self-correction improves the correction success rate by up to 13.5\% over answer-level feedback.

---


### 67. [Can Large Language Models Revolutionize Survey Research? Experiments with Disaster Preparedness Responses](https://arxiv.org/abs/2605.19229)

**<font color=#1a73e8>作者：</font>** Yan Wang, Ziyi Guo, Christopher McCarty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Survey research faces mounting structural challenges: declining response rates, sample bias, block-wise missingness among at-risk respondents, and AI-assisted fraudulent completions in online panels. Large language models (LLMs) have been proposed as a remedy, yet rigorous evaluations across the full survey workflow remain scarce, particularly in disaster contexts where data quality matters most. We present and evaluate a five-stage framework for LLM integration covering questionnaire design, sample selection, pilot testing, missing-data imputation, and post-collection analysis, using the 2024 Hurricane Milton preparedness survey of Florida residents (n=946) as a shared empirical testbed. We introduce a Protection Motivation Theory (PMT)-constrained co-occurrence knowledge graph and develop seven LLM configurations spanning zero-shot inference, retrieval-augmented baselines, and novel theory-informed variants. Our proposed Anchored Marginal Theory-Informed LLM (A-TLM) outperforms all three classical imputation baselines (IPW/MI, MICE+PMM, missForest) on RMSE under disaster-relevant block-wise MNAR conditions (S4 RMSE 1.439 vs. 1.496 for the next-best), while achieving near-zero signed bias (-0.121) where the random-forest imputer produces the largest absolute bias (-0.631). Organizing retrieval around PMT causal structure and integrating all evidence in a single model call outperforms unstructured retrieval and staged sequential inference (MAE 0.993 vs. 1.097 for standard RAG). We document that near-zero aggregate bias can mask opposing subgroup errors and propose subgroup-stratified bias auditing as a reporting standard. A retrieval-constrained knowledge-graph chatbot demonstrates that hallucination is architecturally manageable through grounded refusal.

---


### 68. [CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring](https://arxiv.org/abs/2605.19240)

**<font color=#1a73e8>作者：</font>** Kavana Venkatesh, Jafar Isbarov, Saad Amin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cascade attacks in LLM multi-agent systems (MAS) arise when adversarial influence propagates across agents and leads to escalated system-level failures through complex agent interactions. Detecting such cascades is challenging, as their signals are distributed, tightly coupled across interaction channels, and often appear plausibly benign locally but may unfold quickly either within a single turn or gradually across multiple turns. Existing defenses, being largely local and text-centric, fail to capture such cross-channel, temporally coordinated dynamics of cascade propagation. Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents. CASPIAN models multi-agent interactions using a unified, dynamic causal influence matrix across channels, estimated efficiently via a late-interaction conditional transfer entropy (LI-CTE) formulation, thereby enabling the detection of cascade onset from emergent system-level structure rather than isolated anomalies. It further performs online causal attribution, identifying the origin, bridge, and amplifier agents driving the cascade and reconstructing its principal propagation pathways, capabilities not supported by existing methods. Across diverse multi-agent frameworks and benchmarks, CASPIAN consistently outperforms semantic guardrails, LLM-based judges, and graph-based anomaly detectors in both detection accuracy and early cascade identification while operating with sub-1% relative overhead latency. These results demonstrate that unified cross-channel causal modeling is essential for reliably detecting and understanding cascade failures in LLM multi-agent systems.

---


### 69. [PhyWorld: Physics-Faithful World Model for Video Generation](https://arxiv.org/abs/2605.19242)

**<font color=#1a73e8>作者：</font>** Pu Zhao, Juyi Lin, Timothy Rupprecht 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World simulators can provide safe and scalable environments for training Physical AI systems before real-world deployment. Large video generation models are emerging as a promising basis for such simulators because they can generate diverse and realistic visual futures. However, using them as world simulators requires physically faithful video continuations, namely, generated videos that preserve the physical state implied by the conditioning input, and evolve in ways consistent with basic physical principles. We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training. In the first stage, we improve video-to-video continuation with flow matching fine-tuning, encouraging stable visual attributes and coherent motion dynamics across frames. In the second stage, we align generated dynamics with physical principles using Direct Preference Optimization (DPO) over physics preference pairs, guiding the model toward outputs with higher physical plausibility. To evaluate PhyWorld, we use both standard video-quality benchmarks and a dedicated physical-faithfulness benchmark with per-law scoring. Experiments show that PhyWorld improves video consistency, achieving an average score of 0.769 on VBench compared with 0.756 or below for state-of-the-art baselines. PhyWorld also improves physical plausibility, reaching an average score of 3.09 on our physical-faithfulness benchmark compared with 2.99 for the strongest baseline. These results suggest that post-training large video generation models with continuation and physics-preference signals can make them more effective world simulators for Physical AI.

---


### 70. [Structuring Open-Ended NAS: Semi-Automated Design Knowledge Structuring with LLMs for Efficient Neural Architecture Search](https://arxiv.org/abs/2605.19247)

**<font color=#1a73e8>作者：</font>** Yuiko Sakuma, Masakazu Yoshimura, Marcel Gröpl 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current neural architecture search (NAS) methods are often limited by their predefined, restrictive search spaces. While recent large language model (LLM)-assisted NAS methods enable open-ended search spaces, they often suffer from inefficient exploration due to biased or low-quality design ideas. To address these issues, we propose to semi-automatically structure model design knowledge to guide the search process. Our approach first defines a high-level structural template of architectural attributes. An LLM then populates this template by analyzing papers, creating a rich and diverse search space that embodies this structured design knowledge. To efficiently explore this vast space, we introduce FairNAD, using a multi-type mutation that enables broad exploration through mutation with fair idea sampling, Pareto-aware mutation, LLM-driven iterative mutation, and a fine-grained feedback loop. We demonstrate the effectiveness of FairNAD in discovering high-performing architectures that yield 0.84, 2.17, and 2.35 points improvement on CIFAR-10, CIFAR-100, and ImageNet16-120, respectively, compared to current state-of-the-art methods.

---


### 71. [Causal Evidence for Attention Head Imbalance in Modality Conflict Hallucination](https://arxiv.org/abs/2605.19250)

**<font color=#1a73e8>作者：</font>** Jinrui Jiang, Zhangtai Wu, Zhen Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modality-conflict hallucination occurs when multimodal large language models (MLLMs) prioritize erroneous textual premises over contradictory visual evidence. To understand why visual evidence fails to prevail during generation, we take a mechanistic perspective and examine which internal components drive or resist this failure. We perform head-level causal analysis using path patching across five open-source MLLMs and identify two groups of attention heads with opposing causal roles: hallucination-driving heads and hallucination-resisting heads. We find a consistent asymmetry: driving effects are more broadly distributed and carry greater aggregate weight, whereas resisting effects concentrate in a small number of high-importance heads. Ablation experiments further confirm that these groups exert opposing effects during generation: distributed driving influence and localized resistance together form an imbalanced routing structure that biases generation toward the erroneous premise. Motivated by this finding, we propose MACI (Modality-conflict-Aware Causal Intervention), a conditional intervention that suppresses causally identified hallucination-driving heads only when conflict is detected. Across five MLLMs, MACI achieves the largest hallucination reduction among compared inference-time baselines on the MMMC benchmark with a favorable hallucination-accuracy trade-off, and transfers zero-shot to the SCI-SemanticConflict test.

---


### 72. [Backdooring Masked Diffusion Language Models](https://arxiv.org/abs/2605.19262)

**<font color=#1a73e8>作者：</font>** Daniel Yiming Cao, Chengzhong Wang, Sheng-Yen Chou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) are emerging as a compelling new paradigm for text generation, but their training-time security remains largely unexplored. Existing backdoor attacks on Gaussian diffusion models or autoregressive language models do not directly apply to MDLMs because MDLMs rely on discrete state corruption and iterative denoising rather than continuous noising or left-to-right prediction. In this work, we present the first systematic study of training-time backdoor attacks on MDLMs. We propose SHADOWMASK, a backdoor attack that modifies the MDLM forward corruption process by replacing the standard all-mask terminal distribution with a trigger-mask mixture prior. This creates a dedicated denoising pathway from trigger-corrupted states to attacker-specified targets while preserving clean denoising behavior. We further provide a principled mathematical formulation by defining the backdoored forward process, deriving the reverse-time posterior, and obtaining the continuous-time training objective. Evaluations on DiT-based MDLM and LLaDA-8B-Instruct across WikiText-103, OpenWebText, and Alpaca show that SHADOWMASK achieves near-100% attack success, substantially outperforms standard data poisoning, largely preserves clean utility, remains effective under full-model and parameter-efficient fine-tuning, and is robust against representative defenses.

---


### 73. [DECOR: Auditing LLM Deception via Information Manipulation Theory](https://arxiv.org/abs/2605.19270)

**<font color=#1a73e8>作者：</font>** Linyue Cai, Samuel Yeh, Jwala Dhamala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can deceive by subtly manipulating truthful information -- omitting key facts, shifting focus, or obscuring meaning -- making such behavior difficult to detect. Existing black-box methods rely on coarse-grained judgments, offering limited interpretability and failing to pinpoint which facts were distorted and how. We introduce DECOR, a multi-agent framework grounded in Information Manipulation Theory for fine-grained auditing of strategic deception in LLM responses. DECOR decomposes input contexts into atomic informational units and scores each unit against the response across four dimensions of manipulation, producing interpretable manipulation profiles that are aggregated into a global deception index. We comprehensively evaluate DECOR on both single-turn and multi-turn deception detection benchmarks spanning real-world domains, and show that DECOR achieves state-of-the-art performance on both, outperforming competitive baselines. The framework generalizes across 15 frontier models, and ablation studies confirm the contribution of each key design component. Our findings demonstrate that fine-grained, theory-grounded auditing of information manipulation offers an effective and interpretable path for LLM deception detection.

---


### 74. [OpenCompass: A Universal Evaluation Platform for Large Language Models](https://arxiv.org/abs/2605.19276)

**<font color=#1a73e8>作者：</font>** Maosong Cao, Kai Chen, Haodong Duan 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, the field of artificial intelligence has undergone a paradigm shift from task-specific small-scale models to general-purpose large language models (LLMs). With the rapid iteration of LLMs, objective, quantitative, and comprehensive evaluation of their capabilities has become a critical link in advancing technological development. Currently, the mainstream static benchmark dataset-based evaluation methods face challenges such as the diversity of task types, inconsistent evaluation criteria, and fragmentation of data and processing workflows, making it difficult to efficiently conduct cross-domain and large-scale model evaluation. To address the aforementioned issues, this paper proposes and open-sources OpenCompass, a one-stop, scalable, and high-concurrency-supported general-purpose LLM evaluation platform. Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency. The core architecture of OpenCompass comprises five key components: the Configuration System, Task Partitioning Module, Execution and Scheduling Module, Task Execution Unit, and Result Visualization Module. Its workflow provides rule-based, LLM-as-a-Judge, and cascaded evaluators to adapt to the requirements of different task scenarios. Supporting mainstream benchmark datasets across multiple domains, including knowledge, reasoning, computation, science, language, code, etc., the platform offers a unified and efficient LLM evaluation tool for both academia and industry, facilitating the accurate identification of strengths and weaknesses of LLMs as well as their subsequent optimization.

---


### 75. [Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR](https://arxiv.org/abs/2605.19282)

**<font color=#1a73e8>作者：</font>** Chongyu Fan, Gaowen Liu, Mingyi Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is a matrix-aware optimizer that leverages Newton-Schulz (NS) iterations to enforce spectral gradient orthogonalization by driving all singular values of the momentum matrix toward 1. While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable. To address these challenges, we propose Pion, a drop-in replacement for Muon that preserves its computational efficiency while replacing uniform spectral whitening with a two-stage Promotion+Suppression mechanism, which we call the high-pass NS iteration. This design induces a sharp spectral high-pass effect, anchoring dominant singular values at 1 while suppressing noisy tail components toward 0, with controllable filter strength. To preserve pretrained per-head heterogeneity, Pion also supports a per-head mode that applies updates independently across attention heads via a simple reshape, at no extra cost. In VLA training on LIBERO and LIBERO-Plus, Pion consistently outperforms both baselines across l_1-regression (VLA-Adapter) and flow-matching (VLANeXt) architectures, e.g., reaching 100% success rate on LIBERO Object after 1,500 training steps with VLA-Adapter, vs. 97.0% for Muon and only 32.2% for AdamW. The advantage of Pion further extends to a real Franka Research 3 robot with a pi_0.5 backbone under the DROID setup on three grasp-and-place tasks. In RLVR post-training on Qwen3-1.7B/4B with GRPO and GMPO, Pion also outperforms AdamW on MATH and GSM8K while Muon collapses to zero.

---


### 76. [Language models struggle with compartmentalization](https://arxiv.org/abs/2605.19284)

**<font color=#1a73e8>作者：</font>** Thomas Vincent Howe, David Wingate  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the training data used by large language models (LLMs), the same latent concept is often presented in multiple distinct ways: the same facts appear in English and Swahili; many functions can be expressed in both Python and Haskell; we can express propositions in both formal and natural language. We show that LLMs can exhibit compartmentalization, where they fail to identify and share statistical strength between distinct presentations of unified concepts. In the worst case, LLMs simply learn parallel internal representations of each presentation of the concept, saturating model capacity with redundancies and decreasing sample efficiency with the number of such presentations. We also demonstrate that synthetic parallel data can fail to improve this despite being easily learned itself. Under this framework, we find that, for small models, early multilingual learning is nearly entirely compartmentalized. Finally, all interventions that we study exhibit a phase transition in which their effectiveness depends on the number of distinct presentations, suggesting that the language modeling objective may only inconsistently unify representations.

---


### 77. [Are Rationales Necessary and Sufficient? Tuning LLMs for Explainable Misinformation Detection](https://arxiv.org/abs/2605.19285)

**<font color=#1a73e8>作者：</font>** Bing Wang, Rui Miao, Ximing Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid spread of misinformation on social media platforms has become a formidable challenge. To mitigate its proliferation, Misinformation Detection (MD) has emerged as a critical research topic. Traditional MD approaches based on small models typically perform binary classification through a black-box process. Recently, the rise of Large Language Models (LLMs) has enabled explainable MD, where models generate rationales that explain their decisions, thereby enhancing transparency. Existing explainable MD methods primarily focus on crafting sophisticated prompts to elicit rationales from off-the-shelf LLMs. In this work, we propose a pipeline to fine-tune a dedicated LLM specifically for explainable MD. Our pipeline begins by collecting large-scale fact-checked articles, and then uses multiple strong LLMs to produce veracity predictions and rationales. To ensure high-quality training data, we leverage a filtering strategy that selects only the correct instances for fine-tuning. While this pipeline is intuitive and prevalent, our experiments reveal that naive filtering based solely on label correctness is insufficient in practice and suffers from two critical limitations: (1) Coarse-grained labels cause insufficient rationales: Rationales filtered solely based on binary labels are insufficient to adequately support their decisions; (2) Over-verification behavior causes unnecessary rationales: Stronger LLMs tend to exhibit over-verification behavior, producing excessively verbose and unnecessary rationales. To address these issues, we introduce LONSREX, a novel data synthesis pipeline to Locate Necessary and Sufficient Rationales for Explainable MD. Specifically, we propose a metric that quantifies the contribution of each verification step to the final prediction, thereby evaluating its necessity and sufficiency. Experimental results demonstrate the effectiveness of LONSREX.

---


### 78. [iGSP:Implicit Gradient Subspace Projection for Efficient Continual Learning of Vision-Language Models](https://arxiv.org/abs/2605.19301)

**<font color=#1a73e8>作者：</font>** Xuezhi Cui, Dongbo Zhou, Wang Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models require efficient adaptation to continually emerging downstream tasks. While Parameter-Efficient Fine-Tuning mitigates catastrophic forgetting, assigning isolated modules per task leads to parameter explosion. Conversely, recent similarity-driven sharing mechanisms falsely equate superficial visual similarity with underlying alignment consistency. This fundamental mismatch triggers severe negative transfer between visually similar but logically distinct tasks and fails to exploit alignment reuse across visually diverse ones. We argue thatalignment sharing is fundamentally a geometric problem of overlapping optimization trajectories within shared low-rank subspaces. Grounded in this insight, we propose iGSP, a novel framework that achieves efficient adaptation via implicit gradient subspace projection. Leveraging the early convergence of MoE routers to establish the subspace basis, iGSP bifurcates the adaptation process into two phases. First, the Subspace Identification phase introduces candidate experts via basis pre-expansion, applies a novel subspace-constrained regularization to implicitly project new task gradients onto the historical subspace, and precisely prunes redundant dimensions by treating routing probabilities as gradient flow indicators, ultimately to maximize knowledge reuse. Second, the Orthogonal Subspace Fine-Tuning phase fixes this structural basis and removes the regularization to rapidly fit the task-specific residual loss. Extensive experiments on the MTIL benchmark demonstrate that iGSP achieves state-of-the-art accuracy while significantly improving training efficiency, reducing the average trainable parameters by 42.7\% compared to current SOTA methods, and decreasing the final total parameters by 86.9\% relative to counterparts. The source code is available at this https URL.

---


### 79. [MetaRA: Metamorphic Robustness Assessment for Multimodal Large Language Model-based Visual Question Answering Systems](https://arxiv.org/abs/2605.19307)

**<font color=#1a73e8>作者：</font>** Quanxing Xu, Yuhao Tian, Ling Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA), as the representative multimodal task, serves as a key benchmark for evaluating the reasoning capabilities of Multimodal Large Language Models (MLLMs). However, existing evaluations largely rely on static datasets and accuracy-based metrics, which fail to capture robustness, consistency, and generalization. Inspired by Metamorphic Testing (MT), we propose Metamorphic Robustness Assessment (MetaRA), a testing framework that employs Metamorphic Relations (MRs) to systematically probe vulnerabilities in MLLM-based VQA systems. MetaRA generates controlled variations of image-question inputs based on specific MRs and evaluates models across diverse conditions. Applying MetaRA to multiple MLLM-based VQA models across different tasks reveals nuanced failure patterns, including sensitivity to linguistic perturbations, over-reliance on superficial visual cues, and deeper weaknesses in multimodal reasoning. Experimental results demonstrate that MetaRA provides richer diagnostic insights than conventional accuracy metrics, exposing failure modes that remain hidden under standard benchmarks. Overall, this work highlights the need for systematic robustness evaluation in VQA and positions metamorphic assessment as a scalable, model-agnostic approach toward trustworthy multimodal AI.

---


### 80. [A Multi-Agent Framework for Feature-Constrained Difficulty Control in Reading Comprehension Item Generation](https://arxiv.org/abs/2605.19316)

**<font color=#1a73e8>作者：</font>** Seonjeong Hwang, Jun Seo, Hyounghun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent studies in difficulty-controlled reading comprehension item generation have leveraged large language models (LLMs) to produce items by adjusting difficulty-related features. However, existing methods typically rely on a single-agent prompting approach, which often fails to consistently satisfy specified feature constraints, resulting in items that deviate from the target difficulty level. To address this limitation, we introduce MAFIG, a Multi-agent Framework for Feature-constrained Item Generation, where multiple LLM agents and feature-specific evaluators collaborate to generate and iteratively revise items based on intended constraints. Furthermore, to verify the efficacy of MAFIG in difficulty control, we propose a method for constructing a sequence of feature constraint sets that yield items with monotonically increasing difficulty. Experimental results demonstrate that MAFIG generates items that adhere to target constraints at a significantly higher rate than baselines, achieving robust difficulty control through the difficulty-calibrated constraint sequence.

---


### 81. [SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution](https://arxiv.org/abs/2605.19319)

**<font color=#1a73e8>作者：</font>** Yiren Song, Yihan Wang, Xiyao Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prediction has emerged as a promising paradigm for embodied control, where future observations are generated and then translated into actions. However, dense video generation is computationally expensive and often unnecessary for many manipulation tasks, whose progress can be summarized by a small number of task-relevant visual states. In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout. We first conduct a controlled comparison between the video generation model Wan2.2 and the image editing model FLUX-Kontext under the same robotic data setting, and find that image editing produces more reliable task-level keyframes with better visual fidelity and substantially lower inference cost. Motivated by this observation, we propose SWEET, a one-shot sparse visual planning framework that progressively generates a sequence of task-relevant manipulation keyframes through successive image editing, conditioned on language instructions and optional arrow-based spatial guidance. A goal-conditioned diffusion action predictor then converts adjacent imagined keyframes into executable action chunks. To reduce the mismatch between real and edited visual subgoals, we further introduce a mixed-training strategy with filtered edited targets. Experiments on DROID and RoboMimic show that SWEET improves keyframe prediction across seen and unseen scenes and enables a full pipeline from sequential keyframe planning to executable robot actions, suggesting that image editing is a promising and underexplored direction for embodied visual prediction.

---


### 82. [TextAlign: Preference Alignment for Text Rendering with Hierarchical Rewards](https://arxiv.org/abs/2605.19320)

**<font color=#1a73e8>作者：</font>** Mingxuan Cui, Jingpu Yang, Fengxian Ji 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Faithful text rendering remains a persistent weakness of large text-to-image generative models, as it requires both semantic instruction following and fine-grained glyph-level structure. Prior methods often improve this ability through architecture-specific modules or encoder modifications, which complicate deployment across foundation models. We study text rendering as a post-training preference-alignment problem and propose TextAlign, a non-invasive framework that keeps the generator architecture unchanged. The key component is a hierarchical vision-language model (VLM)-based reward that decomposes rendering errors into global, word, and glyph levels, then converts binary defect judgments into a scalar preference signal. The resulting signal supports both Group Relative Policy Optimization (GRPO) and Direct Preference Optimization (DPO). Experiments on FLUX.1-dev and Z-Image-Turbo show consistent gains in OCR-based text accuracy without degrading general generation quality. Compared with strong foundation and text-rendering baselines, including SD3.5, Qwen-Image, AnyText, and TextDiffuser, these results indicate that reward design offers a scalable alternative to model redesign for improving text rendering.

---


### 83. [DynaTok: Temporally Adaptive and Positional Bias-Aware Token Compression for Video-LLMs](https://arxiv.org/abs/2605.19322)

**<font color=#1a73e8>作者：</font>** Minyoung Park, Taehun Kong, Sangjun Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Video Large Language Models (Video-LLMs) have greatly expanded multimodal reasoning capabilities. However, the massive number of visual tokens extracted from long video sequences incurs prohibitive computational costs, limiting their deployment in real-world scenarios. Existing training-free token compression methods select tokens based on attention magnitude as a proxy for semantic importance, but often overlook positional bias and rely only on short-term temporal locality, leading to redundant spatio-temporal coverage and inefficient token usage. We present DynaTok, a training-free, temporally adaptive and bias-aware token compression framework that allocates token budgets across both temporal and spatial dimensions. Through a lightweight exponential moving average (EMA) memory, the Temporal Budget Allocation (TBA) module dynamically assigns fewer tokens to redundant frames and more to novel frames, capturing long-term temporal variation. The Spatial Budget Allocation (SBA) module complements this by selecting spatially diverse and semantically important features using activation-based attention maps, while leveraging a spatial memory to reduce redundancy from previously selected regions and mitigate positional bias. DynaTok integrates seamlessly with existing Video-LLMs such as LLaVA-OneVision and LLaVA-Video without retraining, and effectively preserves semantic coverage under aggressive compression. Experiments on four representative VideoQA benchmarks-MVBench, LongVideoBench, MLVU, and VideoMME-show that DynaTok retains over 95% of baseline accuracy even with a 90% token reduction, surpassing recent training-free approaches. These results demonstrate that DynaTok provides a principled foundation for efficient and robust video reasoning, paving the way toward real-time streaming video understanding with future Video-LLMs.

---


### 84. [RE-VLM: Event-Augmented Vision-Language Model for Scene Understanding](https://arxiv.org/abs/2605.19329)

**<font color=#1a73e8>作者：</font>** Hanqing Liu, Mingjie Liu, Luoping Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional vision-language models (VLMs) struggle to interpret scenes captured under adverse conditions (e.g., low light, high dynamic range, or fast motion) because standard RGB images degrade in such environments. Event cameras provide a complementary modality: they asynchronously record per-pixel brightness changes with high temporal resolution and wide dynamic range, preserving motion cues where frames fail. We propose RE-VLM, the first dual-stream vision-language model that jointly leverages RGB images and event streams for robust scene understanding across both normal and challenging conditions. RE-VLM employs parallel RGB and event encoders together with a progressive training strategy that aligns heterogeneous visual features with language. To address the scarcity of RGB-Event-Text supervision, we further propose a graph-driven pipeline that converts synchronized RGB-Event streams into verifiable scene graphs, from which we synthesize captions and question-answer (QA) pairs. To develop and evaluate RE-VLM, we construct two datasets: PEOD-Chat, targeting illumination-challenged scenes, and RGBE-Chat, covering diverse scenarios. On captioning and VQA benchmarks, RE-VLM consistently outperforms state-of-the-art RGB-only and event-only models with comparable parameter counts, with particularly large gains under challenging conditions. These results demonstrate the effectiveness of event-augmented VLMs in achieving robust vision-language understanding across a wide range of real-world environments. Code and datasets are available at this https URL.

---


### 85. [Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/abs/2605.19337)

**<font color=#1a73e8>作者：</font>** Yihan Xia, Panpan You, Taotao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A growing body of work explores how Large Language Models (LLMs) can be embedded in trading systems as agents that perceive market information, retrieve context, reason about decisions, emit tradable actions, and adapt under market feedback. This paper reframes LLM-based trading agents as expert-system decision pipelines and presents an audit-oriented evidence map of 77 included studies in a protocol-coded snapshot screened through 2026-03-09. A primary empirical subset (n=19) satisfies the minimum boundary of Action Output plus Closed-Loop Evaluation; the remaining 58 included studies are retained as background and design context. The central empirical finding is protocol incomparability: within the primary subset, only 2/19 studies report extractable time-consistent split protocols, 1/19 reports an explicit transaction-cost model, 1/19 documents universe or survivorship handling, 11/19 report execution timing or semantics, 15/19 are coded as R0, and no study reaches R3 reproducibility. We therefore use Architecture-Capability-Adaptation as a working analytical lens rather than a validated taxonomy, and we foreground the evidence ledger, reproducibility audit, and reporting checklist as the main contributions. The resulting survey shows that architectural experimentation is expanding rapidly, while comparable evaluation protocols, execution semantics, and reproducible artifacts remain the field's immediate bottlenecks.

---


### 86. [Selective, Regularized, and Calibrated: Harnessing Vision Foundation Models for Cross-Domain Few-Shot Semantic Segmentation](https://arxiv.org/abs/2605.19340)

**<font color=#1a73e8>作者：</font>** Junyuan Ma, Xunzhi Xiang, Wenbin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) have achieved strong performance across various vision tasks. However, it still remains challenging to apply VFMs for cross-domain few-shot segmentation (CD-FSS), which segments objects of novel classes under domain shifts using only a few labeled exemplars. The challenge is mainly driven by two factors: (1) limited labeled exemplars per novel class relative to the scale of VFM pre-training, making the model prone to overfitting during retraining, and (2) target-domain shifts underrepresented during pre-training, inducing cross-domain inconsistency and layer-wise sensitivity. To address these issues, we propose Hierarchical Exemplar Representation Adaptation (HERA), a three-stage select-regularize-calibrate VFM-based segmentation framework that learns effectively from limited labels and adapts to novel domains without source-data retraining. We first design Hierarchical Layer Selection (HLS) to adaptively identify the most informative VFM layer using a data-dependent Exemplar Transfer Risk (ETR) computed for each candidate layer. Then, Prior-Guided Regularization (PGR) regularizes interactions on the selected representation, yielding well-structured local signals for the subsequent stage. Furthermore, Pixelwise Adaptive Calibration (PAC) combines the selected representation with the refined interaction maps to calibrate pixel-wise predictions, producing consistent masks. Together, these stages form a hierarchical select-regularize-calibrate pipeline that guides frozen VFM features in new domains while fine-tuning less than 2.7% of parameters at test time. Extensive experiments show that HERA surpasses the state of the art by more than 4.1 mIoU across multiple CD-FSS benchmarks.

---


### 87. [HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models](https://arxiv.org/abs/2605.19341)

**<font color=#1a73e8>作者：</font>** Emmy Liu, Varun Gangal, Michael Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination remains a central failure mode of large language models, but existing benchmarks operationalize it inconsistently across summarization, question answering, retrieval-augmented generation, and agentic interaction. This fragmentation makes it unclear whether a mitigation that works in one setting reduces hallucinations across contexts. Current benchmarks either require human annotation and fixed references that may be memorized, or rely on observations in settings that are difficult to reproduce. To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world. Building on this view, we construct synthetic and semi-synthetic environments in which the reference world is fully specified, the model's view is controlled, and hallucination labels are generated automatically. HalluWorld spans gridworlds, chess, and realistic terminal tasks, enabling controlled variation of world complexity, observability, temporal change, and source-conflict policy, and disentangling hallucinations into fine-grained error categories. We evaluate frontier and open-weight language models across these settings and find consistent patterns: perceptual hallucination on directly observed information is near-solved for frontier models, while multi-step state tracking and causal forward simulation remain difficult and are not generally solved by extended thinking. In the terminal setting, models also struggle with when to abstain. The uneven profile of failures across probe types and domains suggests that hallucinations arise from distinct failure modes rather than a single capability. Our results suggest that controlled reference worlds offer a scalable and reproducible path toward measuring and reducing hallucinations in modern language models.

---


### 88. [SciCustom: A Framework for Custom Evaluation of Scientific Capabilities in Large Language Models](https://arxiv.org/abs/2605.19357)

**<font color=#1a73e8>作者：</font>** Yiyang Gu, Junwei Yang, Junyu Luo 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied to scientific research, yet existing evaluations often fail to reflect the fine-grained capabilities required in practice. Most benchmarks are manually curated or domain-generic, limiting scalability and alignment with real scientific use cases. In this paper, we propose a new framework named SciCustom to address the problem. It enables the custom construction of benchmarks from large-scale scientific data to evaluate application-specific scientific capabilities in LLMs. SciCustom first organizes scientific knowledge into ontology-grounded knowledge units with controlled granularity and trains a tagger to map large-scale data instances into this knowledge space. Given a custom requirement, relevant knowledge units are identified via voting-based multi-model consensus. These units enable relevance-aware benchmark retrieval via binary search, followed by proxy subset selection and data-grounded benchmark generation for efficient evaluation. Experiments in chemistry and healthcare demonstrate that SciCustom reveals fine-grained differences in LLM scientific capabilities that standard benchmarks overlook, while requiring neither expert annotation nor synthetic question generation. This work provides a scalable and application-aware foundation for benchmarking scientific capabilities in LLMs. The source code is available at this https URL.

---


### 89. [Taming the Thinker: Conditional Entropy Shaping for Adaptive LLM Reasoning](https://arxiv.org/abs/2605.19358)

**<font color=#1a73e8>作者：</font>** Shuyu Wei, Jian Sun, Delai Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entropy-based deep reasoning has emerged as a promising direction for improving the reasoning capabilities of Large Language Models (LLMs), but existing methods often either increase response length indiscriminately or shorten responses at the cost of accuracy. To better balance this trade-off, we introduce Conditional Entropy Shaping (CES), a framework that dynamically controls token-level response entropy, enabling LLMs to produce concise solutions on simple problems while encouraging deeper exploration on hard ones. Built on DAPO, CES uses token-level entropy as an uncertainty signal and applies a conditional bidirectional policy: it penalizes high-entropy "forking point" tokens on correct reasoning paths to improve conciseness, and rewards them on incorrect paths to encourage exploration and error correction. We implement CES on DeepSeek-R1-Distill-7B and evaluate it on 12 mathematical benchmarks. CES consistently improves average accuracy while reducing response length relative to DAPO, and supplementary experiments show similar trends on a smaller 1.5B backbone and on out-of-domain benchmarks.

---


### 90. [Toward User Comprehension Supports for LLM Agent Skill Specifications](https://arxiv.org/abs/2605.19362)

**<font color=#1a73e8>作者：</font>** Zikai Alex Wen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users often interpret and select agent skills through their \texttt{this http URL} specifications. To protect users, existing audits mainly focus on malicious or unsafe skills. We study the complementary question of whether specifications help users form bounded expectations about what a skill consumes, produces, and covers. Across 878 cybersecurity skills, we used rule-based coding to measure textual cues for four comprehension anchors, namely operational basis, output contract, boundary disclosure, and example capability demonstration. Cues for operational basis were common, but only 19.0\% of specifications exhibited cues for an example task, sample, or expected outcome, and only 2.3\% exhibited cues for all four anchors. We further examined a small DNS/C2 telemetry subset (n$=$6) to illustrate why missing examples may matter. Examples appeared to make first local checks easier to construct, while no-example skills typically required helper code inspection to recover command arguments or output fields. We argue that agent-skill evaluation should treat specifications as user-facing capability disclosures, not merely as containers for executable instructions.

---


### 91. [Accurate, Efficient, and Explainable Deep Learning Approaches for Environmental Science Problems](https://arxiv.org/abs/2605.19366)

**<font color=#1a73e8>作者：</font>** Jimeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Environmental science plays a pivotal role in safeguarding ecosystems, a domain driven by large-scale, heterogeneous data. In the big data era, artificial intelligence (AI) has emerged as a transformative tool for learning patterns and supporting decision-making. This dissertation develops AI-based approaches tailored to complex environmental science problems to achieve Environmental Intelligence, studying three specific challenges. First, we focus on flood prediction and management in coastal river systems. Conventional physics-based models are computationally intensive, limiting real-time application. To overcome this, we propose a deep learning (DL)-based model, WaLeF, for water level forecasting, and a forecast-informed DL model, FIDLAr, to manage water levels. Evaluated in a flood-prone coastal system in South Florida characterized by extreme rainfall and sea level fluctuations, FIDLAr outperforms baselines in accuracy and efficiency while providing interpretable outputs. Second, we target global weather prediction, which is challenged by massive data scale. Traditional physics methods are deterministic and computationally heavy. We propose CoDiCast, a conditional diffusion model tailored for probabilistic weather forecasting. Adapted from generative AI for predictive tasks, experiments show CoDiCast achieves accurate, efficient forecasts with explicit uncertainty quantification. Lastly, we address scientific question-answering in environmental science. When answering in-domain questions, large language models (LLMs) often suffer from hallucinations due to out-of-date or limited knowledge. While retrieval-augmented generation (RAG) retrieves domain-specific knowledge, existing methods trade off accuracy, efficiency, or explainability. We propose Hypercube-RAG, built on a structured text cube framework, which successfully exhibits all three properties simultaneously.

---


### 92. [Concept-Guided Noisy Negative Suppression for Zero-Shot Classification and Grounding of Chest X-Ray Findings](https://arxiv.org/abs/2605.19374)

**<font color=#1a73e8>作者：</font>** Chenyu Lian, Hong-Yu Zhou, Chun-Ka Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language alignment using chest X-rays and radiology reports has emerged as an advanced paradigm for zero-shot classification and grounding of chest X-ray findings. However, standard contrastive learning typically treats radiographs and reports from different patients simply as negative pairs. This assumption introduces noisy negatives, as different patients frequently exhibit similar findings. Such noisy negatives cause semantic ambiguity and degrade performance in zero-shot understanding tasks. To address this challenge, we propose CoNNS, a concept-guided noisy-negative suppression framework. To support the negative suppression mechanism, unlike previous methods that use raw reports or templatized texts, we construct a hierarchical concept ontology using large language models. The ontology structures 41 key clinical concepts by explicitly modeling presence, attributes (location and characteristics), and texts (evidential segment and presence statement). Leveraging this ontology, we implement a cross-patient pair relabeling strategy comprising three steps: (1) Fine-Grained Breakdown to categorize pairs based on finding presence; (2) Noisy Negative Filtering to resolve semantic conflicts by removing false negatives; and (3) Hard Negative Mining to identify subtle attribute discrepancies using a lightweight language model. Finally, we propose a Concept-Aware NCE loss to align visual features with text while suppressing the identified noisy negatives. Extensive experiments across multi-granularity zero-shot grounding tasks and five zero-shot classification datasets validate that CoNNS outperforms existing state-of-the-art models. The code is available at this https URL.

---


### 93. [The Evaluation Game: Beyond Static LLM Benchmarking](https://arxiv.org/abs/2605.19377)

**<font color=#1a73e8>作者：</font>** Paul Wang, Jade Garcia-Bourrée, Anne-Marie Kermarrec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As jailbreaks, adversarially crafted inputs that bypass safety constraints, continue to be discovered in Large Language Models, practitioners increasingly rely on fine-tuning as a defensive strategy. Yet the theoretical foundations underlying this robustness fine-tuning remain underexplored. We introduce a game-theoretic framework in which the interaction between an evaluator (auditing the model for jailbreaks) and a trainer is formalized as a two-player game.
A key feature of our approach is the use of group actions, a mathematical structure that captures symmetries and transformations, to formally represent data augmentation. The simplest non-trivial instance is the circle with cyclic translation groups, where we exhibit various regimes depending on the trainer's generalization range. Below a critical threshold, the evaluator maintains a constant miss ratio for linearly many rounds, whereas other settings can yield very different behaviors. We further provide empirical evidence supporting locality-dependence of the model: for the three model families we tested (Llama, Qwen and Mistral), we have significant evidence that fine-tuning on adversarial prompts induces only local generalization, with refusal rates on test examples highly correlated with the distance to the fine-tuning prompts. Our framework recasts the central object of adversarial evaluation: a benchmark is not a static set of prompts but an orbit under the evaluator's group action, and audit protocols that ignore trainer-side adaptation cannot distinguish a genuine fix from a memorized patch.

---


### 94. [LambdaPO: A Lambda Style Policy Optimization for Reasoning Language Models](https://arxiv.org/abs/2605.19416)

**<font color=#1a73e8>作者：</font>** Zhe Yuan, Yipeng Zhou, Jinghan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization(GRPO) has become a cornerstone of modern reinforcement learning alignment, prized for its efficacy in foregoing an explicit value-critic by leveraging reward normalization across sampled trajectory cohorts. However, the method's reliance on a monolithic statistical baseline, such as the group mean, collapses the relational topology of the trajectory space into a single scalar, thereby erasing the fine-grained preference information essential for navigating complex, rank-sensitive reward landscapes. To address this issue, we introduce a novel framework, Lambda Policy Optimization (LambdaPO), that addresses this information-theoretic bottleneck by re-conceptualizing advantage estimation from a scalar value to a decomposed, pairwise preference structure. Specifically, the advantage for any given trajectory is formulated as the integrated sum of reward differentials against all peers in its cohort, where each pairwise comparison is dynamically attenuated by the policy's own probabilistic confidence in the established preference. To further mitigate the sparsity of binary outcome supervision, we augment the objective with a semantic density reward, derived from the precision-recall alignment between generated reasoning traces and ground-truth solutions. As a result, our method can mine more fine-grained optimization signals from a group of rollouts, guiding the LLM to a better optima. Experimental results across challenging math reasoning and question-answering tasks demonstrates that LambdaPO improves performance compared to the baseline methods.

---


### 95. [Backtracking When It Strays: Mitigating Dual Exposure Biases in LLM Reasoning Distillation](https://arxiv.org/abs/2605.19433)

**<font color=#1a73e8>作者：</font>** Bing Wang, Shaotian Yan, Chen Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable success in complex reasoning tasks via long chain-of-thought (CoT), yet their immense computational overhead hinders real-world deployment. LLM reasoning distillation addresses this by transferring reasoning capabilities from formidable teacher models to compact student models. However, existing distillation paradigms face a fundamental dilemma. Typical off-policy distillation strictly utilizes teacher-generated golden trajectories, suffering from an exposure bias due to the mismatch between training distributions and student-generated inference contexts, which leads to error cascades in long CoT reasoning. To address this, on-policy distillation allows students to explore their own trajectories, but we demonstrate that it inherently introduces a reciprocal reversed exposure bias: the teacher model also struggles to provide positive guidance when conditioned on student-generated sub-optimal contexts. To resolve this dual exposure biases problem, we propose Monitoring Trajectories and Backtracking when it strays (MOTAB), a new LLM reasoning distillation pipeline. Specifically, MOTAB dynamically monitors the student's on-policy generation against an adaptive safety boundary. When the generation strays and exceeds this threshold, MOTAB backtracks to the last safe state and leverages teacher intervention to correct the course. This approach inherently tolerates minor student errors to mitigate exposure bias, while preventing sub-optimal contexts to circumvent reversed exposure bias. Extensive experiments on the LIMO-v2 and AceReason datasets demonstrate that MOTAB effectively alleviates the dual exposure biases, yielding a roughly 3% average performance improvement in reasoning tasks.

---


### 96. [Quantifying the Pre-training Dividend: Generative versus Latent Self-Supervised Learning for Time Series Foundation Models](https://arxiv.org/abs/2605.19462)

**<font color=#1a73e8>作者：</font>** Noam Major, Kathy Razmadze, Yoli Shavit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of self-supervised learning (SSL) in vision and NLP has motivated its rapid adoption for time series. However, research has focused primarily on Generative paradigms and forecasting tasks, leaving the broader utility of learned representations unquantified. We establish a controlled framework to evaluate the "pre-training dividend": the value added by SSL across diverse temporal tasks. We systematically compare Generative paradigms against Latent Alignment architectures, introducing adaptations of LeJEPA and DINO for time series. These adaptations utilize Discrete Wavelet Transform (DWT) augmentations to enforce invariance to local fluctuations. Our analysis reveals that the pre-training dividend is highly asymmetric: SSL yields gains of up to 375% for anomaly detection and classification, yet remains marginal for forecasting. We demonstrate that representational utility is non-universal, governed by a precision-invariance trade-off where the specific signal resolution required by the task must align with the objective. Finally, we show that representation quality is largely independent of data origin and saturates at moderate architectural depths, suggesting a path to scaling via massive synthetic generation. Our code is available at: this https URL

---


### 97. [Drifting Objectives for Refining Discrete Diffusion Language Models](https://arxiv.org/abs/2605.19470)

**<font color=#1a73e8>作者：</font>** Daisuke Oba, Hiroki Furuta, Naoaki Okazaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (DDLMs) generate text by iteratively denoising categorical token sequences, while recent drifting methods for continuous generators suggest that part of this sampling-time correction can instead be absorbed into training through an anti-symmetric fixed-point objective. We study how to transfer this principle to DDLMs, where the main challenge is the interface with discrete text: hard token samples are non-differentiable, and categorical predictions do not directly provide continuous samples to drift. We formulate TokenDrift, a drifting objective that lifts categorical predictions to soft-token features, applies anti-symmetric drifting in a frozen semantic space, and backpropagates the resulting stop-gradient feature target to DDLM logits. In controlled continual-training experiments with masked and uniform-state diffusion backbones, TokenDrift improves fixed-NFE generation quality over matched continuation baselines, reducing Gen.-PPL at 4 NFEs by 89% on MDLM and 86% on DUO. These results suggest that drifting can provide a practical refinement objective for DDLMs.

---


### 98. [Attention-Guided Reward for Reinforcement Learning-based Jailbreak against Large Reasoning Models](https://arxiv.org/abs/2605.19485)

**<font color=#1a73e8>作者：</font>** Zheng Lin, Zhenxing Niu, Haoxuan Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have demonstrated remarkable capabilities in solving complex problems by generating structured, step-by-step reasoning content. However, exposing a model's internal reasoning process introduces additional safety risks; for example, recent studies show that LRMs are more vulnerable to jailbreak attacks than standard LLMs. In this paper, we investigate jailbreak attacks on LRMs and reveal that the attack success rate (ASR) is closely correlated with LRMs' attention patterns. Specifically, successful jailbreaks tend to assign lower attention to harmful tokens in the input prompt, while allocating higher attention to those tokens in the reasoning content. Motivated by this finding, we propose a novel jailbreak method for LRMs that leverages reinforcement learning (RL) to enhance attack effectiveness, explicitly incorporating attention signals into the reward function design. In addition, we introduce diverse persuasion strategies to enrich the RL action space, which consistently improves the ASR. Extensive experiments on five open-source and closed-source LRMs across three benchmarks demonstrate that our method achieves substantially higher ASR, outperforming existing approaches in terms of effectiveness, efficiency, and transferability.

---


### 99. [Base Models Look Human To AI Detectors](https://arxiv.org/abs/2605.19516)

**<font color=#1a73e8>作者：</font>** Yixuan Even Xu, Ziqian Zhong, Aditi Raghunathan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI-generated text enters the real-world at scale, institutions increasingly use commercial AI-text detectors, especially in education and academic-integrity workflows. We report a surprising empirical finding about such systems: when evaluated by GPTZero and Pangram, generated text from base models is often judged overwhelmingly human, whereas text generated by their instruction-tuned counterparts is not. Building on this observation, we propose Humanization by Iterative Paraphrasing (HIP), a detector-agnostic pipeline that minimally fine-tunes a base model into a paraphraser and applies it iteratively. Compared with the baselines we test, HIP yields a stronger trade-off between semantic preservation and detector evasion on commercial detectors. Across Llama-3 and Qwen-3 families, spanning model sizes from 0.6B to 70B, HIP consistently improves detector human-likeness. Our findings suggest that current detectors are tracking artifacts of instruction tuning and local context more than any invariant notion of machine-generated text. This, in turn, calls for detector designs that model these factors more explicitly.

---


### 100. [BLINKG: A Benchmark for LLM-Integrated Knowledge Graph Generation](https://arxiv.org/abs/2605.19518)

**<font color=#1a73e8>作者：</font>** Carla Castedo, Enrique Iglesias, Manuel Lama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating Knowledge Graphs (KGs) remains one of the most time-consuming and labor-intensive tasks for knowledge engineers, as they need to identify semantic equivalences between input data sources and ontology terms. While declarative solutions (e.g., RML, SPARQL-Anything) have helped to generalize this process, aligning input schema elements with ontology terms still involves intricate transformations and requires considerable manual effort. With the advent of Large Language Models (LLMs), there is growing interest in leveraging their capabilities to assist KG engineers. Although some studies have explored using LLMs to automate KG construction, there is still no standardized framework for assessing how effectively they establish correspondences between data schemes and ontology concepts. Therefore, in this paper, we propose BLINKG, a benchmark designed to evaluate the mapping capabilities of LLMs in constructing KGs from heterogeneous data sources. The benchmark includes a set of scenarios with increasing complexity, based on real-world use cases. We conduct an extensive experimental evaluation of several stateof-the-art LLMs using BLINK and observe that they already offer promising solutions. However, their performance remains limited in complex scenarios. Thanks to this benchmark, we can already assess the current capabilities of LLMs for KG construction. Additionally, we define a set of requirements for achieving (semi)automated (LLM-driven) KG construction, opening new research lines in this area.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
