# 📦 其他研究 | 2026年07月25日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

---

### 1. [Skill-Contracted Agents for Evidence-Aware Materials Literature Analysis](https://arxiv.org/abs/2607.20431)

**<font color=#1a73e8>作者：</font>** Bixuan Li, Yu Liu, Shuo Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Materials science literature analysis requires simultaneous attention to composition, processing, characterization, and property relationships, yet conventional retrieval-augmented generation pipelines struggle to reconcile heterogeneous tasks within a single retrieve-then-generate architecture. Here we present AlphaAgent, a skill-driven agent framework that decouples retrieval-based question answering from paper-level report generation through explicit skill contracts. A dedicated retrieval skill rewrites user requests into material-specific search intents, queries a curated index of more than 300,000 papers from the Journal Citation Reports Metallurgy and Metallurgical Engineering category, and reformulates queries when initial evidence is insufficient. A separate report-generation skill parses full-text PDFs to produce structured per-paper analytical reports and cross-paper summaries. In a blind evaluation on 40 materials-science questions, half of which required deep analytical reasoning, AlphaAgent substantially outperformed a baseline system matched for underlying model, document index, and retrieval scale, with the largest gains in mechanistic explanation and awareness of credibility boundaries. These results indicate that explicit task separation, refined retrieval intent, and evidence-aware generation improve large-language-model-based literature analysis for materials research.

---


### 2. [Position: Natural Language Should Not Fully Replace Formal Languages](https://arxiv.org/abs/2607.20432)

**<font color=#1a73e8>作者：</font>** Eitan Wagner, Elisha Rosensweig, Omri Abend  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and their widespread adoption have prompted claims that natural language could entirely replace formal languages, such as programming languages for software design. In this position paper, we argue that this perspective overlooks fundamental linguistic properties of natural language, specifically that it is optimized for underspecification in open-ended contexts. We introduce a formal framework centered on *task specificity*, defining it as the information-theoretic reduction of uncertainty in an output space -- such as all possible images -- given a user's specific requirements. We prove a *specificity crossover theorem*, showing the existence of a threshold beyond which the cost to express formal requirements into natural language exceeds the cost of direct formal specification. By analyzing case studies across modalities, such as image generation, code synthesis, and audio production, we demonstrate that natural language excels at low specificity tasks, while formal languages are advantageous on tasks with stricter requirements. We conclude that natural and formal languages are complementary tools and advocate the development of hybrid systems that allow users to move across the specificity spectrum.

---


### 3. [Break Through the Compression Bottleneck: From Theory to Practice](https://arxiv.org/abs/2607.20434)

**<font color=#1a73e8>作者：</font>** Xiusheng Huang, Lu Wang, Yequan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As the parameter size of language models continues to grow, effective model compression is required to reduce their computational and memory overhead. Existing compression methods suffer from bottleneck issues: when the compression ratio is increased, performance degrades significantly. Low-rank decomposition and quantization are two prominent compression methods that have been proven to significantly reduce the computational and memory requirements of Large Language Models (LLMs) while maintaining model accuracy. Evidently, combining these two methods will break through the existing compression bottleneck. However, how these two methods interact when combined remains a critical question for developers, as many assume they are orthogonal, meaning their combination would not introduce additional errors beyond those independently introduced by each method. This paper provides the first mathematical proof that low-rank decomposition and quantization are non-orthogonal. We validate these findings through a series of experiments on large language models. Our results demonstrate that these methods are non-orthogonal, and their combination leads to significant performance degradation. Importantly, we propose a novel approach Diagonal Adhesive Method (DAM), which can effectively combine the two methods and mitigate the performance loss. Our research provides deep insights into model compression and lays a solid theoretical and experimental foundation for future related studies.

---


### 4. [AsymVerify at SemEval-2026 Task 6: Asymmetric Confidence-Gated Verification for Political Evasion Detection](https://arxiv.org/abs/2607.20439)

**<font color=#1a73e8>作者：</font>** Sebastien Kawada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political evasion is difficult to detect because evasive answers often appear cooperative while avoiding concrete commitment. We present AsymVerify, a confidence-gated verification system for SemEval-2026 Task 6, a three-way classification of Clear Reply, Ambivalent, and Clear Non-Reply responses. AsymVerify scored 0.85 Macro F1 on the evaluation split (D_eval, n=237), placing 2nd out of 41 teams on the official leaderboard. The system first classifies each question-answer pair, then selectively applies downgrade verification (CR/CNR -> AMB) or upgrade verification (AMB -> CR) to low-confidence predictions. Development analysis shows that errors concentrate at the Ambivalent boundary in both directions, motivating this asymmetric two-verifier design while confidence gating keeps additional inference cost low. On D_dev (n=308), AsymVerify with GLM-4.7 gains +17.1 Macro F1 over single-pass classification at 1.48 calls/example, and the upgrade verifier alone improves every tested LLM backend on D_dev by +6.8 to +15.2 Macro F1 over its single-pass baseline. Code is available at this https URL.

---


### 5. [Answer-then-Edit: Reasoning Skeleton Editing for Anti-Distillation with Preserved Utility](https://arxiv.org/abs/2607.20440)

**<font color=#1a73e8>作者：</font>** Fan Li, Mengting Pan, Sijia Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proprietary large language models (LLMs) entail substantial intellectual and financial investment, making them valuable intellectual property (IP). However, even when deployed via black-box APIs, these models remain vulnerable to unauthorized knowledge distillation, which allows adversaries to cheaply extract and replicate model capabilities. To address this issue, anti-distillation (AD) has been proposed to generate defensive outputs that hinder distillation effectiveness, overcoming the limitation of watermarking-based approaches that rely on post-hoc verification. However, existing AD methods based on internal model perturbations struggle to balance anti-distillability and utility (e.g., answer accuracy and naturalness) of reasoning traces, with stronger defenses often causing significant utility loss. To fill this gap, we propose \textbf{\underline{S}}keleton-\textbf{\underline{G}}uided \textbf{\underline{R}}easoning \textbf{\underline{E}}diting (SGRE), an \textit{Answer-then-Edit} framework that performs post-hoc trace modification for anti-distillation. In the answer stage, the teacher model first generates clean reasoning traces, preserving the original reasoning accuracy while enabling more flexible control over trace naturalness. In the editing stage, we draw inspiration from Cognitive Load Theory (CLT) and introduce a three-stage strategy consisting of reasoning skeleton extraction, skeleton graph coarsening, and skeleton verbalization. These operations jointly perturb reasoning structures and augment textual complexity to amplify extraneous load on student models, hindering their acquisition of underlying reasoning patterns. Extensive experiments across diverse LLMs demonstrate that SGRE achieves state-of-the-art performance in reducing distillation effectiveness, while maintaining lossless reasoning accuracy and superior trace naturalness.

---


### 6. [GLAN-QnA-KR: A Seedless Taxonomy-Driven Korean Instruction Corpus](https://arxiv.org/abs/2607.20443)

**<font color=#1a73e8>作者：</font>** Daekeun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We release GLAN-QnA-KR, a 303,581-row openly redistributable Korean instruction-QA corpus produced via the seedless taxonomy-driven GLAN synthesis pipeline with Microsoft's Phi-3.5-MoE-instruct as the producer model (generation: 2024-12; release: 2024-12; licence: OpenRAIL). The corpus spans a flat taxonomy of 1,084 English-labelled disciplines paired with Korean question/answer text, a 100-900 difficulty scale, and a median of 313 question characters and 1,098 answer characters per record. Two properties are atypical for synthetic instruction data at this scale: (i) exact duplicate questions number only 1 in 303,581 rows and character-trigram near-duplicate clusters at Jaccard >= 0.9 number zero in a 5,000-sample probe, and (ii) a two-layer contamination audit against KMMLU, KoBEST (five sub-tasks), and HAE-RAE-Bench shows a maximum test-vs-corpus question-level character-trigram Jaccard of 0.163 with zero test items at Jaccard >= 0.7, and a maximum multilingual-E5 cosine of 0.901 with a single test item at cosine >= 0.90 and zero at >= 0.95, across 20,000 sampled GLAN questions and seven evaluation sets. At the time of release, this is, to our knowledge, the largest single-pipeline synthetic Korean instruction corpus verifiable on the Hugging Face Hub and the only Korean >=100k-row corpus built under a seedless taxonomy-driven protocol. This note documents the generation protocol, corpus statistics, the contamination audit, and the licensing boundary in a form suitable for downstream citation.

---


### 7. [SCoPE: Shift-Aware Speaker-Conditioned Priors for Emotion Recognition in Conversations](https://arxiv.org/abs/2607.20445)

