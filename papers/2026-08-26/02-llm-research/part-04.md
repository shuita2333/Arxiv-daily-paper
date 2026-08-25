# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 151. [Mechanistic Interpretability of Chain-of-Thought Reasoning via Sequential Activation Patching](https://arxiv.org/abs/2608.22332)

**<font color=#1a73e8>作者：</font>** Murat Dura, Serkan Öztürk, Selma Tekir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate remarkable problem-solving capabilities when guided by Chain-of-Thought (CoT) prompting, yet the internal mechanisms underlying these improvements remain poorly understood. In this work, we investigate where CoT-related causal effects emerge across the generated reasoning trajectory and which attention heads carry signals that contribute to final-answer computation. Because CoT reasoning unfolds over multiple generated tokens, standard activation patching at a single static token position is insufficient to characterize these temporally distributed effects. To address this limitation, we introduce a sequential activation patching framework that traces CoT-conditioned attention-head activations across token positions and aggregates their effects using Part-of-Speech-guided analysis. We further introduce Sequential Multi-Head Patching to evaluate the joint contribution of distributed head sets, together with cross-question and random activation controls. Targeted zero-ablation experiments show that the identified heads are functionally important for successful answer generation and affect several overlapping mechanisms, including reasoning-trajectory maintenance, answer anchoring, exemplar-target separation, and numerical generation. Overall, our results provide evidence for distributed reasoning-support sub-circuits associated with CoT-conditioned computation.

---


### 152. [When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents](https://arxiv.org/abs/2608.22339)

**<font color=#1a73e8>作者：</font>** Zihan Lin, Zhenyu Chen, Jiawen Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting skills from past successes is critical for the efficient evolution of Large Language Model (LLM) agents. Prevailing agent self-evolution paradigms typically rely on a core assumption: equipping LLMs with skill memories derived from successful trajectories will monotonically improve their problem-solving capabilities. However, probe analyses reveal that extracting skills solely from successful trajectories traps the model in a \textbf{Skill Imitation Trap}. For tasks that resemble past successes but require different tools, retrieving more skills paradoxically increases the model's confidence in wrong tool calls---procedure skills raise the wrong-tool margin by $47\%$ over a memory-free baseline. To overcome this limitation, we propose \textbf{Boundary-Aware Skill Memory} (BASM), which augments each skill with explicit boundary fields---applicability conditions, risk cues, avoidance rules, and recovery notes. These fields transform each retrieved skill from an unconditional action template into state-conditioned guidance: the agent applies the skill when its conditions hold, suppresses inapplicable tool calls when they do not, and issues targeted repairs when execution fails. Across three agent benchmarks and four model scales, BASM consistently outperforms success-distilled skill-memory baselines: it improves task success rate by up to $23.8\%$ on AppWorld, accuracy by up to $5.0\%$ on BFCL, and reduces attack success rate by $4.6\%$ on AgentDojo, while simultaneously reducing average AppWorld steps by up to $6.6\%$ relative to the memory-free baseline.

---


### 153. [Mitigating Error Propagation in Chain-of-Thought: A Tree-of-Thought Framework for Smart Contract Repair](https://arxiv.org/abs/2608.22345)

**<font color=#1a73e8>作者：</font>** Jingping Zhu, Hongping Wang, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts power blockchain applications such as DeFi and NFTs. However, once deployed, they cannot be modified. Even minor bugs can result in significant financial losses. Current AI-based repair methods rely on linear reasoning, which leads to the accumulation of errors and unreliable patches. Our method combines document parsing, static analysis, and Tree of Thoughts reasoning. We first convert audit reports into structured data. Then we use Slither to locate the exact vulnerable code. Our three-step framework explores multiple repair paths simultaneously, evaluates options, and eliminates poor choices. Finally, we verify patches through compilation and manual checks. We test our method on 50 real vulnerabilities from Code4Rena. Our method achieves a 62% single success rate and an 84% top-3 success rate, outperforming ContractTinker by 12 and 6 percentage points, respectively. We also increase the proportion of fully effective patches to 44%, while reducing defective patches from 38% to 22% and invalid patches from 10% to 4%. This approach overcomes the limitations of linear reasoning and makes smart contract repair more accurate and practical.

---


### 154. [Where Cognition Lives: Dissecting Emergent from Computed Function in a Minimal Complete Cognitive Architecture](https://arxiv.org/abs/2608.22347)

**<font color=#1a73e8>作者：</font>** Francisco M. Arrabal-Campos, Francisco G. Montoya, Alfredo Alcayde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A cognitive architecture is more than the module that reasons: it must also decide how long to think and what deserves the effort. We built a minimal but complete system - a recurrent reasoner with adaptive halting, a homeostatic control field, and a value module - and asked of each part: does this function emerge from gradient descent, or must it be computed? Competence emerges. Stopping appears to emerge too, and to be worth more than everything decidable in advance, but that appearance is instrumentation: payoff at matched mean compute climbs from 0.467 (uniform) through 0.546 (difficulty) to 0.698 (ex-ante value), and the further climb to 0.921 (posterior self-observation) does not survive audit. PonderNet-style halting returns a halting-weighted mixture of hidden states while forced-depth baselines return one, and the language head is trained on the mixture alone; equalizing the readout annihilates the apparent advantage of native execution (residual +0.000 [0.000, 0.000]). Value does not emerge: trained couplings capture zero of a payoff an explicit allocator captures completely (+0.151, routing correlation +0.79), so the second-order decisions that pay must be computed, at least where value is orthogonal to content, as here by construction. On a frozen LLM actuator the same instruments show self-consistency voting to be a measured bound (+0.0236 [+0.0150, +0.0326]) and inter-sample agreement nearly worthless as a stopping signal, its mass concentrating on wrong answers. Every null we assert carries a mechanism and a positive control, and the protocol is part of the contribution. Executing our own falsifiable prediction, value under commitment pays +0.1312 [+0.1124, +0.1502] in a cliff-cost family, some seven times the smooth-family estimate - not because the cliff shifts information ex ante, but because it multiplies the attainable range fivefold (5.1x [3.4, 8.2]).

---


### 155. [Addressing the Selection Problem in Explainable AI](https://arxiv.org/abs/2608.22356)

**<font color=#1a73e8>作者：</font>** Claire Vlases, Katelyn Morrison  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) research has produced a plethora of explanation techniques, yet user studies repeatedly show that available explanations are not effective in practice. We argue that, given the siloed nature of conventional XAI, users are struggling to select the appropriate XAI technique. Viewing XAI through a philosophical lens, we offer a formalization of what we call the selection problem: the systematic failure of XAI interfaces to bridge the gap between a user's natural-language uncertainty and the explanation technique that resolves it. Following a logical premise-conclusion format, we show that conventional interfaces require users to translate their uncertainty into a technique selection, a challenging prerequisite to meet. We also propose a structural solution: a multi-agent LLM orchestration tool that translates the user's query to the proper XAI explanation technique. We provide an example of how this structural solution could be instantiated to address the selection problem.

---


### 156. [Pre-Decoding Acoustic Triage for Budgeted Vision-Language Captioning of Untrimmed Egocentric Video](https://arxiv.org/abs/2608.22359)

**<font color=#1a73e8>作者：</font>** Masoud Jalayer, Changyi Li, Yu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatically analyzing hours-long egocentric video is increasingly essential for progress monitoring, quality control, and safety in logistics, construction, and manufacturing. Yet current pipelines that process short, fixed-size windows with a vision-language model (VLM) are prohibitively expensive because cost scales with the number of model calls. To reduce this cost, prior work proposes triage policies to select which windows merit a VLM invocation. However, these policies either sample uniformly or rank windows using visual features, which ironically requires the video decoding that the budget constraints are meant to avoid. We propose audio-first triage: select windows using the lightest modality, scored before any video frame is decoded, so the approach composes naturally with token compression or quantization. The novelty lies in the objective, not the representation: rather than a per-frame sound-event detector, we train the selector to trigger once per action. This objective shift improves action coverage by 4.0-10.8 percentage points across all evaluated call rates, using frozen AudioSet-pretrained features without domain-specific sound-event labels. Using fewer than half of the available calls, the triage cuts 9-20% of VLM calls at matched coverage on EPIC-KITCHENS-100 (EK-100), surpasses uniform sampling through the mid-range on Ego4D over 247 clips, and outperforms two recent visual keyframe selectors. Code, the reference implementation and every results file this manuscript reads are at this https URL.

