# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 101. [Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard](https://arxiv.org/abs/2610.00651)

**<font color=#1a73e8>作者：</font>** Michael Hardy, Ruhana Azam, Anka Reuel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evaluations are increasingly used to compare LLMs and inform deployment decisions, yet ranks can reflect not only the model but also the effects of the evaluation conditions such as the scaffolds or tasks. This makes reliability claim-dependent: an evaluation that reliably ranks deployed systems may not reliably rank underlying models. We ask which conclusions current agent evaluations reliably support and what additional evaluation would improve them. We develop a Bayesian variance-decomposition framework for sparse, imbalanced agent leaderboards and apply it to 22 benchmarks from the Holistic Agent Leaderboard and Harbor Index. The framework separates signal, performance differences relevant to the intended claim, from noise, irrelevant variation that can still change rankings. We find: (1) Reliability depends on the measurement goal. Fixed model-scaffold systems are ranked reliably (0.935-0.994), while underlying-model reliability is substantially lower (0.148-0.841). (2) Scaffold choice can change conclusions. Inter-scaffold reliability measures whether scaffolds preserve model rankings, showing that scaffold effects vary substantially across evaluations. (3) More tasks cannot resolve all uncertainty. Even infinitely many similarly constructed tasks improve model-ranking reliability of a benchmark by at most 0.097 when uncertainty is dominated by limited scaffold coverage. (4) Pooling diverse benchmarks can improve cross-task rankings at lower cost. For rankings across diverse agentic tasks, pooling benchmarks raises projected reliability from 0.44 to 0.75 at the same task budget and can reduce projected cost by up to 83\%. Evaluation design should follow the intended claim: identify what a score or ranking should mean, diagnose what limits its reliability, and spend evaluation budget on the sources of uncertainty that matter.

---


### 102. [When More Data Is Not Enough: The Context-Sufficiency Frontier in Generative AI Personalization](https://arxiv.org/abs/2610.00654)

**<font color=#1a73e8>作者：</font>** Merieme Askour, Ayoub Merimi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalization has long relied on customer data to infer what an individual is likely to value. We call this customer evidence: the customer's historical behavior and preferences. Generative AI extends personalization by allowing providers to supply changing situational information at the moment a response is produced, without encoding every condition in advance. We define this provider-side context as information about what is possible, permitted, or advisable now. This flexibility creates a new problem: once context becomes easy to supply, more is not necessarily better. We develop a theory of context sufficiency in which the relevance of context to the customer's current intent matters more than its volume. The theory identifies four states, insufficiency, sufficiency, saturation, and interference, and introduces the Context-Sufficiency Frontier to locate the minimal relevant set. In a full-factorial experiment with a generative recommender at a large home-furnishing retailer, relevant context improved appropriateness, while irrelevant context reduced it and destabilized retrieval. The framework shifts personalization from supplying more context toward identifying what the current interaction actually requires and enforcing constraints throughout the service process.

---


### 103. [Lingtai: What Concept Geometry Reveals--and Does Not Reveal--About LLM Inference](https://arxiv.org/abs/2610.00656)

**<font color=#1a73e8>作者：</font>** Jiangang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Observing what a large language model computes during autoregressive inference--online and without training probes--remains difficult. We introduce Lingtai, a training-free concept telemetry layer: at each generation step, residual states are projected onto a domain-specific bank of named concept anchors, constructed without labeled concept examples, outcome labels, gradient fitting, or activation-space optimization, producing a structured per-step concept-coordinate signal. Across code generation and grade-school mathematical reasoning, this signal exhibits a robust association with predictive uncertainty: the association survives problem-identity and token-position controls and is not attributable to a single token type, is not explained by a simple correct/incorrect mixture on GSM8K, and is not reproduced by matched random anchors; it is markedly weaker or direction-inconsistent in K-means and PCA projections. Two structures emerge: a recurring uncertainty-linked activity signal whose functional geometry is task-conditioned (distinct activity-entropy shapes on HumanEval, MBPP, and GSM8K), and an execution-specific trajectory identity with strong local inertia but weak re-instantiation invariance--under completion-only elastic alignment, corruption at k=32 (approximately a median quarter of the completion) on the matched re-execution subset still retrieves the archived episode at 62.0%, while a fresh execution retrieves it only 11.7-16.0% of the time. Finally, a matched audit finds no evidence that the scalar concept-activity signal used here supplies a stable correctness coordinate under the tested protocol; we therefore treat correctness as externally supplied. Telemetry adds 0.7-1.6% per-token decode overhead for the 161-anchor code implementation, with unchanged generated tokens.

---


### 104. [Exploring More, Reasoning Better: Stepwise Risk-Sensitive GRPO for Diffusion Language Models](https://arxiv.org/abs/2610.00661)

**<font color=#1a73e8>作者：</font>** Yue YU, Bowen Zuo, David Crandall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate text by denoising a sequence or successive blocks, allowing several tokens to be revealed in parallel. Reinforcement learning with verifiable rewards (RLVR) reuses terminal feedback across these decisions, even as their conditioning context changes. We propose stepwise risk-sensitive GRPO (StepRS-GRPO), which varies the risk coefficient of the group-advantage transformation across denoising states while retaining the underlying trainer. For binary rewards, we show that this transformation is exactly a prompt- and state-dependent rescaling of centered outcome advantages. A capability-based calibration suggests a coefficient scale, while endpoint and interpolation ablations guide schedule selection. Across multiple dLLM backbones and mathematical reasoning benchmarks, StepRS-GRPO improves both pass@1 accuracy and pass@k coverage over centered GRPO, while increasing answer diversity. In our ablation studies, mass-matched controls support the contributions of state allocation and schedule direction, and the gains persist after matching the root mean square (RMS) of the advantages to that of centered GRPO. Reasoning-trace diagnostics further show that the diversity gains from StepRS-GRPO extend beyond final-answer strings.

---


### 105. [PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation](https://arxiv.org/abs/2610.00664)

**<font color=#1a73e8>作者：</font>** Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bengali secondary education lacks curriculum-grounded benchmarks for STEM question-solving, and general-purpose language models struggle with the precise terminology, unit conventions, and derivations that physics problems demand. We introduce PhysicsMate, a benchmark of 1834 question-answer pairs built from the National Curriculum and Textbook Board (NCTB) Grade 9-10 physics syllabus and grounded in a multi-relational knowledge graph of 1760 nodes and 2600 edges across ten ontological types. We Low-Rank Adapt at 0.6B, 1.7B, and 4B parameters, with a unified recipe and demonstrate a significant increase in closed-book accuracy in all scales (+5.5, +15.0, and +23.3 percentage points). A node-type analysis shows that the most benefited by adaptation is the structured curricular knowledge, which consists of physical quantities and named laws, while the least benefited is the loosely specified entity-level knowledge. The 4B model has been adapted and quantized to a small offline binary that can be used for local inference in resource constrained environments and offers a viable path to curriculum aligned physics support in environments with limited connectivity and hardware.

---


### 106. [Analysis of Quantized and Efficiently Adapted Protein Language Models](https://arxiv.org/abs/2610.00665)

**<font color=#1a73e8>作者：</font>** Ilan Yaniv Zeisler, Sebastian Clancy, Pouriya Bayat 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Protein language models (PLMs) are increasingly used for sequence generation and property prediction, but their size makes fine-tuning and deployment expensive. The effects of quantization and parameter efficient fine-tuning on performance, representations and generation remain insufficiently characterized. Results: We evaluated 4-bit quantization and low-rank adapter fine-tuning (QLoRA) across ESM-2, ESMC, ProtBERT, ProtT5, Ankh, Ankh3 and Profluent-E1. Across protein prediction tasks, many model-task pairs retained more than 90% of full fine-tuning performance. Peak GPU memory savings approached 90% for the largest models, although performance and efficiency varied by model, dataset and training configuration. QLoRA often preserved early-layer representations while inducing task-specific adaptations in middle and late layers, resembling full fine-tuning with smaller representational changes. Training speed and power effects were more varied. For unconditional generation with ProLLaMA, ProtGPT2, ProGen2, ProteinGLM and ESM3, 4-bit quantization largely preserved predicted structural and sequence-level properties, but token-level analysis revealed model-dependent shifts in autoregressive output distributions. Conclusion: QLoRA and 4-bit quantization reduce PLM computational requirements, particularly GPU memory usage. Our results support QLoRA as a first-pass strategy for memory limited adaptation, reserving full fine-tuning for challenging tasks, unstable architectures or low validation recovery. For generative PLMs, sequence-level and structural metrics should be complemented with distributional analysis, since downstream predictions alone may miss quantization-induced shifts. These approaches can broaden access to large-scale protein modelling while requiring model- and task-specific validation.

---


### 107. [VisionQ: VLM-as-a-Judge Taxonomy, Dataset and Benchmark for Qualitative Analysis in Computer Vision](https://arxiv.org/abs/2610.00666)