**<font color=#1a73e8>作者：</font>** Burak Can Kaplan, Stefan Wermter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In conversations, human emotions are transient; however, they tend to persist across multiple utterances. For example, we rarely switch instantly between contrasting emotions such as happiness and anger. Instead, emotions tend to evolve smoothly, and these patterns are often speaker-specific. Some people might escalate, while others gradually cool down over time. Furthermore, when emotions change during a conversation, they are often driven by contextual factors, such as newly received information or unexpected events. Even though progress has been made in Emotion Recognition in Conversations (ERC), most existing approaches still rely heavily on overt evidence and do not sufficiently model these non-apparent factors. Especially in multimodal settings, this makes these models fragile when the signals are noisy (e.g., occluded faces, slang expressions, or microphone noise). To address these limitations, we introduce Speaker-Conditioned Priors over Emotions (SCoPE). SCoPE is a light weight module that utilizes the emotional history of each speaker and explicitly models their priors for use in subsequent emotion classification. Second, we incorporate emotion shift prediction, a well-established concept in ERC, to guide the model in balancing the priors from SCoPE and multimodal evidence. Finally, we propose a shift-aware fusion mechanism that performs precision-weighted logit integration between multimodal evidence and the speaker prior, forming a Bayesian-inspired product-of-experts formulation. This dynamic fusion allows the model to rely on historical priors when emotions persist and to prioritize multimodal evidence when shifts are likely. Experimental results show our model achieves superior performance over recent state-of-the-art models on the IEMOCAP dataset in multimodal settings.

---


### 8. [thaulab@EEUCA 2026: Who Said What to Whom? A Targeting-Aware Neural-Symbolic Pipeline for Gaming Toxicity Detection](https://arxiv.org/abs/2607.20447)

**<font color=#1a73e8>作者：</font>** Anmol Guragain, Marcos Estecha-Garitagoitia, Luis Fernando D'Haro Enríquez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our system for the EEUCA 2026 Shared Task on toxicity classification in gaming chat. We implement a three-stage pipeline combining an ensemble of two compact transformers (DeBERTa-v3-base, 184M; XLM-RoBERTa-base, 278M) with a Linguistically-Informed Mediator (LIM) that resolves inter-model disagreements through corpus-backed lexical normalization, class-conditional unigram scoring, multilingual profanity detection, and agentive targeting analysis grounded in speech act theory. The LIM specifically targets the minority classes (Hate \& Harassment, Threats, and Extremism), which are the most safety-critical categories in real-world gaming moderation. To address the extreme class imbalance (1{,}450:1 Non-toxic to Extremism ratio), we introduce a two-stage data augmentation strategy using only the provided training data. Our system achieves a Macro F1 of 0.6441 and accuracy of 0.9062 on the official test set, ranking 3rd in Macro F1 and 1st in accuracy among all teams. The proposed pipeline is domain-portable: adapting to other gaming platforms requires substituting only the game-specific entity lexicon. Code is publicly available at this https URL\_EEUCA.

---


### 9. [ShriNep@EEUCA 2026: RAKSHAK - Multi-Task DeBERTa with Rationale Distillation and Jigsaw-Augmented Training for Toxic Intent Classification](https://arxiv.org/abs/2607.20450)

**<font color=#1a73e8>作者：</font>** Binayak Karki, Aryan Kafle, Pingala Ghimire  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents two systems for the GameTox Shared Task at the Workshop on EEUCA at ACL 2026, which requires classifying World of Tanks chat utterances into six fine-grained toxic intent categories (Labels 0-5). Severe class imbalance, domain-specific multilingual slang, and extremely scarce data for rare categories such as Threats (Label 4, 60 samples) and Extremism (Label 5, 24 samples) make this a challenging classification problem. Our primary submission, RAKSHAK (rak s. aka, Sanskrit for "Protector"), is a multi-task DeBERTa-v3-base (He et al., 2022) framework combining rationale distillation from Qwen2.5-14B (An et al., 2024), Supervised Contrastive Loss, and dedicated rare-class binary heads. RAKSHAK's training data is augmented with cross-domain transfer from the Jigsaw Toxic Comment dataset (16,225 samples mapped to Labels 1-4) and 100 LLM-generated extremism samples for Label 5. Our secondary system (M1) fine-tunes DeBERTa-v3-base with Focal Loss on the original GameTox data plus the same 100 extremism samples, without Jigsaw transfer. RAKSHAK achieves a Macro F1 of 0.5883 on the official test set, ranking 7th out of 35 participating teams, while M1 achieves 0.5252 Macro F1. An ablation comparing M1 with and without Jigsaw data shows that cross-domain transfer accounts for +2.6 F1 points, while RAKSHAK's multi-task architecture contributes a further +3.7 points.

---


### 10. [Semantic Field Theory: Historical Origin, Higher-Order Interaction, and Stabilized Semantic Inference](https://arxiv.org/abs/2607.20451)

**<font color=#1a73e8>作者：</font>** Dimitris Vartziotis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic Field Theory (SFT) has developed from a philosophical critique of strong anti-formalist readings of language games into a proposed computational model class for lexical semantics, higher order composition, and stabilized interpretation. This paper reconstructs that evolution and gives SFT a sharper mathematical core suitable for independent evaluation in computational linguistics and representation learning. The central proposal is that a tractable level of linguistic organization can be modeled through lexical representations expressed as semantic fields, through contextual deformation of those fields, through interaction terms defined over subsets of tokens, and through stabilization governed by semantic energy dynamics. The paper contributes five formal elements. First, it defines a semantic field model as a tuple consisting of a semantic space, a lexical field lifting, a contextual deformation map, an interaction complex, and an interpretation functional. Second, it proves a Gaussian product closure result showing that multiplicative field interactions have explicit centers, precisions, and compatibility factors. Third, it generalizes the three-word problem by using Mobius inversion on the subset lattice to isolate irreducible semantic interactions of arbitrary order. Fourth, it introduces an order spectrum that measures how much field mass is explained at each interaction order. Fifth, it formulates stabilized interpretation as minimization of an energy functional associated with the sentence and gives existence, descent, and stability conditions. A small worked example shows how a three-word summer day triple can be represented by Gaussian semantic fields, implemented in Python, and summarized by a flow diagram. The result is not a completed theory of natural language meaning and does not replace social, pragmatic, or normative accounts of language.

---


### 11. [THOR: A Theta-Gamma Hierarchical Oscillatory Reasoning Framework for Multi-hop QA](https://arxiv.org/abs/2607.20459)

**<font color=#1a73e8>作者：</font>** Ziyang Ling, Ronald X. Xu, Mingzhai Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering requires retrieving and integrating evidence from multiple contexts. Despite the rapid progress of current research, multi-hop reasoning remains constrained by two persistent limitations: attention decay, where the model's focus on main question degrades as the reasoning chain grows, and error accumulation, where mistakes propagate across hops and compounds into final failure. Inspired by Theta-Gamma hierarchical oscillation which decouples global planning from local retrieval, enabling efficient attention transfer between hops and a verification and repair mechanism that interrupts the accumulation of errors in the wrong paths, we present THOR, a brain-inspired Theta-Gamma hierarchical oscillatory reasoning framework. Extensive comparative experiments and specific validation experiments on multi-hop QA benchmarks demonstrate that THOR improves answer accuracy and robustness while mitigating limitations, showcasing its generalization across different backbones.

---


### 12. [Instruct-FD: Can Your Full-Duplex Speech System Follow Turn-Taking Instructions?](https://arxiv.org/abs/2607.20460)

**<font color=#1a73e8>作者：</font>** Yuzhi Tang, Wentao Ma, Xiling Zhao 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current full-duplex (FD) spoken dialogue systems can produce fluid interactions, yet it remains unclear whether they can adapt their turn-taking behavior when explicitly instructed. This is critical for real-world deployment, where conversational policies vary across applications (e.g., proactive tutoring vs. passive counseling). We introduce Instruct-FD, an instruction-conditioned benchmark for evaluating controllable turn management in FD systems. To enable this, we develop a human-validated, scalable synthetic pipeline that generates instruction-conditioned conversations, along with a deployment-agnostic multi-turn evaluation protocol and an LLM-based judge. Benchmarking six state-of-the-art full-duplex systems reveals a substantial gap in instruction-following turn management: the best model achieves only 64.4% adherence. Performance is highly uneven across behaviors and scenarios, with proactive behaviors such as model backchanneling and interruption remaining particularly challenging. These findings establish instruction-following turn management as a crucial direction for building adaptable and deployable full-duplex dialogue systems.

---


### 13. [Can Valence Reflect Morality in Natural Language? A Preliminary Annotation Study](https://arxiv.org/abs/2607.20461)