---


### 157. [Analyzing and Mitigating Cross-Lingual Degradation in Multilingual Medical VQA](https://arxiv.org/abs/2608.22363)

**<font color=#1a73e8>作者：</font>** Jingbo Wang, Sendong Zhao, Haochun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical visual question answering (VQA) is a crucial task in clinical AI, yet its evaluation has so far centered almost exclusively on English, limiting its relevance to linguistically diverse patients and clinicians. Recent multilingual medical VQA benchmarks show that large vision-language models (LVLMs) degrade in non-English languages, but lack a fine-grained analysis of how cross-lingual variation affects the distinct capabilities that medical VQA requires. To this end, we construct a multilingual medical VQA benchmark over eight languages, organized into four representative scenarios that isolate the core capabilities medical VQA requires. Evaluating five open- and closed-source LVLMs, we find that cross-lingual degradation is not uniform but highly scenario-dependent. We therefore propose MedVL-XLRepE, a training-free scenario-aware representation engineering method, leveraging LVLMs' superior English medical VQA capability to steer non-English representations toward their English counterparts at inference time. Across three LVLMs and eight languages, MedVL-XLRepE consistently mitigates cross-lingual degradation, with gains of up to 6.33\%.

---


### 158. [WAM-OPD: On-Policy Distillation for World Action Models](https://arxiv.org/abs/2608.22364)

**<font color=#1a73e8>作者：</font>** Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) couple visual future prediction with robot action generation, but accelerated students can lose task capabilities during distillation and later encounter states that are poorly represented by offline data. We study whether on-policy distillation (OPD) can repair such a student without requiring sparse-reward reinforcement learning. We introduce WAM-OPD, a deployment-consistent post-training recipe for a video-first WAM. The student acts in the environment and therefore determines the history distribution. A frozen teacher labels those student histories with coherent video and action targets, while the student action branch is trained under its own generated video plan, as it is at deployment. Joint video and action losses update lightweight adapters in the shared backbone, together with an action flow-matching regularizer. In preliminary RoboTwin 2.0 studies on two tasks, the released one-video/one-action-step Flash-WAM improves from 0.0% to 58.3% success on HANDOVER MIC, and from 16.7% to 33.3% on PUT OBJECT CABINET. These task-specific results are an initial capability proof rather than evidence of broad or uniform generalization. They nevertheless suggest that dense teacher supervision on student-induced histories is a promising post-training interface for video-first WAMs.

---


### 159. [When Do VLMs Help Arabic Manuscript OCR? A Cross-Dataset Study](https://arxiv.org/abs/2608.22366)

**<font color=#1a73e8>作者：</font>** Moshiur Farazi, Firoj Alam, Abderrahmane Maaradji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly being used for document understanding, yet their role in Arabic and Islamic manuscript recognition remains underexplored. To address such a gap in this paper, we evaluate traditional OCR, general-purpose VLMs, Arabic-specialized VLMs, and OCR-conditioned VLM correction across eight Arabic text datasets spanning historical manuscripts, aged printed books, clean print, multi-domain documents, and handwriting. The results show that no single approach dominates across setups. On line-level historical manuscripts, VLMs are close to Tesseract; on page-level manuscript images, they perform better; and in several settings, an OCR-conditioned corrector improves over both standalone OCR and standalone VLMs. The central finding is an OCR-prior recoverability principle: OCR conditioning helps when the OCR output remains visually and textually recoverable, providing anchors that the VLM can refine against the image. It improves recognition on aged print, clean print, mixed-domain Arabic, and some Naskh manuscripts, but degrades performance when the prior is script-mismatched or systematically misleading, as in Maghribi manuscripts and realistic student handwriting. Additional diagnostics show that Arabic VLM-OCR is sensitive to diacritics, preprocessing, generation budget, and repetition loops. These findings support an adaptive OCR-VLM workflow that routes pages according to script, OCR-prior recoverability, length diagnostics, and failure-mode indicators.

---


### 160. [Context-Aware Cluster Decoding: Semantic Anchor-Driven Coherence in dMLLMs](https://arxiv.org/abs/2608.22367)

**<font color=#1a73e8>作者：</font>** Yikai Zhao, Qiyan Zhao, Jiaquan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion multimodal large language models (dMLLMs) frequently produce long-form outputs marred by semantic drift and repetition, with quality generally degrading as output length increases. We identify two structural deficiencies in existing decoding methods as primary drivers of these failures: confidence-based scoring ignores decoded-neighbor support, and block partitioning prevents access to high-readiness semantic anchors, together causing tokens to be committed before their local context is sufficiently established. We propose \ours{} (\textbf{C}ontext-\textbf{A}ware \textbf{C}luster \textbf{D}ecoding), a training-free decoding method that scores each masked position by a multiplicative composite of softmax confidence and neighbor proximity, promoting contextually ready tokens above isolated candidates while suppressing low-confidence positional noise, operating block-free to keep high-readiness anchors globally accessible. \ours{} further applies architecture-aware calibration to handle confidence heterogeneity induced by diverse visual integration strategies. Experiments on three dMLLMs across four benchmarks demonstrate consistent quality gains and hallucination reduction over Original, with larger gains in several longer generation settings, highlighting the importance of neighbor support and visual integration strategy for future dMLLM decoding method design. Our code is openly available at this https URL.

---


### 161. [LiST: Local-Simplex Test-Time LoRA Fusion](https://arxiv.org/abs/2608.22370)

**<font color=#1a73e8>作者：</font>** Yihua Shao, Jia Li, Siyu Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Task-specific LoRA adapters offer a modular way to specialize large language and vision-language models. However, existing adapter composition methods are mostly static and cannot adapt to individual test inputs. To address these issues, we propose \textbf{LiST}, a label-free test-time LoRA fusion framework that converts an existing LoRA bank into a target-conditioned local simplex and searches sample-specific fusion weights at inference time. LiST builds joint task representations from LoRA parameter anchors and prompt-level behavior vectors, retrieves neighboring adapters as a local search space, and performs branch-preserving fusion without updating the backbone or adapters. Candidate weights are selected by a prompt-level energy with prior, geometric, and stochastic-consistency constraints, and are deployed only when they pass a safe acceptance rule. Otherwise, LiST falls back to a target-conditioned prior. Experiments on multimodal and language benchmarks show that LiST outperforms static LoRA merging and conventional test-time adaptation baselines, while preserving task-specific adapter utility and improving robustness on unseen tasks.

---


### 162. [Can Large Language Models "Hyper-Thread"?](https://arxiv.org/abs/2608.22376)

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models generate tokens sequentially, but can they execute multiple tasks concurrently while forming each token? Broader attention allocation may provide a mechanism for such task concurrency. Existing approaches to scaling inference primarily rely on longer generations, more samples, or additional verification stages, while attention dispersion is often treated as a signal of interference or error. Task concurrency within serial generation therefore remains underexplored. We propose the Model Hyper-Threading Hypothesis and evaluate its predictions using multiple coordinated tasks that share state within the same problem. We design three conditions (Baseline, Serial Functional Scheduling, and Concurrent Functional Loading) and evaluate their benefits and costs using accuracy, output-token distributions, and attention metrics. On an AIME 2025 development set, Concurrent Functional Loading achieves the highest accuracy. Relative to Serial Functional Scheduling, its typical output length is similar and it is shorter on most problems, while exhibiting greater attention dispersion and higher task-relevant coverage, albeit with a heavier output-length tail. Within-step concurrency and its causal mechanism still require direct tests. Our results show that more dispersed attention can coexist with higher accuracy, providing preliminary behavioral and correlational evidence for the hyper-threading hypothesis. These findings motivate a shift in perspective on inference scaling from "generating more tokens" toward "having each generation step carry more tasks," pointing to a new avenue for improving reasoning performance.

---


### 163. [SchemaGUI: A Schema-Driven Benchmark for Controllable GUI Generation Evaluation](https://arxiv.org/abs/2608.22390)