**<font color=#1a73e8>作者：</font>** Vu Dinh Xuan, Duc-Hai Nguyen, Minh-Dung Dao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Qualitative comparison figures are central evidence in computer vision papers, and vision-language models (VLMs) are increasingly used to judge them. Yet existing benchmarks score only scalar quality or overall preference, so a judge can be rewarded for picking the preferred image for the wrong visual reason. We introduce VisionQ, the first benchmark built from peer-reviewed CV comparison figures that grounds every judgment in a named visual criterion: each question states the criterion, and a judge is credited only when it selects the output the authors identify as best on that criterion. We call this task criterion-conditioned visual discrimination. VisionQ comprises (1) a corpus of 1,409 CVPR and ICCV papers with 1,800+ validated comparison figures and 3,911 hand-annotated data points linking method crops to author-stated visual claims; (2) a six-axis, 51-leaf taxonomy of the visual criteria behind qualitative judgment; (3) a criterion-conditioned evaluation protocol that hides method names, captions, and paper identity and reports accuracy per criterion; and (4) VisionQ-Judge, a DPO-tuned Gemma-4-E4B judge trained on symmetric evidence pairs, which reduces last-option predictions by 7.0pp and improves accuracy by 2.5pp on a held-out test set. Evaluating 20 open- and closed-source VLM judges, we find that the strongest reach only 63.1% accuracy (chance 32.2%) and that reliability varies sharply across criteria. Code: this https URL. Data: this https URL.

---


### 108. [Closing the Loop: Practical Training Recipes for Looped Language Models](https://arxiv.org/abs/2610.00673)

**<font color=#1a73e8>作者：</font>** Andrei Marchenko, Viacheslav Bezrukov, Oleg Kashurin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped language models increase effective depth by repeatedly applying a shared block of layers, but existing large-scale recipes require multi-stage training over trillions of tokens, while the benefits of recurrence remain difficult to separate from differences in data and training. In this work, we establish practical training recipes for looped language models, with three main results. (1) We develop a compute-efficient from-scratch pipeline that reduces the training budget from 7.7T tokens in Ouro to 310B tokens while retaining strong reasoning performance. Pretraining followed by high-quality mid-training, together with learning-rate warmup and stronger exit-gate regularization, enables stable recurrent training without prior multi-stage schedules. (2) Under controlled comparisons, our 1.4B LoopLM outperforms a parameter-matched dense model trained on the same data and token budget on all 12 evaluated benchmarks, including +14 points on GSM8K, +10 on MATH, and +22 on DROP. At matched inference compute, it approaches a 3.9B dense model on mathematical reasoning and reading comprehension while using only 36\% as many parameters. (3) We introduce a minimal recipe for converting pretrained dense models into looped ones: a single learned input-mixing scalar and a smoothed exit loss, with no step-specific parameters. Applied to Qwen3-1.7B-Base, Looped Qwen improves over an identically continued dense baseline on every evaluated benchmark across two data regimes, with statistically clear gains on GSM8K, MATH, and MMLU-Pro on the curated mixture. Together, these results make looped language models substantially cheaper to train from scratch and practical to introduce into existing pretrained checkpoints, while isolating the gains due to recurrence itself.

---


### 109. [LabBook: Harnessing Experimental History for Efficient LLM-Driven Discovery](https://arxiv.org/abs/2610.00675)

**<font color=#1a73e8>作者：</font>** Bo Yuan, Wenqian Ye, Zelin Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolutionary approaches to LLM-driven discovery often generate new programs from a small set of selected ancestors. This keeps contexts manageable but can omit useful evidence from other experiments, whereas including the full experimental history produces long, redundant contexts. We introduce a simple, single-agent discovery harness built around LabBook, an agent-maintained memory that serves two complementary roles: guiding retrieval of relevant evidence from a complete experimental log and informing the generation of new solutions. At each iteration, the same agent combines its memory with retrieved evidence and jointly produces the next program and an updated LabBook. This separates complete history retention from selective context construction, without requiring an explicit population or branching search structure. On 49 Frontier-CS problems, LabBook improves the observed quality-cost trade-off over the evaluated evolutionary baselines with two backbones, while remaining competitive across nine additional mathematical, systems, and heuristic-design tasks. Code will be released at this https URL.

---


### 110. [Harnessing Vision-Language Models for Perceptual Quality Assessment and Autonomous Content Adjustment in Augmented Reality](https://arxiv.org/abs/2610.00677)

**<font color=#1a73e8>作者：</font>** Elias Rotondo, Lin Duan, Yanming Xiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advancements in augmented reality (AR) continue to foster innovative solutions, facilitating novel methodologies within educational systems, healthcare delivery, and risk-mitigation protocols. However, optimizing for end-user immersion and comfort remains challenging, as AR head-mounted displays contend with constrained scene geometry, spatial jitter, and temporal instability. User studies are the standard AR evaluation method for visual quality, but their cost, diminishing scalability, and inflexibility pose bottlenecks during iterative application design. To address this problem, we present an automated framework for AR content evaluation and refinement, built on vision-language models (VLMs), to evaluate and predict the visual fidelity of AR scenes as perceived by users. First, we introduce RateAR, a benchmark of AR images and videos collected across diverse scenes and environmental conditions, with good-to-excellent reliability (ICC(2,5) >= .90) across perceptual factors, including object placement, scale, and shadow consistency. Subsequently, we evaluate eleven commercial VLMs on the crafted benchmark. Results support that VLM-based quality predictions strongly correlate with human subjective judgments, achieving Spearman's rank-order correlations of up to 0.8695. An ablation study further suggests that, compared to other prompting strategies, our contextual prompting yields better alignment with human ratings while balancing introduced complexity cues. Building on these findings, we construct an automated AR content adjustment system and conduct a 21-participant user study. More than 90% of participants found that the system improved placement and size coherence of virtual content.

---


### 111. [Bayesian Fine-tuning Yields Language Models that are as Bayesian as their Beliefs Allow](https://arxiv.org/abs/2610.00679)

**<font color=#1a73e8>作者：</font>** Polina Tsvilodub, Andreas Waldis, Linlu Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are increasingly used for tasks that require reasoning about hidden variables from a few observations, for which Bayesian inference is the normatively correct solution. While supervised fine-tuning of an LM on the outputs of an optimal $\textit{Bayesian}$ model leads to near-Bayesian behavior, standard supervised fine-tuning (SFT) on the true answers for the task falls short of it. But behavior alone does not tell us $\textit{why}$ tuning on a $\textit{Bayesian}$ or an $\textit{oracle}$ (true answers) signal differs: whether the resulting LM represents Bayesian beliefs, acts on them, or turns them into a choice the way Bayes' rule does. To compare them, we formulate increasingly demanding requirements for an LM to count as a Bayesian decision maker, spanning its behavior, representations, and computations, and test them on a flight recommendation task. The Bayes-trained LM acts Bayesian, encodes quantities of Bayes' rule in its middle layers, and uses the encoded belief for the recommendation to a certain extent. The oracle-trained LM differs from it both in the beliefs it holds and whether it reads beliefs out into recommendations. Exchanging beliefs between the LMs transfers a part of the Bayesian advantage. Bayes fine-tuning thus installs usable Bayesian beliefs in an LM for reasoning under uncertainty in a way standard SFT on oracle answers cannot, highlighting the advantage of nuanced supervision.

---


### 112. [Ontology-Grounded, Reasoner-Verified Benchmarks for Evaluating LLM Reasoning in Scientific AI](https://arxiv.org/abs/2610.00682)

**<font color=#1a73e8>作者：</font>** Nishtha N. Vaidya, Stephan Grimm, Thomas Hubauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly underpin scientific AI applications that reason over structured knowledge, from biomedical question answering to materials informatics. However, their logical reasoning often falls short, producing factual inaccuracies unacceptable in these settings. Reliable evaluation remains challenging: manual dataset construction scales poorly, and LLM-based generation risks embedding the very flaws it aims to measure. High-quality benchmarks must ground both correct and incorrect labelled examples in explicit background knowledge, formally verifiable by a standard reasoner. We propose a pipeline that automatically generates ontology-grounded multiple-choice question (MCQ) benchmarks from any sufficiently axiomatised OWL 2 ontology, with correct answers grounded in the ontology by design. Distractors are generated by perturbing the right-hand-side class expressions of class definition axioms, and their incorrectness is formally verified by an OWL reasoner via entailment checks. We evaluate the pipeline on three ontologies: Pizza (small, academic), PMDco (complex, materials science), and DOID (large, biomedical), generating 112, 2,491, and 15,216 MCQs respectively. Distractors span four semantic categories from class unsatisfiability to weakened subsumptions, enabling diagnostic evaluation of specific reasoning failures. Items meet natural language quality standards: mean LLM judge scores of 4.02, 4.36, and 3.36 out of 5 confirm fluency, and correct-answer-to-distractor similarity above 0.8 shows that wrong options cannot be dismissed on surface form alone. Six LLMs evaluated zero-shot achieve 41.1-76.8% accuracy, well above the 25% random-guessing baseline, indicating the benchmarks are challenging and discriminative. This work is a step towards more reliable benchmarks for assessing logical reasoning in scientific AI.

