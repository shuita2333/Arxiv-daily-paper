# 🧠 大模型相关研究 | 2026年09月22日

> 本类共 **148** 篇论文：已确认 **139** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-148**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-148**

---

### 101. [PRISM-BN: A Controlled Corpus and Benchmark for Text-to-Parameterized Bayesian Network Extraction](https://arxiv.org/abs/2609.21673)

**<font color=#1a73e8>作者：</font>** Amartya Bhattacharya, Nikhil Singh, Neeti Pokhriyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probabilistic Graphical Models (PGMs), especially Bayesian Networks (BNs), expose directed structure and probabilistic parameters, making them natural symbolic targets for neurosymbolic AI. Yet training text-to-parameterized-BN systems requires paired text-to-BN resources unavailable at scale. We introduce PRISM-BN, a controlled corpus of 5054 BN-grounded descriptions paired with discrete reference BNs containing variables, states, directed edges, root priors, and full multi-parent CPDs across five domains. The instances are derived from 50 Wikipedia-seeded backbones, and their probabilities are internally constructed benchmark targets rather than externally validated causal estimates. PRISM-BN is built with PRISM, a marginal-first pipeline that elicits marginal and local joint distributions, analytically recovers normalized CPDs, and constructs locally reparameterized subgraphs. We define a benchmark with semantic node and state alignment, conditional structural scoring, and strict full-CPD evaluation. Across six LLM extractors, Node F1 ranges from 0.56 to 0.83, conditional Edge F1 from 0.90 to 0.97, and CPD-KL from 1.11 to 3.14. Conditional state and edge recovery remain consistently strong, whereas strict full-CPD agreement remains challenging. These trends persist with independently generated GPT-5.5 references, and a human pilot corroborates structural recoverability and similar probabilistic interpretations. PRISM-BN supports separate evaluation of structural recovery and probabilistic parameter estimation.

---


### 102. [DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning](https://arxiv.org/abs/2609.21675)

**<font color=#1a73e8>作者：</font>** Wan Xu, Yuanfan Guo, Kevin Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable progress in Multimodal Large Language Models (MLLMs), prevailing Chain-of-Thought (CoT) paradigms remain confined to the natural-language expression space. Consequently, they inherently incur excessive linguistic overhead, leading to information dilution and weak visual grounding. To address this challenge, we propose Dense Reasoning Trace (DRT), a paradigm that departs from natural-language-centered CoT by expressing reasoning as compact structured traces, which include concise intermediate states with symbolic connectors and disentangle visual observations from logical deductions. First, we introduce the Dense Trace Initialization to internalize the DRT reasoning mode into the model, substantially improving token efficiency while preserving visual evidence. To further enable the model to faithfully capture the logical relations within traces, we propose the Trace-Grounded Reinforcement Learning framework, which builds reference traces through a tri-perspective verification pipeline and employs Trace-Grounded GRPO with structured rewards, encouraging the model to generate concise DRT-style traces with reduced hallucination and stronger logical grounding. Extensive experiments on challenging reasoning benchmarks show that DRT achieves 5.5$\times$ token efficiency improvement while improving 1.3 accuracy points over the Qwen3-VL baseline. These findings suggest that complex multimodal reasoning may not require verbose natural-language traces, opening a more efficient path for next-generation MLLMs. Our code and data are available at: this https URL

---


### 103. [GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation](https://arxiv.org/abs/2609.21677)

**<font color=#1a73e8>作者：</font>** Zeyu Yan, Guanghao Zhou, Minghui Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large reasoning models (LRMs) have made machine unlearning more challenging, as protected facts or unsafe rationales may surface in intermediate chain-of-thought (CoT) traces before the final answer is produced. Existing unlearning objectives typically suppress the target content or redirect internal representations, but they never specify how the post-forgetting trajectory should continue, which can lead to hallucinated substitutes, malformed boundaries, or repetitive outputs. We argue that LRM unlearning should instead learn a natural forgetting trajectory: a coherent non-disclosing CoT followed by a stable refusal-style answer that replace the original disclosure. To this end, we propose Guided Answer-Reasoning Distillation (GUARD), which converts model-generated unsafe disclosures into safe-exit trajectories, aligns a frozen LRM via guidance tokens, and distills the guided behavior into model this http URL address the lack of metrics for replacement quality beyond leakage, we further introduce Natural Forgetting Reasoning Score (NFRS), which captures structural stability, fluency, and unsupported substitutes in forgotten outputs. Extensive experiments on R-TOFU and a STAR-1-derived harmful-intent setting show that GUARD substantially reduces unsafe and privacy disclosures across two widely adopted distilled LRMs while preserving reasoning utility. Codes are available at this https URL

---


### 104. [SpecQuant: Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference](https://arxiv.org/abs/2609.21704)

**<font color=#1a73e8>作者：</font>** Harish KB, Jagadeeswaran M, Pradheep P 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Running large language models (LLMs) locally continues to be limited by restrictions of compute and memory on consumer hardware. The popular acceleration technologies, such as quantization, speculative decoding, and adaptive inferencing, offer substantial speed boosts but usually necessitate retraining, per architecture tuning, or draft models. SpecQuant is a trainingfree framework, that combines speculative decoding with multiparent quantization to perform adaptive, efficient inference of LLMs. SpecQuant derives multiple quantized variants (INT4, FP8, FP16) from a shared base model, and dynamically routes queries based on predicted complexity; lightweight variants are used for simple or factual tasks, and full-precision models are used for complex reasoning tasks or long-context inputs. The shared-weight design of SpecQuant ensures sufficient token acceptance for speculative decoding without compatibility issues using separate draft parent models. We evaluate SpecQuant on Qwen2.5 based models on the MMLU, AlpacaEval, and GSM8K datasets, or benchmarks, demonstrating 35-43% speedups without degrading accuracy greater than 2%, substantial within the LLM community. SpecQuant enables practical on-device LLM deployment across diverse hardware without special infrastructure or expertise.

---


### 105. [SignGPT: Toward LLM-Mediated Sign Language Interaction through Gloss-Free Translation and Generation](https://arxiv.org/abs/2609.21709)

**<font color=#1a73e8>作者：</font>** Ronghui Li, Jun Dong, Zhongyuan Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) provide limited support for sign language interaction. Unifying sign language translation (SLT) and generation (SLG) to enable sign language as both input and output can reduce switching between separate models during sign-text interaction. We present SignGPT, a unified, pose-based framework for gloss-free SLT and SLG. SignGPT integrates part-aware hierarchical representations of body, hand, and facial motion into a shared language model and employs asymmetric multi-token prediction and progressive training for bidirectional modeling. We evaluate SignGPT on How2Sign (ASL) and Phoenix-2014T (DGS) through benchmark comparisons, qualitative analyses, and component ablations. An exploratory study with 12 Deaf ASL signers assesses an LLM-mediated sign-to-sign response pipeline, highlighting the potential of unified modeling to support sign language conversation (SLC).

---


### 106. [CIBuzzBench: A Benchmark for Cross-Lingual Understanding of Chinese Internet Buzzwords](https://arxiv.org/abs/2609.21722)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Junyu Lu, Qifan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese social media has generated a vast and continually evolving lexicon of internet buzzwords whose meanings are often non-literal and deeply rooted in local cultural and pragmatic contexts. Existing research has primarily focused on interpreting these buzzwords within Chinese, leaving largely unexplored whether LLMs can transfer such culturally grounded knowledge across languages and accurately convey the intended meanings in English. This cross-lingual capability is also critical for safety, as harmful expressions may obscure their offensive content through culture-specific homophony, euphemism, irony, or coded language. In this paper, we investigate the ability of advanced LLMs to understand Chinese internet buzzwords across languages. To this end, we introduce CIBuzzBench, the first benchmark for cross-lingual Chinese-to-English understanding of Chinese internet buzzwords. CIBuzzBench comprises 3,001 Chinese internet buzzwords annotated with English meaning explanations, English equivalents, category labels, and harmfulness labels. Based on these annotations, we design three evaluation tasks: Meaning Explanation, Cross-lingual Equivalent Matching, and Culturally Grounded Harmfulness Detection. We evaluate representative state-of-the-art proprietary and Chinese LLMs under both English- and Chinese-prompting settings. Our results show that LLMs continue to struggle with the cross-lingual understanding of Chinese internet buzzwords, particularly in fine-grained non-literal interpretation, robust equivalent matching under option perturbations, and calibrated harmfulness detection. These findings highlight the persistent challenges posed by culturally grounded language phenomena for multilingual LLMs and safety-oriented evaluation. The dataset and code are available at this https URL.