**<font color=#1a73e8>作者：</font>** Jiarui Dong, Yin Cai, Zhouhong Gu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong potential in graphical user interface (GUI) generation, but reliable evaluation remains challenging due to uncontrolled data distributions, noisy annotations, and limited layout scenario coverage. To address this, we propose SchemaGUI, a template-based benchmark for controllable GUI generation evaluation. By synthesizing paired natural language instructions and deterministic function-call references from parameterized interface schemas, SchemaGUI can generate thousands of deterministically annotated tasks in seconds without human labeling. Based on 1,000 evaluated instances per scenario and language across six representative bilingual scenarios, we benchmark five mainstream models, including the Qwen3.5 family, Qwen3-Coder-30B, and DeepSeek-R1. Our extensive analysis reveals three key insights. First, precise geometric spatial control remains an important bottleneck; while scaling Qwen3.5 from 4B to 27B improves Schema Feasibility from 91.56% to 99.63%, the Geometry score improves more modestly (from 67.05% to 75.30%). Second, generation difficulty is highly sensitive to layout complexity, with current LLMs excelling at simple sequential arrangements but suffering severe coordinate drift in dense grids and multi-region compositions. Third, thinking mode increases token consumption while generally reducing GUI Score, particularly for smaller models.

---


### 164. [Don' t Box Me In: Dynamic Cultural Adaptation and Cognitive Tracking for Social Understanding](https://arxiv.org/abs/2608.22411)

**<font color=#1a73e8>作者：</font>** Chongyuan Dai, Yaling Shen, Shengeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social interaction increasingly takes place in multicultural settings, where individuals may draw on multiple cultural influences and adapt their communicative behavior across contexts. Despite recent advances in equipping Large Language Models (LLMs) with social understanding capabilities, existing approaches often model culture as a static demographic attribute, limiting their ability to accommodate hybrid and dynamically expressed communicative preferences. Therefore, in this paper, we propose \textbf{DyCAC}, a training-free framework that achieves fluid social alignment by incorporating \underline{Dy}namic \underline{C}ultural \underline{A}daptation with continuous \underline{C}ognitive tracking. Rather than inferring a fixed cultural identity, DyCAC models culturally relevant communicative preferences as a time-varying mixture of population-level cultural reference profiles. This reference-based representation is further calibrated using dialogue-style signals observed in the ongoing interaction, enabling the model to capture both composite cultural influences and turn-level shifts in communicative behavior. In parallel, a memory module driven by Theory of Mind (ToM) continuously tracks the cognitive states of the interlocutor. Extensive experiments on interactive social and cultural benchmarks demonstrate the superiority of our approach. The proposed framework outperforms existing baselines, exhibiting enhanced social intelligence and broad adaptability across varied multicultural contexts.

---


### 165. [LLMs for Survey Text Analysis - A Performance Comparison Between Humans and GPT-5 on Inductive Content Analysis](https://arxiv.org/abs/2608.22417)

**<font color=#1a73e8>作者：</font>** Leonardo Bergmann, Renata Gheorghiu, Ana Gvritishvili 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support text analysis in qualitative research, yet evidence on their performance in inductive content analysis remains limited. This study compares human and LLM-based inductive coding of open-ended survey responses from 903 answers across six variables from a European PhD student survey. Five human coders performed inductive content analysis following a standardized coding scheme, while an LLM (GPT-5.4) conducted the same task using an established prompting procedure. Agreement between human and LLM outputs was assessed using the Adjusted Rand Index (ARI). Results showed an alignment between humans and the LLM, with ARI values of 0.61 for coding and 0.54 for theme generation. These values were close to the internal consistency of coding and theme results within humans (ARI = 0.68) and the LLM (ARI = 0.76). Agreement varied widely across variables, with low within-entity consistency consistently linked to low between-entity agreement, underscoring the role of data characteristics and individual performance in reliability. Overall, the findings suggest that LLMs can approximate human coding in this case-specific setting, particularly at the coding level, and may serve as a scalable support tool for inductive qualitative analysis.

---


### 166. [All four leading LLMs talk more than they listen to personality-verified synthetic help-seekers](https://arxiv.org/abs/2608.22425)

**<font color=#1a73e8>作者：</font>** Pablo A. Fonseca, Raquel Rodríguez-Carvajal, Rafael A. Calvo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly consulted at moments of distress, yet single-turn benchmarks neither test sustained exchanges nor distinguish between users. We built a personality-aware evaluation in which four widely used models advised several synthetic help-seekers, each given a psychometrically specified profile, in an acute crisis: a caregiver learning of a relative's dementia diagnosis. Auditors blind to the profile prompt recovered the specified bands from dialogue alone with high agreement on every instrument (ICC(2,4) = 0.91; 0.79-0.96 by instrument; band-score r = 0.78), as expected for the Big Five but equally for coping style, coping self-efficacy, resilience and reactance, which the lexical approach never covered. Such evaluation therefore reaches beyond the Five Factor Model to motivational, regulatory and self-appraisal dispositions. The four models were not distinguishable on emotion stabilisation and failed alike, sharing three modes: verbosity, a talk-to-listen ratio above one, and problem-solving before the situation had been explored.

---


### 167. [Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding](https://arxiv.org/abs/2608.22429)

**<font color=#1a73e8>作者：</font>** Changjiang Jiang, Qiannian Zhao, Lei Xin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally relational visuals (e.g., charts and visual tables) where strict relative spatial arrangements bind textual elements. Without external tools, standard MLLMs struggle with such fine-grained visual reasoning tasks. To address these issues, we propose Think with Structured Grounding (TwSG), a novel fine-grained image perception framework designed to internalize complex images's tool-use capabilities within the model. TwSG distills the benefits of multi-step reasoning and micro-cropping into a single efficient forward pass during inference. Specifically, we use an MLLM to identify key regions guided by ground-truth answers, and then prompt a teacher model to generate high-quality visual question-answering (VQA) data. These fine-grained, region-based supervisory signals are subsequently distilled back into the full-image representation. Our training pipeline consists of two stages: (1) a cold-start supervised fine-tuning (SFT) phase using multi-turn data with focused area descriptions to foster complex reasoning and error recovery; and (2) a reinforcement fine-tuning (RFT) phase driven by a novel process reward mechanism, TL-GRPO, which encourages strategic reasoning. Extensive experiments across various MLLM architectures demonstrate that TwSG reduces inference latency while substantially improving accuracy and robustness, endowing models with native fine-grained region description and flexible reasoning capabilities.

---


### 168. [Rank Reversal in Multilingual LLM Judges: A Label-Free Double-Centering Calibrator](https://arxiv.org/abs/2608.22432)

**<font color=#1a73e8>作者：</font>** Alhasan Mahmood, Samir Abdaljalil, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual LLM judges produce different evaluator-backbone rankings depending on the prompt language: on an eight-language Agent-as-a-Judge benchmark, the top-ranked backbone alternates across English, Arabic, Chinese, Hindi, Japanese, Spanish, Turkish, and Swahili, and 7 of 15 backbone pairs show statistically significant pairwise rank reversal. We treat this as a measurement problem. The multilingual judge score decomposes additively into task difficulty, backbone skill, and a language-backbone interaction term, the last of which is recoverable without human labels by double-centering the cell-mean score matrix. We make this estimator (\textbf{Consensus-Based Calibration}, CBC) explicit, give an $O(1/\sqrt{n})$ finite-sample concentration bound with variance constant $(1-\tfrac{1}{m})(1-\tfrac{1}{k})$, and show that it is unbiased even when task-language interactions are present. Across 7{,}920 judge runs (6 backbones, 8 languages, 55 tasks, 3 frameworks), CBC raises held-out cross-task rank consistency $\tau$ from 0.650 to 0.902 and agrees with the held-out additive-model oracle in 100\% of per-language decisions versus 68.5\% raw; these are consistency diagnostics, not human-grounded correctness measures. On a separately collected M-RewardBench panel (7 languages, 1{,}500 items per language, 10{,}500 language-item instances, 5 evaluators), panel agreement with the public human gold preferences rises from 68.7\% to 76.6\% (gain 7.9 percentage points, 95\% CI $[6.0, 9.9]$), our strongest external evidence of downstream usefulness. The estimator is the standard two-way ANOVA interaction-recovery operation under sum-to-zero contrasts; our contribution is its application as a label-free post-hoc calibrator for multilingual LLM judges, an explicit finite-sample concentration bound, and an unbiasedness result that holds even under task-language misspecification.

---