---


### 113. [Towards Robust Numerical Claim Verification](https://arxiv.org/abs/2610.00689)

**<font color=#1a73e8>作者：</font>** Peter Røysland Aarnes, Vinay Setty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used for claim verification, yet remain brittle for numerical reasoning: even small changes in value can sharply degrade accuracy. We show that this brittleness persists in frontier LLMs, but can be mitigated through adversarial fine-tuning on numerically perturbed examples. Using parameter-efficient fine-tuning, small Qwen3 models (0.6B$\unicode{x2013}$8B) reach 98.7% accuracy on label-flipping perturbations, outperforming larger zero-shot models and frontier systems (GPT-5.4 Pro (74.0%) and Gemini 2.5 Flash (73.9%)). The gains generalise to unseen perturbation types, indicating robust numerical decision boundaries rather than memorised edits. Robustness also transfers without target-domain data, significantly improving cross-lingual performance in Spanish. We further show that the same fine-tuning recipe confers robustness to evidence-side perturbations, using the VitaminC dataset.

---


### 114. [How Divergence Becomes Decision Flips in Compressed Language Models](https://arxiv.org/abs/2610.00694)

**<font color=#1a73e8>作者：</font>** Beatriz Almeida Felicio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compression reports summarize how far a compressed language model moved from the dense one, usually by a KL divergence; a deployment that relies on the dense model's outputs needs to know how many of its decisions changed. We show that total variation, not KL, answers this directly. Across 802 compressed and perturbed copies of 19 open models on five corpora and nine mechanically unrelated perturbation families, the rate at which the arg-max token changes (the \emph{flip rate}) tracks total variation at a ratio with median $1.05$, with no fitted constant. KL converts into flips only through its square root and a factor that varies fourfold across models and corpora, because KL averages over tokens before the root is taken; first-order statistics averaged per token, such as Hellinger distance, avoid this, but reports rarely give them. As a result, of two compressors reported on different models and corpora whose flip rates differ by at least $10%$, KL assigns the smaller divergence to the one that changes more decisions in $11%$ of cases, total variation in $1%$. Two pre-registered tests mark the limits: on a held-out code corpus the ratio held for all eight models while three predictions about KL each failed for half of them or more, and on three new models with real kernels it stayed in its band for 37 of 38 checkpoints but fell below one on code for two models. In vLLM speculative decoding, total variation measured under teacher forcing predicts greedy draft acceptance with a mean relative error of $1.1$--$2.4%$, without the task-specific calibration that KL needs.

---


### 115. [R-GroundBench: A Diagnostic Benchmark for R-Group Groundingin Markush Molecular Editing](https://arxiv.org/abs/2610.00700)

**<font color=#1a73e8>作者：</font>** Xin Wang, Zichuan Ying, Xinna Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI for scientific discovery enable molecular understandingand design, yet reasoning over incomplete chemical representations this http URL structures, which encode molecular families through variable R-groupplaceholders (\textit{R\textsubscript{1}}, \textit{R\textsubscript{2}}, \textit{X}, etc.), are ubiquitous in pharmaceutical patents and requiregrounding across molecular, textual, and chemical this http URL, existing molecule-language benchmarks focus on fully specifiedmolecules, leaving R-group grounding largely this http URL introduce R-GroundBench:, a diagnostic benchmark built from real patent Markushstructures, featuring a Multiple-Choice (VQA) track with controlled difficultyand modality splits, and an open-ended Generation this http URL results reveal a substantial gap between recognition andmolecular this http URL models achieve over 90\% accuracy on Easy VQA, performance drops to56--66\% on Hard VQA when shortcuts are this http URL-domain VLMs also remain unreliable, achieving only 25.7--46.2\% on HardVQA despite domain-specific this http URL, Generation Exact Match remains below 20\% for most models and below8\% when visual input is this http URL findings reveal that current AI systems lack reliable grounding andexecution for Markush editing, highlighting challenges for AI-drivenscientific discovery.

---


### 116. [From Images to Tasks: Characterizing Multimodal LLM Interactions in the Wild](https://arxiv.org/abs/2610.00701)

**<font color=#1a73e8>作者：</font>** Jinyi Ye, Scott Counts, Gaurav Verma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (LLMs) increasingly integrate vision and text, yet how people use them in natural settings remains underexplored. We seek to answer the question: when users upload images, what tasks are they trying to accomplish? Analyzing over 40,000 de-identified image-upload conversations from Microsoft Copilot, we characterize real-world multimodal use through a hierarchical framework of ten capabilities, spanning perception, cognition, and generation. First, we characterize the distribution and composition of these capabilities, finding that the majority of image-upload tasks involve multiple capabilities. Second, we find that multimodal use spans a broader and more diverse task space than text-only interactions, with asymmetric coverage and task classes that rely on cross-modal grounding. Third, mapping observed capability demand onto 253 existing benchmarks reveals uneven alignment between benchmark coverage and real-world use: benchmarks concentrate on perception and reasoning toward fixed answers, while common workflows involving text, code, and data generation remain comparatively undertested. We validate our taxonomy and findings on an independent ChatGPT dataset. Our results provide a large-scale empirical characterization of what users seek to accomplish with multimodal LLMs and highlight opportunities for benchmark design grounded in observed user demand.

---


### 117. [SkillSpec: Consensus-Gated Agent Skill Evolution via Representation Specialization](https://arxiv.org/abs/2610.00704)

**<font color=#1a73e8>作者：</font>** Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language skills are textual procedural memories through which large language model (LLM) agents retain reusable task knowledge without updating model weights. Existing methods typically treat skills as either static artifacts or monolithic documents optimized using aggregate validation scores as feedback. However, representing a skill as a monolithic document restricts optimization to its textual content, without explicitly modeling the structure through which procedural knowledge is retrieved and executed. We identify a key distinction between learning what knowledge to retain and determining how to organize it: textual updates should first be validated through execution evidence, after which the retained knowledge should be structured according to its procedural dependencies and retrieval requirements. To this end, we introduce SkillSpec, a two-phase framework comprising consensus-gated evolution and representation specialization. In the consensus-gated phase, complementary editing intents generate complete candidate skills. An update is committed only when paired evaluations reach consensus, requiring sufficient overall improvement and non-negative aggregate paired gain in every repeated evaluation. In the specialization phase, signals of process and redundancy sensitivity derived from the full optimization trajectory, including accepted and rejected candidates, guide the selection of a flat, graph, or hybrid this http URL six benchmarks and three target language models, SkillSpec improves average success rate over SkillOpt by 6.89%, averaged across the three models. These results demonstrate that reliable skill evolution and representation specialization address complementary objectives: deciding what knowledge to retain and how to structure it for inference.

---


### 118. [Initialization Improves LLM-Driven Discovery](https://arxiv.org/abs/2610.00707)

**<font color=#1a73e8>作者：</font>** Mansi Sakarvadia, Marco Ciccone, Colin Raffel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been used for novel discovery of algorithms, theorems, drugs, and other tasks through the use of harnesses that prompt an LLM to iteratively optimize an objective. In this work, we study the relationship between the population of previous iterates and eventual discovery success. We generalize past work on harness design to develop a suite of 12 harnesses called 'Modular' and characterize their performance across 5 diverse discovery tasks, finding that discovery success is brittle and sensitive to harness design. We uncover mode collapse, characterized by a dramatic drop in the diversity of iterates, as a common failure mode. We find that popular state-of-the-art harnesses and diversity-inducing harness interventions, which aim to prolong this collapse, yield inconsistent gains. Our results instead uncover that the performance of early discoveries is predictive of eventual success. We therefore propose a universally applicable intervention that performs an initial stage of parallel exploration in order to initialize subsequent iterative optimization. Our method provides consistent gains across many harnesses and target applications, confirming the importance of initialization in LLM-driven discovery.

---


### 119. [ReLiveGym: Evaluating Long-Lived Agents over Weeks of Replayed Reality](https://arxiv.org/abs/2610.00710)