**<font color=#1a73e8>作者：</font>** Jonny O'Dwyer, Malika Bendechache, Louise McCormack 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Present implementations of artificial intelligence (AI) ethics do not adequately take feelings, or affect, into account. If AI should be aligned with human ethics, it seems reasonable to thoroughly investigate the possibility of AI behaviour that mirrors virtuous human ethical conduct, where feelings play a role in the actions, judgements or statements one makes. Furthermore, while prominent theories of normative ethics are often discussed in terms of their differences and shortcomings, Virtue, Consequentialist, and Kantian Deontological ethics all share a common feature of considering human feeling to some degree while the popular descriptive ethics theory, Moral Foundations Theory, positions feelings as central to many of its foundations. Therefore, in the present paper, a data set of moral valence is proposed, consisting of 500 annotations by six human participants for both action/judgement and consequence moral valence, ranging from -1 to 1 for text-presented scenarios from the Commonsense Norm Bank data set. The resulting valence features share significant relationships with multi-class (immoral/discretionary/moral) and binary immoral/moral categories while additionally providing a noteworthy test set Matthew's correlation coefficient of 0.764 using regularised logistic regression for binary classification. This provides early evidence of the usefulness of valence features for morality estimation of text, indicating that valenced consequences of responses for others can be considered toward more human morally-aligned AI. In the interest of promoting further affective-moral computing research, this study's annotations will be made available for research on request.

---


### 14. [Enabling Scalable Topology Inference in Distribution Systems via Constrained Multi-Source Inference](https://arxiv.org/abs/2607.20480)

**<font color=#1a73e8>作者：</font>** Haoran Li, Lihao Mai, Muhao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate distribution system topology is essential for outage localization, voltage analytics, and operation of distribution grids, yet maintaining reliable connectivity records remains challenging in practice due to heterogeneous and imperfect utility data. Existing topology identification methods often rely primarily on electrical similarity or spatial records alone, which become unreliable in dense feeders and under inconsistent metadata conditions. This paper formulates distribution topology identification as a constrained inference problem that refines a utility-provided base topology using heterogeneous evidence while enforcing spatial feasibility and physical operational constraints. Instead of reconstructing connectivity from scratch, the proposed framework detects inconsistent assignments, performs localized reconnection within constrained neighborhoods to ensure scalability, and iteratively enforces physical feasibility to produce operationally consistent topology estimates. In addition, a falsification-driven reliability metric evaluates how strongly each inferred connection is supported relative to alternative feasible assignments, enabling utilities to prioritize verification efforts while preserving system-wide observability. The framework is validated using operational data from three feeders comprising more than $8{,}000$ AMI meters in collaboration with a large U.S. utility. Results demonstrate over $95\%$ topology reconstruction accuracy while significantly reducing computational effort compared with global inference approaches. The study further shows that correlation-based methods alone produce ambiguous assignments in dense urban feeders, whereas combining electrical measurements with spatial and operational constraints enables robust and scalable topology recovery under realistic deployment conditions.

---


### 15. [PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails](https://arxiv.org/abs/2607.20482)

**<font color=#1a73e8>作者：</font>** Seungbin Yang, Chaewoon Ki, Dohyun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have enabled web agents to autonomously execute complex tasks. In practice, users frequently provide underspecified instructions, requiring agents to infer the missing context from their raw browsing histories. Existing benchmarks fail to capture this form of personalization, as they either restrict tasks to fully explicit prompts or abstract web interaction history into simplified forms. To bridge this gap, we introduce PersonaTrail, a benchmark for personalized web agents operating in a managed open web environment. By leveraging realistic browsing trajectories as user history, PersonaTrail evaluates an agent's ability to infer user preferences and recall information from past browsing sessions. We further propose Preference-Aware Contextual Memory (PACMem), a framework that decomposes raw browsing histories into two types of structured memory: factual memories that summarize individual sessions and preference memories that distill recurring behavioral patterns. At inference time, the agent retrieves the most relevant entries from these memories to guide personalized navigation. Extensive experiments show that PACMem consistently outperforms existing memory-based baselines on both tasks.

---


### 16. [OPTScientist: Multi-Agent Discovery of Typed Optimizer Programs for Transformer Pretraining](https://arxiv.org/abs/2607.20486)

**<font color=#1a73e8>作者：</font>** Zhongzheng Li, Tiancan Feng, Wenhao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing optimizers for modern deep learning remains a challenging scientific problem, requiring the joint consideration of optimization geometry, state dynamics, numerical stability, implementation constraints, and empirical generalization. Existing automated optimizer discovery methods typically search either over unconstrained code spaces or within narrowly parameterized optimizer families. The former is flexible but often produces invalid or uninterpretable programs, while the latter is stable but limits novelty. We introduce OPTScientist, a theory-guided multi-agent framework for optimizer discovery in a typed domain-specific language (DSL). OPTScientist formulates optimizer design as a constrained scientific search process, where candidate updates are expressed through direction, scaling, preconditioning, regularization, state, and grouping modules. Four role agents, Theorist, Designer, Engineer, and Reviewer, collaborate within a single orchestration loop to propose hypotheses, synthesize DSL candidates, compile and evaluate optimizers, and critique results. To overcome the limitations of a fixed search space, OPTScientist combines evolutionary search over optimizer programs with a second-stage mechanism that proposes small DSL extensions when repeated failures reveal representational bottlenecks. Using this framework, we discover RS-MR, a reduced-state matrix optimizer that improves transformer pretraining over strong baselines under our native evaluation protocol. Our results suggest a path toward automated optimizer science grounded in theory, typed programs, compiler validation, and closed-loop experimentation.

---


### 17. [CRAWO: Custom Resources for Adaptive Workload Orchestration](https://arxiv.org/abs/2607.20490)

**<font color=#1a73e8>作者：</font>** Eugênio Santos, Daniel Maia, Stefano Loss 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Edge Intelligence has emerged as a key paradigm for enabling real-time applications in smart cities by shifting computation from centralized cloud data centers to the network edge, thereby reducing latency and bandwidth consumption. However, deploying Artificial Intelligence (AI) pipelines across heterogeneous edge infrastructures remains challenging due to the wide range of device capabilities, from low-power microcontrollers to accelerator-equipped systems. Existing edge orchestration platforms primarily focus on deployment automation and infrastructure management, but these approaches are often inefficient and limit the ability to adaptively allocate resources under dynamic conditions. To tackle these issues, this paper introduces CRAWO (Custom Resources for Adaptive Workload Orchestration), an architectural framework for coordinating AI pipelines across distributed edge environments. CRAWO follows a control-loop-based model that separates allocation intelligence from execution by managing placement decisions, state management, and inter-stage data flows while instantiating services on edge nodes. The framework incorporates a hardware-aware allocator with a pluggable multi-criteria decision layer that leverages real-time infrastructure metrics to enable adaptive workload placement. The reference implementation adopts a microservices architecture deployed on a lightweight Kubernetes distribution (K3s), using Custom Resource Definitions (CRDs) for domain modeling and a dedicated operator for state reconciliation. Evaluation in a vehicle surveillance scenario using license plate recognition demonstrates improved workload distribution and reduced reliance on centralized cloud processing in latency-sensitive environments.

---


### 18. [DFAH-Bench: Benchmarking Observable Agent Instability in Financial Decision-Making](https://arxiv.org/abs/2607.20491)

**<font color=#1a73e8>作者：</font>** Raffi Khatchadourian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard evaluation benchmarks measure what a tool-using agent decides, not whether it arrives at that decision through the same process each time. We introduce DFAH-Bench, a replay benchmark that measures observable behavioral instability in financial agent decision-making across three channels -- tool-call trajectories, evidence contacts, and decision concentration -- none of which require access to hidden reasoning text. Across 8,127 replay episodes spanning 10 models and 3 financial tasks, we find that outcome agreement alone is an incomplete stability signal: frontier models can agree on decisions 95% of the time while following the same tool path only 77% of the time -- an 18-percentage-point gap (95% CI: [0.14, 0.22]) that outcome-only evaluation misses entirely. Among frontier-model case groups with high decision agreement, over 55% exhibit meaningful trajectory divergence. We identify three behavioral profiles: pattern matchers that achieve near-perfect agreement by collapsing to a single output regardless of input, stable executors with relatively consistent tool-use processes, and trajectory divergers that reach the same conclusions through materially different tool paths and evidence contacts. The benchmark code, metric scripts, replay logs, benchmark card, dataset README, and release manifest are released in the accompanying repository.

---


### 19. [Attention-based Experience Replay Framework for Continual Learning of Agnostic Time Series Forecasting Models](https://arxiv.org/abs/2607.20493)

