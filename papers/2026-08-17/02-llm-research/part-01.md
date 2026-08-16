# 🧠 大模型相关研究 | 2026年08月17日

> 本类共 **183** 篇论文：已确认 **168** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

---

### 1. [LLMs Know the Constraint But Do Not Use It: Activation Bottlenecks in Pragmatic Constraint Reasoning](https://arxiv.org/abs/2608.12321)

**<font color=#1a73e8>作者：</font>** Yubo Li, Ramayya Krishnan, Rema Padman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a salient surface cue competes with an implicit feasibility constraint, LLMs often fail -- but aggregate accuracy conflates genuine constraint inference with conservative defaulting. We formalize the distinction as conditional constraint activation: the constraint is internally encoded (Knowledge) symmetrically across constraint-present and -absent prompts (Symmetry), yet only sometimes routed into the decision (Routing) and repairable by a donor activation (Repair). A quartet diagnostic over 14 models reveals two failure modes; probes on two open weights decode the constraint above $88\%$, yet activation patching repairs one ($+6.4$ nats) and not the other ($-0.07$). On a mitigation frontier, no prompted intervention reaches the repair corner: all inflate conservative bias through a single mediation pathway -- prerequisite mention. Hidden-constraint failure is a routing problem, not a knowledge problem.

---


### 2. [What Drives LLM Self-Reflection? A Controlled Ablation of Uncertainty Routing in Armed Conflict Forecasting](https://arxiv.org/abs/2608.12322)

**<font color=#1a73e8>作者：</font>** Poli Nemkova, Haeshitha Indukuri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-reflection is widely assumed to improve LLM reasoning, yet which component drives the gain remains poorly understood. We present a controlled six-condition ablation isolating four components of LLM self-reflection: evidence exposure, diagnostic scaffolding, taxonomy vocabulary, and action routing. Two precise null results converge on a single mechanism. First, structured diagnostic questions add no measurable value over unstructured reflection ($\text{F1} = 0.296$ vs $0.297$, $p = 1.000$, 95\% CI $[-0.041, +0.040]$). Second, presenting the full uncertainty taxonomy while collapsing the action space to a single generic action also adds no value ($\Delta\text{F1} = +0.008$, overlapping 95\% CIs), ruling out taxonomy vocabulary as the mechanism. Typed action routing provides consistent directional gains ($\text{F1} = 0.379$ vs $0.296$); the conservative estimate controlling for taxonomy vocabulary is $\Delta\text{F1} = +0.075$, and the overall gain over the single-shot baseline is significant by bootstrap CI ($\Delta\text{F1} = +0.101$, 95\% CI $[+0.020, +0.185]$). The vocabulary-routing decomposition replicates on GPT-4o: taxonomy vocabulary adds no significant value over generic reflection ($p = 0.773$), while action routing provides significant gains ($p = 0.025$), confirming the mechanism holds across backbones. Gains concentrate on structurally novel conflicts: in Myanmar ($\text{F1}: 0.000 \rightarrow 0.353$) and Ukraine ($0.167 \rightarrow 0.500$), the vocabulary-only condition recovers no more than generic reflection while action routing breaks the degenerate prior. These findings identify typed action routing -- not diagnostic scaffolding or taxonomy vocabulary -- as a promising design principle for metacognitive LLM forecasting agents, while motivating larger-scale evaluation across conflict typologies.

---


### 3. [Why Do AI Agents Break Rules? How Framing, Context, and Social Signals Shape Compliance](https://arxiv.org/abs/2608.12323)

**<font color=#1a73e8>作者：</font>** Mika Okamoto, Ansel Kaplan Erol, Kutluhan Erol  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Specifying a penalty can paradoxically convert a legal obligation into a cost-benefit calculation that favors violation. We demonstrate that this enforcement information paradox systematically occurs in AI agents. While most AI safety evaluations test whether models fail, we investigate why, applying compliance theory from law and economics as a diagnostic tool. We treat compliance theories not as metaphors but as empirical hypotheses and show that each predicts the behavior of a distinct model class. We evaluate our hypotheses across twelve instruction-tuned language models operating as enterprise procurement chatbots. Drawing on theories of deterrence, legitimacy, and expressive law, we show that safety-fine-tuned models maintain compliance broadly, while task-optimized and agentic models treat regulatory signals as mere optimization parameters. These latter models fail to comply under conditions predicted by theory, such as low enforcement penalties and non-command phrasing. Across all models, introducing financial incentives, managerial demands, peer outcomes, or employee pressure produces large compliance failures. AI procurement agents systematically violate regulatory constraints to satisfy local user objectives in ways not captured by standard alignment benchmarks. Ultimately, compliance cannot be achieved by rule embedding alone; model selection is itself a governance decision, and benchmark-based evaluation is insufficient for compliance-sensitive deployments.

---


### 4. [Position: Reasoning is a Learnable Rule-Based Process](https://arxiv.org/abs/2608.12325)

**<font color=#1a73e8>作者：</font>** Rachel Lawrence, Jacqueline Maasch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous reasoning is among the most scientifically and economically motivating topics in AI today. Historically the purview of symbolic AI, recent advances have mainly emerged from deep probabilistic generative models. Despite immense interest and rapid progress, the generative AI community has not clearly converged on operational definitions for reasoning and often implicitly rejects the historical treatment of this topic in logic and verifiable automated reasoning. This position contends that definitional ambiguity leaves the construct validity of reasoning evaluation unverifiable, undermining quantifiable progress toward trustworthy autonomous reasoning. We also contend that this ambiguity is addressable. To that end, we provide (1) operational definitions based on a synthesis of the literature, positioning valid and sound reasoning as a learnable rule-based process; and (2) a checklist for best practices in the communication of AI reasoning research.

---


### 5. [On Measuring Semantic Preservation in Legal Ontology Learning](https://arxiv.org/abs/2608.12326)

**<font color=#1a73e8>作者：</font>** Albert Sadowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ontology learning transforms unstructured text into structured representations for automated reasoning. Yet structuring information risks losing it, and current evaluation methodologies cannot detect such loss, focusing on structural correctness while failing to measure whether meaning survives transformation. We propose an evaluation methodology that addresses this: comparing LLM task performance on source documents against performance on transformed representations, with the difference quantifying semantic loss. We demonstrate this approach on legal merger agreement analysis, a domain chosen for its complex language and precise semantic requirements, comparing direct LLM application against three ontology learning methods across six language models. The results reveal systematic semantic loss with significant variation based on reasoning complexity and model-method interactions. Our contributions are: (1) an evaluation framework for measuring semantic preservation in ontology learning, and (2) empirical evidence that semantic loss varies dramatically with model-method pairing, providing guidance for selecting optimal configurations in legal knowledge systems.

---


### 6. [LoRA-Diffusion: Parameter-Efficient Fine-Tuning via Low-Rank Trajectory Decomposition](https://arxiv.org/abs/2608.12328)

**<font color=#1a73e8>作者：</font>** Iman Khazrak, Narges Nejad, Mohammadhossein Homaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning methods such as LoRA have transformed the adaptation of large autoregressive language models, enabling task-specific customization with substantially fewer trainable parameters. However, these methods have not been successfully extended to diffusion-based language models, which generate text through iterative denoising rather than sequential token prediction. We propose LoRA-Diffusion, a parameter-efficient fine-tuning approach that applies low-rank decomposition to the denoising trajectory instead of model weights. Unlike weight-based LoRA, which modifies individual transformation matrices, our method learns low-rank perturbations to the entire diffusion path from noise to output. We introduce trajectory-level low-rank adapters that modify each denoising step, step-adaptive rank allocation across diffusion phases, and compositional multi-task learning that allows merging task-specific modules at inference without retraining. On SST-2, QNLI, and MRPC, we report token-level denoising validation accuracy over five random seeds. LoRA-Diffusion achieves the highest mean performance on SST-2 and strong performance on QNLI and MRPC. Joint multi-task training further shows that LoRA-Diffusion achieves the highest token-level accuracy among the evaluated methods. The approach reduces per-task storage compared with full fine-tuning and establishes a parameter-efficient fine-tuning framework for diffusion language models.

---