**<font color=#1a73e8>作者：</font>** Xisen Jin, Jingheng Li, Zhenglun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents become widely adopted, they are increasingly deployed for tasks that require persistent monitoring or recurring actions (e.g., market analysis). These agents are expected to operate unattended for days or weeks, act at the right timing, and adapt to the dynamic environment over time. These challenges are not fully captured in the existing long-horizon agent work, as they often consider a static environment that is not temporally changing. We introduce ReLiveGym, a diagnostic evaluation environment of long-lived tasks in which agents act sparsely over simulated weeks of chronologically replayed real-world news, market, and social-media streams. The tasks span diverse levels of time sensitivity, reasoning intensity, and recurrence. Across eight base language models, we investigate how model choice and harness design affect agent performance on such long-lived tasks. Our results show that how agents determine when to act arises as an important harness-design axis for long-lived tasks; and that the optimal design varies across tasks and sometimes model choices as well. We also evaluate how continuous learning from hindsight feedback affects performance and addresses failure modes observed in these long-lived tasks. These findings indicate model choice, action timing mechanism, and use of feedback as important considerations in the design of long-lived agents. Code: this https URL

---


### 120. [Robust Nash Alignment under Preference Uncertainty](https://arxiv.org/abs/2610.00715)

**<font color=#1a73e8>作者：</font>** Shihab Ahmed, Debamita Ghosh, David Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference-based alignment methods typically optimize against a single preference model, and can therefore be brittle when pairwise preferences are uncertain: noisy, heterogeneous, or shift after deployment. To address these issues, we propose Robust Nash Alignment, a game-theoretic framework for alignment to uncertain pairwise preferences. Our formulation has a major learner seeking a policy with a large worst-case win rate against both an adversarial competitor and any preference kernel lying in an ambiguity set around a nominal preference. When the ambiguity set captures the uncertainty in preferences, the resulting robust objective of the game directly yields a certified lower bound on worst-case performance. However, we note this problem is computationally challenging to optimize, and to address this, we introduce a four-player primal-dual proxy game involving the leader policy, follower policy, adversarial kernel, and dual variable, and develop a single-loop optimistic mirror descent-ascent algorithm for it. We show that the proxy always lower-bounds the truncated hard-constrained objective, quantify the proxy-to-hard gap, and characterize an exactness condition under which the proxy recovers the robust objective. We then prove an \(\mathcal{O}(1/\sqrt{T})\) average-iteration convergence for the proxy-game duality gap, which implies a near-optimal robust policy for the original robust objective. Experiments on controlled tabular games and LLM alignment with uncertain preference further validate the convergence theory and show improved performance over nominal baselines.

---


### 121. [Sequential Functional Structured Tucker Compression for Large Language Model Attentions](https://arxiv.org/abs/2610.00717)

**<font color=#1a73e8>作者：</font>** Jiangfeng Chen, Xinyu Wang, Tianshuo Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training compression of LLM attention is often formulated as independent matrix approximation, ignoring both the shared structure among attention projections and the representation shift introduced by earlier compression. We propose FTC, a sequential structured compression framework that adapts the approximation to the current compressed model while jointly exploiting the native Q/K/V head structure under a fixed storage budget. The output projection is handled separately to account for the changed post-attention representation. FTC requires neither fine-tuning nor gradient-based recovery. Across seven decoder-only LLMs from 6B to 32B parameters, FTC achieves the lowest WikiText-2 perplexity among the compared methods at every tested keep ratio on five modern GQA models, with the largest gains under aggressive compression. The improvements transfer to downstream tasks and remain substantial at the 32B scale.

---


### 122. [Reason in Style: Discovering and Controlling Style in Language Models](https://arxiv.org/abs/2610.00724)

**<font color=#1a73e8>作者：</font>** Ioana Marinescu, Eric Karl Oermann, Kyunghyun Cho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models learn content and style jointly, making stylistic variation in their outputs difficult to identify and control. We study whether recurring styles in model responses can be discovered without supervision and explicitly controlled. We design an algorithm that learns to separate representations of content and style from language models' outputs and validate its effectiveness on math questions in a controlled setting. By applying this method to over 100K verified traces from nine distinct teacher models, we discover six recurring yet imbalanced styles. We then fine-tune smaller student models to follow these styles when explicitly conditioned on them, using importance weighting to balance the contribution of the styles represented in the corpus. This approach improves Pass@$k$ over standard fine-tuning on the same data across six math reasoning benchmarks, demonstrating that we can diversify the style of answers effectively. We confirm that this also results in strong correspondence between requested and realized styles. We find that style affects correctness: the probability of solving a problem depends on the style we condition on, and different problems benefit from different styles. In summary, our results show that stylistic variation in model-generated data can be discovered in an unsupervised way, and made explicit, providing a source of both control and improved reasoning performance.

---


### 123. [Benchmarking Generative Models for Weather Data Assimilation on Real Station Observations](https://arxiv.org/abs/2610.00728)

**<font color=#1a73e8>作者：</font>** Ruizhe Huang, Qidong Yang, Jonathan Giezendanner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weather reanalysis products rely on computationally intensive numerical weather predictions followed by data assimilation that corrects the forecast toward observations. Deep generative models offer a cheaper alternative that shifts much of this cost from inference to offline training. However, existing generative approaches have been evaluated on synthetic observations or under different datasets and evaluation schemes, making it unclear which design choices actually improve real-world data assimilation. We present the first controlled benchmark of generative weather data assimilation on real weather station observations. Using 11,849 NOAA MADIS stations across the contiguous United States and four weather variables, we evaluate methods while holding the dataset, observation operator, and deep learning architecture fixed. The benchmark compares the major design choices, including diffusion versus flow matching, pixel versus latent-space formulations, and multiple inference-time conditioning strategies, against a classical 3D-Var baseline. The benchmark reveals three clear conclusions. First, learned generative priors outperform the Gaussian prior of 3D-Var (35.7% vs. 33.3% RMSE reduction over ERA5) despite using no ERA5 background field at inference. Second, full-gradient guidance consistently outperforms stop-gradient and initial-noise optimization. Third, other choices provide little measurable benefit: diffusion and flow matching perform nearly identically under matched conditions, and latent-space variable mixing does not help. We further evaluate both dense and sparse station settings and find advantages from generative AI and full-gradient guidance more pronounced under sparsity. Together, these results identify which components of generative weather data assimilation improve performance on real station observations and establish a standardized benchmark for future work.

---


### 124. [Video Evidence Indexing: Learning Where to Look from Video Previews for Token-Budgeted Long-Video Question Answering](https://arxiv.org/abs/2610.00757)

**<font color=#1a73e8>作者：</font>** Haowen Guan, Shengzhi Li, Shichao Pei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering is limited by the high cost of visual tokens and by the fixed context width of current VLMs. A long-video question may require broad temporal coverage, but the answer is often supported by only a compact set of moments. To locate these moments efficiently, we propose token-budgeted Video Evidence Indexing (VEI): given a dense low-resolution Video Preview, the model constructs a compact high-resolution Evidence Set for final reasoning. We treat VEI as a policy that must jointly solve \textit{evidence localization}, which finds question-relevant moments, and \textit{budget planning}, which decides where to spend the limited high-resolution frame budget. We implement this idea with an inference pipeline: the Video Preview provides cheap global coverage, Video Evidence Indexing constructs the Evidence Set, and Answer Generation combines both inputs for final VQA. To address missing frame-level supervision, we adopt privileged self-distillation, where an answer-aware teacher guides the normal test-time policy on student-generated indexing traces. We explore previews at 1, 6, 12, and 24 visual tokens per frame, training a single policy that supports all four resolutions. Experiments show that Video Evidence Indexing improves accuracy under limited visual budgets, and self-distillation further improves both QA accuracy and temporal evidence localization.

---


### 125. [LeanSide: A Formally Verified Co-Reasoning System for Natural-language Proofs](https://arxiv.org/abs/2610.00760)

**<font color=#1a73e8>作者：</font>** Chenjun Guo, Manooshree Patel, Arnav Mehta 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as collaborators on deductive-reasoning tasks, but their outputs can hallucinate or pull users away from intended reasoning. Formal proof assistants provide machine-checked verification, but have a steep learning curve and require more granular reasoning than human written proofs. We explore an interface that combines these strengths, allowing users to write and revise free-form natural-language proofs while a verified backend checks their reasoning and returns feedback at the user's granularity. We study this interface in the context of undergraduate mathematics education by developing LeanSide, a formally verified co-reasoning system, which auto-formalizes student reasoning into Lean and informalizes verifier output into understandable feedback. We conducted user studies through classroom deployment and analyzed which system properties helped students make progress and which caused them to get stuck. We use these findings to derive design implications for using a formally verified backend in human-AI co-reasoning systems.

---


### 126. [Effective Synthetic Data Curation Requires Group-Level Signals](https://arxiv.org/abs/2610.00779)