---


### 107. [GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills](https://arxiv.org/abs/2609.21749)

**<font color=#1a73e8>作者：</font>** Rui Sun, Zhi Zheng, Zhenkun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Skills can improve the performance of Large Language Model (LLM) agents by providing task-specific procedural guidance, while skill optimization further improves their effectiveness through iterative refinement. However, existing skill optimization methods typically represent skills as unstructured natural-language instructions, creating two key challenges: 1) Unstructured skills often lack explicit workflow-level guidance and contain substantial redundancy, making them difficult for LLMs to execute; 2) the vast search space of unconstrained natural-language skills makes skill optimization ineffective. To address these challenges, we propose representing skills as graph-structured natural-language artifacts. In graph-structured skills, each node represents an execution step together with its operational guidance, while directed edges encode context-dependent transitions between steps. Compared to unstructured skills, graph-structured skills can provide clear workflow-level guidance. Moreover, the proposed graph-structured skill can also facilitate skill optimization. Building on this structured representation, we introduce GraphSkillEvo, a population-based evolutionary optimization framework with mutation and crossover operators for graph-structured skills. By maintaining multiple candidate skills and combining effective components, GraphSkillEvo enables broader and more comprehensive exploration of the structured skill space than purely LLM-based iterative self-refinement. Extensive experiments across five agent benchmarks demonstrate that GraphSkillEvo consistently outperforms the strong skill optimization baseline SkillOpt, improving average accuracy by 4.01% on GPT-5.4-nano and 1.76% on GPT-5.4. Our code is available at this https URL.

---


### 108. [ECG Mirage: Revealing and Mitigating the Underutilisation of ECGs in Vision-Language Models for Clinical Prediction](https://arxiv.org/abs/2609.21755)

**<font color=#1a73e8>作者：</font>** Jinning Liang, Mingcheng Zhu, Tingting Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergency department (ED) decision-making relies on heterogeneous clinical information, including patient history, vital signs, laboratory results, and electrocardiograms (ECGs). Vision--language models (VLMs) can jointly process these modalities, but strong predictive performance does not necessarily imply meaningful use of the correct patient's ECG. We term this failure mode ECG Mirage: apparent multimodal capability without useful dependence on patient-specific ECG information. We distinguish two forms: ECG neglect, where ECGs provide little predictive benefit, and ECG confusion, where matched ECGs outperform no-image inputs but not mismatched ECGs. To evaluate these behaviours, we compare predictions obtained with matched ECGs, outcome-discordant mismatched ECGs, and no-image inputs while holding the clinical text and prediction targets fixed. Across four VLMs on MDS-ED, matched ECGs provide no consistent advantage for either ICU admission or clinical deterioration prediction. We then train four restricted visual prompts using supervised learning followed by conditional direct preference optimisation, while keeping the VLM backbone frozen. The resulting models achieve balanced accuracies of 70.6% for ICU admission and 67.5% for deterioration and increase the matched-versus-mismatched performance gap to approximately 16.5 and 5.5 percentage points, respectively. Overall, our study identifies ECG Mirage in multimodal clinical prediction and introduces visual prompt tuning as an efficient mitigation strategy.

---


### 109. [Beyond Benchmark Scores: Auditing Medical Vision-Language Models for Chest X-Ray Tuberculosis Screening](https://arxiv.org/abs/2609.21763)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, M. Tanveer, Mohd. Arshad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A medical model's benchmark score does not establish that the same conclusion holds under a different evaluation. This study tests whether claims about model ranking, score reliability and screening performance survive changes in cohort, prompt, negative spectrum, specified prevalence and operating threshold. We audit three medical vision-language models (BioMedCLIP, CheXficient, and MedSigLIP) and a general-domain OpenCLIP comparator on 12,200 chest radiograph records from four datasets (Montgomery, Shenzhen, TBX11K, and VinDr-CXR). Five fixed prompt families yield 244,000 model--image--prompt scores. No model leads every cohort and reliability criterion. Prompt-family changes alter AUROC in 21 of 48 multiplicity-controlled comparisons. Replacing healthy controls with sick non-tuberculosis controls reduces AUROC by 0.075--0.306 across all four models. On VinDr-CXR, the three medical models distinguish tuberculosis from no-finding controls substantially better than from pneumonia or lung tumor; their AUROC point estimates for both named diseases fall below 0.5. CheXficient has documented VinDr-CXR pretraining exposure, which limits the interpretation of its results. Thresholds chosen for 95\% sensitivity on TBX11K training retain that constraint by point estimate in only four of sixteen target evaluations. A five-seed supervised source model reaches 0.999 AUROC on TBX11K validation but 0.629 on each of two external cohorts. Conservative exclusion of perceptual-overlap candidates narrows this gap without closing it. These retrospective, single-task results show that discrimination, score reliability and threshold retention support different portability claims. Evidence for chest X-ray tuberculosis screening should identify the complete evaluation specification rather than attribute clinical portability to a checkpoint alone.

---


### 110. [LLM-Generated Feature Pools for Time Series Anomaly Detection](https://arxiv.org/abs/2609.21801)

**<font color=#1a73e8>作者：</font>** Youssef Attia El Hili, Malik Tiomoko, Corinne Ancourt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how far a simple statistical pipeline can go on univariate time series anomaly detection under a strict selection protocol. The method extracts a small pool of statistics over sliding windows, scores each window with a transductive robust (MAD) model, and selects a feature subset per domain on a held-out tuning split. On TSB-AD-U it reaches $0.529$ per-series VUS-PR, above the best neural ($0.45$) and statistical ($0.44$) entries on the public leaderboard and within $0.06$ of the strongest pretrained foundation model, several of which use more supervision than ours. Ablations locate the cause: across three selection strategies and a hindsight oracle the score moves by $0.031$, and across the aggregation grid by $0.096$, while changing the candidate pool moves it by $0.226$. The candidate pool sets the ceiling; the search over it is second-order. We therefore generate a pool per domain by prompting a multimodal LLM with in-context example windows from that domain. The generated pools match the hand-crafted one under matched selection, and the two cover different domains: selecting over their union improves on the generated pool in all twelve generator-seed pairs and lifts the pipeline to $0.588$, matching the performance of the best entry on the leaderboard.

---


### 111. [RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/abs/2609.21827)

**<font color=#1a73e8>作者：</font>** Qiao Hu, Yepeng Weng, Bo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by drafting multiple tokens in parallel, with tree-based methods further improving efficiency through hierarchical structures. Dynamic-tree methods such as EAGLE-3 perform well under greedy decoding via deterministic top-K expansion and global pruning. However, in stochastic decoding (T>0), this mechanism collapses the draft distribution into one-hot probabilities, causing a severe drop in acceptance rate. This creates a dilemma: dynamic-tree methods sacrifice stochastic sampling to preserve context-aware topology, while static-tree methods preserve stochastic sampling with context-agnostic structures. The issue arises because the same probability distribution is used for two conflicting tasks: constructing the tree and verifying tokens. This coupling makes direct injection of randomness challenging due to the resulting stochastic process. We resolve this by decoupling these roles: RheoSampling assigns a token sampled from the draft distribution a proxy probability for tree expansion and pruning alongside its true sampling probability for verification. Specifically, we inject a sampled token among the deterministic top-K slots and treat it with different probabilities during construction and verification, making RheoSampling the first dynamic-tree method with both context-aware top-K construction and stochastic sampling while maintaining losslessness. We establish the lossless guarantee through an equivalence-class analysis that compresses the stochastic tree space into tractable classes. An OT-based verification strategy and a sparse draft mechanism ensure that theoretical gains translate into practical efficiency. Experiments across LLMs and benchmarks demonstrate improvements in acceptance rate and speedup over state-of-the-art dynamic tree methods. This framework may provide a template for analyzing stochastic tree structures.