### 7. [AnchorSIPS: A Synthetic Dataset and Evaluation Resource for Evidence-Supported Psychosis-Risk Symptom Measurement](https://arxiv.org/abs/2608.12329)

**<font color=#1a73e8>作者：</font>** Guilherme C. Oliveira, Stephanie Fong, Zimu Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Progress on AI for psychosis-risk assessment is limited by a data-access bottleneck. Real clinical interviews are difficult to share because of privacy, governance, and consent constraints. We present AnchorSIPS, a synthetic dataset of 10K structured psychosis-risk interviews with transcript-grounded measurement targets. Each interview is modeled on Mini-SIPS, a clinician-administered psychosis-risk interview. It captures history, 24 symptom questions, follow-up evidence for items the patient affirms, decisions about delusion-like symptoms (unusual beliefs), hallucination-like symptoms (unusual perceptions), and disorganized communication, exclusion of clear psychotic-level symptoms ("frank psychosis"), and a final attenuated psychosis syndrome (APS) diagnosis, a high-risk state of milder or early psychotic symptoms. The APS diagnosis is not a standalone label. It depends on earlier endorsements, supporting follow-up details, symptom-class decisions, and the frank-psychosis check. Every intermediate decision is anchored to its supporting transcript turns. AnchorSIPS is generated by a plan-then-realize pipeline. A hidden case sheet specifies the patient's clinical state, a deterministic planner fixes the interview structure, and an LLM realizes only the patient utterances under validation and bounded repair. Fixing labels and structure before generation avoids the inter-turn inconsistencies typical of multi-turn LLM dialogue. Across seven LLM baselines, models recover coarse decisions but fail to extract follow-up details or cite supporting transcript turns, so final-label performance overstates interview competence. AnchorSIPS is intended for research on evidence extraction, transcript-grounded measurement, and uncertainty under partial disclosure.

---


### 8. [Reliability-Aware Sexism Detection: Combining DPO with Annotator Agreement and Token-Level Confidence Scoring](https://arxiv.org/abs/2608.12330)

**<font color=#1a73e8>作者：</font>** Hadi Mohammadi, Shihan Wang, Masoume M. Raeissi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The detection of online sexism remains an open problem. Sexism detection is inherently subjective, yet most existing systems reduce multi-annotator labels to a single majority decision and treat all instances uniformly. This ignores two informative signals: annotator agreement and model uncertainty. We propose RA-DPO (Reliability-Aware Direct Preference Optimization), which integrates annotator agreement, model confidence, and a token-level uncertainty signal into a single reliability score. RA-DPO uses this score to select high-value preference pairs during training and to support inference-time abstention, which allows the model to trade coverage for accuracy. We evaluate RA-DPO on 6,920 multilingual posts from EXIST 2023, fine-tune OpenAI gpt-4o base via DPO, and validate on two open-weight 3B models (Llama, Qwen). Results show that training on the top 30% most reliable pairs matches full-data DPO, which indicates that reliability-aware selection can reduce training cost without sacrificing performance. At inference, selective prediction reaches 96.2% accuracy at 50% coverage in the true-agreement setting and 88.7% in the deployable predicted-agreement setting, both exceeding the 85.3% no-agreement baseline. These results suggest that accounting for annotation uncertainty is beneficial for both efficient training and reliable deployment in subjective classification.

---


### 9. [Thought-Aware KV Cache Compaction for Reasoning via Adaptive Attention Matching](https://arxiv.org/abs/2608.12331)

**<font color=#1a73e8>作者：</font>** Yang Liu, Bin Chong, Chongyang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models generate lengthy chain-of-thought (CoT) sequences whose key-value (KV) cache grows linearly and becomes a memory bottleneck during decoding. Existing compaction methods treat reasoning trajectories as flat token sequences and apply uniform compression, ignoring the hierarchical structure of CoT reasoning where different steps vary drastically in importance. We propose \textbf{Thought-Aware Attention Matching (TAM)}, which exploits this structure through three mechanisms: (i)~thought segmentation that decomposes the trajectory into reasoning blocks, (ii)~adaptive budget allocation that assigns compression budget based on each segment's importance and size, and (iii)~pivotal token protection that preserves high-attention reasoning anchors. We prove that the allocation rule is optimal under a convex error model and that cumulative error under sequential compaction remains bounded. Experiments on AIME 2024 and MATH-500 with Qwen3-4B show that TAM improves accuracy over uniform compaction at the same memory footprint, with periodic compaction bounding peak memory to 3.1--3.2\,GB (a 65\% reduction) while maintaining competitive accuracy.

---


### 10. [Vision-Language Models are Fragile Multilingual Associators](https://arxiv.org/abs/2608.12333)

**<font color=#1a73e8>作者：</font>** Ritabrata Chakraborty, Rajatsubhra Chakraborty, Shivakumara Palaiahnakote 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models must associate visual entities with textual attributes. Whether these associations or concept bindings remain stable when the language of the input changes is unexplored. We introduce M$^2$BIND, a benchmark varying the language of the context and query across multiple languages. We evaluate binding both extrinsically through task performance metrics and intrinsically through causal interventions. We find that binding is not language-invariant: cross-family and cross-script settings trigger significant binding collapse, with the model's internal binding computation shifting to later layers and losing causal strength. Closely related languages preserve associations comparatively better. In a broader sense, our findings indicate how VLMs deployed globally in multilingual settings cannot be assumed to maintain the same association quality observed in monolingual evaluation.

---


### 11. [Steering the Language Axis: From Linear Decodability to Causal Control](https://arxiv.org/abs/2608.12334)

**<font color=#1a73e8>作者：</font>** Arnav Srivastav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the impressive multilingual capabilities of Large Language Models, the latent dynamics dictating language selection remain poorly understood. In this work, we ask whether language identity is merely linearly decodable from hidden states, or if it can be causally controlled by a compact activation direction. We conduct an exhaustive causal intervention analysis across multiple model families, including Qwen 3.5-2B and Llama-3.2-1B-Instruct, isolating PCA-derived "language axes" to perform steering and ablation experiments across 1.26 million generations on the FLORES-200 dataset.
Steering along these geometric directions reliably forces language switching in both cross-script (English to Chinese) and same-script (English to Spanish) settings, whereas equal-magnitude random perturbations yield virtually no effect. Our layerwise analysis reveals that language commitment is highly localized and explicitly language-pair-dependent. While English to Chinese switching resists early intervention and steers easily in the later layers, the English-Spanish transition shifts earlier, displaying a distinct, bimodal sensitivity. Furthermore, targeted ablation uncovers a fundamental reversion to English: once the language signal is removed, the model falls back to English regardless of the input prompt. Ultimately, these findings demonstrate that language decision boundaries function during inference as causally active features that are direction-dependent and layer-specific.

---


### 12. [HC-RAG: Evidence-Centric Retrieval-Augmented Generation over Heterogeneous Financial Filings](https://arxiv.org/abs/2608.12335)

**<font color=#1a73e8>作者：</font>** Siyuan Chen, Huaye Tan, You Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial question answering over annual reports requires more than retrieving semantically similar passages. It often involves identifying relevant companies and fiscal years, locating standardized filing sections, collecting textual and tabular evidence, and checking answers against the original documents. Existing RAG systems, however, usually flatten long filings into unordered chunks, pay limited attention to the typed structure of financial reports, and use fixed text-table fusion strategies without considering query intent. To address these limitations, we propose \textbf{HC-RAG}, a hierarchical cross-modal retrieval-augmented generation framework for evidence-centric financial QA. HC-RAG organizes filings into a typed financial evidence graph with documents, sections, text units, table units, and metadata nodes. It retrieves evidence through document-section-unit paths, aligns textual and tabular evidence in a shared retrieval space, and routes evidence according to four semantic intents: calculation, trend, fact, and comparison. We further introduce \textbf{Multi-Doc-2025}, a benchmark containing 2,327 expert-verified QA pairs from 179 SEC 10-K filings of 87 S\&P 500 companies across fiscal years 2022--2024, with labels for intent, difficulty, and structural evidence attributes. Experiments on public financial QA benchmarks and Multi-Doc-2025 show that HC-RAG improves both answer quality and evidence localization, especially in long-document, table-related, and cross-document settings. HC-RAG outperforms RAPTOR by 6.6 F1 points on DocFinQA and GraphRAG by 10.9 F1 points on Multi-Doc-2025. Evidence-level analysis and ablation studies show that the improvements mainly come from more accurate section localization, table grounding, cross-document evidence aggregation, and intent-aware text-table routing.