**<font color=#1a73e8>作者：</font>** Cathy Jiao, Chenyan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data now is essential to LLM training, used to strengthen advanced capabilities such as autonomous and long-horizon task execution. Yet recent work shows that training on it at scale can degrade model generation, making it important to decide what synthetic data is worth training on. While current data curation practices do so with individual-level signals (i.e., estimates of each data sample's training utility in isolation), across pre-training and post-training settings we show that this is insufficient for synthetic data, and that group-level signals (i.e., estimates of utility that account for interactions among data samples) are necessary for effective data curation. First, we show that individual-level signals are blind to how samples jointly affect training: synthetic datasets with different compositions can be indistinguishable under individual-level influence yet differ sharply under group-level influence, and curating by the latter yields better downstream performance, particularly in generative capability. Second, we find that group-level signals matter more as training pipelines become increasingly synthetic: among widely used data curation methods, only those incorporating them improve over baseline, with gains increasing when weights capturing relations among samples are amplified. Finally, we translate these findings into practice -- for model developers under a compute budget, we offer a cheap diagnostic that prioritizes which groups of synthetic data most need group-level estimation, recovering much of the benefit of full group-level scoring at a fraction of the compute cost.

---


### 127. [Identity-Bound Governance Under Execution Uncertainty: An Accountability Proof Block for LLM Agent Persistent Halts, with Cryptographic Implementation and Cross-Model Calibration](https://arxiv.org/abs/2610.00787)

**<font color=#1a73e8>作者：</font>** Marcelo Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A correctly governed LLM agent can reach a state in which neither continuing execution nor automatically halting is admissible: the system has detected a persistent failure of its observability or drift-detection layer, but cannot itself decide who has the authority to resume, deny, or recalibrate the deployment. We call this an identity-bound governance event and formalise the mechanism that resolves it. We introduce the Accountability Proof Block (APB): a system-constructed evidence block, a human-supplied decision block, and an ed25519 signature binding both to a registered principal. The system cannot forge the signature, and the principal cannot alter the evidence undetected. We prove four theorems: Protocol-Bounded Governance Completeness, Non-Repudiability, Impossibility of Anonymous Re-Authorization, and Finite-Time APB Construction Termination. The implementation uses RFC 8785 JSON canonicalization and a UUID4-based replay predicate. Empirically, governance completeness holds over 3,812 halt events with zero unresolved cases; the verifier detects 100% of 1,800 attacks across 9 adversarial vectors; a k-of-n multi-principal variant shows 0 false acceptances in 2,000 single-key capture attempts. A study of six open LLMs finds the drift threshold T* stable within model (sigma/T* < 2%) but varying across models, refuting size-monotonicity: the largest model did not drift. T* must therefore be measured per deployment, and the APB is the vehicle by which that threshold yields accountable authority transfer.

---


### 128. [Can large language models unlock discrete data in ophthalmic diagnostic reports?](https://arxiv.org/abs/2610.00795)

**<font color=#1a73e8>作者：</font>** Umair A. Zaidi, An-Lun Wu, Wei-Chun Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective: To assess the accuracy and efficiency of a large language model (LLM) using two prompt strategies to extract structured data from ophthalmic diagnostic PDF reports. Methods: Twenty deidentified reports across four types (Visual Field, OCT Glaucoma Overview, OCT retinal nerve fiber layer Single Exam, and OCT Thickness Map; n = 5 each) were processed using two GPT-4o-assisted pipelines and compared with a reconciled manual ground truth. Schema-Constrained used Structured Output mode with a predefined JSON Schema; Prompt-Only used a detailed instruction prompt followed by Python conversion to JSON. Outcomes were value accuracy, formatting accuracy, and extraction time. Results: Schema-Constrained value accuracy was 100.00% for Visual Field and RNFL Single Exam, 97.45% for Glaucoma Overview, and 98.00% for Thickness Map; Prompt-Only achieved 100.00% across all four report types. Formatting accuracy was 100.00% for Schema-Constrained across all report types and 100.00% for Prompt-Only except RNFL Single Exam (90.14%). Mean extraction time was 56.51 s per report for manual review versus 5.04 s for Schema-Constrained and 4.70 s for Prompt-Only, an approximately 92% reduction. Conclusions: In this small proof-of-concept dataset, general-purpose LLM-assisted pipelines extracted structured data from ophthalmic diagnostic PDFs with high accuracy and substantially reduced processing time. Prompt-Only achieved the highest value accuracy, while Schema-Constrained produced schema-compliant output with 100% formatting accuracy. These complementary strengths support further evaluation of hybrid, validation-aware workflows for research and clinical data abstraction.

---


### 129. [Paying for Too Many Tokens? Valid and Cost-Efficient Multimodal LLM Annotation with Simple Heuristics](https://arxiv.org/abs/2610.00809)

**<font color=#1a73e8>作者：</font>** Zhixi Zhu, Kristina Gligoric  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) enable video annotation at scale, but costs accumulate quickly: processing a typical 60-second short-form video at one frame per second requires millions of tokens. To reduce costs, researchers rely on heuristics such as sampling a subset of frames, compressing videos into image grids, or using only a single modality. However, it remains unclear which heuristics save cost, and whether they preserve the downstream conclusions these annotations enable. To address this gap, we conduct a systematic evaluation of these heuristics using short-form videos, on two computational social science (CSS) tasks: sentiment and topic classification. We evaluate each configuration along three axes the literature typically treats separately: classification accuracy, validity of downstream inference, and per-video token cost. First, we find that accuracy and validity diverge: the highest-accuracy configuration can produce wrong conclusions. Second, modality value is not guaranteed: text alone can yield strong performance, indicating that adding modalities can add cost without adding signal. Finally, we find that cost can be decoupled from video length when annotating short-form videos: a single $2\times8$ image grid built via simple shot-transition detection approaches full-video understanding ($\kappa$ within~.05), at $\sim 15\%$ of the token cost. Based on these findings, we derive guidelines that can enable cost-aware VLM annotation in CSS.

---


### 130. [Training-Aware Target Coverage for Synthetic Data Selection](https://arxiv.org/abs/2610.00814)

**<font color=#1a73e8>作者：</font>** Yang Ba, Michelle V. Mancenido, Rong Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data are increasingly used to scale LLM training, yet more synthetic data do not necessarily produce better models. Useful synthetic data must add information relevant to the target task without introducing errors that offset their benefit, and the value of an example can change as the training set grows. We develop a linear theory that characterizes this tradeoff and determines where synthetic data are useful, how much should be added, and the marginal value of adding one example to an existing set. The analysis shows the conditions when input coverage alone is sufficient and when synthetic errors must also be considered. Guided by these results, we introduce \emph{Training-Aware Target Coverage} (TATC), a synthetic data selection method for LLM fine-tuning. TATC identifies candidates whose training effects are beneficial to the target task and selects among them to expand coverage of target-relevant directions not already represented by the available data. Experiments on text and image data verify the linear theory. With mathematical reasoning tasks, TATC selects synthetic solutions for fine-tuning Qwen2.5-Math-1.5B-Instruct and outperforms alternative synthetic-data selection methods on GSM8K across selection budgets. In summary, we provide a principled approach to synthetic data selection by quantifying and maximizing its value to the target task.

---


### 131. [SafeDepth: Safety-Aware Token-Level Adaptive Computation](https://arxiv.org/abs/2610.00815)

**<font color=#1a73e8>作者：</font>** Nizhang Li, Ian G. Harris  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent studies suggest that not every token needs to pass through all Transformer layers, motivating token-level adaptive models that selectively skip layers to reduce computation. Our experiments show that these execution choices also affect safety: existing token-level adaptive reasoning models exhibit higher harmful-response rates than their reference backbones. The safety effects depend on which layers are skipped and whether skipping occurs during prompt processing or answer generation. We further find that recognizing harmful requests and producing refusals depend on different layer-wise computations. We introduce SafeDepth, a lightweight, plug-in framework that uses selective layer execution to improve both safety and efficiency. SafeDepth learns to retain computations that support safe responses and bypass those that contribute to unsafe generation. A router selects layer execution based on token representations, layer position, and inference phase, while an adapter supports the skipped paths. We jointly train these modules to reduce computation and harmful responses while preserving performance on benign tasks, targeting a better safety-efficiency trade-off. The pretrained backbone remains frozen throughout, requiring no additional pretraining. Experimental results on Llama-3-8B-Instruct show that SafeDepth reduces computation relative to full-depth inference while largely preserving task performance. Compared with FlexiDepth, it lowers unsafe-response rates across all five harmful-request benchmarks, with the largest absolute decrease on HarmBench-HJ (from 55.44% to 25.25%), while reducing the XSTest false-refusal rate from 12.0% to 4.0%.

---


### 132. [Align Then Reason: A Multimodal Lip-Sync Judge for Dubbing](https://arxiv.org/abs/2610.00825)