### 169. [When Persona Simulations Are Informative: Graph-Structured Signals for Pluralistic Opinion Sensing](https://arxiv.org/abs/2608.22438)

**<font color=#1a73e8>作者：</font>** Taehyeon An, Jaehyeong Park, Donghyuk Shin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persona-conditioned large language models (LLMs) are increasingly used to simulate survey responses across diverse domains. However, apparent response variation can reflect unconditioned model priors or token sampling noise rather than systematic persona conditioning. We argue that persona-conditioned variation is informative when semantically similar personas exhibit concordant response shifts. To operationalize this principle, we introduce Persona-Conditioned Informativeness (PCI), an unsupervised diagnostic metric that measures whether semantically similar personas deviate in concordant directions relative to item-level sample baselines. By modeling personas as a similarity graph, PCI uses Local Moran's I to quantify local spatial coherence and extract compact persona subsets without using construct labels. To evaluate PCI without external human benchmarks, we test its ability to recover established latent value structure using the 57-item Portrait Values Questionnaire-Revised (PVQ-RR). Confirmatory factor analysis (CFA) shows that a PCI-selected 10% subset substantially improves overall construct recovery relative to response-stability and random selection. These findings support PCI as a principled internal diagnostic for screening synthetic respondents in survey pipelines.

---


### 170. [Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations](https://arxiv.org/abs/2608.22444)

**<font color=#1a73e8>作者：</font>** Isotta Magistrali, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

---


### 171. [From Exposure to Expectation: Frequency, Surprisal, and Language Across Development in Spanish](https://arxiv.org/abs/2608.22452)

**<font color=#1a73e8>作者：</font>** Francisco Portillo López  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal, the negative log-probability a language model assigns to a word given its preceding context, reliably predicts adult reading times. Does it contribute as much to explaining when children acquire individual words? Frequency reflects a learner's cumulative exposure to a word, whereas surprisal reflects how predictable a single occurrence is given its context. We investigate this question across two corpus-based studies of Spanish.
In Study 1, we modeled age of acquisition (AoA) for 225 Spanish nouns using lexical frequency and contextual diversity from child-directed speech, plus surprisal from three language models differing in architecture and training language (BETO, BERTIN, mGPT). Frequency strongly predicted AoA (r=-.597, p<.001); surprisal added little beyond frequency and word length, including in a naturalistic-context analysis.
In Study 2, we modeled adult fixation durations in the Chilean Spanish subsample of the Multilingual Eye-movement Corpus (MECO Wave 2), using mGPT surprisal alongside two independent frequency measures. Surprisal robustly predicted longer fixation durations after controlling for frequency and word length, consistent across both frequency sources. A matched word-type-level comparison showed the surprisal-behavior association was stronger in reading than in acquisition (z=3.63, p<.001).
The findings suggest cumulative lexical exposure and contextual predictability play different roles across the language trajectory: frequency is particularly informative about when early lexical representations are acquired, whereas surprisal captures moment-to-moment processing difficulty in an already-established linguistic system. We discuss this pattern in relation to usage-based and entrenchment-based accounts of lexical development and to the evaluation of language models as models of human language behavior.

---


### 172. ["I want to be pushed, I want to grow": Enabling social workers to design evaluations of LLM augmentation in their work](https://arxiv.org/abs/2608.22459)

**<font color=#1a73e8>作者：</font>** Anna Kawakami, Chloe Qianhui Zhao, Renee Shelby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Workers are increasingly asked to adopt AI systems to assist their work, yet are rarely given a voice in defining what meaningful AI augmentation should look like or how to evaluate for it. In this paper, we propose worker-driven AI measurement---a bottom-up approach to AI evaluation where workers collaboratively shape decisions about which tasks AI should augment, what "successful" augmentation looks like, and how it should be measured. We explore how to support this through a case study with 19 workers from a local school social work organization. Through a series of eight workshops, workers iteratively develop their own measurement goals for AI evaluation, systematize these goals, and then design a benchmark to capture how effectively an LLM can "challenge" them to reflect on their own assumptions and biases in the context of their day-to-day work. Workers collaboratively design and refine an LLM-as-a-judge rubric based on their professional and lived expertise. In validations of the worker-created benchmark, we find that there is strong agreement between worker and LLM judge ratings and that the resulting benchmark can differentiate performance across six state-of-the-art LLMs. Based on our case study, we discuss opportunities for future work to support worker-driven AI measurement as a complementary approach to existing top-down AI evaluation approaches.

---


### 173. [The Variance of Thought: Policy Variance, Critical Forks, and Local Credit Assignment](https://arxiv.org/abs/2608.22467)

**<font color=#1a73e8>作者：</font>** Yingru Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon language-model tasks --- multi-step reasoning and tool-using agents alike --- are limited by credit assignment. We analyze it through the policy variance $\sigma_\pi^2(s)=\operatorname{Var}_{a\sim\pi}[Q_{\pi}(s,a)]$, which in a deterministic MDP is the sole source of return variance and is injected in discrete pulses at states we call critical forks. Three results follow. (i) Policy variance is a discovery budget: observing an action of advantage $c$ requires $\Omega(c^2/\sigma_\pi^2(s))$ draws, a bound that is exact on the canonical two-point fork. (ii) Policy variance is bounded by the policy's Gini dispersion, $\sigma_\pi^2(s)\le 1-\|\pi(\cdot|s)\|_2^2$, a rollout-free necessary condition for criticality computable from logits alone. (iii) The remaining horizon sets the estimation cost: at a fork whose downstream success probability is $P$, the Monte Carlo advantage estimate has signal-to-noise ratio of order $\sqrt{P}$, so its sample cost scales as $1/P$ --- a cost that branched sampling shares. Bootstrapping removes it by converting a product of survival probabilities into a sum, provided the value representation is multiplicatively accurate, which argues for log-value parameterization.

---


### 174. [Small Reasoning Models are Instruction Followers in Function Calling](https://arxiv.org/abs/2608.22472)

**<font color=#1a73e8>作者：</font>** Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work demonstrates that LLMs achieve superior accuracy in function calling in instruction-following contexts (i.e., standard user-assistant interactions) rather than a tool calling context. We introduce Instruction-Followed Function Calling (IFFC), a novel framework that decouples function-calling logic from the primary LLM and delegates it to a dedicated smaller model operating within the instruction-following paradigm. Our method consistently outperforms both native function calling (NFC) and prompt-based function calling (PFC) baselines, with particularly strong gains on reasoning-oriented LLMs. Furthermore, we demonstrate that IFFC maintains robust performance under aggressive quantization, enabling efficient on-device deployment without significant accuracy degradation. This work establishes a new paradigm for reliable, resource-efficient function calling in edge-computing scenarios.

---


### 175. [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning](https://arxiv.org/abs/2608.22479)

**<font color=#1a73e8>作者：</font>** Jun Chen, Yongchao Liu, Pengyu Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enables LLMs to access external knowledge for answering knowledge-intensive questions. For complex multi-hop questions, multi-turn retrieval-augmented reasoning extends RAG into an iterative process that repeatedly searches for and integrates evidence across documents. However, existing reinforcement-learning (RL) approaches for agentic RAG are typically optimized with final-answer rewards, which provide sparse supervision and overlook whether the model actually retrieves the required evidence chain. We present \textsc{GTA-RAG}, a graph-trajectory-augmented RL framework for multi-turn retrieval-augmented reasoning. From an entity--document graph, we sample connected document paths, synthesize multi-hop QA trajectories, and validate them with the deployed retriever to obtain executable trajectory-level supervision. We then optimize the retrieval policy with Group Relative Policy Optimization (GRPO) and a trajectory-guided reward that encourages both accurate answers and acquisition of target evidence documents, followed by answer-reward training on natural QA instances. Experiments on three multi-hop and two simple QA benchmarks show that \method{} consistently outperforms RL-based RAG baselines with both Qwen2.5-3B and Qwen2.5-7B backbones, while substantially improving evidence-chain coverage. Our code is available at this https URL.

---


### 176. [Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models](https://arxiv.org/abs/2608.22483)