---


### 13. [StorySpark: Module-wise Evolutionary Search for Story Premise Generation](https://arxiv.org/abs/2608.12336)

**<font color=#1a73e8>作者：</font>** Yang Yang, Zining Zhong, Qian Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A story premise is the creative spark from which a full narrative can grow. Yet LLM-based story generation has mostly emphasized later-stage planning, controllability, coherence, and prose expansion, while premise-level ideation remains comparatively underexplored. We introduce StorySpark, a module-wise evolutionary search framework for story premise generation. StorySpark operates over interpretable narrative modules such as background, persona, event, ending, and twist, treating each active module not as a static field to fill once, but as a local search space conditioned on the partial premise built so far. For each module, it generates alternatives, evaluates them in context, refines them through feedback-driven mutation and recombination, preserves complementary strengths with Pareto-guided selection, and reallocates frontier capacity to balance branch coverage with promising directions. Multi-view automatic and human evaluations show that StorySpark produces stronger final premises than competitive baselines, with especially consistent gains in originality; when expanded with the same story writer, its premises also lead to higher-quality downstream stories while maintaining completeness, fascination, and diverse usable narrative directions.

---


### 14. [Mimicry without understanding: the origins of decision bias in large language models](https://arxiv.org/abs/2608.12339)

**<font color=#1a73e8>作者：</font>** Eldad Yechiam, Adi Tarabeih  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language models (LLMs) were found to be susceptible to a host of social, affective, and cognitive biases. We examined two mechanisms through which such biases can be generated even when human preferences (in the training data) are not biased or when they are correctly categorized as being biased. The first is faulty mimicry of preferences based on human behavior: this involves LLMs inferring human preferences even when behaviors are logically unrelated to preferences. The second is mimicry of explicitly biased human behaviors. In four studies focusing on economic biases, we find that ChatGPT-4o and Qwen exhibited social proof biases even when prompted with reports of human behaviors that were clearly non-indicative of individuals' actual preferences. LLMs also displayed loss aversion when it was explicitly described as a bias. Indeed, when prompted with detailed scientific reports, the extent of the bias (i.e., loss aversion) in the scientific report predicted LLMs' own subsequent bias. Scientific papers of biases can thus become self-fulfilling prophecies, at least when it comes to LLMs' responses. The current study goes beyond fleshing out LLM biases and sheds light on the underlying component processes.

---


### 15. [Class-Structure Preservation Beats Diversity: A Comprehensive Benchmark of Text Augmentation Methods for Imbalanced Text Classification](https://arxiv.org/abs/2608.12340)

**<font color=#1a73e8>作者：</font>** Keito Inoshita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), generative data augmentation has attracted considerable attention for imbalanced text classification in natural language processing. However, no empirical benchmark to date has compared LLM-based augmentation against the embedding-space SMOTE-style retrieval (EmbSMOTE), a strong classical reference for imbalanced classification. In this study, a controlled benchmark of 11 augmentation methods, spanning classical perturbation, embedding-space retrieval, and LLM-based generation, is newly constructed on seven public text classification datasets covering class counts $K=2$-$28$ and imbalance ratios of 1.1 to over 500, evaluated with five random seeds per cell using macro F1, Welch's $t$-tests, five distributional metrics, and an LLM-family sensitivity analysis based on Qwen3-8B. The experimental results reveal that all LLM-based methods are statistically equivalent or inferior to EmbSMOTE, with the performance gap widening monotonically as imbalance increases and reaching $\Delta\text{F1}_\text{macro}\!\approx\!0.063$ on GoEmotions-28. Furthermore, it is observed that surface-level uniqueness has negligible correlation with downstream performance, whereas LLM-specific artifacts, such as text elongation and label-distribution uniformization, are negatively associated with classification accuracy. Compared with six LLM-based and four classical augmentation baselines, these results demonstrate that the effective variable is not surface-level diversity but class-conditional structural fidelity, namely the degree to which augmented samples preserve the class-conditioned geometry of the training distribution. Accordingly, retrieval-based oversampling should be adopted as the default for imbalanced multi-class classification, and a higher empirical bar should be required before LLM-based augmentation is deployed in practice.

---


### 16. [The "Knowledge-Behavior Gap" in Cultural Taboo Safety of Large Language Models](https://arxiv.org/abs/2608.12341)

**<font color=#1a73e8>作者：</font>** Ying He, Sihang Jiang, Xingzhou Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural taboo safety is essential for deploying large language models (LLMs), as culturally insensitive outputs may cause offense or even social harm. However, existing cultural benchmarks primarily assess cultural knowledge or values biases, while overlooking whether LLMs can recognize and respect cultural taboos, especially when taboos are implicitly hidden in seemingly harmless questions. Besides, cultural taboos are implicit, and context-dependent, thus poss unique challenges for reliable evaluation. To address these gaps, we introduce \textbf{CulShield}, the first public benchmark dedicated to evaluating and improving the cultural taboo safety of LLMs. CulShield spans 77 countries and territories, and includes over 2,020 taboos. It evaluates models along both explicit knowledge and implicit behaviors. Experiments on several advanced LLMs (e.g., GPT-4o-mini, Gemini-2.5-pro) reveal a clear ``knowledge-behavior gap'': models often fail to apply known taboos during interaction. We further show that variations in linguistic context can significantly affect LLMs' cultural taboo safety. Code and data is accessible here: this https URL.

---


### 17. [Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](https://arxiv.org/abs/2608.12342)

**<font color=#1a73e8>作者：</font>** Ying He, Zhouhong Gu, Zhecheng Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring the accuracy of financial documents is critical for economic analysis, regulatory compliance, and corporate decision-making. Several studies have shown that Large Language Models (LLMs) perform well in many financial tasks, such as stock price movements and financial analytics. However, a critical task remains unexplored: the ability of LLMs to identify errors in financial documents. In this paper, we introduce \textbf{FinED-Bench}, the first publicly \textbf{Bench}mark for \textbf{Fin}ancial \textbf{E}rror \textbf{D}etection across three levels of cognitive complexity. FinED-Bench covers nine real-world financial scenarios, and includes over 900 documents reported in 2025 that are unseen by existing language models. We detail the benchmark construction process and evaluate several advanced LLMs (e.g., GPT-4o, Qwen3-14B) on this tasks, which requires both financial domain knowledge and reasoning capabilities. Experimental results show that current LLMs still struggle with this task, especially in high-complexity cases. Besides, supervised fine-tuning can significantly improve the performance of weaker LLMs on this task. Our data and code are available at this https URL.

---


### 18. [Large Language Models Pass the History Exam But Miss the <<History>>: A Polish High School Exit Exam Matura Benchmark](https://arxiv.org/abs/2608.12343)

**<font color=#1a73e8>作者：</font>** Adrian Trzoss, Kacper Dudzic, Wiktor Werner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI chatbots are widely used by students as knowledge sources, yet LLM benchmarks rarely assess interpretative historical reasoning. We evaluate eight leading LLMs on the Polish high school exit exams (Matura) in history - three official papers from 2023-2025, comprising short-answer questions and extended essays - comparing model performance against the human examinee population. Every model dramatically outperforms human examinees, yet aggregate scores mask distinct competency profiles: rankings are unstable across task type, source modality, and geographical scope, with a consistent penalty on Polish versus Global history content. Qualitative error analysis reveals two recurring failure modes - source conflation, in which models reason from source content rather than treating it as an object of analysis, and temporal disorientation, in which responses are historically misplaced. This study introduces the first LLM history benchmark grounded in Polish national curriculum.

---


### 19. [Predicting consumer-technology ownership without a diffusion history](https://arxiv.org/abs/2608.12344)