**<font color=#1a73e8>作者：</font>** Quentin Besnard, Nicolas Ragot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has led to remarkable progress in artificial intelligence, particularly in robotics, imaging and sound processing. However, a major limitation of neural networks remains their strong dependence on large and stationary datasets. In many real-world applications, these conditions are rarely met due to evolving and dynamic environments where data distributions change over time. Continual learning aims to address this challenge by developing models capable of adapting incrementally while maintaining a balance between stability and plasticity under computational constraints. In this work, we introduce a novel framework for continual time series forecasting, designed to extend existing static forecasting models commonly used in the literature by incorporating an Experience Replay strategy guided by Attention mechanisms. This approach allows the model to adapt dynamically to new contexts while preserving prior knowledge, effectively mitigating catastrophic forgetting. The framework is evaluated on standard forecasting benchmarks as well as on a piezometric dataset exhibiting diverse temporal behaviors. Results show that our approach effectively increases or maintains predictive performance over time while reducing retraining costs and data requirements, thus facilitating the deployment of forecasting models in dynamic and real-world settings.

---


### 20. [Workload-Aware Caching for Multi-Agent Systems](https://arxiv.org/abs/2607.20495)

**<font color=#1a73e8>作者：</font>** Anas Mohamed, Kaizan Haque, Azal Ahmad Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems decompose complex tasks into directed acyclic graphs (DAGs) of specialized agent executions, creating natural opportunities for caching intermediate results across queries. However, existing cache eviction policies treat all cached entries uniformly based on access history, ignoring structural and workload signals uniquely available in agentic execution environments. We present a workload-aware eviction policy that combines three signals, namely recomputation cost, DAG dependency count, and agent invocation frequency, into a unified scoring function that retains the most valuable entries under memory constraints. Evaluated across three multi-agent benchmarks spanning diverse reuse regimes, our policy reduces latency by up to 64.7% relative to the uncached baseline and achieves on average a 31.1% latency reduction over the next best finite-capacity baseline, while approaching the performance of an unbounded cache and maintaining accuracy on par with or exceeding all competing finite-capacity methods. We further show that workload-aware content caching is complementary to other agentic system optimization methods, including plan-level caching and parallel agent execution, with each technique targeting a distinct efficiency bottleneck in multi-agent pipelines.

---


### 21. [From Errors to Rules: Iterative Prompt Optimization for Text Classification](https://arxiv.org/abs/2607.20497)

**<font color=#1a73e8>作者：</font>** Yueying Cui, Renhao Xue, Yi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization for text classification spans diverse approaches, from demonstration selection to exploration-based search to error-driven diagnosis, each with known but incompletely characterized strengths and limitations. We conduct a comprehensive empirical study across diverse classification benchmarks (2 to 150 classes) comparing these paradigms through both quantitative evaluation and qualitative analysis of optimization traces, revealing that each paradigm excels on structurally different task types and that no single method dominates. Guided by these insights, we propose Error-Guided Optimization (ERGO), an error-driven method that iterates over the full training set in non-overlapping batches, diagnoses classification failures, and generates targeted decision rules through a diagnose-prescribe-rewrite feedback loop. ERGO achieves the best accuracy on tasks where errors concentrate in specific confused label pairs (which we term boundary-learnable tasks): TREC: 90.0%, CLINC150: 94.4%, converges in 3-5 iterations, and produces interpretable decision rules. While ERGO does not achieve the highest overall average, it fills a complementary role: demonstration-based ICL wins on coverage-dependent tasks, exploration-based search wins on many-class intent, and ERGO wins where decision boundaries are learnable from error patterns. We provide a complementarity framework linking task characteristics to optimal paradigm selection, offering practical guidance for practitioners.

---


### 22. [MKEvolve: A Modular Multi-Agent Framework for Kernel Code Generation](https://arxiv.org/abs/2607.20501)

**<font color=#1a73e8>作者：</font>** Jason Yoo, Rajarshi Saha, Shaowei Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in LLM-based code generation, writing correct and performant kernels for hardware accelerators remains a key bottleneck in scaling modern ML workloads. We present MKEvolve (Modular Kernel Evolve), a framework that iteratively co-evolves a modular decomposition of complex PyTorch modules and the LLM-generated kernel for each submodule, refining the decomposition by splitting and fusing across iterations while independently improving each subkernel via LLM-driven beam search. The resulting kernels are programmatic compositions of independently verified subkernels, making them configurable (subkernel implementations are swappable), interpretable (errors and speedups are traceable to specific subkernels), and readily adaptable to related model architectures. Experiments with Triton on KernelBench L2 and L3, spanning multi-operator sequences and full model architectures, show that MKEvolve improves both correctness and speedup over end-to-end direct synthesis baselines while reducing LLM token usage by up to 35%.

---


### 23. [Inducing Comparability of Factorised Probability Distributions](https://arxiv.org/abs/2607.20502)

**<font color=#1a73e8>作者：</font>** Jan Speller, Malte Luttermann, Marcel Gehrke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To allow for principled comparison between two probabilistic graphical models defined over non-identical variable sets, they have to be lifted to a common measurable space. To this end, we propose an extension scheme for any two given models and establish the formal foundation: Unmatched components are completed using conditionally uniform (Laplace) extensions such that the resulting joint distributions differ from the original ones only by multiplicative constants and coincide under projection. This preserves the probabilistic semantics while enabling the application of well-defined distributional discrepancy measures. We establish the invariance of the induced joint under projection and use the extensions to provide a minimal structural extension of two factor graphs to the smalles common measurable space as well as to a common graphical structure by a deterministic algorithm. In addition, we discuss structural and measure-theoretic properties and identify promising criteria for comparison methodologies.

---


### 24. [LeanFlow: A Case Study in Workflow-Driven Lean Autoformalization](https://arxiv.org/abs/2607.20503)

**<font color=#1a73e8>作者：</font>** Lazar Milikic, Simon Guilloud, Khanh Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present and evaluate LeanFlow, an LLM agent system specialized for translating mathematical papers into buildable Lean projects. Recent verifier-in-the-loop systems show that large formal artifacts can be produced, but it remains unclear which runtime mechanisms affect completion, auditability, or efficiency in document-to-project formalization. We study this question through case studies on two previously unformalized mathematical papers in number theory and measure theory, using model, proof-workflow, and toolset ablations with Kimi2.6 and GPT5.5; we report task outcome, API calls, input tokens, and output tokens. With Kimi2.6, the full workflow completes both document-level projects within the 2000-call budget, while no-queue variants reach the budget limit; with GPT5.5, all document-level variants complete, and the full workflow has the lowest or tied-lowest input-token cost on both sources. As complementary calibration, LeanFlow reaches 75.7% BEq+ on the PFR slice of RLM25 and solves all five ICML 2026 AI for Math TCS challenge projects in our GPT5.5 runs.

---


### 25. [Telco-GAIA: Bilingual Benchmark for Agents in Telecom Domain](https://arxiv.org/abs/2607.20510)

**<font color=#1a73e8>作者：</font>** Dmitrii Khizbullin, Zaid Alyafeai, Abdelrahman Eldesokey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Telco-GAIA, a bilingual, multi-modal benchmark for evaluating tool-using agents on the data of a real-world telecommunications operator. Telco-GAIA comprises 100 human-verified question-answering tasks, in English and Arabic, that each demand multi-hop reasoning (4.2 hops on average) over three heterogeneous sources: a static website snapshot (HTML, images, and linked PDFs), a synthetic relational SQL database, and external web archives, spanning text, image, and tabular modalities. The benchmark is delivered as a sandboxed Docker environment and scored by normalized exact string matching, making evaluation objective, deterministic, and reproducible over time without any LLM-as-a-Judge. Evaluating a purpose-built reference agent across twelve commercial and open LLMs, we find Telco-GAIA challenging: even the strongest model solves only 71% of tasks; under a moderate cost budget, this falls to about 40%, and the visually grounded categories remain the weakest, where the average backend scores below 30%, leaving substantial headroom in document and image understanding. Telco-GAIA offers a rigorous, reproducible testbed for enterprise agents and a template for constructing closed-domain benchmarks.

---


### 26. [The Active Ingredient in Muon's Grokking](https://arxiv.org/abs/2607.20512)