---


### 112. [Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments](https://arxiv.org/abs/2609.21828)

**<font color=#1a73e8>作者：</font>** George Xi Wang, Xiangyu Li, Shaoyue Wen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Blind and low-vision users often face challenges when locating and physically acquiring objects in unfamiliar indoor environments. Existing vision-language-model-based assistants can provide semantic descriptions but may introduce latency, hallucinations, and guidance that is poorly aligned with embodied action. We present Touvigation, a hands-free object acquisition system that combines vision-language understanding with persistent local spatial modeling to provide low-latency, body-relative guidance. Drawing on formative interviews with eight blind and low-vision participants, we design a multi-stage guidance framework that adapts spatial references as users transition from orienting, to walking, to reaching and tactile verification. We evaluated Touvigation with 12 blind and low-vision participants against a multimodal large-language-model assistant and unassisted search. Touvigation achieved 100% task success, compared with 58% for the multimodal assistant and 85% for unassisted search, while reducing completion time and cognitive workload. Our findings demonstrate how persistent spatial grounding and adaptive embodied guidance can improve object acquisition for blind and low-vision users.

---


### 113. [EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise](https://arxiv.org/abs/2609.21841)

**<font color=#1a73e8>作者：</font>** Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models now produce professional deliverables that expert graders judge to match human work on a substantial share of economically valuable tasks, yet most enterprise GenAI initiatives fail to show a measurable business effect and a large fraction of agentic projects are expected to be cancelled. We argue that this is substantially a measurement problem: public benchmarks answer "what can the model do?", whereas a deployment decision requires "is this workflow fit, reliable, safe and worth scaling - here, on our data, under our controls?". We present EnterpriseVal, a use-case-level evaluation system that closes this gap. It comprises (i) a formal specification of the use case and of the frozen socio-technical configuration under test, model, prompts, retrieval, tools, guardrails and human oversight, with an autonomy level and consequence tier that jointly set the required evaluation intensity; (ii) a metric catalogue spanning fidelity, utility, efficiency, reliability, assurance and oversight; (iii) a grading protocol that scales blinded expert judgement with calibrated LLM-as-judge scoring through prediction-powered inference; (iv) a two-tier threshold gate, stated as an executable algorithm, that maps metric vectors with confidence bounds to REJECT/CONDITIONAL/SCALE decisions; and (v) a value-and-risk model in which the reviewer catch rate is a measured parameter. We report a pilot across three workflows in a global bank. In credit-memo drafting, human-graded citation precision reached 88% and hallucination rate 1.6% for the best model against gates of 70% and 5%; in procedure transformation, analyst refinement effort fell from an estimated 27.4 to 2.9 hours per document. We separate established results, documented pilot evidence, the proposed system and open hypotheses, and specify the experiments required for full validation

---


### 114. [The Weight Is Over - Interactive Diffusion on Consumer GPUs](https://arxiv.org/abs/2609.21849)

**<font color=#1a73e8>作者：</font>** Frieder Ganz, Maximilian Müller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device inference is booming, but the momentum is almost all in language models. Diffusion pipelines are memory hungry, latency-sensitive, and require orchestrating an embedder, a transformer, a decoder, and often further postprocessing that is not as standardized as LLM inference loops are. We navigate the trade-off between performance, quality, and model footprint to reach as many client devices in the wild as possible. We make three contributions: an embedding translator that maps a small text encoder into a large encoder space to cut weight and latency; a reproducible sweep recipe for navigating the speed/quality/memory triangle in diffusion pipelines; and an interactive on-device image generation editor achieving sub-second TTFI on recent GPUs.

---


### 115. [Do Personality-Tuned LLMs Make Better Social Agents?](https://arxiv.org/abs/2609.21857)

**<font color=#1a73e8>作者：</font>** Tim Krabbe, Xiaodan Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used in social simulations for socially interactive agents and robots, offering more flexibility than rule-based systems. However, even though they mimic human behaviour very well, there is a persistent alienness to them. This work investigates whether personality-aware fine-tuning can reduce this gap by improving the consistency and controllability of personality-conditioned dialogue generation compared with instruction prompting alone. We fine-tune two small open-weight LLMs, Qwen2.5-7B-Instruct and Ministral-8B-Instruct, using a corpus that combines personality-labelled social media posts and dialogues to create a personality-based dialogue engine for social simulation. The resulting models are evaluated across multiple social interaction scenarios using three independent LLM judges, which assess personality fidelity and provide evidence-based behavioral interpretations. We additionally quantify inter-rater agreement and lexical characteristics of the generated dialogue. Results indicate that fine-tuned models are not better at role-playing different personalities than their respective baseline models. However, low inter-rater agreement limits the confidence with which these results can be interpreted. Concerning the quality of generated texts, fine-tuned models are mostly comparable to the baselines, with fine-tuning improving the linguistic diversity of the Qwen models. While the results appear generally usable and the baseline models offer the best overall performance, future studies should place greater emphasis on the quality and domain alignment of training data for accurate personality role-playing.

---


### 116. [Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/abs/2609.21858)

**<font color=#1a73e8>作者：</font>** Yanxiao Liu, Sicheng Wan, Zhan Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved state-of-the-art performance across a wide range of tasks, motivating two important aspects of deployment: inference efficiency and output provenance, which can be tackled by speculative sampling and watermarking, respectively. However, recent works have shown that combining these two goals is highly nontrivial and can be potentially impossible. In this work, we develop a novel multi-draft speculative sampling algorithm based on Poisson processes that improves the frontier of this fundamental trade-off. The proposed algorithm has strong sampling efficiency on its own and, more interestingly, is naturally watermarkable: we can embed an unbiased watermark without degrading speculative acceptance. Moreover, our algorithm is based on an exact list-coupling-without-communication scheme, which yields a drafter invariance property that benefits both sampling and watermarking. It is the first multi-draft, drafter-invariant speculative sampling scheme that maintains both watermark strength and sampling efficiency, and we experimentally verify its strong performance in both aspects.

---


### 117. [TrialAtlas: Multi-Agent Research Organization for Clinical Trial Design and Optimization](https://arxiv.org/abs/2609.21859)

**<font color=#1a73e8>作者：</font>** Jiacheng Lin, Zifeng Wang, Zheng Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nearly 90% of drugs entering clinical development ultimately fail, despite billions of dollars in investment. Pharmaceutical companies therefore rely on clinical development planning (CDP) and probability of technical and regulatory success assessment to anticipate development risks, yet these decisions remain labor-intensive and subjective, requiring experts across clinical science, statistics, regulatory affairs, and competitive intelligence to jointly acquire, synthesize, and reason over heterogeneous evidence. Here, we introduce TrialAtlas, a memory-augmented multi-agent research organization for CDP that mirrors this collaborative process by coordinating specialized agents for literature synthesis, competitive trial intelligence, regulatory precedent analysis, and integrated reasoning over trial design and development risk. TrialAtlas further learns from historical clinical trials and regulatory outcomes, including prior New Drug Applications (NDAs), to ground its decisions in accumulated development experience. To evaluate these capabilities in an authentic regulatory setting, we introduce TrialAtlasBench, constructed from 291 FDA Complete Response Letters and spanning three practical tasks: detecting trial design deficiencies, recommending actionable design improvements, and predicting technical and regulatory success. TrialAtlas achieves an F1 score of 50.0% for deficiency detection, outperforming the strongest baseline by 6.1 points, and reaches 85.3% balanced accuracy and 84.7% F1 for prediction of technical and regulatory success, improving over the best baselines by 6.7 points in balanced accuracy and 12.0 points in Cohen's kappa. In expert evaluation, 86.4% of TrialAtlas-generated concerns were judged valid, compared with 83.1% for OpenAI DeepResearch and 59.3% for Gemini DeepResearch.