**<font color=#1a73e8>作者：</font>** Irina Vartanova, Niels Selling, Jennifer Viberg Johansson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We test whether the perceived attributes of a consumer technology predict how widely it is owned. In a 2022 Prolific survey of US adults (n = 678), respondents rated 65 consumer technologies on six attributes. We then elicited the same ratings from two frontier language models, Anthropic Claude Opus 4.7 and OpenAI GPT-5.5. We regress ownership prevalence on four UTAUT2 acceptance attributes plus a log-age covariate with a sign-constrained penalized regression and evaluate it by holding out one technology at a time. The attribute model improves on a baseline of years-since-launch: mean absolute error falls by 17% with the human ratings, and by more with either model, most with Opus 4.7. Over the short 2022-to-2025 window, where ownership moved little, the same attributes do not improve on a no-change baseline. We set out the limitations of the approach, including the possibility that language-model ratings reflect prior knowledge of these technologies rather than independent attribute reasoning. We include a deployment illustration: 2027 ownership predictions for eleven products launched in 2025 and 2026.

---


### 20. [Diagnostic Foundation for Evaluating LLMs' Research Integrity as Co-Scientists](https://arxiv.org/abs/2608.12345)

**<font color=#1a73e8>作者：</font>** Yash Tripathi, Silu Sharma, Sai Sidhanth Manoharan Jayanthi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly deployed as co-scientists, yet their ability to uphold research integrity under institutional pressure remains unmeasured. We introduce IntegrityBench, a benchmark evaluating misconduct classification, ethical action reasoning and artifact-grounded decision making across 36 paired tasks under a 5-level implicit-explicit pressure protocol spanning 3 domains and 4 research stages. Evaluating 18 frontier model variants, we find that under peak pressure, models fail roughly 1 in 3 integrity-critical decisions, and neither scale nor reasoning ability reliably mitigates this. Explicit pressures induce compliance with misconduct, while implicit contextual reframing more often causes over-refusal of legitimate research tasks. Interestingly, models failing to classify research requests accurately perform equally or better on artifact-grounded decision making (85.7 vs. 79.4), suggesting the three facets are structurally dissociated and correct ethical action does not require accurate classification. Frontier models can thus appear helpful while harbouring integrity failures that create two distinct deployment risks: facilitating research misconduct and eroding trust in AI-assisted research.

---


### 21. [Humans are Missing from AI Coding Agent Research](https://arxiv.org/abs/2608.12355)

**<font color=#1a73e8>作者：</font>** Zora Z. Wang, John Yang, Kilian Lieret 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent progress in AI coding agent research has led to rapid improvements in agents' ability to autonomously perform complex software engineering tasks, from editing large codebases to executing long-horizon development workflows. As these systems make strides, however, the primary bottleneck to practical usefulness increasingly shifts away from pure task-solving capability, and toward challenges in how users communicate with, supervise, and trust agents. In this position paper, we argue for a reorientation from autonomous to human-centered coding agents: systems designed not only to complete tasks, but to collaborate effectively with people. We identify four core interaction-level dimensions that characterize the human-agent task-solving loop: task alignment, verifiability, steerability, and adaptability. Finally, we outline concrete research directions to advance these dimensions, including user-involved coding environments, comprehensive verification mechanisms, and principled measures of human-agent interaction quality.

---


### 22. [New Terms, New Toxicity: Consensus-based Chinese Neologism Toxicity Detection via Search-Augmented LLMs](https://arxiv.org/abs/2608.12361)

**<font color=#1a73e8>作者：</font>** Shiyao Cui, QingLin Zhang, Di Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neologisms, emerging terms in meaning or form, can serve as new vehicles for toxic expression, like "country girl" as a stigmatizing label targeting feminism. Such toxic neologisms appear benign but have evolved into toxic usage in public consensus, posing challenges to moderation systems and remaining underexplored. In this paper, we investigate how to detect implicit toxicity expressed via neologisms. We first propose a taxonomy that captures the origins and consensus-verification criteria of toxic neologisms, followed by the construction of a lexicon spanning widely observed risk categories. To capture toxicity grounded in public consensus, we introduce SeTox, a search-augmented framework that enables static large language models (LLMs) to incorporate real-time web context for neologism toxicity detection. Experiments show that SeTox, even with 3B-scale models, outperforms recent large-scale models, demonstrating its scalability to incorporate real-world knowledge for toxic neologism detection. Disclaimer: this paper has offensive contents that may be disturbing to some readers.

---


### 23. [Agreement Is Not Alignment: Divergent Moral Grounds in Human and LLM Ethical Judgments](https://arxiv.org/abs/2608.12368)

**<font color=#1a73e8>作者：</font>** Octavian M. Machidon, Alina L. Machidon, Vojko Strahovnik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agreement with human judgments is a common proxy for evaluating the alignment of large language models (LLMs). Yet agreement in final labels does not show that human annotators and models rely on the same moral grounds. Two agents may reach the same judgment while appealing to different principles, contextual assumptions, or interpretations of the situation.
We test this distinction using a curated 500-item ETHICS-derived benchmark spanning five domains of moral judgment, with new human annotator and LLM annotations of both final labels and supporting rationales. Across frontier and open model families, agreement with human annotator majority labels is often high. However, rationale-level analysis reveals systematic divergence in the moral grounds expressed by human annotators and models. In particular, models redistribute attention across categories such as harm, respect, promise-keeping, justice, desert, and excuse relevance, even when their final labels match the human annotator majority.
Our results show that agreement should not be treated as equivalent to alignment. Label-based evaluation can therefore be misleadingly reassuring unless complemented by analysis of the reasons, principles, and moral priorities expressed in model judgments.

---


### 24. [Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing](https://arxiv.org/abs/2608.12371)

**<font color=#1a73e8>作者：</font>** Sabeur Lajili, Zaki Brahmi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stream-processing systems increasingly operate across heterogeneous mobile edge--cloud infrastructures, where workload volatility, resource contention, and stringent quality-of-service (QoS) requirements complicate decentralized scheduling. This paper proposes \emph{MAS-DecStream}, whose main contribution is \emph{LLM-MR-CNP}: an extension of the classical Contract Net Protocol with semantic CFP formulation, progressive context disclosure, multi-round proposal revision, negotiation memory, and deterministic validation. Edge-cluster agents refine natural-language offloading proposals from local observations, predicted resource states, and qualitative runtime context, while hard resource and QoS constraints remain deterministic. Experiments derived from the Alibaba ASI Trace evaluate the extension at three levels: single- versus multi-round CNP, rule-based versus LLM-assisted refinement, and fixed-model single- versus multi-round negotiation. Under the evaluated configurations, MAS-DecStream reduces latency violations to 3\%, eliminates resource overcommitment, reaches a conflict-resolution rate of 0.91 with 20 agents, and improves utility by up to 22\% over the multi-round rule-based baseline. A separate 25-case evaluation shows model- and prompt-dependent accuracy--cost trade-offs. The results provide initial evidence that multi-round CNP refinement is the principal protocol-level gain, with LLM assistance adding value for qualitative and uncertain runtime context.

---


### 25. [Are you Talking Logic to Me? Assessing Language Models Syllogistic Reasoning Capabilities](https://arxiv.org/abs/2608.12374)

**<font color=#1a73e8>作者：</font>** Hanna Abi Akl, Fabien Gandon, Catherine Faron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) struggle with logical tasks like reasoning on syllogisms. It has been shown that Knowledge Representation (KR) plays a crucial role in expressing input information to help models solve tasks. This observation motivates our study of the impact of different formal KR notations on syllogistic reasoning by extending the FOLIO and P-FOLIO datasets. Our experiments on Small Language Models (SLMs) in Supervised Fine-Tuning (SFT) and Zero-Shot (ZS) settings show that the choice of input notation can yield performances competitive with natural language while enabling faster inference. We also propose a syllogistic categorization method (SEF) and use it to enrich ZS prompts with logical definitions, which boost reasoning in small models. We open-source our framework, Common Logic Grammar Construction (CLGC), as the first Python library for automatically generating syllogisms in KR notations and defining their SEF categories.

---


### 26. [Dual-Flow Transformers: Decoupling the Primary Prefill Path from Additional Decode Computation](https://arxiv.org/abs/2608.12385)