**<font color=#1a73e8>作者：</font>** Toghrul Abbasli, Kentaroh Toyoda, Yuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly support decision-making in high-stakes domains, but they often hallucinate and express confidence that is misaligned with factual correctness. Response-level confidence is a coarse signal: a single generation can mix correct and incorrect statements, so a single number is not actionable for users that must accept, reject, or verify individual pieces of information. We study claim-level confidence calibration as a decision-relevant uncertainty signal: each response is decomposed into atomic, verifiable claims, and each claim is assigned a calibrated confidence using inference-time signals from consistency across samples and self-verification. Our framework operates in closed-box settings (no logits, no fine-tuning) and applies post-hoc calibration directly at the claim level, enabling selective intervention such as evidence retrieval or human review for low-confidence claims. Across TriviaQA and TruthfulQA we evaluate seven baselines on six recent models (Llama-3.1, Mistral, Qwen2.5, DeepSeek-R1, GPT-4, GPT-4o), and show that claim-level decomposition combined with post-hoc calibration reduces expected calibration error on factual questions while exposing failure modes on adversarial false-premise questions where decision-makers most need reliable uncertainty estimates.

---


### 177. [HeatTok: Enhancing Remote Sensing Image Understanding via Thermodiffusion-based Tokenization](https://arxiv.org/abs/2608.22485)

**<font color=#1a73e8>作者：</font>** Yingying Yan, Jiaqi Tang, Wei Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current visual tokenizers in Multimodal Large Language Models (MLLMs) predominantly rely on patch-based partitioning, which causes severe semantic mixture and object fragmentation in remote sensing imagery due to the irregular contours of geo-objects. Moreover, existing adaptive methods struggle to extract precise object-level tokens and lack dedicated geometric positional encodings for irregular regions. In this paper, we propose HeatTok, a semantic-aware tokenizer driven by thermodiffusion aggregation. Inspired by the physical principles of heat conduction, HeatTok adaptively merges adjacent homogeneous regions to generate semantically independent, object-aligned irregular tokens. To enable MLLMs to perceive these irregular shapes, we design the Gaussian Multimodal Rotary Positional Embedding (G-MRoPE), which models token spatial distributions via 2D Gaussians and explicitly injects center, scale, and orientation cues. Extensive evaluations on the VRSBench and EarthVQA datasets demonstrate that HeatTok effectively preserves object-level semantic integrity and achieves state-of-the-art performance under a reasonable token budget. The code is available: this https URL.

---


### 178. [Learning Sample-wise Rank-aware Interpolation Weights for Composed Visual Data Retrieval](https://arxiv.org/abs/2608.22500)

**<font color=#1a73e8>作者：</font>** Boseung Jeong, Taegyu Park, Donghyeon Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> At the heart of composed visual data retrieval is the fusion of a reference visual input and a textual modification into a single query. While current state-of-the-art methods utilize multimodal large language models for this fusion, their complexity introduces prohibitive querytime latency, limiting their scalability. We instead revisit the efficacy of simple linear interpolation within an embedding space, and introduce SRAIN, the first framework that dynamically predicts query-specific interpolation weights. The key challenge lies in the fact that the quality of an interpolation weight should be measured by the interpolated embedding's discriminability from negatives as well as its proximity to true targets; this makes collecting and predicting optimal weights intractable. We overcome this bottleneck through two key innovations: batch-wise rank-aware weight estimation during training, and a compact memory bank that synthesizes hard negatives during inference. SRAIN achieves the best in composed video retrieval and matches the current state of the art in composed image retrieval, all while substantially reducing querytime latency compared to MLLM-based alternatives.

---


### 179. [Kernel Token Contradiction: a Fast and Principled Approach for LLM Claim Uncertainty Quantification](https://arxiv.org/abs/2608.22506)

**<font color=#1a73e8>作者：</font>** Jérémie Dentan, Alexi Canesse, Mahammed El Sharkawy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Claim-level Uncertainty Quantification (UQ) aims to mitigate the lack of reliability of Large Language Models (LLMs) by evaluating the factuality of each claim in their outputs. We introduce Kernel Token Contradiction (KTC), a lightweight approach to compute claim-level UQ under realistic white-box conditions. KTC represents the candidate tokens involved in LLM generation as a positive semi-definite kernel that integrates both the LLM's conditional distribution and a token contradiction score. We then use the Von Neumann entropy to quantify the uncertainty of this kernel. To estimate token contradiction, we develop a new approach based on frequency statistics from the Wikipedia corpus. Although CPU-only, our approach achieves over an 8.2x speedup compared to state-of-the-art GPU-accelerated methods based on cross-encoders, and over a 65x speedup compared to CPU-only methods with comparable performance. Our evaluation spans two benchmarks across four European languages and 16 different models. KTC not only matches the average performance of existing methods but also outperforms them in high-precision regimes. This combination of computational efficiency and accuracy makes real-time monitoring of LLM outputs practical in production.

---


### 180. [From Detrimental to Beneficial: Dynamic Influence-based Valuation and Editing](https://arxiv.org/abs/2608.22522)

**<font color=#1a73e8>作者：</font>** Adrian Nyakairu, Hongfu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data valuation is a cornerstone of data-centric learning, where prior efforts primarily focus on designing algorithms to classify training samples as either beneficial or detrimental for the learning task. However, leveraging these valuation estimates for subsequent data intervention remains underexplored; conventional approaches typically discard or downweight harmful samples, thereby underutilizing available data resources. In this paper, we present Dynamic Influence-based Valuation and Editing (DIVE), a novel and efficient framework that dynamically estimates sample values at the batch level and transforms detrimental data into beneficial contributions. Rather than altering the raw data, DIVE operates at the optimization level by strategically reversing the gradient directions of harmful samples during training, ensuring seamless integration with standard learning procedures with minimal overhead. Extensive empirical evaluations demonstrate that DIVE consistently improves classification performance, maximizes data efficiency, stabilizes optimization, and effectively generalizes to large language model fine-tuning.

---


### 181. [Stress Testing Unlearning Algorithms](https://arxiv.org/abs/2608.22527)

**<font color=#1a73e8>作者：</font>** Noam Diamant, Ethan Fetaya, Neta Glazer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, machine unlearning, the removal of specific training data influence from a model, has gained increasing attention. In large language models (LLMs), unlearning is particularly challenging due to the ambiguity of inputs and outputs. Con- sequently, rigorous evaluation is critical for assessing both safety and utility, and for driving progress in unlearning meth- ods. We identify two key shortcomings in existing unlearning benchmarks: (1) they do not actively test whether unlearned information can still be forcibly extracted, and (2) they fail to evaluate performance preservation on boundary questions, be- nign queries that are semantically close to the unlearned con- tent. Here we introduce WMDP++, an extension of WMDP that addresses these gaps by incorporating targeted extrac- tion of unlearned information and systematic evaluation on boundary questions. WMDP++ provides a more stringent and informative benchmark for evaluating unlearning in LLMs.

---


### 182. [CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories](https://arxiv.org/abs/2608.22533)

**<font color=#1a73e8>作者：</font>** Zheyuan Deng, Binghang Lu, Hanqi Feng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous computer-use agents are increasingly applied to long-horizon tasks requiring coordinated application calls, persistent state tracking, and verifier-sensitive writes, yet they remain prone to procedural failures: misreading application state, tool semantics, or task progress. Procedural memory promises more consistent decisions and less redundant exploration, but constructing high-quality memory without model training remains challenging. We introduce CONTRAMEM, a source-flexible, training-free framework for self-evolving procedural memory that treats same-task outcome variation as supervision: differences in correctness, efficiency, recovery, and failure modes expose outcome-relevant procedural distinctions, distilled into a compact bank of app-level Function Cards and task-level Skill Cards that evolves through localized curation rather than append-only accumulation or whole-bank rewriting. On held-out GAIA2/ARE computer-use tasks, CONTRAMEM more than doubles the success rate across the three source-model targets (26.2% to 55.3%), with consistent per-model gains (GPT-5.5: 27.5 to 61.0; Claude Sonnet 4.6: 28.0 to 52.5; DeepSeek V4 Pro: 23.0 to 52.5). The same bank transfers unchanged to the unseen Qwen3.7 Plus (18.5 to 35.5), indicating transferable procedural knowledge rather than model-specific behavior. The same construction carries over unchanged to AppWorld, beating both no memory and its own single-source self-memory variant for all three mid-tier agents on both public test splits. Under a matched trajectory budget, heterogeneous multi-model trajectories yield stronger memory than self- or same-model multi-rollout memory: the margin comes from contrastive behavioral diversity, not stronger source agents or more sampling.