---


### 118. [AutoRecLab: Describe the Experiment, Get the Code!](https://arxiv.org/abs/2609.21863)

**<font color=#1a73e8>作者：</font>** Moritz Baumgart, Philipp Meister, Justus Krell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empirical evaluation is central to recommender-systems (RecSys) research, but turning experimental designs into executable code remains a manual and error-prone task. We present AutoRecLab, a Python-based autonomous RecSys lab that automates RecSys experiments from natural-language prompts. Given a research idea, AutoRecLab derives explicit experiment requirements, builds and validates a prototype, and iteratively expands it into the requested full experiment. The workflow combines retrieval-augmented generation (RAG) for documentation lookup, static type verification, and execution-steered tree search. In our demonstration, AutoRecLab autonomously implements an explicit-to-implicit feedback conversion study. In a baseline comparison across six algorithms and three datasets, 8 of 9 runs succeed at an average cost of approx- imately $1 per run with GPT-5.4-mini.

---


### 119. [Benchmarking the Explanatory Quality of Open-Weight Vision-Language Models in Face Recognition](https://arxiv.org/abs/2609.21879)

**<font color=#1a73e8>作者：</font>** Laurent Colbois, Sébastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have recently been proposed as promising tools for face recognition, as they can produce natural language explanations alongside similarity scores. This capability is considered appealing for face comparisons in forensic contexts, which require decisions to be transparent and auditable. However, existing evaluations of VLMs for that use case focus mostly on recognition accuracy, while the validity of generated explanations remains unquantified. In this work, we introduce a benchmarking framework for VLM-based face recognition that treats explanation quality as a core evaluation axis. We propose two criteria that explanations should satisfy: relevance, i.e., reliance on identity-stable facial features; and faithfulness, i.e., alignment with the visible image content without hallucinated features. We jointly develop a methodology enabling the quantification of relevance and faithfulness of evaluated models, based on constraining model outputs to a structured explanation format that supports automated querying and auditing. Using this framework, we benchmark several families of open-weight VLMs, jointly evaluating face verification accuracy and explanation quality. Our results highlight remaining shortcomings of produced explanations, and emphasize the need for such explanation quality metrics to get a complete picture of model performance. The proposed benchmark and open-source evaluation harness provide a foundation for proper benchmarking and future fine-tuning of explainable face recognition systems.

---


### 120. [Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](https://arxiv.org/abs/2609.21888)

**<font color=#1a73e8>作者：</font>** Chenye Ke, Zirui Liu, Qi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting pretraining data in large language models is challenging because high likelihood can reflect either training exposure or strong generalization. In the joint space of prediction loss and predictive entropy, a likelihood-only detector uses a horizontal boundary and can mistake predictable non-members for members. Motivated by this, we introduce an inclined boundary that evaluates prediction loss relative to predictive entropy. Our analysis shows that entropy correction can preserve the expected membership signal while reducing its variance, thereby improving standardized member--non-member separation. We further extend the mean--variance analysis to the more general setting with a nonzero mean entropy gap. Interestingly, this entropy-adjusted score admits a Helmholtz free-energy interpretation, leading to Energy Transfer Detection (ETD), which views pretraining data detection from a macroscopic residual free-energy transfer perspective. Extensive experiments show that ETD achieves the best average detection performance, improving average AUROC by up to 3.5\% and TPR@5\%FPR by up to 5.1\%, while remaining robust across diverse settings.

---


### 121. [LLMs as Feature Engineers for Text-and-Tabular Prediction](https://arxiv.org/abs/2609.21894)

**<font color=#1a73e8>作者：</font>** Merwan Barlier, Blaz Skrlj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce an iterative framework that automates the extraction of interpretable, schema-bound categorical features from unstructured text for tabular prediction models. To navigate the feature space, a generator LLM proposes semantic definitions, a separate extractor LLM materializes the features, and a downstream tabular model evaluates their predictive performance. We optimize this search by translating explicit model errors, such as AUC ranking inversions, into natural-language feedback, steering the LLM to resolve specific predictive failures. Evaluated across three public datasets, this error-driven loop accelerates feature discovery by up to $3\times$ compared to unguided search. Empirically, the generated features demonstrate strong multi-view complementarity, strictly outperforming any subset when combined with TF-IDF and dense embeddings. Finally, the framework guarantees instance-level interpretability: the discovered features dominate SHAP importance rankings and provide a fully transparent, semantic audit trail for every prediction.

---


### 122. [ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment](https://arxiv.org/abs/2609.21899)

**<font color=#1a73e8>作者：</font>** Yanxiao Liu, Sicheng Wan, Deniz Gündüz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-of-$n$ (BoN) sampling is a simple yet effective inference-time alignment method, but hard maximization provides only coarse control over the trade-off between reward and distribution shift. Soft Best-of-$n$ (Verdun et al. 2025) provides smoother control and converges to the optimal distribution associated with KL-regularized reward maximization. In this paper, we introduce ExpBoN, an alternative soft BoN method based on the exponential-noise report-noisy-max mechanism. It admits an exact finite-$n$ decomposition, which yields exponentially fast convergence in total variation, expected reward, and both directions of KL divergence. We provide comprehensive theoretical analyses of its convergence and regret behavior. We further integrate ExpBoN into the guided speculative inference (GSI) framework (Geuter, Mroueh, and AlvarezMelis 2025), resulting in ExpGSI, for efficient reward-guided LLM alignment. ExpGSI yields substantial reductions in computational cost while maintaining comparable accuracy. Experiments on MATH500, MMLU-STEM, and Minerva Math with the Qwen2.5-Math and Qwen3 model families show that ExpGSI reduces estimated computation by $14\%$-$39\%$ across candidate budgets for Qwen2.5-Math and by up to $45\%$ at $n=16$ for Qwen3. Overall, our results provide a theoretical and algorithmic foundation for exponential-noise BoN and efficient test-time LLM alignment.

---


### 123. [Can I Trust My Body? A Three-Year Autoethnography of ChatGPT's Place in My Support System for Panic Attacks](https://arxiv.org/abs/2609.21925)

**<font color=#1a73e8>作者：</font>** Dongyijie Primo Pan, Pan Hui, Mirjana Prpa  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly seek mental health support from large language models, yet little is known about their use across years of recurrent panic. We present a three-year analytic autoethnography of the first author's ChatGPT use while living with panic disorder, drawing on conversations, personal records, and accounts from friends or family members and professionals. Narrative analysis traces how my questions shaped ChatGPT's roles and how earlier experiences influenced later responses to symptoms. Familiar explanations could make sensations less frightening, while changed symptoms renewed fears of serious illness. During sudden panic, advice could be difficult to follow, and some replies prompted further checking. Conversations could end while symptoms, checking, or help-seeking continued. We propose trajectory-level safety during and after panic: usable advice (Fit), a stopping point for repeated checking and reassurance seeking (Closure), and useful understanding and human support that remain available over time (Continuity).

---


### 124. [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](https://arxiv.org/abs/2609.21940)