**<font color=#1a73e8>作者：</font>** Liming Liu, Mingze Wang, Tuo Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models serve more requests, cumulative inference cost is becoming increasingly important relative to one-time training cost. The two inference phases stress hardware differently: prompt prefill is parallel and typically compute-bound, whereas autoregressive decode is sequential and often memory-bandwidth-bound. Conventional width or depth scaling increases both costs together because every added layer is evaluated in both phases. We ask whether additional learned computation can instead be allocated to continuation prediction while preserving the prompt-wide primary computation and a single persistent key-value (KV) cache. We introduce the Dual-Flow Transformer. Its primary flow is a complete causal language model that processes the prompt and writes the KV cache. The auxiliary flow is omitted during prompt processing and activated only from the final prompt position onward, adding continuation-prediction computation without writing persistent state or influencing the primary flow. The two flows share major attention, MLP, and output matrices, while using separate token embeddings and lightweight coupling. Sharing weights and the primary cache also creates opportunities to reuse loaded weights and cached keys and values during grouped execution. Across matched-token comparisons, Dual-Flow achieves lower validation loss across architectures and data configurations. In MoE models, the separation makes primary and auxiliary expert fan-outs independent controls over prompt cost, continuation cost, and predictive quality. We study two regimes: increasing decode computation at fixed prefill expert computation, and reallocating a fixed decode expert budget between the two flows. These experiments expose a prefill-decode-quality trade-off and demonstrate the potential of phase-specific expert allocation.

---


### 27. [Query Timing Produces Opposite Positional Biases Between LLMs and Humans](https://arxiv.org/abs/2608.12387)

**<font color=#1a73e8>作者：</font>** Jasin Cekinmez, Addison J. Wu, Thomas L. Griffiths  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Positional biases such as recency and primacy effects have been documented in large language models (LLMs), yet the underlying mechanism by which these models make their evaluations remains poorly understood. Both primacy and recency biases have been observed in human judgments in response to evidence, but recent work suggest that \emph{when} the listener updates their beliefs -- during the presentation of evidence or only at the end -- influences the presence of such effects. We investigate whether a similar phenomenon holds for LLMs, finding divergence from human behavior. These biases are more exacerbated in newer models compared to their predecessors.

---


### 28. [Learning to Adapt Cross-Domain Preferences via Meta-LoRA for LLM Personalization](https://arxiv.org/abs/2608.12389)

**<font color=#1a73e8>作者：</font>** Xuefei Wang, Jun Han, Zixuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-domain zero- or few-shot personalization aims to generate user-preferred responses in unseen conversational domains from only a handful of target-domain interactions. Existing adaptation methods struggle to calibrate update magnitude under sparse evidence and thus overfit, whereas history-transfer methods often entangle user preferences with source-domain artifacts, yielding unreliable personalization priors and negative transfer. To calibrate adaptation to evidence quality, we propose PAC-Bayes-regularized Meta-LoRA, which uses a meta-learned LoRA initialization as both the adaptation start and prior center, while adjusting update strength according to support-set size and predictive uncertainty. This limits overfitting under sparse or ambiguous evidence while permitting stronger personalization as evidence grows. Controlled adaptation alone does not determine which preferences should transfer across domains or how they should be expressed. We therefore functionally decompose personalization priors into user and domain components, using a human-readable prompt for stable preferences and topology-preserving soft tokens for domain-specific hidden-space conditioning. Experiments across multiple benchmarks and personalization tasks show consistent gains over strong baselines. On HiCUPID, our method reduces cross-domain win-rate degradation by 47.9% relative to the best competing baseline and improves win rate by 110.2% under unseen-user cold start.

---


### 29. [Unified Multi-Dimensional Benchmark for Complex Graph Reasoning in Large Language Models](https://arxiv.org/abs/2608.12391)

**<font color=#1a73e8>作者：</font>** Fali Wang, Ali Al-Lawati, Iliyas Bektas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph reasoning provides a promising testbed for evaluating the reasoning ability of large language models (LLMs), as graph instances can be programmatically generated, structurally controlled, and naturally scaled to long-input settings. However, existing graph reasoning benchmarks have limited coverage of data complexity, rely heavily on manual construction, and lack unified evaluation across text-based and code-based reasoning modes. To address these limitations, we propose {\dataset}, a five-stage \textit{semi-automatic} framework for constructing complex graph reasoning benchmarks. It expands benchmark coverage along five dimensions: \textit{Graph Size}, \textit{Task Complexity}, \textit{Task Description}, \textit{Graph Loading}, and \textit{Task Source}. The framework uses an LLM-based data generator to automatically produce task descriptions, graph data, reference solutions, graph-loading scripts, question forms, and evaluation scripts, while retaining human validation at key quality-control stages. Based on it, we construct a benchmark with $202$ tasks and evaluate LLMs under text-based, code-based, and augmented reasoning settings. Experiments show that the complexity dimensions reveal model limitations that are less visible in existing benchmarks; existing fine-tuned models struggle to generalize to GraphGym, whereas retrieval-augmented methods show scenario-dependent adaptability, improving textual reasoning but not consistently improving coding reasoning. These findings suggest that ours serves as a challenging and diagnostic benchmark for graph reasoning and provides empirical guidance for future enhancement methods. Code and dataset will be published soon.

---


### 30. [Research Assistant: AstraZeneca's Agentic System for R&D](https://arxiv.org/abs/2608.12395)

**<font color=#1a73e8>作者：</font>** Piotr Grabowski, Mohamed Alameen, Jorge Bretones 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe Research Assistant, an internal LLM-based system developed at AstraZeneca to help scientists and clinicians explore biomedical questions across a broad range of data sources. The system provides a chat-style interface that brings together evidence from scientific literature, knowledge graphs, chemistry, clinical trials, safety resources, expression data, and internal experimental systems. It supports both a fast mode for direct question answering and a multi-step mode for more complex research tasks. Responses are grounded in retrieved evidence and linked back to the original sources, allowing users to review and further explore the underlying data. In this technical note, we outline the system architecture, the main design choices behind the product, and lessons learned from deploying it at scale to support day-to-day R&D workflows across AstraZeneca.

---


### 31. [LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining](https://arxiv.org/abs/2608.12419)

**<font color=#1a73e8>作者：</font>** Qiuwu Chen, Zimo Liu, Yuchen Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable breakthroughs across various applications. However, their architectures remain inefficient in pretraining due to two main limitations: (i) self-attention lacks an explicit inductive bias for locality, leading to redundant modeling of sequence-internal local information; (ii) mixture-of-experts (MoE) implicitly couples knowledge storage with computational pathways, hindering flexible access to sequence-external global knowledge. To overcome these limitations, we propose LoKiFormer, a novel LLM architecture that augments the standard decoder with two dedicated modules: 1) Local Fusion Attention (LFA), which incorporates a convolutional fusion to attention, explicitly capturing local patterns and allowing the attention to operate on more informative representations; 2) Knowledge Memory Module (KMM), which introduces a parametric key-value memory that explicitly stores global knowledge in addressable slots, decoupling storage from computation and enabling direct knowledge retrieval. Together, these modules enable LoKiFormer to achieve more efficient and effective integration of information at both levels. Experimental results show that LoKiFormer converges 1.33x faster in pre-training than baseline models, underscoring its superiority over existing LLM architectures.

---


### 32. [Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction](https://arxiv.org/abs/2608.12426)

**<font color=#1a73e8>作者：</font>** Mariya I. Vasileva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in settings that require simultaneous adherence to multiple explicit constraints - reasoning structure, safety boundaries, output schemas. Individual constraints are handled proficiently, but the compositional regime, where many must hold jointly, remains poorly characterized: how rapidly does performance degrade, what governs the degradation, and can the collapse be mitigated? We introduce Constraint Saturation Evaluation (CSE), a procedurally generated benchmark that systematically varies the number of simultaneous constraints (k), with every constraint scored by a deterministic, rule-based verifier and zero LLM-judge involvement: 15 models, 36 constraint types, 369,753 checks at k=1-12. Three findings emerge. First, per-constraint pass rate decays gradually and predictably, while the chance of satisfying all k constraints collapses - a model passing individual constraints at ~41% at k=8 succeeds on all eight just 5.7% of the time. Second, constraints do not degrade equally: structural constraints lose 2x more baseline capability per added constraint than lexical ones, ordered by a comprehension-maintenance gap that separates constraints requiring sustained tracking from binary decisions immune to composition. Third, failures are nearly independent, which is what makes the accumulation multiplicative; the residual coupling that does exist tracks shared output features rather than pairwise interference - a wrong sentence count fails every constraint that reads it. Reliable instruction following breaks down beyond 5-6 simultaneous constraints: probe-level success falls below 50% at 7 constraints for the strongest model, and at 3 or fewer for 12 of 15.