**<font color=#1a73e8>作者：</font>** Yufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer reaches the grokking threshold on modular arithmetic faster than AdamW. Prior work attributes this to "spectral-norm constraints plus orthogonalized momentum" but does not isolate which mechanism matters. To better understand Moun's behavior, we run multi-seed and multi-learning-rate sweeps to decompose and stress-test the effect. First, an ablation shows the speedup comes from orthogonalization (the Newton-Schulz iteration): orthogonalize-only matches full Muon, whereas spectral-only is no faster than AdamW and is unreliable, and this verdict holds across learning rates. Second, a mechanistic analysis finds that orthogonalizing optimizers reach generalization at roughly 3x lower spectral norm and, controlling for how much the embedding actually moves, settle into a lower-norm solution rather than simply perturbing the embedding less. Third, reducing the Newton-Schulz iteration count from five to one accelerates reaching the threshold but makes the grokked solution fragile, prone to transient collapse, with fragility that grows with learning rate; a single iteration is fast and stable only at small learning rate, while the canonical five iterations are the learning-rate-robust choice. We also show spectral scaling can be dropped at no measured cost. A methodological thread runs throughout: under a stability-aware metric, "faster" claims about grokking optimizers can invert, so we report both first-crossing and sustained-grok times. To support reproducibility, we release our full training and analysis code at this https URL

---


### 27. [CANN Bench: Benchmarking Agent Generated Kernels against Real NPU and Algorithmic Limits](https://arxiv.org/abs/2607.20518)

**<font color=#1a73e8>作者：</font>** Xue-Jian Gao, Deng Pan, Yueming Su 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are now capable of writing, compiling, and iteratively optimizing low-level operator kernels on different hardware platforms. Existing benchmarks, however, focus almost exclusively on CUDA and Triton, leaving hardware ecosystems with less-exposed programming models without a common evaluation baseline. We present CANN Bench, an open benchmark for AI-generated operator code on Huawei's Ascend NPU. The current release covers 53 operators and 1060 test cases organized into four difficulty tiers -- from simple elementwise primitives to MoE dispatch and FlashAttention kernels -- spanning FP16, BF16, FP32, and INT8 precision formats. Evaluation adopts a \textbf{three-dimensional weighted composite score} that treats compilation, functional correctness, and performance as independent axes, providing a principled reward signal for kernel-generation agents. Performance is graded against an out-of-the-box PyTorch-on-Ascend baseline and an analytical per-case Hardware-Anchored Performance (HAP) limit on real NPU hardware, ensuring scores reflect genuine optimization headroom rather than measurement artifacts. The evaluation harness is designed to resist reward hacking from the ground up. CANN Bench is versioned within the official CANN repository and is designed for long-term community co-construction, providing the Ascend ecosystem with a quantitative, reproducible, and sustainably maintained yardstick for AI operator-authoring capability.

---


### 28. [Adaptive Depth in Looped Transformers: Diagnosing Learned Halting Gates and Trajectory Readouts](https://arxiv.org/abs/2607.20519)

**<font color=#1a73e8>作者：</font>** Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase test-time computation by repeatedly applying a shared recurrent block. Learned halting objectives in looped Transformers typically use a single exit distribution both as the inference-time stopping rule and as the training-time weighting of per-depth losses. This entangles exit selection with trajectory formation: the gate not only chooses which recurrent state to use, but also determines how strongly each intermediate state is supervised. Consequently, poor adaptive-compute performance can arise from the readout, the induced trajectory, or their interaction. We study adaptive depth in looped Transformers through this trajectory--readout lens, across controlled synthetic tasks (modular arithmetic and binary parity) and large-scale Ouro-1.4B and 2.6B checkpoints. We find that fixed-prior depth supervision, which shapes the trajectory without an input-dependent halting policy, produces difficulty-aware trajectories whose intermediate states expose useful stopping signals, and that simple post-hoc confidence readouts often match or outperform learned linear and MLP gates. Fitting gates on frozen trajectories localizes the failure: it appears to stem mainly from the trajectory induced by joint gate training rather than from limited gate expressivity. The same pattern is present in Ouro evaluations, where pretrained ponder gates are competitive but not uniformly Pareto-optimal, and measured latency confirms that the resulting reductions in average exit depth translate into practical inference-time savings. Our systematic diagnostic evaluation reframes adaptive depth in looped Transformers as a joint problem of trajectory formation and exit readout, rather than gate learning alone, highlighting a distinction that prior learned-halting work has often left implicit.

---


### 29. [Generative Bayesian Filtering for State Estimation](https://arxiv.org/abs/2607.20521)

**<font color=#1a73e8>作者：</font>** Lei Cao, Sihang Feng, Jixin Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The state of a dynamic system evolves over time, switching among several latent modes that govern its observable behavior. Filtering methods infer the latent state from observations. Classical filtering approaches, including Kalman filters, typically rely on simple observation models, such as linear-Gaussian models, that are incapable of characterizing the increasingly nonlinear and heterogeneous patterns in high-dimensional sensor signals. To tackle the challenge, we propose Generative Bayesian Filtering (GBF), a filtering framework that replaces restrictive observation models with pretrained conditional generative models parametrized by conditional variational autoencoders (CVAE). For online inference, GBF performs a Bayesian prediction-update recursion in which the measurement update is formulated as a posterior sampling problem that combines the dynamical prior with the CVAE-induced likelihood. The resulting filtering problem is then transformed into a score-based sampling problem, which naturally inherits the flexibility from generative models and the uncertainty quantification capabilities from ensembling. Experiments on synthetic datasets and real-world applications involving manufacturing system monitoring and arrhythmia diagnosis demonstrate that GBF improves state estimation accuracy and robustness relative to baseline approaches.

---


### 30. [Do Active SAE Feature Planes Carry More Holonomy? A Preregistered Reversal in Gemma](https://arxiv.org/abs/2607.20522)

**<font color=#1a73e8>作者：</font>** Larry Richards  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper tests whether holonomy concentrates on active sparse-autoencoder (SAE) feature planes in Gemma 2 2B, a concrete operationalization of the broader semantic-concentration prediction. Holonomy is measured at the final-token layer-12 to layer-13 residual-stream readout by carrying a local frame around small loops using the instrument's restricted-Jacobian transport rule, then normalizing the resulting rotation by enclosed area. The design, materiality threshold, analysis, and verdict rules were preregistered and frozen before the analysed measurements were inspected. The prediction was falsified in reverse: active-feature planes carried less holonomy than matched mixed-feature controls, with an adjusted log contrast of -0.29439 and 95% interval [-0.43989, -0.14889]. A magnitude-only explanation was not supported in this design, while the three-way ordering across random, mixed-feature, and active-feature planes was undefined at matched magnitude because common support failed. Post-freeze diagnostics at the same readout supported the area law on a small validation subset, bounded matched-center displacement under a simple paired regression, and identified transport distortion as a live mechanism or confound. The result is therefore a narrow, auditable operational reversal, not a causal claim that meaning suppresses holonomy. The cause remains open, with activation-strength geometry, degree of feature engagement, dictionary geometry, matched-center displacement, activation-manifold proximity, and transport shear as live alternatives.

---


### 31. [CLOE: Christoffel Loss Autoencoder for Anomaly Detection](https://arxiv.org/abs/2607.20530)

**<font color=#1a73e8>作者：</font>** Léa Billet, Louise Travé-Massuyès, Elodie Chanthery 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised anomaly detection plays a key role in diverse fields such as process monitoring, healthcare, and finance. However, lightweight methods often struggle with high-dimensional data and typically require careful tuning of multiple hyperparameters. Among existing approaches, Christoffel Function--based methods are attractive due to their simplicity, requiring at most a single hyperparameter. They also benefit from a well-established theoretical foundation that yields several interesting results for data science. However, their main limitation is poor scalability to high-dimensional settings. In this paper, we introduce CLOE, a new method that combines an autoencoder for dimensionality reduction with a Christoffel Function--based detector applied in the latent space. To better align representation learning with anomaly detection, we design a novel loss function that leverages the Christoffel Function to guide the autoencoder toward representations that better capture the support of the normal data distribution. We further propose a principled procedure to set the detection threshold and an efficient strategy to tune the single remaining hyperparameter. Experiments on multiple high-dimensional tabular anomaly detection benchmarks demonstrate that CLOE achieves superior performance compared to existing methods, while preserving the lightweight and low-tuning advantages of Christoffel Function--based approaches.

---


### 32. [Position: Stop Reactively Patching Your Model Every Time and Start Proactive Test-Driven AI Development](https://arxiv.org/abs/2607.20532)

**<font color=#1a73e8>作者：</font>** Nadine Chang, Maying Shen, Jialiang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern AI systems are designed to operate under diverse, open-ended, use-cases. To help generalize deployed systems, many deployed-system maintenance pipelines use a reactive AI flywheel that observes emerging feedback from user behavior (errors) and patches the model accordingly. However, when used as the primary maintenance mechanism, these flywheels often ignore the broader context of these errors within the system's objectives, failing to preempt potential future edge cases, which leads to more unnecessary flywheel iterations. Also, it is statistically increasingly difficult to collect remaining errors due to the long-tail nature of open-world use-cases. This position paper argues that a proactive test-driven flywheel is required to address reactive flywheel's limitations and to approach a generalizable system. We advocate for creating a "test space" to technically map feedback data to task objectives, evolving the flywheel from reactive to proactive. We augment our position by mathematically proving a proactive one achieves better long-term scaling with fewer iterations than the reactive flywheel.