**<font color=#1a73e8>作者：</font>** Zijie Cao, Xijun Qu, Zhicheng Gu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for large language model (LLM) agents to maintain consistency and personalization over extended interactions. Existing memory systems typically rely on fixed granularities or static schemas, but these designs struggle when heterogeneous information, such as preferences, events, constraints, and temporal updates, is embedded in a single mixed representation. The resulting semantic interference makes top-K retrieval sensitive to noise and often leaves relevant evidence poorly ranked. We present AutoViewMem, a data-driven framework that organizes long-term conversational memory into self-configuring, low-overlap semantic views before indexing. AutoViewMem discovers candidate views from interaction traces, selects a compact complementary view set, and uses these views to guide write-time structured extraction of provenance-grounded memories. This representation-first design moves semantic disentanglement from retrieval time to write time, allowing standard top-K similarity search to retrieve focused evidence without explicit routing or iterative retrieval. We further apply offline consolidation to improve memory compactness and consistency. Experiments on the LoCoMo and PersonaMem benchmarks, under both Qwen3-8B and Qwen3-14B backbones, show that AutoViewMem improves long-horizon question answering and personalization over strong memory baselines while preserving a simple inference pipeline.

---


### 125. [NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities](https://arxiv.org/abs/2609.21967)

**<font color=#1a73e8>作者：</font>** Jagadeesh Balam, Travis Bartley, Edresson Casanova 等 49 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce NemotronLabs VoiceChat, an open full-duplex speech-to-speech model with native tool-calling capabilities. NemotronLabs VoiceChat combines a streaming speech encoder and decoder-only language model with parallel specialized output streams for agent text and structured function calls, an auxiliary RNN-T branch for incremental user transcription, and a streaming TTS decoder. This design enables the model to listen, transcribe, reason, invoke tools, and speak within a unified streaming architecture while preserving the temporal behavior required for natural conversation. On Full-Duplex-Bench 1.0, NemotronLabs VoiceChat achieves the lowest pause-handling takeover rates among evaluated open-weight systems, 100\% takeover following user interruptions, and a 4.33/5 post-interruption response-quality score. On Full-Duplex-Bench 1.5, it resumes its response after user backchannels in 93\% of cases. NemotronLabs VoiceChat obtains a 55.1 normalized average on VoiceBench and, on Full-Duplex-Bench 3.0 (FDB 3.0), achieves 82.5\% tool-selection F1, while argument accuracy and end-to-end tool execution remain areas for improvement. These results demonstrate that full-duplex interaction, speech recognition and generation, general language capabilities, and external tool use can be integrated in a single open speech-to-speech model without sacrificing real-time conversational behavior.

---


### 126. [A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/abs/2609.21996)

**<font color=#1a73e8>作者：</font>** Hiskias Dingeto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can hold knowledge they do not report. A model may sandbag on a capability evaluation, or answer against what it internally knows, and its outputs alone cannot tell whether it is hiding an answer or simply does not have one. We borrow the Concealed Information Test, a forensic method that identifies guilty knowledge by presenting a suspect with the true detail among plausible decoys and measuring a stronger response to the item they recognize. Our method, Probe of Internal Recognition (PIR), does the same inside a model. It presents a question with its candidate answers and reads, from the model's internal states, which candidate the model recognizes as correct. PIR is reference-free, needing no honest reference model and no labeled truth corpus. Across eight models from five families (Gemma, Qwen, Llama, Mistral, and Phi), PIR recovers the recognized answer at 0.70 to 0.87 balanced accuracy, well above the 0.28 to 0.40 unknown-item baseline and the 0.25 chance rate. It stays readable across every form of concealment we test, from prompted deception and trained sandbagging to external password-locked and circuit-broken checkpoints, with recognition between 0.85 and 0.93. When the model hides a known answer, recognition stays high. When unlearning removes the knowledge, recognition drops to the level of a question the model never knew. PIR therefore separates a model that will not answer from one that cannot, which supports sandbagging audits and unlearning verification. The signal is causal, adds information beyond black-box behavioral cues, and extends from multiple-choice questions to free-form generation.

---


### 127. [Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents](https://arxiv.org/abs/2609.21997)

**<font color=#1a73e8>作者：</font>** Hafsa Akbar, Daniel Platnick, Marjan Alirezaie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents in social simulation revise their opinions implicitly, in context: how open an agent is to persuasion can neither be specified nor verified, and collective outcomes inherit the model's training prior. We introduce Bayesian Chronicle Agents (BCA), a minimal belief layer separating \emph{what} an agent believes from \emph{how} it speaks. Each stance is a probability, updated by one Bayesian step per utterance heard. A single prior-strength parameter $\kappa$ encodes stubbornness, modeled after its role in Friedkin--Johnsen (FJ) opinion dynamics. We then sweep this parameter to yield three canonical regimes of opinion dynamics on demand (consensus, persistent disagreement, committed-minority influence), with persistent disagreement matching the FJ closed-form fixed points at $R^2\!=\!0.93$--$0.99$. We further show that prescribed $\kappa$ remains recoverable after the language round-trip, with perfect rank-order recovery across all four models. Explicit belief also makes simulation auditable: the layer surfaces systematic per-model stance biases that end-to-end simulation would silently absorb.

---


### 128. [RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents](https://arxiv.org/abs/2609.22000)

**<font color=#1a73e8>作者：</font>** Shuai Bai, Jiayong Deng, Yikun Fu 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) have advanced along two separate lines: graphical interaction and software development through code and the command line. Real digital work requires both, interleaved rather than stacked end to end. We study hybrid CUAs that autonomously decide when to explore an interface, implement software, and run and visually verify their artifacts. We introduce RecreationWorld, a five-platform framework built around recreation: given a running reference, an agent must discover its behavior and build a faithful implementation with no prescribed workflow. RecreationWorld provides reproducible environments on Ubuntu, macOS, Windows, Android, and Web, plus a unified harness with native GUI control and coding tools. The running reference serves as an oracle for hidden behavioral tests, providing execution-grounded rewards. We scale trajectory generation with high-quality open-source applications. Models trained on these trajectories improve across five out-of-distribution coding and hybrid computer-use benchmarks and more frequently verify their rendered outputs, providing evidence of transfer beyond recreation. For held-out evaluation, we introduce RecreationBench, comprising 250 diverse tasks across domains and platforms. Reference-grounded programmatic and visual assertions cover action-conditioned outcomes at multiple interaction depths; each is validated on the reference and by human reviewers before the suite is frozen for automatic scoring. GPT-6 Astra leads at 58.1% overall, but passes all programmatic tests on just 2.8% of tasks. Agents reproduce static interface structure more reliably than interactions and computed outputs, while generated applications remain smaller and more monolithic than their references. We release the benchmark, environments, and test suites.

---


### 129. [Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](https://arxiv.org/abs/2609.22005)

**<font color=#1a73e8>作者：</font>** Richard Zhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gating the value pathway of attention reportedly improves language model pretraining, and prior studies disagree on why. We argue and provide experimental evidence that such gates supply two different things that softmax attention lacks: abstention and noise filtering. The first is abstention, which allows an attention head to output nothing, bypassing the requirement that attention weights must sum to one. The second is noise filtering, which allows the value pathway of an attention head to suppress interference from superposed features in the residual stream. In our experiments in matched models from 10M to 350M parameters, we supply abstention through a learned per-head sink logit in the softmax and noise filtering through a gate on each value. We report three empirical findings. First, the benefit of abstention, measured as the reduction in validation loss relative to a matched baseline, declines as models grow, whereas the benefit of noise filtering increases with scale. In particular, abstention accounts for nearly all of the gain from gating at 10M and filtering for most of it at 350M. Second, the best model at every scale is the one with both primitives built in. Third, injecting controlled interference into the values a head reads confirms that the gate removes such interference, and reveals that each of the two gate forms we study has a characteristic blind spot. Supplying both primitives adds negligible parameters and remains compatible with the key-value cache.

---


### 130. [DiaVLo: Diagnosing Behaviours of Vision-Language Models](https://arxiv.org/abs/2609.22008)