---


### 33. [Non-Degenerate Risk Certification for Automated Security Decisions: A Decision-Contract Theory with ATT\&CK-Aligned Triage as a Worked Instance](https://arxiv.org/abs/2608.12444)

**<font color=#1a73e8>作者：</font>** Zhenpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An unconditional risk bound on automated decisions can be satisfied without automating anything, since a selector that never acts drives the bound to zero. We show this is structural: any risk certificate is defined over a decision contract, the inputs a system acts on plus the semantic relation under which an output counts correct, and weakening either hides base-classifier error. We develop a decision-contract theory: an error-conservation law showing error is only reassigned among harmful automation, human deferral, and semantic masking; a label-free singleton capacity certifying structural incapacity, with a risk-feasible refinement separating recoverable threshold misalignment from risk-constrained incapacity; and a non-degenerate actionability certificate excluding all-abstain solutions by construction. We instantiate this on ATT\&CK-aligned alert triage for LLM-based intrusion detection, the setting that exposed the vacuity failure. Across 3 IDS datasets, 6 LLMs, and 4 error-rate thresholds, empirical false-attribution risk stays at or below target in 90.3% of configurations, with 83.4% mean correct automation. The capacity diagnostic explains every low-utility configuration; its refinement separates genuine misalignment from risk-constrained incapacity, confirmed by an exhibited alternative threshold; a training-stability re-run finds no confirmed structural-incapacity instance; and real fine-grained attack-subtype labels confirm the coarsening-transfer identity under a genuine many-to-one map, with small but non-zero masking mass.

---


### 34. [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](https://arxiv.org/abs/2608.12476)

**<font color=#1a73e8>作者：</font>** Guodong Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head.
On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches.
These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

---


### 35. [DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution](https://arxiv.org/abs/2608.12486)

**<font color=#1a73e8>作者：</font>** Siheng Xiong, Ali Payani, Oguzhan Gungordu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) cannot retain post-deployment experience without parameter updates. We introduce DIVE, a diversity-driven framework that enables frozen LLMs to improve by evolving persistent natural-language skills from task experience and verifier feedback. These skills encode reusable reasoning procedures, verification strategies, common failure modes, and output constraints and are both executed and revised by the same underlying model without access to a teacher model. Since natural-language skill evolution is a stochastic, non-convex search process, optimizing a single skill trajectory can overfit to sampled experience or converge to a suboptimal solution. DIVE mitigates this optimization variance by independently evolving multiple skill populations from bootstrapped experience, adaptively refining them through diverse transformations, and jointly selecting a complementary set of skills. Across six mathematical and logical reasoning tasks and multiple model families, DIVE consistently outperforms existing reasoning methods, prompt-optimization approaches, skill-development frameworks, and memory-based baselines. It achieves rapid self-improvement from accumulated experience, obtaining substantially larger performance gains with fewer rollouts than parameter-based methods such as SFT and GRPO, and prompt optimization with GEPA. Further, the resulting skills transfer across model scales and families, enabling smaller models such as GPT-5-nano to match or outperform larger counterparts, i.e., GPT-5, under conventional prompting. These results establish diversity-driven skill evolution as an effective, interpretable, and parameter-free approach to LLM self-improvement.

---


### 36. [SoK: From Generation to Consumption of Privacy Documents in Software Systems](https://arxiv.org/abs/2608.12511)

**<font color=#1a73e8>作者：</font>** Shidong Pan, Clark LaChance, Zhen Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy documents (e.g., privacy policies) are a central mechanism through which digital services disclose data practices and seek user consent. Over the past decades, research on privacy documents has expanded significantly, encompassing not only traditional privacy policies but also short notices (e.g., privacy labels) and interface-level transparency mechanisms. As this research area continues to grow, it has become increasingly difficult to obtain a coherent view of how privacy documents are created, analyzed, evaluated, and maintained across their lifecycle. This SoK provides a unified, lifecycle-oriented view of privacy documents from a software engineering perspective. We systematically review and analyze 290 papers published between 2010 and 2025, organizing them around five research questions that examine how privacy documents are (1) defined and scoped, (2) generated, (3) analyzed and extracted, (4) checked for inconsistencies and noncompliance, and (5) evaluated and improved for usability. Building on our findings, we identify 15 key research trends and 21 open opportunities. We further chart four broader research directions that highlight (i) emerging challenges in AI-centric platforms, (ii) the need for diverse and up-to-date data foundations, (iii) LLM-based unified policy-code analysis, and (iv) dual usability for end-users and developers. We hope this SoK provides a shared foundation for future research on privacy policies and privacy documents.

---


### 37. [Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?](https://arxiv.org/abs/2608.12515)

**<font color=#1a73e8>作者：</font>** Vladyslava Rudas, Dmytro Kuzmenko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning. We evaluate three opensource vision-language models (VLMs) (\textit{InternVL}, \textit{Qwen-VL}, and \textit{SmolVLM}) on the classification of egocentric robot images into four danger levels, comparing three prompting strategies and two rounds of QLoRA fine-tuning against a stratified random baseline. Without fine-tuning, all models perform near the baseline, while fine-tuning yields only modest overall improvements. However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models. An analysis of person localization further shows that correct danger classification does not correspond to better spatial grounding, indicating that a model may produce a useful safety label without attending to the relevant region of the scene. These results show that current VLMs remain limited in fine-grained proxemic reasoning and spatial grounding, although targeted prompting and fine-tuning can improve high-danger detection in selected models.

---


### 38. [$\varepsilon$-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution](https://arxiv.org/abs/2608.12522)

**<font color=#1a73e8>作者：</font>** Aofan Liu, Shiyuan Song, Yiyan Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based program evolution systems such as FunSearch and AlphaEvolve have shown strong ability to discover novel algorithms, but typically optimize each task in isolation, discarding search experience after completion. We introduce $\varepsilon$-MemEvo, a framework for cross-task knowledge transfer in LLM program evolution. $\varepsilon$-MemEvo stores prior experience as task-agnostic tactic memories: compact natural-language summaries of successful algorithmic strategies rather than raw code, enabling transfer across tasks with different APIs and evaluators. To avoid negative transfer from semantically mismatched memories, $\varepsilon$-MemEvo uses an adaptive injection gate that decides whether retrieved memories should be injected, and at what intensity. We evaluate $\varepsilon$-MemEvo on 8 diverse optimization benchmarks spanning mathematical optimization and systems engineering, using a content-level Leave-One-Out protocol that excludes target-task memory entries. On the primary GPT-5 backbone, $\varepsilon$-MemEvo improves AUCC over AdaEvolve on all 8 tasks, with a mean relative gain of +8.7%, and improves early-stage convergence by +9.4% on average. Ablations show that naive memory injection can fail catastrophically, while adaptive gating remains safe across all five ablation tasks. The data-updated posterior is interpretable in observed states: it favors skip during improving search and shifts from skip to hint across early and late plateaus. These gains incur less than 1% computational overhead.

---


### 39. [Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games](https://arxiv.org/abs/2608.12547)