**<font color=#1a73e8>作者：</font>** Rui Liu, Bhavin Jawade, Haoqi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dubbing quality control requires a reference-free judge that can determine whether a candidate text line matches a speaker's visible articulation in both content and timing, using only silent video and text because dubbed audio may not yet exist. Existing visual speech recognizers and video-language models are poorly suited to this setting: even when fine-tuned to recover spoken content from lip motion, they remain largely insensitive to temporal errors. We introduce $\textit{Align Then Reason}$ (ATR), a multilingual lip-sync judge that first establishes a monotonic alignment between frame-level lip representations and the phonetic units of the candidate line, then reasons over this alignment to make the final judgment. An alignment scorer provides the LLM with both local evidence for each phonetic unit and a calibrated global alignment score, enabling it to reason jointly about content and timing. On a seven-language benchmark, our method improves mean AUC over the corresponding Qwen3.5 SFT baselines by 59.4%, 50.2%, and 50.8% with 2B, 4B, and 9B reasoners, respectively. The gains generalize across LLM families, reaching mean AUC improvements of 45.9% and 46.6% over the best baseline for LLaMA-3.1-8B and Mistral-7B, respectively. They also transfer across datasets to three unseen MuAViC languages. Furthermore, we evaluate on two downstream tasks built from real dubbing lines. On dub-line reranking, ATR-9B outperforms the best lip-reading baseline by 52.0%, while on script-to-clip assignment, ATR-9B improves over the best lip-reading baseline by 17.7%.

---


### 133. [Verbalized and Internal Probabilities Are Coupled in Large Language Models](https://arxiv.org/abs/2610.00827)

**<font color=#1a73e8>作者：</font>** Sinead Williamson, Jiaxuan Li, Nick Foti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models carry an internal notion of uncertainty in their sampling distribution, i.e., the probabilities they place on generating one answer rather than another. They can also be asked to state a confidence, in words or as a number: a verbalized uncertainty. Prior work suggests that internal probabilities track relative frequencies in the training data, and that verbalized probabilities track explicit probabilistic assertions in the training data. However, we do not know whether these two readouts are aligned, except when frequencies and probabilistic assertions in the training data happen to align. This limits our understanding of when we can use verbalized uncertainties as a proxy for either training data frequencies, or a model's internal distribution. We resolve this gap by systematically exploring how LLMs probability readouts are impacted by training and in-context data, via intervening on the underlying uncertainty sources in the data. We find that both internal and verbalized probability readouts are impacted by both distributional and asserted uncertainty in the training data. Further, we find that verbalized and internal probabilities are aligned beyond what would be expected by independently tracking the same uncertainty sources, suggesting that verbalized probabilities can be used to probe a model's internal distribution.

---


### 134. [AnyJev Technical Report](https://arxiv.org/abs/2610.00831)

**<font color=#1a73e8>作者：</font>** Jiamu Zhang, Tianze Yang, Yucheng Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A typed decision is a choice among a fixed set of options, returned as a probability rather than as text. Systems that need typed decisions today use models trained for that purpose. This report describes AnyJev, which reads a typed decision from one prefill of a pretrained instruction-tuned language model. The readout restricts the next-token distribution at the answer position to the option tokens. It has two defects: the model assigns higher probability to some labels whatever the input, and to some positions in the option list. AnyJev corrects both with no gradient steps and no parameter changes: it divides out a label prior estimated from unlabelled inputs, and it averages log-probabilities over the K cyclic rotations of the option list. On two 20-option tasks the rotations lower the order-flip rate from 0.33 to 0.14 and from 0.33 to 0.18, and raise accuracy on 11 of 11 models on both. Reading every rotation requires K prefills. A stopping rule selected against the full-rotation decision on unlabelled states cuts that. Selecting the threshold on one unlabelled split and bounding its disagreement on a second, it reads 10.6 rotations of 18 at a verified 0.008 bound on two of four cells; selected and bounded on one split, as our serving run did, it reads 7.3 and serves 2.2 times as many decisions per second on vLLM. The code is open source.

---


### 135. [VERITYGATE: A Four-Gate Schema-Level Faithfulness Framework and Paired Benchmark for Grounded LLM Narrations over Structured Evidence](https://arxiv.org/abs/2610.00833)

**<font color=#1a73e8>作者：</font>** Sachin Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fluent LLM explanations may not follow the evidence from a structured system. We present VERITYGATE, a four-gate checker for declared evidence IDs, entities, numbers, and claim types. It checks a fixed schema; it does not verify every fact in the prose. At r=0 and r=1, we test 900 instances per setting (450 grounded-ungrounded pairs) with GPT-4o-mini, Llama-3.3-70B, and Claude Sonnet 4.6. Under this schema-level contract and before repair, 80.3% of mini claims and 47.9% of Sonnet claims fail. These are verifier rejection rates, not prose-hallucination rates. One repair pass raises claim survival from 19.7% to 28.0% for mini and from 52.1% to 54.3% for Sonnet. Verified claims per example change by +0.14 for mini, -0.71 for Llama, and -0.47 for Sonnet, so survival and output volume must be reported together. A second Sonnet pass gives no clear gain. At r=1, Gate 4 covers 97.0%, 98.7%, and 100% of failing claims for mini, Llama, and Sonnet. Small human studies support the rules but show gaps between schema checks and correct prose. A domain-specific GPT-4o judge test shows an order effect, so it is only a usefulness check. We release the code and data.

---


### 136. [Kepler: Auditable World Models for ARC-AGI-3](https://arxiv.org/abs/2610.00834)

**<font color=#1a73e8>作者：</font>** Wensen Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation. We present Kepler, an open-source harness that represents hypotheses as executable world models and validates them through retrospective transition checks and conditional prediction checks. Under one frozen Claude Opus 5 configuration, Kepler obtained a server-verified 100.00 RHAE on all 25 public games, with no per-game model selection or score-conditioned reruns. On 181 of 183 completed levels, the final Opus attempt used no more actions than the corresponding median-human baseline. The retained board runs used 8,256 environment actions, of which 7,292 occurred in scored levels. Retained local provider-session records yield 858.0 million tokens, 97.37% cache reads, and a \$777.72 cost at September 1, 2026 API list-equivalent rates. We also report three evaluation failures: source-code leakage that produced an invalid perfect run, agents reconstructing a removed harness in a control condition, and autonomous repair masking a broken planner. A single-game observation case study showed that animation frames contained task-relevant information absent from settled text grids. Across the final Claude Opus 5 and GPT-5.6 Sol boards, 48 of 50 game-model cells reached 100. These results indicate that public-set score alone has limited discriminative value and motivate first-attempt, cost-conditioned, and verification-aware reporting.

---


### 137. [SHARPO: Segment-Level Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.00838)

**<font color=#1a73e8>作者：</font>** Xinchen Du, Zhengze Zhou, Wenhui Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) trains a large language model (LLM) to act over long, multi-step interactions. However, a single localized error can cause task failure, while trajectory-level rewards provide limited guidance for assigning credit to individual decisions. To address this limitation, we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization (GRPO) at the level of environment-facing segments. Inspired by the existing on-policy self-distillation (OPSD) method, SHARPO computes teacher-student log-probability gaps within each segment and uses the resulting signal to compute a bounded multiplier on the GRPO advantage. This multiplier is shared by all tokens within the segment, allowing credit to vary across different segments. With Qwen2.5-7B-Instruct, SHARPO outperforms existing baselines on the ALFWorld and WebShop benchmarks, including GRPO, SDAR, RLSD, and StepOPSD.

---


### 138. [Contextual trajectory and incremental contextual displacement: Towards using LLMs to understand dynamic, utterance-specific meaning construction](https://arxiv.org/abs/2610.00840)

**<font color=#1a73e8>作者：</font>** Grayson Wycliffe Storer, Julia Witte Zimmerman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models (LLMs) such as RoBERTa represent text using contextual word embeddings (CWEs), which alter the embeddings associated with each token based on surrounding context. We construct token-wise incremental trajectories by repeatedly recomputing a token's CWE as successive words are added to a sentence, yielding a representation of how contextualized embeddings evolve as the utterance unfolds. We evaluate this approach using garden-path sentences as a test case with characteristic features. Token-wise trajectories reproduce known features of garden-path processing, including disruption around the critical region, and reliably distinguish garden-path sentences from matched disambiguated controls. We introduce several metrics for quantifying representational displacement across contextual increments and show that trajectory information can be highly predictive of sentence type. We find that ambiguity-related information is recoverable not only from the sentence-level CLS representation but also from ordinary vocabulary tokens, suggesting that utterance-level information is distributed across multiple representational scales. In exploratory analyses, we find qualitatively similar trajectory structures in other ambiguity- and misdirection-related linguistic phenomena. Together, these results establish token-wise incremental trajectories as a promising framework for studying utterance-specific meaning construction using LLMs.

---


### 139. [Geometric Similarity in VLM Low-Level Vision Representations](https://arxiv.org/abs/2610.00848)