**<font color=#1a73e8>作者：</font>** Lorenzo Corti, Jie Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) rely on storing and transferring appropriate information across their sub-components. Verifying that the VLMs exhibit desired behaviours, while avoiding harmful ones, is central to their reliable deployment. Yet, methods that identify VLM behaviours remain scarce. We present DiaVLo, a diagnostic framework that leverages human curation and VLMs' generation capabilities to construct specifications of desired and observed VLM behaviours, surfacing potential misalignments. Beyond this, DiaVLo also provides causal estimates to identify the most influential concepts steering VLM behaviours. We evaluate DiaVLo on several open-source VLMs under both classification and generation conditions. Our experiments show that DiaVLo produces behaviour labels that correlate with model performance and provide context for measured performance. DiaVLo surfaced behaviours that are clearly aligned and misaligned, alongside patterns in how VLMs perceive, organise, and prioritise concepts.

---


### 131. [Beyond Reactive Assistance: PV-Care Using Low-Density EEG and AI to Provide Proactive, Context-Aware Help for MCI](https://arxiv.org/abs/2609.22024)

**<font color=#1a73e8>作者：</font>** Simon L Liu, Manish Kumar Krishne Gowda  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing elderly population gives rise to an urgent need for intelligent support systems, particularly for individuals with Mild Cognitive Impairment (MCI). This paper presents PV-Care, a proactive AI-driven assistance scheme that integrates wearable electroencephalogram (EEG) sensing with visual environmental perception to provide real-time, context-aware voice assistance for MCI users. Unlike traditional assistant systems that passively wait for user commands, PV-Care actively initiates helpful interactions based on the user's detected brain states, including Learning, Memory Recall, and Resting, using a novel deep neural architecture named Spatial and Frequency Refinement Network (SFR-Net). By combining EEG-based cognitive-state recognition with AI-based visual analysis, PV-Care generates structured "4W-UT" prompts to guide the output of large language models (LLMs). Simulation results and user studies validate the high accuracy of the proposed SFR-Net and the effectiveness of PV-Care's context-aware assistance. These results indicate that PV-Care is a feasible and promising solution for MCI caring.

---


### 132. [QuranicMMLU: A Cognitively-Aware Benchmark for Evaluating Generative AI Solutions on Quranic Linguistic Knowledge](https://arxiv.org/abs/2609.22038)

**<font color=#1a73e8>作者：</font>** Rawan El Ghali, Umm Kulsoom, Anas Madkoor 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce QuranicMMLU, a benchmark for evaluating generative AI on Quranic Arabic across multiple dimensions of linguistic complexity. Existing Quranic benchmarks center on general question answering and semantic retrieval, without probing specific linguistic competencies or stratifying by cognitive demand and verse difficulty. We construct a five-pillar Quranic taxonomy spanning Phonology, Morphology, Syntax, Semantics, and Pragmatics, with 31 leaves covering phenomena from tajwīd and root-and-pattern morphology to occasions of revelation and inter-surah coherence. For each leaf we generate questions stratified by Bloom's cognitive level and verse perplexity, then have LLM as a judge to independently answer and score every item and route the annotations to manual review. The resulting dataset comprises 980 human-reviewed questions, each issued in both open-ended and multiple-choice form. We benchmark 12 systems on these items and find that the Islamic-specialized model leads, yet every system scores higher on multiple-choice accuracy (average 84%) than open-ended answer quality (average 60%): the two rankings agree closely (Kendall's {\tau}=0.73), but multiple-choice scoring hides failures that surface only once answer choices are removed. QuranicMMLU thus offers a rigorous, linguistically grounded framework for evaluating Arabic NLP in the Quranic domain.

---


### 133. [PRIME: Perception Feedback with Situational Memory Embeddings in VLA Models](https://arxiv.org/abs/2609.22040)

**<font color=#1a73e8>作者：</font>** Erik Deinzer, Naya Baslan, Luca Paparusso 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Vision-Language-Action (VLA) models for autonomous driving operate primarily through feedforward inference across the perception--reasoning--planning hierarchy. While modern architectures maintain temporal recurrence within the perceptual module, early perception remains blind to downstream reasoning and navigation goals, processing visual inputs agnostically without prioritizing cues informed by prior decisions. To bridge this gap, this paper introduces PRIME, a learned feedback mechanism that conditions the VLA perceptual queries on a novel Situational Memory. By aggregating latent representations of past perception, reasoning, navigation goals, and predicted behaviors across an L-step window via cross-attention, PRIME enables intent-driven perceptual attention at minimal computational cost, adding only a maximum of 29.7M parameters (0.41% of the 7.3B-parameter base model). Evaluated on the Bench2Drive closed-loop benchmark, PRIME achieves a state-of-the-art Driving Score of 82.47 (+4.73 over ORION) and a Success Rate of 60.00% (+5.38 percentage points), the highest reported Driving Score among published VLAs trained on Think2Drive demonstrations.

---


### 134. [$λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource](https://arxiv.org/abs/2609.22041)

**<font color=#1a73e8>作者：</font>** Yufeng Wang, Parivesh Priye, Meeshawn Marathe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is increasingly used to align image generators with reward signals, and Flow-GRPO recently extended this paradigm to flow-matching models by treating the denoising sampler as a stochastic policy that can be optimized from reward feedback. Training in this setting is unstable in a way specific to multi-step denoising: the policy update changes systematically across denoising steps, with importance ratios drifting below one, becoming increasingly dispersed, clipping at different rates, and leaving fewer usable samples late in training. Prior work treats these effects as separate failure modes and addresses each with a hand-tuned stabilizer. We show instead that they arise from a single per-step quantity, which we call path variance. This quantity is determined exactly by the sampler's Gaussian transition kernel and can be estimated cheaply during training. This reframes instability as a resource that can be measured and budgeted rather than a collection of symptoms to repair. Our method, $\lambda$-Controlled GRPO, calibrates importance-ratio behavior from this predicted law rather than from noisy empirical statistics, and allocates gradient effort across denoising steps according to their predicted cost. The two scales governing the update are fixed by standard policy choices rather than introduced as free tuning parameters. On a text-to-image model under two reward settings, rendering difficult target text scored by optical character recognition and matching human preferences scored by a preference model, $\lambda$-Controlled GRPO improves both text accuracy and preference reward over the strongest empirical stabilizer. It also keeps late-step path variance within its intended budget, precisely where the baseline systematically overshoots. The result is a Flow-GRPO update calibrated by its own transition law rather than stabilized after instability appears.

---


### 135. [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](https://arxiv.org/abs/2609.22043)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Jinghong Zhang, Haoran Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memory store contains conflicting positions, standard retrieval-augmented generation (RAG) blindly injects memories and amplifies hallucinations: in models susceptible to memory injection, the RAG hallucination rate under conflicting memories is markedly higher than that of a memory-free baseline. Inspired by memory signaling mechanisms in the prefrontal cortex, we propose the Memory Decision Layer (MDL), a zero-parameter memory decision controller situated between the retrieval and generation stages. Its core is a three-signal complementary encoder that fuses relevance, reliability, and task risk through QR-based orthogonal subspace projection and a meta-working-memory signal into an interpretable decision representation that quantifies the trustworthiness of retrieved memories. Building on this encoder, MDL explicitly decouples confidence from consistency and introduces risk inversion and explicit abstention. Evaluations on mainstream large language models and multiple open-source datasets show that MDL reduces the hallucination rate under conflicting memories by about 56.04% in general scenarios and approaches zero hallucination in high-risk scenarios. The controller is fully white-box: it relies purely on geometric operations, requires no trained parameters, and adds only about 0.14 ms per decision -- roughly 50x faster than the embedding-retrieval step that precedes it and four to five orders of magnitude faster than an LLM self-evaluation call.

---


### 136. [Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw](https://arxiv.org/abs/2609.22067)