**<font color=#1a73e8>作者：</font>** Deborah Sinishaw, Qile Zhu, Edwin Meriaux 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model agents deployed without a central controller are often assumed to require communication to coordinate their actions. We ask what remains possible without it: when independent instances of the same model cannot communicate, can they still reason about their counterparts well enough to exceed the standard game-theoretic baseline for uncoordinated play? We introduce a benchmark of one-shot, no-communication games in which each of thirteen language models is told only that its counterparts are running the same model and is evaluated against the Nash equilibrium of the underlying game. In two-player matrix games spanning seven archetypes and two to ten actions per player, two frontier-hosted models consistently exceed their Nash benchmark, approaching the optimal joint outcome in several archetypes, while most open-weight models achieve only partial gains that vary sharply by game structure. Performance degrades substantially in team-based games with four or more interchangeable agents, particularly as the action space grows, suggesting that whatever capability drives self-play gains in dyadic games does not transfer to larger multi-agent teams.

---


### 40. [StrAD: A Streaming Method and Benchmark for Audio Description Generation for Long-form Videos](https://arxiv.org/abs/2608.12549)

**<font color=#1a73e8>作者：</font>** Julian Spravil, Sebastian Houben, Sven Behnke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual content is the dominant medium of communication, yet without audio descriptions (ADs), it remains inaccessible to blind and low-vision people. ADs narrate context-relevant visual events during natural audio pauses. Manually creating ADs is expensive, limiting coverage to a small fraction of available content. Most existing automatic AD generation methods frame the task as video clip captioning, requiring ground-truth timestamps and additional context cues such as character databases. Current benchmarks reinforce this framing, consisting of short video segments paired with automatic or task-mismatched annotations. We introduce StrAD, a benchmark for long-form AD generation on full-length videos spanning diverse genres such as movies, documentaries, short films, performances, and video games. We reformulate AD generation as streaming dense video captioning. Our approach processes full-length videos with a sliding window, inserting ADs into existing transcripts without ground-truth timestamps, and supports both fine-tuned models and zero-shot prompting of vision-language models. On the segment-level task with given timestamps, our fine-tuned StrAD-FT sets the state of the art on CMD-AD with 36.3 CIDEr (+10.0 over Shot-by-shot), establishes a reference point on StrAD (51.0 CIDEr), and remains competitive on MAD-Eval at 24.9 CIDEr. On the full-video streaming task, StrAD-FT reaches a SODA score of 2.4 against 1.1 for our zero-shot baseline StrAD-Zero, though both exhibit limitations in temporal localization and narrative coherence. While prior work has tackled full-video AD generation in an offline, multi-stage fashion, ours is the first streaming approach, generating ADs on the fly without ground-truth timestamps. StrAD makes progress on full-video AD generation measurable, a prerequisite for scaling accessibility.

---


### 41. [Scaling Automatic Research Agents via World Models](https://arxiv.org/abs/2608.12564)

**<font color=#1a73e8>作者：</font>** Xiyuan Yang, Sheikh Sarwar, Jingru Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment execution) scale in very different manners, since all generation shares compute through batching, while each execution occupies its exclusive sandbox and real machine time. As a result, the environment execution dominates the training cost and becomes the bottleneck as trajectories grow. To resolve this tension, we propose World Model RL (WMRL), which replaces environment execution with a world model to remove this bottleneck. Additionally, the world model can be imperfect, as its rewards are corrupted by bias and noise. Therefore, we further equip WMRL with two mitigations, Online Debiasing and Inverse-Variance Denoising, which offset the bias and suppress the noise respectively. Theoretically, we prove that both mitigations of WMRL strictly improve the convergence guarantee. Empirically, WMRL accelerates training by 3-4x on various tasks at different agent scales, while exceeding the performance of standard RL baselines. Moreover, our post-trained 4B and 9B agents outperform much larger open-weight agents of 48B and 120B on held-out benchmarks. Beyond AutoResearch, WMRL also transfers to post-training embodied VLA policies, which demonstrates the generalizability of our method.

---


### 42. [Trie Automata for Constrained Decoding over Large Finite Sets](https://arxiv.org/abs/2608.12574)

**<font color=#1a73e8>作者：</font>** Xingzi Xu, Karim Bouyarmane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly need to generate structured outputs that conform to predefined schemas, with one common constraint being selection from a finite set of valid strings. Current constrained decoding systems handle this through general-purpose grammar compilation, which becomes prohibitively slow as the number of valid values grows into the thousands, a cardinality wall. We introduce the trie automaton, a specialized mechanism that exploits finite-set structure (shared prefixes, bounded depth, known cardinality) via Aho-Corasick multi-pattern matching to precompute per-node token masks. The trie achieves 7X faster per-step valid-token computation (0.65 us vs. 5.8 us) compared to XGrammar, one of the primary backends in vLLM and SGLang, and 2--6.5X faster compilation at K >= 300. Because precomputed masks enable a stateless serving path that bypasses the guided decoding pipeline, this advantage compounds in batch serving: end-to-end vLLM throughput reaches 219 req/s vs. XGrammar's 7.5 req/s at batch size 256 (29X). The 29X combines the algorithmic speedup with integration-path savings that only precomputed masks can unlock. Across seven tokenizer families (32K--262K vocabulary), the trie maintains sub-100ms compilation up to K = 10,000 and flat per-step cost regardless of set size, while guaranteeing 100% output validity.

---


### 43. [Not All Nudges Land: Behavioral Controllability and Elaboration Quality in AI-Supported Journaling](https://arxiv.org/abs/2608.12582)

**<font color=#1a73e8>作者：</font>** Nadia Mehjabin, Henry Kautz, Subigya Nepal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI journaling tools can tailor prompts to a person's own sensed behavior, but it is unclear which behaviors respond to them. We analyzed 369 journal entries from an eight-week passive sensing study. An LLM labeled each entry as expressing an intention to change a behavior or not, and we measured follow-through against 26 sensor features with a 3-day before/after comparison. Responsiveness depended most on whether a behavior involves other people. Behaviors that depend on others improved in only 15 to 22% of cases, while behaviors a person can act on alone improved more often, up to 50 to 63%, though unevenly. How users wrote mattered less. No single text feature separated improved from unimproved entries; writing carried signal only within specific behaviors, most clearly for text messaging and for longer, more personal intention entries. The sample is small, so we treat these as exploratory patterns that point to where AI journaling nudges are most likely to work.

---


### 44. [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](https://arxiv.org/abs/2608.12585)

**<font color=#1a73e8>作者：</font>** Congchao Wang, Diwakar Singh, Qiaozi Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving reasoning LLMs requires the ability to judge the quality of long reasoning traces for effective reasoning data curation, strong training signals during reinforcement learning, and an in-depth understanding of reasoning behaviors during model performance evaluation. Additionally, surfacing reasoning mistakes that the model makes would enable improving the model's performance at runtime through providing feedback. Due to the difficulty of this complex task on long reasoning traces, single-model judges (even frontier models) do not do well at identifying reasoning defects. Additionally, leveraging frontier models during online training of reasoning LLMs is generally prohibited due to guardrails in terms of use. In this work, we introduce Reasoning Jury, a system that replaces the single judge with a jury of LLMs and a moderated consensus mechanism, to improve the fidelity of judgments for identifying reasoning defects. In reasoning jury, defects of a reasoning trace and their severity are surfaced through a deliberation where a moderator conducts a discussion amongst the jury where the jurors critique each other's judgments and get to modify their initial votes. The moderator derives a consensus through deliberation amongst jurors or consolidation of judgements. We show that Reasoning Jury with a jury of open-weight models (e.g., gpt-oss-120b) is able to significantly outperform frontier models (opus-4.6, sonnet-4.6, and gemini-3.1-pro) at correctly identifying reasoning defects. Besides accuracy performance improvements, the aggregated cost of the jury (initial verdicts, deliberations, consolidation, etc.) is a fraction (8 to 15%) of the cost of running frontier models in LLM-as-a-judge setup. We also show how these judgements can be leveraged to understand failure modes of reasoning LLMs on benchmarks, which allows much deeper understanding of a model's performance.

---


### 45. [Auditable agentic AI for evidence-grounded thyroid ultrasound diagnosis and reporting](https://arxiv.org/abs/2608.12590)