---


### 183. [BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning](https://arxiv.org/abs/2608.22557)

**<font color=#1a73e8>作者：</font>** Md Toufikuzzaman, Ahmad Mousavi, Dongwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing LLM unlearning methods struggle with robustness: unbounded forget losses degrade model coherence, fixed-weight balancing cannot adapt as retain difficulty shifts mid-training, and methods that work on one benchmark falter under scaling or repeated application. We propose BLADE, a constrained bilevel framework whose three mechanisms give smooth, predictable control over the optimization landscape: a clamped-entropy forget loss whose gradient is exactly zero once a token reaches sufficient uncertainty; an asymmetric augmented Lagrangian that permanently ratchets retain protection after any violation; and a bilevel structure confined to LoRA adapters that repairs retain damage before each forgetting step. BLADE dominates across three benchmark families, improving average composite scores over the strongest baselines by $6$% on TOFU, $9$% on MUSE Books, and $7$% on KnowUndo, and it remains stable under $4\times$ scaling and $4$ sequential unlearning steps on MUSE News where the best competing method collapses entirely.

---


### 184. [ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation](https://arxiv.org/abs/2608.22559)

**<font color=#1a73e8>作者：</font>** Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubrics aim to make language-model evaluation transparent by decomposing response quality into interpretable criteria. However, natural-language rubrics are often ambiguous, require black-box LLM judges, and typically assume criteria aggregate independently through linear weighted sums, limiting their ability to capture dependencies, alternatives, penalties, and override conditions. We propose ExecRubrics, a framework for representing rubrics as compact executable programs. ExecRubrics encodes evaluation logic as verifiable Python scoring functions, giving natural-language rubric intent an operational semantics: a fixed decision procedure that can be inspected, executed, and edited. On three long-form response benchmarks-HealthBench, HelpSteer, and ArgQuality-we show that ExecRubrics can substitute for expensive black-box judges in ranking preferred over dispreferred responses, matching or improving NL rubric baselines with best preference accuracies of 53%, 78%, and 92%, respectively, while reducing evaluation latency by up to 320 times. We show that incorporating external logic and resources from text processing libraries such as NLTK and spaCy further improves preference accuracy. Our results suggest a novel way of looking at evaluation, by offering a faster, more explainable, and less ambiguous alternative to black-box rubric evaluation, particularly in high-stakes domains such as healthcare and banking where precision and auditability are critical.

---


### 185. [From Diagnosis to Redesign: Using Quantitative Ethnography to Improve Multi-Agent LLM Reasoning](https://arxiv.org/abs/2608.22566)

**<font color=#1a73e8>作者：</font>** Vedant Khatri, Anthony Cusimano, Zachari Swiecki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems are designed to improve reasoning by decomposing tasks across multiple agents with specialized functions, but the presence of multiple agents does not inherently guarantee coherent reasoning or outputs that align with task objectives. This paper introduces a quantitative ethnographic (QE) approach for diagnosing and redesigning multi-agent LLM systems based on the discourse produced through agent interactions. We test this approach using automated essay scoring as an example context, applying Epistemic Network Analysis (ENA) to model a five-agent multi-agent debate system and examine differences between debates that produced correct versus incorrect scoring decisions. Results show that, in the initial system, correct scoring decisions were characterized by rubric-grounded justification, agreement, and elaboration. Incorrect scoring decisions, in contrast, were characterized by extended proposition-challenge-response exchanges that were less consistently tied to rubric criteria. We then used the findings to revise the agents' prompts. The revised system improved exact scoring accuracy from 27.78% to 40.28% and shifted the discourse of incorrect debates toward the rubric-grounded pattern of correct ones, making the two nearly indistinguishable. Based on these results, we argue that QE can support a diagnostic-to-redesign loop for AI reasoning by tracing how patterns of agent interaction relate to system performance, informing prompt redesign, and evaluating whether those redesigns change both outcomes and interaction patterns.

---


### 186. [Hybrid Panels: Toward Human-AI Collaboration in Survey Research](https://arxiv.org/abs/2608.22582)

**<font color=#1a73e8>作者：</font>** Julia Romberg, Tobias Gummer, Gabriella Lapesa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale population surveys are essential for generating robust social and scientific insights, yet they face significant challenges, including declining response rates, increasing data collection costs, long delays between data collection and data provision, and the risk of nonresponse bias. Advances in artificial intelligence (AI) have opened up new opportunities for AI-supported survey infrastructures where the goal is to overcome these challenges without limiting the data quality. A promising AI-enabled survey infrastructure for which we build a first pilot is a hybrid panel. A hybrid panel is a longitudinal AI-enabled survey which allows to iteratively improve the alignment between large language models (LLMs) and the population they aim to simulate and use the errors to inform the design and implementation of the next survey wave (e.g., inform the participant recruitment, assignment of questions to participants). It incorporates both human participants and LLMs as fundamental elements of its design. In this research note, we introduce the concept of a hybrid panel by providing a definition and outlining an overarching framework, spanning data collection to data validation. We detail results from a first pilot study to illustrate (open) challenges that we identify for hybrid panels.

---


### 187. [Vision-Language Models for Occupational Physical Exposure Assessment: Estimating External Hand Forces in Manual Material Handling Tasks from RGB Video](https://arxiv.org/abs/2608.22586)

**<font color=#1a73e8>作者：</font>** Mohammad Sadra Rajabi, Aanuoluwapo Ojelade, Sunwook Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> External hand forces are important inputs to biomechanical analyses of occupational physical exposure and injury risk, yet continuous force measurements during manual material handling (MMH) typically requires instrumented objects or specialized sensing. We evaluated a vision-language model (VLM)-based pipeline that combines task-specific textual cues, visual representations, and known box mass to estimate dynamic, triaxial, bilateral external hand forces from RGB video. Thirty-five healthy young adults performed five MMH tasks involving lifting, carrying, pushing, and pulling with box masses of 6, 9, and 12 kg. The pipeline used text-guided localization of participant and handled-object regions of interest (ROIs), pretrained vision-transformer feature extraction, and transformer-based temporal regression. Performance was evaluated using leave-one-subject-out validation across seven camera-view conditions (three single-view and four multi-view conditions) and four ROI strategies. Overall, root mean square error was ~4.7-5.6 N for the horizontal and mediolateral force components and ~10.6-11.0 N for the vertical component. Including the handled object as a second ROI generally improved force estimation, with some of the largest benefits under single-camera conditions, whereas pixel-level segmentation provided little additional improvement. Multi-camera capture provided the clearest benefit for peak-force estimation, particularly for the vertical component, whereas differences in overall frame-level error among camera configurations were comparatively modest. These findings demonstrate the feasibility of estimating continuous, bilateral, directional hand-force estimates from RGB video and known load mass without requiring sensors on the worker or handled objects as model inputs, supporting the development of more scalable occupational physical exposure and risk assessments.

---


### 188. [Coalition-Aware Skill Reliability for Self-Evolving Agents](https://arxiv.org/abs/2608.22610)

**<font color=#1a73e8>作者：</font>** Qiyan Zhao, Xiaofeng Zhang, Bo Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills, structured artifacts distilled from interaction trajectories and dynamically reused from skill banks, have become a central mechanism for enabling large language model (LLM)-based self-evolving agents to learn from past experience. Yet existing work has largely focused on the operational aspects of skills, such as acquisition, evolution, and retrieval, while leaving a more fundamental reliability question unresolved: Do accumulated skills in an agent's skill bank actually make positive mechanistic contributions? We investigate this question through systematic skill-bank audits across alternative bank compositions and deployment domains, measuring the resulting changes in agent behavior. These audits reveal two recurring reliability failures: coalition pollution, where bank-level gains conceal negative coalition-level skill contributions, and cross-domain utility reversal, where source-beneficial skills reverse their effects after transfer. These findings motivate two reliability interventions: coalition-aware skill selection during skill accumulation and label-free skill masking after transfer. Coalition-Aware Skill Selection (CASS) selects more reliable candidate skills for the current bank using sampled Shapley marginals. Unsupervised Skill-Masked Coalition Optimizer (u-SMCO) masks transferred skills whose exclusion improves retrieval quality on unlabeled target-domain data. Agentic experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld show that CASS and u-SMCO consistently improve task performance and cross-domain generalization over strong skill-based self-evolving agent baselines. Beyond accuracy, coalition-conditioned reliability modeling reduces sensitivity to noisy outcome-reward fluctuations during reinforcement learning and exposes the limits of isolation-based skill evaluation.