**<font color=#1a73e8>作者：</font>** Renkai Ma, Ruyuan Wan, Xuan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users increasingly delegate work to autonomous AI agents, yet evaluations typically measure task completion rather than the values users prioritize. Using Value Sensitive Design, we analyzed, with LLM assistance, 73,093 first-person Reddit posts about using OpenClaw, each for its human value, agent aspect, value fulfillment, and user outcome. The 21 values form six value groups, including Autonomous, Dependable, and Affordable Operation, Bounded Reach, Reviewability, and Equitable Access. Relative to each aspect's corpus share, values clustered not at the agent's outputs but at the operating conditions users set around a run. Values were usually met where users described what the agent delivered, in five of six groups, and mostly unmet where users described supervising it, in all six groups. We conceptualize this pattern as value-sensitive delegation. Supporting human values requires attention not only to what an agent accomplishes, but to the conditions users set around delegation, including cost, access, and oversight.

---


### 137. [CodeMidas: Scaling Agentic Coding RL Environments from Code Itself](https://arxiv.org/abs/2609.22068)

**<font color=#1a73e8>作者：</font>** Bowen Ye, Lei Li, Shicheng Li 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training capable coding agents via reinforcement learning (RL) requires diverse tasks with reliable verifiers. Open-source codebases offer a rich source of such tasks, while existing methods typically rely on development artifacts such as issues and commits, limiting the range of tasks that can be extracted. To better scale RL environments, we present CodeMidas, an agentic pipeline that turns implemented functionality in existing codebases into executable RL environments using source code as its only task-specific input. CodeMidas allocates agentic compute to every stage of environment construction: agents explore implemented functionality to formulate behavioral specifications, construct tests grounded in execution of the original code, and validate and filter candidate tasks through execution checks and repeated solution rollouts. The resulting dataset has 5,545 training tasks from 3,185 open-source codebases spanning 23 programming languages and 15 technical domains. Training MiMo-V2.5 on these tasks with GRPO improves performance on all five diverse benchmarks, covering issue repair (DeepSWE + 11.7%), whole-program construction (ProgramBench +17%), and terminal work (Terminal-Bench v2.1 +8.5%). Ablations show that increasing the number of high-quality training tasks improves performance. Trajectory analysis shows the RL-trained agent demonstrates better behaviors like increasing codebase exploration and more diverse self-verification. These results establish source code as a scalable foundation for constructing RL environments that improve coding agents across diverse software tasks.

---


### 138. [MintAct: A Unified Visual Agent for Digital Environments](https://arxiv.org/abs/2609.22083)

**<font color=#1a73e8>作者：</font>** Mingfei Gao, Rui Tian, Haiming Gang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MintAct, a family of vision-language models that unifies UI grounding, multi-step navigation across mobile, desktop, and web, and visual tool use, trained at 2B, 4B, and 8B scales. Through careful design of our environments, data, and training recipes, MintAct models match the performance of per-domain specialists across all of these capabilities. To enable this, we develop a scalable environment and reinforcement learning (RL) infrastructure. On the environment side, we host hundreds of concurrent instances across heterogeneous per-domain backends, serving both trajectory data collection and online RL. To enable efficient and scalable RL training, an asynchronous framework keeps explicit control over the cross-domain training distribution and remains stable under noisy environment feedback and off-policy drift. Experimental results show that MintAct achieves state-of-the-art performance (48.9 on OSWorld-Verified) across a wide range of benchmarks at comparable model sizes.

---


### 139. [Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://arxiv.org/abs/2609.22086)

**<font color=#1a73e8>作者：</font>** Hongyang Du, Lan Yan, Christian Flores 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Professional graphic design is a long-horizon agentic task in which structured, editable artifacts emerge from many interdependent actions, yet outcomes admit no reliable programmatic oracle. We introduce a continual adaptation framework in which a frozen frontier model operates professional design software through more than 230 tools, while an external procedural memory of natural-language skills accumulates and refines reusable design procedures from experience. The memory widens by acquiring procedures for recurring uncovered subtasks and deepens by revising existing procedures against their own successful and failed executions, while a matched replay gate admits only changes that repair failures without regressing observed successes. Five rounds over 1,406 real user briefs and 1,869 automatically graded trajectories, with no weight updates and no human labels, grow the bank from 76 documentation-derived skills to 139 and raise GenEval2 execution success on Claude-Sonnet-4 from 72.7% to 99.3% (+11.99 points in generation quality), with 61.8% and 67.6% win rates against the no-skill agent across four specialized design benchmarks on Claude-Sonnet-4 and Claude-Opus-4.6. We further show the two mechanisms are effective in combination: on 200 held-out briefs from user-traffic benchmark, widening or deepening alone reaches a 49.4% / 48.6% win rate over the no-skill agent, while their combination reaches 58.5% (p = 0.025). Procedural memory offers a practical route to continual adaptation of agents under noisy, unverifiable feedback.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 140. [Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding](https://arxiv.org/abs/2609.20888)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Themistoklis Haris, Henry Li, Maryam Karimzadehgan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Massive KV caches can cause severe memory-bandwidth bottlenecks during long-context decoding. Sparse attention methods mitigate this via selective loading, but that comes at a cost: rigid heuristics drop necessary context, leading to quality degradation. We introduce \textbf{Elastic Threshold Attention (ETA)}, an end-to-end trainable architecture that achieves hardware-accelerated decoding speed without sacrificing dense model quality. ETA predicts dynamic, contextual thresholds directly from query representations, allowing the model to allocate dense-like context to difficult retrieval or reasoning steps while pruning routine tokens. To learn this policy from scratch without representation collapse, ETA \emph{multiplicatively suppresses} sub-threshold logits toward zero during training rather than deleting them. Training against this smooth uniform attention floor provides a distributed probability reservoir that \textbf{causes localized attention sinks on initial tokens to disappear}. It also enables the model to hard-prune uninformative KV blocks at inference time and absorb incidental tokens co-admitted by coarse GPU block selection. As a result, a 1.45B pretrained ETA model rivals dense attention across language modeling, commonsense reasoning, and long-context needle retrieval at $\approx 85\%$ training sparsity and $\approx 38\%$ active decode density. At inference time, we implement a custom decode kernel in Triton that screens KV blocks in $O(1)$ time using cached geometric-probabilistic bounds, delivering up to $2.5\times$ wall-clock decode speedups over FlashAttention-2 on sequences up to 512K tokens. Finally, we introduce an offline calibration algorithm for domain-specific deployments that freezes per-head constant thresholds to eliminate predictor overhead, cutting attention compute by an additional $27\%$.

---


### 141. [Origin Is All You Need: Provenance-Aware Transformers for Structural Trust-Boundary Separation](https://arxiv.org/abs/2609.21088)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxuan Zhang, Jeff Huang, Guofei Gu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection (IPI) remains a central safety and security challenge for large language model (LLM) systems because standard transformers lack architectural notion of source authority. Retrieved documents, user inputs, and system instructions are all processed through the same undifferentiated attention mechanism, forcing the model to infer from wording alone what should be obeyed and what should be treated as data. We propose Provenance-Aware Transformers, a provenance-aware defense that makes application-supplied source labels actionable inside the model. Each input token is assigned a ring ID encoding its origin, and the model is augmented with origin embeddings, a learnable origin attention bias, and a learnable origin scale that preserves provenance under normalization. The resulting architecture enforces a structural boundary between authoritative and non-authoritative sources during generation. To instantiate this architecture on released pretrained models, we propose a two-stage fine-tuning pipeline to teach the model origin semantics and task behavior under ring constraints. Evaluation shows that Provenance-Aware Transformers maintain robust resistance to IPI both in-distribution and out-of-distribution while preserving utility comparable to the base pretrained model. More broadly, our work shows that exposing provenance as a first-class architectural signal can shift LLM safety alignment from brittle pattern matching toward explicit trust separation.

---