---


### 33. [Grounding Investor Views: Neural Predicates in the Black-Litterman Model](https://arxiv.org/abs/2607.20533)

**<font color=#1a73e8>作者：</font>** Marcos Florencio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Portfolio construction under the Black-Litterman model requires investors to specify views on asset returns alongside explicit uncertainty estimates -- a process that remains largely subjective and difficult to scale. We propose a formal approach in which neural predicates serve as a structured, probabilistic mechanism for view generation. In our formulation, structured financial analysis data is processed through a compositional hierarchy of neural predicates whose outputs -- probability distributions over market stances -- are mapped to the pick matrix $\mathbf{P}$, the view return vector $\mathbf{q}$, and the view uncertainty matrix $\boldsymbol{\Omega}$ of the Black-Litterman model. View confidence is derived from predicate output distributions, providing a data-driven alternative to subjective uncertainty elicitation. The resulting approach is interpretable, in the sense that any portfolio weight can be traced back through the predicate's logical chain to the underlying data, and fully differentiable, enabling end-to-end learning.

---


### 34. [A Graph Neural Network approach to zero-shot Digital Twins](https://arxiv.org/abs/2607.20535)

**<font color=#1a73e8>作者：</font>** Alicia Tierz, Icíar Alfaro, David González 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional Predictive Digital Twins often remain geometrically rigid, requiring extensive retraining or fine-tuning whenever the underlying physical domain or boundary conditions change. To overcome this limitation, we present a novel framework for \textit{Zero-Shot Digital Twins} that seamlessly couples real-time visual perception with a geometry-agnostic, physics-informed reasoning engine. At the core of our architecture is the Thermodynamics-Informed Graph Neural Network architecture, a Geometric Deep Learning solver grounded in a metriplectic thermodynamic formalism that enforces energy conservation and non-negative entropy production locally through graph message passing. The framework integrates an auxiliary Graph Neural Network to infer unobservable fields (such as stress tensors or velocity and energy distributions) directly from sparse initial visual boundaries, mitigating numerical start-up transients. To bridge the sim-to-real gap, we implement a continuous closed-loop data assimilation mechanism; the pipeline tracks macroscopic deformations and free-surface fluid boundaries in real-time using deep segmentation networks combined with sparse optical flow, dynamically correcting the autoregressive simulation rollout and eliminating numerical drift. To test the validity of our approach, we demonstrate the extreme generalization capabilities of our approach across two disparate physical regimes: the large deformations of a viscoelastic beam and the non-linear sloshing of a viscous fluid. In both scenarios, the unified framework instantiates physically accurate simulations on novel, unseen geometries without case-specific retraining, operating well within real-time latency budgets (approximately 25 ms per frame) and enabling the direct projection of latent mechanical variables via Augmented Reality.

---


### 35. [AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use](https://arxiv.org/abs/2607.20536)

**<font color=#1a73e8>作者：</font>** Junzhi Chen, Harsh Trivedi, Jane Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-use agents that address day-to-day digital tasks such as ordering groceries must not only operate applications, but also interact with the user, e.g., to ask clarification questions, prompt for confirmation, and inform the user when the instruction is infeasible. However, current benchmarks for evaluating agent-user interactions do not capture the diversity of such interactions. Further, they operate in small environments with few, often non-state-changing, APIs. To address this gap, we introduce AppWorld-UL, a ``user-in-the-loop'' benchmark of 516 challenging tasks requiring diverse agent-user interactions. Building upon the AppWorld framework with 9 popular simulated apps like Amazon and Spotify, we systematically modify original tasks to introduce ambiguities and constraints that necessitate various types of agent-user interaction. User behavior is simulated by an LLM prompted to respond with carefully designed knowledge boundaries, offering more reliable simulation than the unconstrained or overly rigid alternatives used in prior work. Our evaluation reveals that a state-of-the-art LLM, Claude Opus 4.7, achieves only 48.6% success on AppWorld-UL, and only 35.7% on the harder, compositional subset. On the stricter, scenario-level metric, compositional task performance drops to only 21.3%. Our analysis reveals that correct user-interaction is crucial for success. This demonstrates the benchmark's difficulty and its potential to advance research on user-in-the-loop tool-use agents.

---


### 36. [ReliableTableQA:How Much Supervision Does Reliability Annotation Need?](https://arxiv.org/abs/2607.20537)

**<font color=#1a73e8>作者：</font>** Huei-Chung Hu, Hsin-Tai Wu, Koyo Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ReliableTableQA, a framework for training an LLM to annotate the statistical reliability of tabular QA results, not whether the query is answerable, but whether the computed answer is statistically meaningful. In real enterprise analytics, a syntactically correct SQL query can return a value that is based on too small a sample, has an excessively wide confidence interval, or is too confounded to support action. Existing systems answer confidently in all such cases, a failure we quantify as the Unreliable Confident Answer Rate (UCAR). We contribute (1) a ten-category reliability taxonomy (R1-R10) covering hazards such as small-sample aggregates, multiple-comparison inflation, and distribution-tail mismatch; (2) a program-first data pipeline that generates 50,000 reliability-labeled training examples from a context-free grammar over public retail schemas, with schema-stratified SFT/GRPO splits; and (3) a controlled study of how much supervision calibrated reliability annotation actually requires. We find that a small, schema-stratified SFT set is remarkably sufficient: 200 examples raise reliability-flag F1 from 0.61 to 0.98 and parse rate from 0.52 to 1.00, drive UCAR to zero, and yield a model that generalizes to an unseen retail domain (Rel-F1 0.997 on held-out H&M). Against this strong SFT baseline, GRPO, commonly assumed to be essential, helps only when SFT is under-trained (+0.06-0.16 exact-flag-set match at 100 examples, in- and out-of-distribution) and provides no measurable benefit once SFT is adequate, a null result we confirm across a hard compound-flag slice, a strict exact-match metric, and out-of-distribution evaluation. Our findings reframe reliability annotation as a data-efficiency problem and delineate precisely when reinforcement fine-tuning does and does not pay off.

---


### 37. [Codec-Gauge: Learning Compression-Friendly Gauges for Transformer KV Caches](https://arxiv.org/abs/2607.20538)

**<font color=#1a73e8>作者：</font>** Yitao Jiang, Yaoqing Yang, Luyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context Transformer inference increasingly relies on KV-cache compression or quantization. Prior rotation and transform-coding results suggest that the channel basis of each key/value vector affects how faithfully a fixed backend preserves model behavior. We introduce Codec-Gauge, a post-training cache-coordinate layer that learns small orthogonal channel transforms around existing compression and quantization backends. Its frequency-distribution objective combines a token-channel DCT spectral-centroid loss with a smooth rate proxy to concentrate KV energy in low-frequency codec-facing layouts. We evaluate actual compression and decompression using measured bytes and rolling compressed-history scoring. Across six models at $3$, $4$, and $6$ bits/value, learned gauges reduce zfp KL divergence by $44.0\%$ on average relative to raw coordinates and outperform random, Hadamard, DCT, and PCA/KLT controls. The same gauges improve quality preservation for block-uniform and KIVI-style quantization. Experiments on a 27B model and long-context task prompts reproduce the quality trend, while serial storage and timing measurements validate the implemented compressed-cache paths. These results establish cache-coordinate geometry as a practical post-training variable for improving compression fidelity without changing model weights, attention semantics, or backend coding rules.

---


### 38. [From Atoms to Entropy: Optimal Noise Allocation for Diffusion Training in the Convex Regime](https://arxiv.org/abs/2607.20540)

**<font color=#1a73e8>作者：</font>** Luca Ambrogioni, Giulio Franzese, Alberto Foresti 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How should a diffusion model decide which noise levels to train on, and how much? Despite the importance of this choice, current noise schedules are based largely on heuristics or empirical tuning. Here, we develop a general statistical framework for studying asymptotically optimal noise-level allocation in diffusion training. Our first main result concerns the fully coupled regime, where information can spread between different time points. Under convexity or Polyak-Lojasiewicz-type assumptions, we show that the optimized training schedule admits an atomic minimizer, concentrated on finitely many noise levels. Our second main result specializes this framework to an idealized independent-learner regime, intended to model temporal specialization in neural networks. Under an additional feature-noise decoupling condition, a random-matrix analysis leads to an information-theoretic proxy: the decoupled sampling density is proportional to the square root of the generative entropy rate, the rate at which conditional entropy grows along the forward process. We test these predictions in controlled settings where the coupled objective can be optimized directly, including Dirac mixtures, low-dimensional manifolds, and MNIST. In these settings, the optimized schedules are consistently finite-support, while the smooth entropic proxy closely tracks the atomic optimum in neural-network models and breaks down mainly in the fully coupled parametric case, as the theory suggests. We then evaluate the entropic schedule in larger-scale experiments, where full schedule optimization is currently intractable. The results indicate that square-root entropy scheduling can substantially improve training efficiency on discrete domains and remains competitive with standard EDM-style heuristics on continuous images.