**<font color=#1a73e8>作者：</font>** Shao-Jun Xia, Huixin Zhang, Zhen Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have emerged as powerful candidates for universal vision backbones, with representative architectures including autoregressive (AR) models and diffusion transformers (DiTs). Yet, adapting them efficiently for all-in-one low-level image restoration remains a challenge. Crucially, the field lacks an understanding of how VLMs organize hidden-layer representations and whether these structurally distinct paradigms share a common geometric organization for pixel-level perception. Such shared organization is a prerequisite for building highly transferable, unified restoration VLMs and adapters. In this paper, we systematically investigate representational similarity across 24 low-level tasks spanning 5 categories. We propose GeoSim, a unified four-level framework that analyzes task-conditioned representations from global similarity, local geometry, sparse feature decomposition, and topological verification perspectives. Our formulation applies to the analysis of hidden states in AR models and feature maps in DiTs across same- and cross-task/model settings. Our results reveal the organizing principles of low-level visual representations while exposing their limits in cross-task and cross-model agreement. Ultimately, GeoSim provides an interpretability lens for probing latent transferability in low-level vision and diagnosing model limitations in task- or model-specific scenarios.

---


### 140. [AuraForge: Scaling Security Supervision for Training Coding Agents](https://arxiv.org/abs/2610.00850)

**<font color=#1a73e8>作者：</font>** Danqing Wang, Songwen Zhao, Harsh Sharma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents are now proficient enough to generate complex software applications from a single prompt. As their capabilities have grown, human oversight has increasingly shifted from line-by-line code review toward hands-off evaluation of outcomes. However, recent studies have shown that such a transition exposes a critical risk: functional correctness alone does not guarantee a secure implementation. Despite growing attention to code security, training safer coding agents remains challenging because reliable security supervision is difficult to obtain at scale from real-world repositories. We introduce AuraForge to synthesize and validate executable security tests for training secure coding agents. Our approach combines attack-oriented test synthesis, language-extensible task construction, and safeguards against reward hacking. Using AuraForge, we construct AuraGym, a multi-language and multi-CWE executable training gym: 679 executable feature-implementation tasks from 344 real-world repositories across Python, JavaScript, and TypeScript, covering 177 CWE categories. On the subset with human-written security tests, AuraForge produces about 3 times as many test cases on average and reduces the false-positive rate by 83.23%, allowing alternative secure implementations to receive correct supervision. Training Qwen3.5-4B with synthesized security tests gains larger improvements than human-written security tests (average 19.7 FuncPass and 6.2 SecPass vs. 14.9 FuncPass and 4.4 SecPass) on three languages. These results demonstrate that AuraForge provides more diverse and reliable security supervision to train secure coding agents.

---


### 141. [Lang3DSeg: Annotation-Free Open-Vocabulary 3D Segmentation with Point Transformers](https://arxiv.org/abs/2610.00855)

**<font color=#1a73e8>作者：</font>** Cigdem Kokenoz, Amir Salarpour, Alkim Domeke 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D semantic perception is critical for safe autonomous navigation. However, supervised LiDAR segmentation remains tied to closed taxonomies and to the cost of point-wise manual annotation. Open-vocabulary methods avoid that cost by projecting the output of 2D vision-language models onto LiDAR and distilling it into a 3D network. These methods rely almost exclusively on voxel-based sparse convolutions, and point transformers have so far been limited to indoor environments, where 3D data is dense and bounded. We present Lang3DSeg, which establishes a point transformer as the backbone for annotation-free open-vocabulary segmentation of outdoor 3D LiDAR, and is trained from scratch without geometric pre-training. This training paradigm necessitates addressing the inherent noise in 2D-to-3D label projections; specifically, naive projection often suffers from depth ambiguity, where points behind an object are erroneously assigned its semantic label. We therefore composite masks using an explicit class-priority rule and truncate each projected instance at the first gap in its depth distribution, correcting the projection error directly rather than averaging it over registered sequences. Lang3DSeg achieves 52.8% mIoU on nuScenes validation and 41.4% on SemanticKITTI, the highest among published annotation-free methods on both benchmarks. Every 3D semantic segmentation is on a single LiDAR sweep, and inference operates in real-time without running vision-language models.

---


### 142. [An Educator-Guided LLM Pedagogical Agent for Scaffolded Feedback in Conceptual Database Design](https://arxiv.org/abs/2610.00870)

**<font color=#1a73e8>作者：</font>** Sara Riazi, Pedram Rooshenas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an educator-guided LLM pedagogical agent for scaffolded feedback in conceptual database design. Integrated into an entity--relationship diagram (ERD) editor, the system grounds feedback in the student artifact, assignment requirements, educator-authored rubrics, and instructional resources. Its architecture separates hidden, artifact-grounded diagnosis from the workflow that controls the form and disclosure level of student-facing support.
We instantiate the architecture as a four-stage workflow progressing from concept checks and guided application to low-detail feedback and localized clarification. Each feedback request creates a stateful episode linked to versioned ERD states. In a deployment spanning three ERD environments and 383 feedback episodes, 71.1\% of observed target-level changes fully or partially incorporated the hidden diagnostic target, including many after Stages~1--2. Qualitative analysis showed that staged disclosure sometimes withheld inaccurate details, supported selective uptake, or allowed later recovery, though some errors still shaped revisions. Survey responses from a self-selected sample favored delayed disclosure and student agency but noted indirectness and repetition.

---


### 143. [MemFit: Efficient Long-Term Agentic Memory](https://arxiv.org/abs/2610.00872)

**<font color=#1a73e8>作者：</font>** Mitchell Piehl, Muchao Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations. To address this limitation, we propose MemFit, a long-term memory system for conversational agents that reduces the cost and latency of memory operations. Unlike existing systems that rely on expensive LLM calls for memory construction or discard surface-level details through compression, MemFit stores each turn verbatim in an append-only store with near-instantaneous, LLM-free insertion, indexing turns with segment summaries rather than replacing them. Additionally, MemFit uses an LLM-free, multi-path retrieval strategy that combines lexical and semantic signals with cross-encoder reranking over caption- augmented episodes in both textual and multimodal settings. Empirical results on three widely used benchmarks, LoCoMo, MemGallery, and LongMemEval-S, show that MemFit achieves state-of-the-art performance while reducing memory construction time and cost several-fold, providing a scalable and efficient solution for persistent agentic memory.

---


### 144. [Match the Distribution, Not the Compute: Post-Training Multi-Token Prediction Heads](https://arxiv.org/abs/2610.00888)

**<font color=#1a73e8>作者：</font>** Prachi Badarayani, Aidan Jay, Chenghui Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-token prediction (MTP) improves the throughput of autoregressive generation by enabling the language model to draft multiple next tokens per forward pass, while a verification step over draft tokens ensures that token distribution of the backbone is preserved. Every open MTP-family release (MiMo-7B, DeepSeek-V3, Qwen3) trains its heads jointly with the backbone over the full pretraining run of tens of trillions of tokens, thus setting the drafter quality at pretraining time. We ask whether a lightweight post-training pass on target-generated chain-of-thought is enough to reach the same expected throughput speedup on a frozen reasoning model, and study how a serving-time system built on such a checkpoint can be optimized. We present three findings. 1) On a frozen Qwen3-8B with $K{=}3$ chained MTP heads, we show that a post-training recipe with plain cross-entropy on $\approx\!2.5$B tokens reaches or exceeds the expected speedup of jointly trained MiMo-7B on math, coding and knowledge benchmarks. Our post-training recipe utilizes $10^3$-$10^4\times$ less MTP-training tokens as compared with joint pre-training of MiMO-7B MTP baseline. 2) We propose a chain-aware relaxation of draft token verification rule that allows a bounded drift from backbone language model token distribution. We show that this relaxation lifts expected speedups by $+12$ to $+16\%$ per benchmark while preserving task accuracy. 3) We propose an adaptive controller that dynamically chooses the number of MTP heads to be engaged at inference time and demonstrate recovery of upto $11$--$14\%$ loss in speedup using fixed maximum MTP draft length.

---


### 145. [Cross-Benchmark Transfer from RL on Agentic Coding Tasks](https://arxiv.org/abs/2610.00890)