---


### 189. [What AstroPT knows about galaxies, and what that can teach us about LLMs](https://arxiv.org/abs/2608.22614)

**<font color=#1a73e8>作者：</font>** UniverseTBD, Kshitij Duraphe, Aman Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability research increasingly asks when concepts emerge during training and whether linear probes recover real structure, but in language models these claims are hard to validate because language offers little ground-truth ordering of concepts or relationships among them. We propose the use of astronomical ground truth through AstroPT, a transformer trained on millions of galaxy images, as a calibration testbed. AstroPT is an LLM-like model trained within a domain where the difficulty ordering of concepts and the relations among them are known in advance. Probing frozen representations across checkpoints, layers, model sizes, and objective choices, we find that galaxy properties emerge in a fixed order that tracks their known difficulty---quantities written almost directly into the pixels (band magnitude) become decodable early in training and shallow in the network, while multiband/spectra based and inferred quantities (such as redshift and specific star formation rate) emerge later and deeper. This order is invariant to our tested training objectives, and scales in magnitude but not in sequence with capacity. Our linear probe directions further recover the known physical structure among galaxy properties. Our findings suggest that astronomy offers a controlled sandbox for calibrating mechanistic interpretability methods we otherwise apply to LLMs blind.

---


### 190. [DeepSAGE: Stage-Aware Reinforcement Learning for Structured CBT Counseling Dialogue](https://arxiv.org/abs/2608.22615)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Heajun An, Prakriti Dumaru 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based counseling agents can generate fluent and supportive responses, but they often lack the structured, goal-directed progression required to conduct a coherent therapeutic session. We present DeepSAGE (Strategic AI Guidance Engine), a hybrid LLM--Deep Reinforcement Learning (DRL) framework for stage-aware counseling dialogue grounded in the first session of Cognitive Behavioral Therapy (CBT). DeepSAGE represents the session as eleven stages with explicit therapeutic objectives, with an external controller determines stage completion and the DRL model selects therapeutic intentions that guide LLM response generation. We evaluate DeepSAGE against six retrieval-, prompting-, stage-, and policy-based alternatives. DeepSAGE elicits higher simulated client engagement and openness and achieves the strongest balance of stage-goal completion and dialogue efficiency among stage-structured systems. Domain expert review further indicates that the generated conversations exhibit broadly plausible emotional trajectories and recognizable CBT processes. Because the evaluation relies primarily on simulated clients and model-based metrics, these findings demonstrate comparative dialogue-control improvements rather than clinical effectiveness. These results suggest that combining stage-structured dialogue with learned strategy selection is a promising approach for AI counseling, though clinical effectiveness, safety, and real-world utility require further human evaluation.

---


### 191. [KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation](https://arxiv.org/abs/2608.22618)

**<font color=#1a73e8>作者：</font>** Jalen Jiang, Chufan Gao, Ethan Rasmussen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual patient data (IPD) from clinical trials is the substrate for survival modeling, meta-analysis, and safety research, yet IPD is rarely released. Prior work has addressed only half of this gap: reconstructing Kaplan-Meier (KM) curves from published plots -- typically requiring manual digitization or human-in-the-loop correction -- while offering no mechanism for generating the adverse-event (AE) streams that constitute the other half of a patient record. We introduce KMGen, the first end-to-end framework that (i) fully automates KM curve extraction at accuracy competitive with human-guided tools, and (ii) generates synthetic per-patient AE trajectories from public trial registry records. The extraction stage is a fully automated agentic pipeline -- an agent generates code to extract each step in the KM curve -- achieving a mean Integrated Absolute Error (IAE) of 0.0151 on a 32-plot benchmark spanning clean, edge-case, and adversarial conditions. The IPD generation stage decouples patient archetype extraction from statistical sampling: an LLM distills the trial record into arm-specific statistics, adverse events, patient demographics, and risk multipliers. A mechanistic sampler generates patient events via clinical archetypes, bootstrap rank-correlation coupling to the empirical KM curve (preserving the marginal survival distribution exactly), and cycle-based AE scheduling with an induction/maintenance split. Across three held-out oncology trials spanning an order of magnitude in cohort size and 30 independent regenerations per trial, KMGen achieves mean integrated KM absolute difference $\Delta_{\text{KM}}\,{\leq}\,0.051$, sex/ECOG JSD ${\leq}\,0.013$ on 5 of 6 demographic slots, and recovers ${\geq}\,71\%$ of the top-15 AEs by exact MedDRA term under a single fixed parameter set. The pipeline is released as open source at this https URL.

---


### 192. [Teaching LLMs How ICU Physicians Approach Clinical Reasoning Through OMOP-Aligned Retrieval Improves Reasoning Across Clinical Domains](https://arxiv.org/abs/2608.22622)

**<font color=#1a73e8>作者：</font>** Miguel Contreras, Scott Siegel, Subhash Nerella 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making relies on identifying relevant patient information to guide diagnosis and treatment, a challenge that is especially difficult in the data-dense and rapidly changing intensive care unit (ICU). Large language models (LLMs) could support this task. However, existing applications and datasets mostly emphasize surface-level retrieval or factual recall rather than the inductive and deductive reasoning clinicians practice to select and reason over decision-relevant evidence. We hypothesized that training LLMs on expert ICU reasoning could yield clinical reasoning skills that generalize beyond critical care. Here we introduce ICU-REACT, a reasoning dataset developed with 19 clinicians through a clinician-in-the-loop framework to teach LLMs to perform information retrieval and context-aware clinical reasoning in the ICU. Using ICU-REACT, we fine-tuned Clin-REACT models spanning 8B-70B parameters and three model families. Across five clinical reasoning benchmarks, Clin-REACT consistently outperformed its backbone models and open-source general-purpose and medical LLMs. Gains extended to different tasks including script concordance tests, and downstream diagnosis and treatment tasks. These findings suggest that expert reasoning supervision in critical care can improve broader clinical reasoning, although prospective evaluation is needed before real-world clinical use.

---


### 193. [Learning Generalizable Behaviors for Terminal Agents](https://arxiv.org/abs/2608.22631)

**<font color=#1a73e8>作者：</font>** Yihang Yao, Bo Pang, Xuan Phi Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terminal agents are a compelling application of large language models (LLMs), with the potential to integrate deeply into users' daily workflows. Reinforcement learning (RL) is a key technique for improving their capabilities, making scalable training environments a central challenge. Since public real-user interaction data are scarce, synthetic environments provide a practical alternative, but often suffer from domain gaps and limited fidelity, leading to poor generalization. Existing work mainly scales the quantity and diversity of synthetic environments, while reward-signal quality and the mechanisms governing generalization remain under-explored. We study how RL improves terminal agents and propose the Agentic Compositional Generalization hypothesis: rather than teaching new domain-specific skills from scratch, RL primarily shapes high-level decision-making behaviors that compose and route low-level skills acquired during pre-training and supervised fine-tuning (SFT). This account is consistent with our empirical results and suggests that verifier quality, which determines which behaviors are reinforced, is more important than simply increasing environment quantity or diversity. Motivated by this insight, we propose River, a simple training recipe that improves reward quality by filtering low-quality environments and augmenting outcome rewards with process-level behavior regularization. Using this recipe, our RL-trained agent achieves the best performance among evaluated open-source RL-trained 8B models across four terminal-agent benchmarks. River also generalizes across model families, scales, agent harnesses, and RL objectives. Using fewer than 30% of the TMax training environments, River improves RL gains by 106% and 30% on average for models ranging from 2B to 27B on Terminal-Bench-Lite and Terminal-Bench-v2.1, respectively.

---


### 194. [GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering](https://arxiv.org/abs/2608.22634)