**<font color=#1a73e8>作者：</font>** Haifan Gong, Shiyu Chen, Bodong Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Thyroid ultrasound diagnosis requires coordinated lesion localization, measurement, risk stratification and reporting, yet most AI systems address these tasks in isolation and provide limited support for clinical review. We present ThyroidXAgent, a clinician-interactive agentic AI system that coordinates specialized diagnostic tools and stores their outputs as an auditable case-level evidence record. The system was developed using OpenThyroidDB, a multicentre, multitask resource integrating approximately 0.3 million ultrasound images and 24,000 paired reports, and was evaluated on 28,458 non-overlapping test cases, including 8,721 cases from 35 centres in the private NHC-MISD-TUS cohort. Across heterogeneous datasets, ThyroidXAgent achieved a mean Dice score of 87.21 percent for nodule segmentation and a mean AUROC of 0.9466 for benign-malignant classification. The same workflow supported lymph-node metastasis prediction and follicular versus papillary thyroid carcinoma classification, with AUROCs of 0.864 and 0.805, respectively. For report generation, evidence-grounded assembly outperformed multimodal language-model baselines across three cohorts. ThyClinScore, a lesion-level clinical semantic metric introduced here, showed the strongest correlation with a location-aware language-model judge. ThyroidXAgent improved physician classification accuracy, increased report diagnostic consistency from 70.3 percent to 86.2 percent, and reduced segmentation and reporting time by 35.9 percent and 27.4 percent, respectively. These findings support auditable, clinician-correctable agentic AI for thyroid ultrasound diagnosis and reporting.

---


### 46. [Predicting When Random Low-Dimensional Reparameterizations Train Neural Networks](https://arxiv.org/abs/2608.12597)

**<font color=#1a73e8>作者：</font>** Andrew Cheng, Ali Eslamian, Jie Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks can often be trained or fine-tuned through random low-dimensional reparameterization, where a small latent vector is mapped into a full parameter update by a frozen random map. This raises a practical question: how large must the latent search space be to reach a low-loss region? We first express the known accessibility transition in an equivalent conic form, centered for compact convex targets at the statistical dimension of the polar cone. Our main theoretical contribution is an orientation-resolved quadratic master formula that predicts the random-slice residual from both the curvature spectrum and the reference-to-solution displacement profile. It yields a self-consistent isotropic-orientation predictor and, in a conservative radius-only specialization, recovers the earlier Gaussian-width quadratic bound. Building on this analysis, we introduce Random Mapping Networks (RaMaN), which instantiate the predicted latent dimension using structured Hadamard or seed-regenerated Gaussian maps. These constructions avoid the O(dP) storage of dense random maps and reduce optimizer-state memory from O(P) to O(d). We also develop matrix-free curvature approximations and sweep-free dimension selection. Across controlled quadratic and neural-curvature experiments, the orientation-resolved predictor closely tracks measured transition locations and outperforms orientation-agnostic approximations when displacement direction matters. End-to-end experiments further show sharp, protocol-dependent training transitions across image and language models.

---


### 47. [Dead text or binding clause? Measuring and restoring constraint influence in black-box LLM dialogues](https://arxiv.org/abs/2608.12599)

**<font color=#1a73e8>作者：</font>** Haoyuan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-turn dialogues let users revoke constraints as easily as impose them, but revocation does not reliably take effect: models keep enacting withdrawn requirements (occasionally beneath comments asserting their removal), a failure we call \emph{behavioral relapse}, or revocation inertia. No existing instrument measures this influence per clause, predicts it before delivery, or repairs it under matched budgets. \sysname{} closes the three gaps through the model API alone: a contract ledger pairs every constraint with an executable checker, records revocations as tombstones, and compiles the net constraint state ahead of time into a single specification; a sequential ablation probe measures per-clause adherence and incremental behavioral effect; a repair ladder operates under token- and attempt-matched budgets. On \dataname{} (\NTasks{} HumanEval tasks, \NClauses{} verified checkers), relapse at an 8B operating point climbs from \ScaleDelayedMTwo{} to \ScaleDelayedMEight{} as constraint load grows, while stronger models sit at floor. Under matched checkers, model, and budget, ahead-of-time compilation significantly reduces relapse against a no-ledger verifier-retry baseline (\RestoreDiff{}, 95\% CI \RestoreDiffCI{}, $p$ \RestoreDiffP{}); adaptive ladder interventions stacked on top add no detectable gain (95\% confidence excludes gains $\geq$ \LadderExcludedGain{}). The probe predicts relapse before delivery (AUROC \AurocPrimary{}); a one-sentence tombstone note recovers about a third of the compilation effect and survives a placebo control. At \CostDeliveryFactor{} delivery overhead and \CostTotalHedged{} of API compute for every result, revocation failure becomes a measurable, predictable, and repairable property of dialogue state rather than an invisible one.

---


### 48. [From Visual Widgets to UI Code: Efficient Tool-Grounded Generation](https://arxiv.org/abs/2608.12611)

**<font color=#1a73e8>作者：</font>** Houston H. Zhang, Tao Zhang, Li Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing screenshot-to-code systems face a trade-off between flexibility and controllability. Direct multimodal generation can hallucinate visible details, whereas structured pipelines reduce such errors through component-wise decomposition, predefined templates, and customized intermediate representations. These structures, however, introduce additional generative orchestration and restrict outputs to designs covered by the representation. We investigate whether selective tool grounding can improve the fidelity--efficiency trade-off of direct widget-to-code generation. We introduce \textbf{WidgetGen}, a lightweight tool-grounded framework that extracts observable text and color evidence, performs high-level layout and optional chart reasoning, and directly generates executable JavaScript XML (\emph{JSX}). This design reduces reliance on component-wise generation while avoiding a fixed UI schema. Across six multimodal models and \(1{,}000\) held-out widgets, WidgetGen outperforms direct prompting and the structured Widget2Code pipeline on most visual reconstruction metrics, with consistent gains in area, legibility, and style. Finally, reconstruction-derived image-code pairs improve six Qwen-family open-weight models across every reported metric through supervised fine-tuning. These results establish WidgetGen as a strong lightweight baseline and show that selective evidence grounding offers an effective alternative to extensive representation constraints.

---


### 49. [LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning](https://arxiv.org/abs/2608.12626)

**<font color=#1a73e8>作者：</font>** Yi Wu, Zhimin Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals. In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps. This limitation leads to strategic drift, where localized decisions fail to sustain a coherent trajectory across reasoning. To address this, we introduce EpicStar, a framework that enables agents to learn memory as policy to tackle long-horizon reasoning. Specifically, the agent maintains a bank of successful past episodes as a heuristic alongside a working memory to track short-term environmental changes. During inference, a dynamic gating mechanism determines whether to execute a retrieved action directly or to perform new reasoning through a contextual fusion of the retrieved episodes and current working memory. Utilizing StarCraft II as the testbed, we evaluated EpicStar against diverse opponent styles. It significantly outperforms baseline methods, achieving higher win rates while consuming an order of magnitude fewer tokens, and it maintains this advantage consistently across difficulty levels and opponent strategies. Our findings provide compelling evidence that structured cross-episode memory is essential for enabling LLM agents to perform robust, long-term strategic execution in dynamic, autonomous settings.

---


### 50. [EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory](https://arxiv.org/abs/2608.12627)

**<font color=#1a73e8>作者：</font>** Le Zhang, Ke Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon egocentric memory transforms continuous first-person video and audio into a searchable record of past experiences. We demonstrate two bottlenecks in existing systems: indices built from context-poor captions are unreliable for agentic search, while retrieval ignores a question's temporal intent. To address both bottlenecks, we introduce EgoCITE (Egocentric Context-augmented Indexing and Time-aware Evidence retrieval), a long-horizon agentic memory framework for egocentric QA. EgoCITE comprises three components. EgoScheme uses local multimodal context to turn fragmentary video captions and speech transcripts into self-contained atomic memory indices. EgoIndex organizes complementary action, activity, utterance, and conversation representations into searchable multi-view memory indices at multiple granularities. EgoRetrv combines semantic search with question-conditioned temporal relevance scoring and curation of retrieved evidence. We evaluate EgoCITE on EgoLifeQA, EgoMem, and EgoR1-Bench in terms of answer accuracy and target-event retrieval alignment. EgoCITE improves accuracy over agentic memory baselines by at least 4.4--14.2\% while achieving 36$\times$ lower cost than long-context LLM agents.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