**<font color=#1a73e8>作者：</font>** Sushant Mehta, Logan Ritchie, Edwin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents often fail in the last mile: they build most of a feature but drop a requirement, test only the cases their implementation already handles, break behavior that was supposed to stay intact, or validate against an unchecked assumption. We ask whether reinforcement learning (RL) on expert-built agentic coding tasks closes this gap, and whether what the agent learns transfers beyond the training distribution. We post-train Kimi K2.7 Code, a 1T-parameter (32B active) open-weight mixture-of-experts model, with RL alone on 1,700 tasks: 1,000 repository tasks graded by hidden fail-to-pass tests and by pass-to-pass tests of existing behavior, and 700 terminal tasks graded by expert-written hidden verifiers. The reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails. One epoch of GSPO on a rank-32 LoRA adapter improves pass@1 on each of the six external benchmarks we evaluated, across three agent harnesses: SWE-Bench Pro (60.1 to 64.8), DeepSWE (31.0 to 43.4), Terminal-Bench 2.1 (67.4 to 82.0), Terminal-Bench 3 (1.4 to 12.1), Terminal-Bench 4 (0.0 to 7.6), and SWE-Marathon (5.0 to 25.0). Pooled over the five independent task sets (Terminal-Bench 4 revises Terminal-Bench 3), the improvement is significant (p < 0.001), and it remains significant on the three sets released after the training data was collected (p = 0.004); the model also improves under both harnesses never used in training. Median trajectories on DeepSWE and Terminal-Bench 3 are 24-35% shorter in agent steps. The base model's failed DeepSWE runs are mostly near-misses, and on the tasks the trained model newly solves, paired trajectories show it avoiding each of the four failure modes above.

---


### 146. [Clock Diffusion: Efficient Semi-Autoregressive Continuous Diffusion Language Models](https://arxiv.org/abs/2610.00894)

**<font color=#1a73e8>作者：</font>** Yair Schiff, Omer Belhasin, Roy Uziel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent works on continuous diffusion for discrete data have demonstrated performance on par with comparable discrete diffusion models. However, these continuous counterparts lack key features that are essential to practical use as language models, namely variable-length generation and support for a key-value cache, and they still lag behind the frontier of autoregressive and discrete diffusion quality. In this work, we address these limitations. We do so by introducing a model parameterization that uses position-dependent noise schedules to define semi-autoregressive (SAR) continuous diffusion language models (DLMs). Together with efficient training and sampling algorithms, we call this framework Clock Diffusion, and we present two special cases of our method: block and sliding window generation. We then define ClockDLMs, a family of Gaussian DLMs based on sliding window Clock Diffusion that attain state-of-the-art diffusion likelihood bounds on OpenWebText, even beating the performant block SAR discrete diffusion models. ClockDLMs trained on TinyGSM also substantially outperform continuous baselines on the GSM8K benchmark and match and exceed comparable SAR discrete diffusion models. Finally, building on our parameterization, we propose more efficient samplers that we dub Cache Grab, which adapt techniques from accelerated inference in discrete diffusion, such as committing tokens whose probabilities exceed a confidence threshold and self-speculative decoding, further improving our models' quality and efficiency.

---


### 147. [When Do Biological Reasoning Models Use Their Biological Inputs?](https://arxiv.org/abs/2610.00898)

**<font color=#1a73e8>作者：</font>** Ada Fang, Nikitha Thoduguli, Lukas Fesser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological reasoning models use post-training to connect LLMs to biological foundation model representations and biological text. Their benchmark accuracy is taken as evidence that LLMs reason over these inputs. We test this assumption in six biological reasoning models across DNA, protein, and single-cell tasks. We perturb one biological input while holding the query and other inputs fixed, construct evidence conflicts that pair the foundation model representation of one genome, protein, or cell with the text of another, fit linear probes to the representations the language model receives, and analyze reasoning traces against the biological inputs. Evo2 and ESM3 contribute little to BioReason and BioReason-Pro performance on the evaluated tasks. Shuffling the DNA sequence barely changes BioReason disease prediction accuracy, and in evidence conflicts the two models follow the text in 97.9% and 99.7% of cases. Linear probes trained on the Evo2 and ESM3 representations predict the task targets, so these foundation models encode information relevant to the task, but provide limited overall performance improvement to BioReason and BioReason-Pro. In contrast, foundation model inputs contribute to ChatNT, Prot2Text-V2, and CellWhisperer performance, and differentially expressed genes in the gene sentence contribute to Cell2Sentence-Scale performance. Across SFT and RL checkpoints of BioReason-Pro and 42 BioReason checkpoints, increases in accuracy do not imply greater performance contributions from biological inputs. BioReason traces misstate nucleotide changes, while BioReason-Pro traces describe functions omitted from final predictions under evidence conflicts. We find that current post-training strategies do not ensure that foundation model representations contribute to task performance.

---


### 148. [Sharpen Before You Adapt: Data-Free Entry-State Sharpening for Test-Time Reinforcement Learning](https://arxiv.org/abs/2610.00903)

**<font color=#1a73e8>作者：</font>** Zhanming Zhang, Vinoth Selvendran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning (TTRL) adapts language models on unlabeled test problems using supervision derived from their own samples. This makes the checkpoint's \emph{entry state} consequential: a diffuse policy provides noisier self-supervision and may spend much of a limited adaptation budget merely concentrating probability mass before reliably expressing capability it already possesses. We propose \textbf{entry-state sharpening}: use data-free training \emph{before} TTRL to prepare a general-purpose checkpoint in a state that subsequent label-free adaptation can exploit more efficiently. The idea is not tied to one training recipe; different data-free objectives can move the same base model to different entry states. Across five data-free checkpoints derived from Qwen3-4B and evaluated under an identical 15-step TTRL protocol, entry policy entropy strongly rank-orders endpoint conversion efficiency, a reliability-to-reachability measure (Spearman $\rho=-0.90$; $\rho=-0.99$ after controlling for entry reachability). The contrast across objectives is striking: R-Zero remains diffuse at $3.39$ nats and finishes below the untuned base in 6/6 matched comparisons across MATH, GPQA, and AMC, whereas SPIRAL reaches $0.07$ nats and achieves the highest post-TTRL accuracy on MATH and GPQA despite its self-play stage using no math training data. An in-domain label-free self-distillation intervention further shows that the entry state can be deliberately sharpened. These results motivate treating checkpoint preparation as a \emph{state-control problem}: use data-free training to improve TTRL readiness, with entry entropy as a label-free control signal and reachable capability as the constraint.

---


### 149. [ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization](https://arxiv.org/abs/2610.00906)

**<font color=#1a73e8>作者：</font>** Sungho Park, Wonjoong Kim, Jue Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated harness optimization can substantially improve LLM agents by iteratively updating their prompts, tool interfaces, and control logic from execution feedback. However, existing methods primarily optimize how the harness is updated while largely fixing which training scenarios generate the feedback that drives those updates. As the harness evolves, the scenarios most useful for further optimization can change, suggesting that the training curriculum itself should adapt alongside the harness. We formulate this missing dimension of harness optimization as an automated curriculum learning problem and introduce ActiveSaddler. ActiveSaddler models the evolving curriculum as a non-stationary bandit with dynamically instantiated optimization targets. It abstracts recurring failures into reusable failure-pattern arms, estimates the potential learning progress from further targeting each pattern, and adaptively balances revisiting known weaknesses with exploring unseen scenarios for new ones. Optimization outcomes continually update both the set of discovered failure patterns and their priorities, allowing the curriculum to co-evolve with the harness. Experiments on GAIA2 and Terminal-Bench 2.0 show that ActiveSaddler consistently discovers stronger harnesses, improving test Pass@1 by 4.4 and 7.5 percentage points over the same harness optimizer using a scenario order fixed before optimization, respectively. Ablations further show that these gains depend on dynamically constructing optimization targets, estimating their evolving utility, and balancing continued optimization with new failure discovery. Together, these results establish automated curriculum learning as a new crucial optimization dimension for harness optimization.

---


### 150. [The Geometry of Contextual Relations: Language Models Address Facts by Order of Mention](https://arxiv.org/abs/2610.00910)

**<font color=#1a73e8>作者：</font>** Yufa Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human reasoning depends on how objects are related within propositions. \textit{How do relations organize the language representations of contextual contents?} We give an LLM a list of facts in its context (e.g., \emph{Alice eats an apple. Bob eats a pear.}) and measure how its hidden state changes when the question switches from what Alice eats to what Bob eats. Averaged over many lists, this change is a steering vector, which we call the \emph{ordinal vector}. It points to a fact by its \emph{order of mention}, the order in which the facts were stated in the context. We find that LLMs represent the fact a question asks about by its order of mention, not by the name the question contains. We state this as the \textit{ordinal addressing hypothesis}: each order of mention has a \emph{fact address} in the model's state, shared by all contexts, and a question moves the state to the fact address of the fact it asks about, while the context supplies what that fact says. Across Qwen, Gemma, and Llama, fact addresses are (1) \emph{ordered by mention}: query states are organized by the order of facts, not of names, even when one fact has multiple subjects; (2) \emph{steerable}: added to a question about the first fact of a new list, the ordinal vector makes the model answer with the second fact of that list; (3) \emph{low-rank}: they span a low-rank subspace in which the first-mentioned fact is the easiest to reach, surprisingly similar to human recall; and (4) \emph{emergent}: they are shared in late-middle layers, hold from 1.5B to 32B parameters, and form early in pretraining. Language models reach a stated fact by where it was mentioned, deepening our understanding of LLM reasoning.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