**<font color=#1a73e8>作者：</font>** Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current work on improving reliability in large language model (LLM)- generated answers has primarily leveraged Retrieval-Augmented Generation (RAG), knowledge-graph augmentation, and reinforcement learning. While these methods are adept at enhancing and measuring reliability through semantic similarity and faithfulness, they often struggle to distinguish semantic similarity from geographic validity. This is especially critical in natural hazard management domains where geographic granularity (i.e., town vs. city vs. state) is significant for decision-making, as responses valid in one municipality may not transfer to another. In such domains, a confidently wrong answer carries greater risk than abstaining. We present GeoRisk-RAG, a novel hierarchy-aware framework that addresses this geographic-validity gap through selective answering. This framework explicitly estimates geographic applicability using a Directed Acyclic Graph (DAG)-based distance for context retrieval before response generation. Experiments on a novel held-out wildfire-related question-answering (QA) dataset show that GeoRisk-RAG significantly reduces false confidence rates for location-dependent questions, lowering the rate to 0.009 compared with ~0.090 for standard semantic similarity and reranking baselines, while consistently achieving higher human preference alignment. This work provides a more comprehensive assessment of end-to-end RAG pipelines by integrating geographic validity and selective-answering behavior for safer decision-making in geospatial domains.

---


### 195. [OmniCAD: A Large-Scale Benchmark for 3D Spatial Reasoning in Robotics Assemblies](https://arxiv.org/abs/2608.22637)

**<font color=#1a73e8>作者：</font>** Mingjia Wang, Taiting Lu, Ziwei Dong 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models (VLMs) show strong capabilities in robotic perception and spatial reasoning, yet their ability to reason about complex mechanical assemblies remains underexplored. We introduce OmniCAD, a large-scale benchmark for assembly-aware 3D spatial reasoning across diverse industrial systems, including robotic mechanisms, automotive components, aerospace structures, and agricultural machinery. OmniCAD contains 25k mechanical assemblies, with an average of 12 parts per assembly and 21 types of mate relationships. Each assembly includes a human-verified ground-truth 3D model and renderings from 20 viewpoints. The benchmark evaluates three capabilities: (1) component-level 3D spatial reasoning, requiring prediction of part positions and orientations; (2) part-to-part relational reasoning, requiring identification of mating relationships and assembly constraints; and (3) tool-augmented agentic reasoning, where models iteratively select viewpoints, inspect visual evidence, and refine predictions. Experiments show that current VLMs struggle with industrial assembly reasoning, often producing inaccurate poses, invalid mating relationships, part interpenetration, and degraded performance as assembly complexity increases. We will open-source the benchmark, evaluation code, and tool interfaces to support research on accurate, physically valid, and scalable 3D assembly reasoning.

---


### 196. [Poetic Heritage for Culturally Grounded Emotional Support: An Interaction Design Framework and Its Multimodal Agentic Instantiation](https://arxiv.org/abs/2608.22639)

**<font color=#1a73e8>作者：</font>** Yangming Zhang, Zhiqian Li, Bin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital systems increasingly mediate emotional support, yet their interactions often remain culturally generic. Accordingly, we examine how a poetic tradition can be operationalized as a culturally grounded interactive medium and how generative AI can support such engagement. The resulting interaction design framework translates staged literature-based support and tradition-specific poetic aesthetics into guidance for digital system design. Poemithy instantiates the framework as a multimodal, LLM-enabled multi-agent system for guided reflection through classical Chinese poetry. A controlled between-subjects study with 50 participants compared text-only and multimodal versions. Both conditions showed medium-to-large within-session improvements in affect, anxiety, and emotion regulation, while between-condition tests detected no differences in these changes. Among secondary post-session user-experience measures, the clearest observed differences favored multimodality in perceived attunement, perceived task success, and engagement; usability and hedonic quality were descriptively higher, while workload did not differ detectably. Post-only cultural ratings were descriptively favorable in both conditions for cultural identification, poetry-engagement and dissemination intentions, and perceived cultural enrichment. Together, the findings suggest that culturally grounded content and structured guidance should anchor system design, while multimodal presentation may strengthen resonance and engagement. More broadly, the work shows how generative AI can mediate engagement with poetic heritage in culturally grounded emotional-support interactions.

---


### 197. [CAI-DLLM: Convergence Aware Inference for Diffusion Language Models](https://arxiv.org/abs/2608.22646)

**<font color=#1a73e8>作者：</font>** Farhana Amin, Sabiha Afroz, Dimitrios S. Nikolopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models can generate many tokens in parallel, but they still require repeated denoising steps during inference. This makes generation costly, especially when the model continues to recompute tokens that are already stable. To address these limitations, we propose CAI-DLLM, a training-free inference method that uses first-step confidence to guide denoising and reduce inference time. Specifically, CAI-DLLM commits easy tokens earlier, allocates more denoising steps to harder tokens, and adjusts decoding schedules across output blocks. As it relies only on first-step confidence signals, it does not require retraining, extra predictors, or weight updates. We evaluate CAI-DLLM on LLaDA-8B-Instruct and Dream-7B-Instruct across math, code, reasoning, commonsense, and long-context tasks. CAI-DLLM achieves up to 18.2x wall clock inference speedup on LLaDA GSM8K while improving accuracy from 76.27% to 77.41%, and up to 13.1x speedup on Dream HumanEval while achieving higher pass@1 than no-cache inference, 48.17% compared with 46.95%. On harder reasoning tasks, speedups reach 44.8x, with a largest accuracy drop of 4.4 points, while energy consumption is reduced by up to 95.3%.

---


### 198. [Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing](https://arxiv.org/abs/2608.22695)

**<font color=#1a73e8>作者：</font>** Nazib Sorathiya, Daniel Zhang, Bardiya Akhbari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable profiles, and an online retrieve-then-rank pipeline that returns a ranked shortlist without invoking any candidates online. We show that from N=10 to 7,278 capabilities, in-context routing's top-1 accuracy (Match@1) collapses (0.85 to 0.12), while retrieve-then-rank degrades more gently (0.81 to 0.39) because its reranker still ranks the right capability first 0.70-0.87 of the time once retrieval finds it. In the Nova Micro sweep, the crossover is around N=500. We compare against two in-context baselines. Full-Ctx puts the whole registry in the prompt and asks the LLM to pick. Search&Pick gives the LLM a search tool to narrow candidates before it picks. At full scale the pipeline leads Search&Pick by 6.5 percentage points (pp) on Match@1 at about half the cost. It reduces cost 70x versus Full-Ctx. We use a fixed configuration (same enrichment, retriever, and scorer weights) across agent, tool, and skill registries. The pipeline runs in production as the default capability-discovery layer of a large-scale multi-agent platform.

---


### 199. [Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf](https://arxiv.org/abs/2608.22697)

**<font color=#1a73e8>作者：</font>** Davood Wadi, Yu Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are examined and bought more often. Consumers are now delegating search to AI agents that can ingest an entire results page at once. Randomizing the order of one hundred hotel listings across 5,000 AI agent sessions, we compare four large language models against human field data. AI agents search more deeply than humans and never decline to buy. Position still predicts which listings are inspected, but weakly and non-monotonically: the middle of a results page has the lowest probability of inspection, not the bottom. Position reaches the choice stage for some models and not others, a heterogeneity that tracks neither provider nor capability. All models nonetheless converge on the same undominated listing. For agentic search, the attributes displayed on a results page matter more than placement within it.

---


### 200. [AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations](https://arxiv.org/abs/2608.22702)

**<font color=#1a73e8>作者：</font>** Nishanth Chidambaram, Kaustubh Paliwal, Kayla Hom 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-generated personas are being increasingly used for support, training and simulations. While generative AI models possess abilities to generate affect-aware responses, their embodiment into visual personas is an active area of investigation. Naturalistic exchanges require understanding of the conversational partners' turn completions, whether the agent should respond or keep listening and rely on non-verbal cues aligned with one's emotional states. Seamless human-AI conversation in a multimodal setting requires all modalities being generated to act in coordination. We present AffAdapt, a seamless interaction design framework for AI-personas, which coordinates streaming speech recognition, proactive turn-management, persona-grounded response generation, a persistent emotional state, and synchronized embodied output into a single interaction loop. We demonstrate the architecture in the context of practicing sensitive, high-stakes conversations, and report an initial case study showing fluid turn management and adaptive, persona-consistent behavior, alongside open challenges in interruption handling, open-ended dialogue, and multimodal affective alignment. AffAdapt's interaction loop is a generalizable pattern for coordinating timing, identity, and affect in real-time AI personas - applicable to training, coaching, education, and simulation contexts wherever believable, responsive interaction matters.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