### 142. [A Fully Differentiable Neuro-Soft-Symbolic Framework for Perceptual Task Planning](https://arxiv.org/abs/2609.21221)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hongyan Wei, Wael AbdAlmageed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Perceptual planning tasks require two key capabilities: accurately perceiving uncertain scenes and planning valid action sequences following logical rules. Conventional methods convert perception into discrete symbolic facts and then plan, discarding perceptual uncertainty and severing task-level feedback to perception. We introduce a generic, fully differentiable neuro-soft-symbolic framework that connects visual perception and task planning within a single computational graph. The framework maintains a continuous soft symbolic state, lifts domain rules into a differentiable soft-$T_P$ transition operator, and optimizes action logits over a short planning horizon. Gradients from the planning objective can also update the perception parameters, allowing task-relevant perceptual representations to be refined during planning. On Blocksworld, our method solves 40/40 LatPlan-40 tasks and 596/600 PlanBench-600 tasks, compared with 33/40 for LatPlan and 587/600 for the reasoning-model baseline, while requiring substantially less computation and time. In the perceptual-uncertainty ablation, our method improves the success rate from 59\% with frozen perception to 83\%. We further conduct task-and-motion simulations on Blocksworld scenes, providing an execution-level validation of the compatibility between decoded task plans and downstream robotic motion execution.

---


### 143. [When Does Reasoning Help in Machine Translation? A Hierarchical Analysis of LRM Reasoning Traces](https://arxiv.org/abs/2609.21247)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxiang Liu, Jiaming Luo, Eleftheria Briakou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models increasingly use intermediate traces for machine translation, but it remains unclear when such reasoning helps or hurts. We analyze reasoning traces across models, languages, domains, and datasets, focusing on reasoning language, length, and structure. We find that the best reasoning language is model-specific, reasoning length has a non-monotonic relationship with quality, and traces exhibit recurring functional patterns. To uncover these patterns, we introduce Hierarchical Meta-Summarization (HMS), a scalable framework that induces coarse- and fine-grained reasoning structures without predefined taxonomies. HMS reveals a shared organization--understanding/planning, translating/drafting, and refining/verifying--alongside domain-specific variation. Our results suggest that MT reasoning should be controlled in a model-aware, length-aware, and pattern-aware manner rather than uniformly encouraged.

---


### 144. [Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering](https://arxiv.org/abs/2609.21502)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianchen Deng, Guole Shen, Yilin Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D foundation models enable generalizable geometric reasoning from RGB images but remain limited in persistent memory, scalability, and renderable scene modeling. We present a memory-centric 3D foundation model for scalable robotic localization, reconstruction, and Gaussian rendering. Its core is an adaptive world memory mechanism that combines transformer-based gated updates with test-time temporal-spatial regulation. Learned gates control recurrent memory propagation, while temporal state evolution and spatial observation-state consistency regulate token-wise updates and forgetting over long image sequences. To support large-scale mapping, we organize memory into local submaps and integrate progressive mapping and tracking, loop closure, and SL(4)-based global refinement to maintain local accuracy and global consistency. A Gaussian reconstruction head decodes memory-enhanced features into renderable primitives, unifying camera pose estimation, dense point-cloud reconstruction, and photorealistic rendering within a single model. Experiments on public benchmarks and self-collected datasets from diverse robotic platforms demonstrate improved trajectory accuracy, reconstruction completeness, and rendering quality over existing 3D foundation reconstruction and SLAM baselines. These results support adaptive memory as a foundation for persistent robotic world modeling. The dataset and code will be made publicly available at \href{this https URL}{this https URL}.

---


### 145. [On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://arxiv.org/abs/2609.21561)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anton Baumann, Akmal Ashirmatov, Leo Schmidt-Traub 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation provides dense, token-level supervision by conditioning a model on privileged information and distilling the resulting teacher distribution back into the model. However, privileged information can change not only what the teacher knows, but also how it behaves, entangling correctness-relevant learning signals with unintended behavioral shifts. We study this effect in reasoning tasks by contrasting attractive self-distillation, which moves the model toward a privileged teacher, with repulsive self-distillation, which moves it away from a privileged teacher. We find that both objectives can induce strong and opposing behavioral shifts: attraction suppresses exploratory reasoning and promotes shorter, more confident responses, whereas repulsion increases response length, can trigger unintended switches into a model's latent thinking mode, and ultimately becomes unstable. Motivated by these observations, we study contrastive self-distillation, which combines attraction toward a correct-solution-conditioned teacher with repulsion from an incorrect-solution-conditioned teacher. In contrast to prior work that combines such distillation signals with a GRPO objective, we isolate the self-distillation objective and study its behavior on its own. We find that the shared behavioral shifts of the two teachers largely cancel, leaving a token-level signal that more directly reflects correctness. Across non-thinking, instruct-only, and already-thinking models, this contrastive objective improves reasoning performance while maintaining stable response lengths.

---


### 146. [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](https://arxiv.org/abs/2609.21573)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pedro Pereira, Eva Maia, Isabel Praça  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves large language models by grounding outputs in external knowledge sources, but this dependency also creates a surface for poisoning attacks. This paper introduces Micro-Collaborative Poisoning, a distributed attack in which a false target claim is divided across multiple locally plausible documents instead of being concentrated in a single malicious passage. We evaluate the attack across 108 RAG configurations by varying dataset, retriever architecture, retrieval depth, database composition, number of poisoned databases, and generator model. The results indicate that Micro-Collaborative Poisoning is not driven by a single dominant poisoned passage, but by the accumulation of weak adversarial signals across retrieved sources. Increasing top-$k$ and poisoning multiple databases make it more likely that these signals will appear together in the retrieved context, while clean database diversity and stronger retrievers can reduce their influence. The document-level poisoning visibility analysis further shows that this threat is difficult to expose through isolated document inspection, since Micro-Collaborative Poisoning achieves downstream influence while leaving a weaker explicit poisoning signature than direct poisoning.

---


### 147. [Trading Depth for Time in Recurrent Transformers](https://arxiv.org/abs/2609.21605)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeyi Huang, Xuehai He, Yong Jae Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent Transformers increase computational depth through temporal recurrence, feeding each token's high-level hidden state into the computation of the next. This raises a natural question: is additional computation better spent on more temporal steps or greater physical depth? We investigate this question using Latent Recurrent Transformers (LRTs), which retain one backbone forward pass per vocabulary token during decoding and provide a controlled setting for comparing these two ways of adding computation. Specifically, we insert a latent thought token between consecutive vocabulary tokens. Each thought token passes through the same $L$ layers as a vocabulary token, sharing the backbone parameters and providing an additional stage of hidden-state refinement before predicting the next token. We compare this $L$-layer LRT against a $2L$-layer LRT without thought tokens. Both execute $2L$ Transformer blocks per vocabulary token during decoding, but the thought-token model uses fewer parameters. On 16- and 20-layer mixture-of-experts NanoChat backbones, one thought token brings the shallower model within 0.006 and 0.004 bits per byte of its double-depth counterpart, recovering 67% and 81% of the improvement with approximately 48% fewer total parameters. These results suggest that temporal thinking offers a parameter-efficient alternative to increasing physical depth in recurrent Transformers.

---


### 148. [CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](https://arxiv.org/abs/2609.21793)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiale Luo, Eric Han  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defenses against jailbreak attacks on Large Language Models (LLMs) operate at different pipeline stages, such as input modification or output guard, but it remains unclear which defenses to deploy at each stage and how to combine them. Prior empirical studies, fragmented by inconsistent attack-success-rate definitions and experimental settings, have evaluated defenses largely in isolation. Here we present the first systematic study, to our knowledge, of defense combinations both within and across pipeline stages, under a consistent threat model of direct, black-box, single-turn attacks. Our decision framework standardizes evaluation through a principled attack-success-rate formulation with controlled query budgets, together with explicit fairness rules. Across 19 attacks and 15 defenses, we find that no single defense is universally best, but well-chosen combinations achieve substantial safety with minimal utility degradation, yielding practical recommendations for layered defense pipelines.

---


> [!TIP]
> 当前位于：**101-148**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-148**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