---


### 39. [HypNO: A Graph-Based Neural Operator with Physics-Informed Message Passing for Hyperbolic Conservation Laws](https://arxiv.org/abs/2607.20541)

**<font color=#1a73e8>作者：</font>** Dimitrije Ždrale, Cassie An Jeng, Katie Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce HypNO, a graph-based neural operator for scalar hyperbolic conservation laws. HypNO operates directly on a space-time graph of finite-volume cells and uses adjacency-factored, physics-informed message passing to respect upwinding and entropy admissibility near shocks. We benchmark the architecture on the Lighthill-Whitham-Richards (LWR) and Aw-Rascle-Zhang (ARZ) traffic-flow models, a stress test for operator-learning methods because of their simultaneous global transport and shock formation. HypNO predicts solution snapshots accurately across a range of initial conditions while capturing the shocks and discontinuities of the solution.

---


### 40. [Improving Access to Essential Medicines via Decision-Aware Machine Learning](https://arxiv.org/abs/2607.20542)

**<font color=#1a73e8>作者：</font>** Angel Tsai-Hsuan Chung, Jatu Abdulai, Patrick Bayoh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A critical challenge in healthcare systems in low- and middle-income countries (LMICs) is the efficient and equitable allocation of scarce resources, particularly essential medicines. This problem is complicated by limited high-quality data, which restricts the applicability of traditional data-driven techniques. We propose a novel decision-aware machine learning framework for essential medicines allocation, which additionally leverages multi-task learning to ensure sample efficiency and catalytic priors to ensure equitable allocation. In collaboration with the Sierra Leone national government, we performed a staggered, nationwide deployment of our system as a decision support tool. Our econometric evaluation finds an estimated 19% increase in consumption of allocated products in treated districts, demonstrating its efficacy at improving access to essential medicines. Our tool was subsequently scaled nationwide, covering an estimated 2 million women and children under five. Our work demonstrates how machine learning methods can improve efficiency at very low cost in resource-constrained global health settings.

---


### 41. [When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion](https://arxiv.org/abs/2607.20543)

**<font color=#1a73e8>作者：</font>** Todd Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling. We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$. The failure concentrates on boundary prompts, where the base model contains rare correct trajectories that are recoverable by sampling but too sparse to reliably appear in finite RLVR rollout groups. We argue that a two-mode account explains this as an absence-of-evidence failure: rare correct trajectories may disappear before RLVR samples and reinforces them often enough. The main contribution is this diagnostic and mechanistic framing. Per-Problem Base Anchoring (PBA) is a deliberately simple proof-of-concept: sharpen prompts with sufficient frozen-base correct evidence, and anchor risky prompts to the base distribution. Across three training seeds on Omni-MATH-Test, with MATH500 as a secondary high-coverage validation benchmark, PBA improves both \PassK{1} and high-budget coverage over matched GRPO. A 3000-prompt regime-controlled diagnostic study is consistent across seeds with the expected signature: ordinary GRPO loses base-solvable boundary prompts, while PBA preserves rare verifier-positive trajectories. We use mathematical verifiers as a controlled testbed for verifier-guided optimization; the same pass@k inversion risk applies to ECCV-relevant vision-language agents when repeated visual, spatial, or chart-reasoning attempts are checked by external tools or verifiers. Reasoning post-training should decide not only how strongly to optimize, but which prompts are safe to optimize.

---


### 42. [StrideDiffusion: Accelerating Diffusion Models for Time-series Generation](https://arxiv.org/abs/2607.20545)

**<font color=#1a73e8>作者：</font>** Du Yin, Estrid He, Julián Jerónimo Bañuelos 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become competitive generators for time series, but their practical use is limited by the large number of sequential denoising steps required at inference time. Existing fast samplers typically use fixed or generic timestep schedules, overlooking a distinctive property of time-series diffusion: different spectral bands evolve at different rates during the reverse process. We introduce StrideDiffusion, a training-free spectral-aware sampler that adaptively selects the denoising stride from band-level activity. At each step, StrideDiffusion monitors relative band energy, log-power drift, and phase velocity to identify whether high- frequency dynamics remain active or whether the trajectory is dominated by stable low-frequency structure. It then takes fine steps when rapidly varying bands are active and larger jumps once only coarse components remain. A bandwise stability analysis shows that inactive frequency bands change only linearly with the jump size under deterministic affine reverse updates, providing a local justification for spectral activity as a step-size indicator. Across six unconditional time-series generation benchmarks, StrideDiffusion uses only 14-66 function evaluations instead of 500/1000 denoising steps, achieving up to 18.9x wall-clock speedup while preserving or improving generation quality. On conditional imputation and forecasting, it further delivers 5-14x average acceleration with comparable predictive accuracy. These results show that spectral evolution provides a practical and principled signal for fast time-series diffusion sampling. Our code is available at this https URL.

---


### 43. [Conflict Resolution under Degraded Surveillance in Air Corridors Using Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2607.20547)

**<font color=#1a73e8>作者：</font>** Esrat Farhana Dulia, Syed Arbab Mohd Shihab, Caleb Adams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe Advanced Air Mobility operations require aircraft to maintain separation when surveillance information is noisy, delayed, incomplete, or temporarily unavailable. This study develops a Deep Q-Network-based Multi-Agent Reinforcement Learning framework for decentralized conflict resolution among heterogeneous small unmanned aerial vehicles and electric vertical takeoff and landing aircraft operating within a structured three-dimensional corridor. Separate policies are trained for the two aircraft categories using local observations and a 14-action space that includes maintaining course, turning, vertical maneuvering, landing, and speed control. The simulation incorporates aircraft-specific dynamics, energy use, corridor constraints, observation noise, communication delay, information dropout, wind disturbance, actuator uncertainty, and model uncertainty. The trained policies are evaluated across 90 combinations of traffic density and minimum separation thresholds. Loss-of-separation frequency and duration generally increase with traffic density and separation requirements, although most events are resolved within 1s. Under safe conditions, agents maintain their motion approximately 79% of the time. During conflicts, turning accounts for 33% of actions, followed by maintaining motion at 29%, speed control at 25%, and vertical maneuvers at 13%. Six Pareto-optimal configurations reveal trade-offs between safety and corridor capacity. The framework supports the simulation-based evaluation of safer AAM conflict-resolution strategies under degraded surveillance conditions.

---


### 44. [SevDiff: Severity-Conditioned Diffusion for Long-Tail Conflict Trajectory Generation](https://arxiv.org/abs/2607.20549)

**<font color=#1a73e8>作者：</font>** Eni Solomon Laughter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory datasets used in ADAS evaluation are heavily biased toward routine driving; genuine vehicle-to-vehicle conflict events are rare, and the rarer the event, the higher the cost when an ADAS system fails to handle it. Existing generative approaches address this imbalance by conditioning on scene-level properties - spatial goals, agent structure, or natural-language adversarial objectives - but none can accept a target Time-to-Collision (TTC) value as input and be held to producing it within a measurable error. This paper introduces SevDiff, a severity-conditioned denoising diffusion probabilistic model (DDPM) that accepts a requested minimum TTC value as a scalar conditioning signal and generates paired vehicle interaction trajectories whose realized conflict severity matches the request, evaluated through a hit-rate metric. Trained on 468 interaction windows extracted from the UTE SQM-W-1 expressway weaving-section dataset (1,041 vehicles, 822,691 observations after smoothing), SevDiff achieves 100% hit-rate within +/-0.5 s for TTC targets of 0.5-1.5 s and 97-99% at 2.0-2.5 s, with graceful degradation to 39% at TTC = 5.0 s. Generated kinematic features are physically plausible, with a maximum out-of-range rate of 4.7% across 12 features and no negative speed or gap values in more than 96.5% of samples. The hit-rate degradation pattern is physically interpretable as the strength of the conditioning signal relative to the training prior, making it a precision characterization of the generator rather than a pass/fail result.

---


### 45. [Beyond SBDD: Geometric Deep Learning in Polypharmacology and Multi-target Drug Design](https://arxiv.org/abs/2607.20550)

**<font color=#1a73e8>作者：</font>** Tianming Han, Zhijie Pan, Wenchi Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The traditional "one drug, one target" paradigm of structure-based drug design (SBDD) frequently proves inadequate for treating multifactorial diseases such as cancer and neurodegenerative disorders, owing to compensatory signaling pathways and the emergence of drug resistance. While polypharmacology offers a synergistic therapeutic strategy, the rational design of ligands capable of simultaneously satisfying the geometric constraints imposed by multiple targets remains a major computational bottleneck. This review positions geometric deep learning (GDL) as a powerful integrative approach to overcome these limitations. We systematically survey GDL architectures ranging from invariant graph neural networks to SE(3)-equivariant diffusion models that harness non-Euclidean molecular data to capture intrinsic three-dimensional (3D) structural interdependencies. We critically analyze GDL applications across three core dimensions, including the characterization of shared binding pockets via geometric embeddings, multi-target bioactivity prediction through heterogeneous graph fusion, and de novo generation of dual-target ligands. Particular emphasis is placed on emerging structure-conditioned generative algorithms that integrate diffusion models with reinforcement learning to autonomously resolve complex geometric conflicts between competing binding sites. Furthermore, we evaluate the pivotal role of multimodal omics integration and specialized geometric benchmarking infrastructures in validating these models. By synthesizing these methodological advances, this review elucidates the paradigm shift in drug discovery from serendipitous exploration to rational, structure-driven polypharmacological molecular engineering, thereby providing a clear, structured guide for navigating the complexities of next-generation therapeutics.

---


### 46. [SenCos-GEM: SENet-Calibrated and Law-of-Cosines-Constrained Geometry-Enhanced Molecular Representation for Property Prediction](https://arxiv.org/abs/2607.20551)

**<font color=#1a73e8>作者：</font>** Tianming Han, Li Zhang, Qi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective molecular representation learning is crucial for accurate molecular property prediction. Recently, numerous self-supervised learning (SSL) approaches leveraging 3D GNNs have been developed to capture comprehensive 3D structural information for drug discovery. However, existing methods lack explicit physical constraints and are highly susceptible to geometric noise induced by coarse empirical force fields during large-scale this http URL, they overlook dynamic feature modulation during downstream adaptation, often resulting in catastrophic forgetting and negative transfer. To address these limitations, we introduce SenCos-GEM, a novel explicitly decoupled geometry-enhanced molecular representation learning framework that incorporates SENet-calibrated and law-of-cosines-constrained enhancements. SenCos-GEM employs a physics-guided geometric consistency loss based on the law of cosines to derive high-fidelity and mathematically invariant 3D spatial priors. In addition, lightweight Squeeze-and-Excitation (SE) modules are integrated into the backbone as task-specific adapters, while a dual-modulation prediction head combines Feature-wise Linear Modulation (FiLM) and SENet mechanisms to enable dynamic feature recalibration. SenCos-GEM demonstrates highly competitive performance across diverse classification and regression tasks on MoleculeNet benchmark, establishing new state-of-the-art results specifically on 3D conformation-sensitive regression tasks, such as FreeSolv, Lipophilicity, and QM9, achieving relative error reductions of 12.9% (RMSE), 5.3% (RMSE), and 8.2% (MAE), respectively. Moreover, our model exhibits superior capability in distinguishing stereoisomers and discriminating conformational perturbations, underscoring its robust spatial modeling performance. Collectively, SenCos-GEM represents a significant breakthrough in accurate molecular property prediction.

---


### 47. [Thermodynamic Weight Decay: Exploring Grokking Acceleration via Attention Specific Heat](https://arxiv.org/abs/2607.20552)

**<font color=#1a73e8>作者：</font>** Chitraansh Pandey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking -- the delayed generalization of neural networks long after they have memorized their training data -- wastes thousands of training epochs and is notoriously unpredictable. Building on the recent result that Transformer attention is formally isomorphic to a thermodynamic system, we treat the variance of attention logits as a specific heat Cv and show that its peak reliably precedes the generalization transition. We introduce CvAdamW, a drop-in AdamW variant that monitors Cv online and injects thermal energy by dynamically scaling weight decay when a phase transition is detected. Through a strictly iterative development process we identify three failure modes -- initialization noise, mini-batch micro-ripples, and slingshot blinding -- and resolve them with a memorization gate and an exponential-moving-average shock absorber. On modular arithmetic (a+b mod 97), CvAdamW enables grokking at epoch 2802 in a 4000-epoch budget where the baseline never groks. We further propose a scale-invariant z-score reformulation that removes task-specific hyperparameters, and evaluate it across 10 paired seeds. A paired analysis shows the cold-start variant reduces mean grokking latency by 257 epochs (6.0%; median 166 epochs; Wilcoxon p=0.049, Cohen's d=0.68, bootstrap 95% CI [53,489]), improving 8 of 10 seeds; on this single task Cv peaks before grokking in all 10 seeds. Our results indicate that neural networks may expose detectable precursors of impending generalization transitions, and that a physically motivated, proportional intervention can facilitate generalization within a fixed compute budget. Code and data are public.

---


### 48. [CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning](https://arxiv.org/abs/2607.20553)

**<font color=#1a73e8>作者：</font>** Yubo Wang, Qiuyu Zhao, Zenghui Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory Manager models are pivotal in agent systems. Existing methods rely predominantly on LLM-judged synthetic question-answer (QA) pairs, making memory valuation dependent on sampled queries and the downstream reader. To address this limitation, we propose \textbf{CMI-Mem}, a reinforcement learning(RL)-based lightweight memory manager model with a hybrid reward that combines downstream QA correctness and intrinsic Conditional Mutual Information (CMI). CMI evaluates the information contributed by new conversational inputs relative to the current memory state without conditioning on a sampled QA query, thereby complementing rather than replacing QA grounding. Our codes are available at: this https URL , and the CMI-Mem-4B model checkpoint is available at: this https URL

---


### 49. [AI-Driven Multi-Hop Relay Selection for Smart Urban NR-V2X Networks via Learning-to-Optimize Graph Neural Networks](https://arxiv.org/abs/2607.20554)

**<font color=#1a73e8>作者：</font>** Giambattista Amati, Federica Mangiatordi, Simone Angelini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable and low-latency NR-V2X communications are essential for smart mobility in dense urban environments. However, limited Road-Side Unit (RSU) density, frequent non-line-of-sight conditions, and highly dynamic vehicular topologies often prevent many Connected and Automated Vehicles (CAVs) from maintaining stable single-hop connectivity. Although multi-hop relay-assisted communication can extend infrastructure coverage, selecting relay links in real time under practical flow, capacity, and connectivity constraints remains challenging.
Mixed-Integer Linear Programming (MILP) yields optimal multi-hop relay decisions, but its computational complexity scales sharply with network density, limiting real-time applicability. To address this, we propose a Learning-to-Optimise (L2O) framework based on Graph Neural Networks (GNNs) for real-time NR-V2X relay selection. Vehicular communication states are modeled as attributed graphs, where CAVs and RSUs are nodes and candidate radio links are enriched with propagation-aware features. An offline MILP oracle provides optimal supervision, while an edge-aware Graph Isomorphism Network (GINE) approximates oracle decisions with near-constant inference latency. Experiments on large-scale urban datasets generated by an integrated SUMO--GEMV2 simulation pipeline show that the proposed approach achieves connectivity comparable to that of the MILP oracle while reducing execution time by orders of magnitude. The framework enables cost-effective enhancement of urban V2X connectivity by leveraging existing vehicular assets and supporting scalable, real-time NR-V2X operation in smart city environments.

---


### 50. [Double-Scoring: Reliable Extraction of Strong Lottery Tickets](https://arxiv.org/abs/2607.20555)

**<font color=#1a73e8>作者：</font>** Bryce A. Christopherson, Jack Baretz, Darian Colgrove 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The lottery ticket hypothesis proposes that large random neural networks contain sparse subnetworks that can match the performance of dense models after comparable training. A stronger version asserts that sufficiently overparameterized random networks contain subnetworks that are already accurate before any weight training. Existing theory establishes that such strong lottery tickets exist, but reliable extraction remains difficult. We revisit edge-popup, a frozen-weight score-training method for extracting strong tickets, and identify layerwise sparsity selection as a central bottleneck. We introduce double-scoring, an augmented score-space parameterization that replaces a layerwise sparsity search with optimization over enlarged score tensors. We prove that fixed-density masking in an augmented score space preserves access to all original-coordinate masks, and we show that the resulting method can be interpreted as edge-popup on a zero-augmented network. In controlled experiments, double-scoring substantially improves strong-ticket extraction over fixed-density edge-popup and pruning-at-initialization baselines, improves on the performance of rewound sparse-training topologies, and exhibits markedly lower sensitivity to sparsity hyperparameters. Ablations show that the gain is not merely due to additional trainable score parameters, but is tied to the augmented score-space competition that induces the effective original sparsity.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
