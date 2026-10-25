# 🧠 大模型相关研究 | 2026年10月26日

> 本类共 **241** 篇论文：已确认 **225** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-241](./part-05.md)

---

### 151. [Investigating Multi-Cultural Value Selection Biases in LLMs](https://arxiv.org/abs/2610.31199)

**<font color=#1a73e8>作者：</font>** Siddhesh Pawar, Arnav Arora, Dustin Wright 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) serve users whose cultural identities are multi-layered, yet cultural evaluations commonly reduce identity to one label. In this work, we study LLMs under simultaneous identity cues, with a country persona in the system prompt and a second identity signaled in the user turn, either by naming a country (explicit cue) or through the query language (implicit cue). We test World Values Survey (WVS) multiple-choice probing and open-ended sociopolitical generation. In multiple-choice probing, language cues shift answers about three times more than explicit cues but away from the associated country's distribution, and explicit cues do not consistently move answers toward the named country. Across 1.6 million open-ended responses, naming a country closes 30-44% of the gap to the model's own responses for that country, and explicit cues produce more differentiated value changes than language cues. Our results suggest that country and language cues should be evaluated as distinct signals rather than interchangeable proxies for culture.

---


### 152. [A Visual Grounding Benchmark for Retinal OCT with Multimodal Large Language Models](https://arxiv.org/abs/2610.31205)

**<font color=#1a73e8>作者：</font>** Ronald Fecso, José Morano, Botond Fazekas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can answer clinical questions about medical images, but trustworthy use requires visual grounding: models should localize the pathology they report rather than rely on spurious shortcuts. Whether MLLMs can visually ground clinical findings in retinal optical coherence tomography (OCT), the most widely used imaging modality in ophthalmology, remains largely unexplored. To address this gap, we introduce RetinaGroundBench, the first benchmark for biomarker visual grounding in retinal OCT. It comprises 815 B-scans exhaustively annotated by ophthalmologists with 4,537 bounding boxes covering 13 biomarkers across 8 diseases. Because MLLMs often fragment a single lesion into multiple partial predictions, we propose AggIoU, a metric that evaluates whether the union of overlapping predicted boxes covers the annotated region. Across 27 open-source MLLMs (0.8-38B parameters), we find that visual grounding remains largely unsolved: the best general-purpose model achieves a macro F1 of just 23.7%, with consistently low recall, despite reaching up to 73% balanced accuracy on biomarker presence questions. To narrow this gap, we developed RetGrounder, an MLLM fine-tuned using an OCT-specific strategy integrating grounding and textual information. Despite its relatively small size (8B), RetGrounder improves grounding F1 to 33.9%, a 43% relative improvement. Our benchmark provides a reference point for measuring progress in the field of OCT diagnosis with MLLMs.

---


### 153. [Trion-1: Unifying Language, Protein Sequence, and Structure with Diffusion Language Models](https://arxiv.org/abs/2610.31215)

**<font color=#1a73e8>作者：</font>** Tianyu Lu, Kaicheng Yang, Jiangtao Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We envision a general-purpose protein foundation model as a unified, interactive model of sequence, structure, and function, capable of understanding, generation, and cross-modal translation while retaining the instruction-following and reasoning capabilities of modern LLMs. Toward this vision, we introduce Trion-1, the first native, unified, multimodal diffusion language model (dLLM) for proteins. Trion-1 is built on two key design choices: (1) a unified discrete token space that jointly represents sequence, structure, and natural language; (2) a dLLM backbone that replaces strict left-to-right factorization with bidirectional or semi-bidirectional token interactions, enabling global residue communication and long-range contact modeling that are naturally suited to structure modeling. This formulation unifies six core capabilities: folding, inverse folding, sequence understanding, structure understanding, sequence design, and structure design, while retaining the native language capabilities of general-purpose LLMs. On established benchmarks, Trion-1 achieves broadly competitive performance. In folding, Trion-1 achieves a TM-score above 0.8 with a single sample under strict homology control, matching or exceeding the existing tri-modal model using 200 samples. For sequence understanding, Trion-1 performs on par with top-tier LLMs such as Claude Opus 4.7 (62.37%). These results support well-aligned sequence-structure-language representations and strong cross-modal generative capabilities.

---


### 154. [IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark](https://arxiv.org/abs/2610.31256)

**<font color=#1a73e8>作者：</font>** Tirana Noor Fatyanosa, Ummu Ditya Erliana, Mahendra Data 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We introduce IndoNutriQA, an expert-curated Indonesian clinical QA benchmark of 911 question-answer pairs built from real clinical-nutrition reports. Rather than a large-scale training corpus, it is positioned as a high-quality evaluation resource: every pair is grounded in a clinically relevant context, enriched with structured metadata (anthropometric assessment, medical diagnosis, document provenance, chunk segmentation). Eight standardised question types following the Nutrition Care Process (NCP), including the Problem, Etiology, Sign and Symptom (PES) diagnosis statement, are answered for every report, which was written by a graduate-level dietetic intern, by one of three nutritionists. Answers are free-form clinical prose rather than extractive spans, and an expert validation study finds 6-10% of reference answers contestable. The dataset supports generative, extractive and retrieval-augmented QA as well as zero- and few-shot LLM evaluation. We report fine-tuned baselines (IndoBERT variants, mT5, RAG) with 5-fold cross-validation, learning curves and bootstrap 95% confidence intervals, and benchmark eight contemporary LLMs zero- and five-shot. We further calibrate our LLM-as-judge rubric against three expert raters (one RD, two nutritionists), finding it human-comparable on factuality and completeness but unreliable on clinical safety, and a human error analysis shows it misses unsupported content that the raters identify. IndoNutriQA is released to foster research in Indonesian clinical NLP and nutritional decision support.

---


### 155. [A Systematic Comparison of Search Space Complexity and Efficiency for Time-Synchronous End-to-End ASR Models](https://arxiv.org/abs/2610.31259)

**<font color=#1a73e8>作者：</font>** Simon Berger, Larissa Kleppel, Ralf Schlüter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search is a central component of Automatic Speech Recognition (ASR) systems and has been deeply investigated for classical ASR modeling based on Hidden Markov Models (HMMs). However, in work on current sequence-to-sequence ASR architectures it is often simplified to a small fixed-size beam search without external Language Model (LM). In this work, we present a comparative analysis of search space complexity and efficiency for Connectionist Temporal Classification (CTC) and neural transducer models under different pruning strategies and LM configurations. We show that these end-to-end (E2E) models work with a small search space most of the time but exhibit large temporary peaks in hypothesis count during periods of uncertainty. Score-based pruning dynamically adapts the search to model uncertainty, leading to a significantly lower Real-Time Factor (RTF). Our results highlight the limitations of search with low fixed-size beam pruning and provide practical guidelines for efficient search in E2E ASR.

---


### 156. [Memory-Aware Reward Modeling: Learning Human Preferences for LLM Memory Use](https://arxiv.org/abs/2610.31272)

**<font color=#1a73e8>作者：</font>** Yijiang River Dong, Zexue He, Cheng Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory enables language model assistants to maintain continuity across sessions and generate personalized responses, but knowing more about a user does not necessarily produce responses they prefer. Existing evaluations assess memory capabilities without directly establishing whether memory use benefits the user. To study this gap, we collect approximately 1,000 pairwise judgments from 87 participants using their own ChatGPT queries and personal memories. We find that memory-conditioned responses are not consistently preferred over responses generated without memory and in some cases, users strongly prefer the latter. Automatic evaluators also show limited agreement with users and favor memory-conditioned responses substantially more often than users do. Motivated by these gaps, we introduce a memory-aware reward model that learns from user judgments, achieving 72.8\% preference prediction accuracy and outperforming the existing baselines. Our findings motivate evaluation and optimization objectives that align memory use with the preferences of the people whose information is being used.

---


### 157. [PointerBench: A Diagnostic Benchmark for Fine-Grained GUI Grounding](https://arxiv.org/abs/2610.31274)

**<font color=#1a73e8>作者：</font>** Valentino Sacco, Saurabh Pandey, Alexander Florian Jercher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models have shown promising performance in computer-use tasks, from planning user workflows to grounding natural-language actions to precise UI targets. Existing end-to-end benchmarks primarily emphasize long-horizon task completion, while GUI grounding benchmarks remain focused on conventional controls and a limited set of professional interfaces. We introduce POINTERBENCH, a diagnostic suite of 1,500 screenshot-instruction pairs probing three complementary capabilities: thin sub-element identification and geometric grounding in spreadsheets (POINTERBENCH-Sheets), character-level grounding in long-text documents (POINTERBENCH-Text), and mixed GUI grounding across 100 professional applications (POINTERBENCH-Pro). We carefully curate each task with pixel-exact target geometry and evaluate both general-purpose multimodal models and 39 specialist GUI grounding configurations. We find text grounding to be the most challenging setting, with Claude Fable 5, GPT-5.6 Sol, and the leading native specialist UI-Venus-2-9B achieving 69.6%, 53.4%, and 25.8% success on POINTERBENCH-Text despite respective 83.2%, 77.7%, and 54.5% average success across POINTERBENCH. These results reveal substantial headroom in fine-grained GUI grounding across frontier and specialist models. We publicly release the benchmark and evaluation code at this https URL.

---


### 158. [RIPPLE: Recovery Internalization through Process-Level Policy Learning and Effect-Aware Credit for Long-Horizon Agentic Coding](https://arxiv.org/abs/2610.31276)

**<font color=#1a73e8>作者：</font>** Jingxuan Xu, Zihang Xu, Yuechen Luo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon coding agents can observe a failure and generate a plausible critique yet continue along the same incorrect trajectory. We call this the Critique-to-Action Handoff Gap. We introduce RIPPLE, a recovery-oriented training framework that internalizes process-level guidance into a single self-recovering policy. A prefix-only teacher provides evidence-grounded recovery supervision without access to future actions or terminal outcomes. After lightweight distillation, reinforcement learning assigns stage-specific credit to reflection triggering, diagnosis, and corrective action. Local validity signals gate trajectory advantages so that intermediate recovery decisions do not indiscriminately inherit terminal outcomes. Across four repository-level software-engineering benchmarks, RIPPLE improves the base policy by an arithmetic mean of 4.8 score points, with no auxiliary critic at deployment. Controlled ablations isolate the benefits of local, stage-aligned credit, and matched-prefix interventions show that critique semantics affect subsequent correction. Recovery gains concentrate where the prefix contains sufficient diagnostic evidence and the repository state remains reversible within the remaining budget.

---


### 159. [CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring](https://arxiv.org/abs/2610.31277)

**<font color=#1a73e8>作者：</font>** Shmuel Amar, Benjamin Lieber, Ori Shapira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typically address isolated writing phases, leaving comprehensive end-to-end human-LLM collaboration largely unexplored. In this paper, we introduce CoWriter, a proactive agentic scheme that adapts expert human (co-)authoring methodologies from cognitive science to flexibly steer the entire writing workflow while actively encouraging the user to engage. In an exploratory user study, compared to a standard LLM baseline, authors using CoWriter better expressed their perspectives and maintained a higher sense of document ownership, supported quantitatively by $2.2\times$ more successful agent engagements. Furthermore, external reader judges rated the resulting texts higher in "human touch" qualities like storytelling and integrating unique personal experiences. Overall, our results demonstrate that proactively engaging users through established human practices is beneficial for effective LLM-supported co-authoring, providing useful methodologies, techniques and insights for future research on collaborative agents.

---


### 160. [ReCoG: Relational Concept Graph for Training-Free Personalization](https://arxiv.org/abs/2610.31282)

**<font color=#1a73e8>作者：</font>** Changseon Yu, Hyeokjun Kweon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free personalization adapts a frozen vision-language model (VLM) to recognize user-defined concepts from only a few exemplars by retrieving concept entries at inference time. While recent retriever-based methods enrich each concept with descriptive evidence, they largely treat concepts in isolation, so the retrieved information can be plausible yet non-discriminative, especially when the personalized concept set contains highly confusable, fine-grained categories. We argue that personalization is inherently relational: correct recognition depends on the specific distinctions between a concept and its nearest alternatives. To this end, we propose ReCoG, a Relational Concept Graph for retrieval-augmented personalization. ReCoG represents concepts as nodes and augments them with directed edges that explicitly capture discriminative cues between concept pairs, elicited by a frozen VLM during database construction. At inference, ReCoG retrieves a shortlist and resolves ambiguity via explicit pairwise comparisons conditioned on the corresponding relational edges, selecting the concept that consistently wins against competing candidates. We also introduce FINGER benchmark to test personalized recognition on confusable concept sets. Across FINGER, ReCoG substantially outperforms prior methods, with the largest gains in the most confusable regimes. ReCoG also achieves consistently best performance on established personalization benchmarks including captioning and VQA, confirming that relational evidence is broadly beneficial beyond fine-grained settings. Project Page: this https URL

---


### 161. [Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering](https://arxiv.org/abs/2610.31284)

**<font color=#1a73e8>作者：</font>** Raffaele Cali, Giuseppe Lando, Rosario Forte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long egocentric videos pose a central challenge for multimodal language models: the visual stream must be compressed into a memory representation that can be searched efficiently while still preserving the evidence needed for question answering. Building on an online textual-memory framework in which first-person videos are converted into temporally grounded captions, this work systematically studies the role of retrieval in episodic-memory video question answering. We evaluate how different retrieval units, query formulations, context budgets, and reranking strategies affect multiple-choice answering on QAEgo4D-Closed, isolating retrieval as the main variable while keeping the underlying generated memory fixed.
Our best configuration, Parent, matches fine-grained caption subchunks, then provides their full parent captions to the reasoner. It achieves 56.4 % accuracy, matching strong full-memory and retrieval baselines while exposing only a small fraction of the textual memory at question time. More importantly, our analysis shows that better temporal coverage does not necessarily translate into better answers: increasing the retrieval budget improves temporal Hit@K and Recall@K, but can reduce accuracy by introducing visually plausible distractors and uncertain caption evidence. These findings suggest that retrieval-augmented egocentric memory should not be optimized only for evidence recall, but also for the reliability, specificity, and answer-discriminative value of the retrieved context. The study motivates more structured episodic memories that move beyond raw caption retrieval toward evidence-aware representations for long-form egocentric reasoning.

---


### 162. [The Value of Memory in Language Agents](https://arxiv.org/abs/2610.31303)

**<font color=#1a73e8>作者：</font>** Zehao Lin, Erenkai Zhu, Helan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory enables language agents to carry useful distinctions from past experience into future decisions. Its value depends on which distinctions survive, whether a bounded agent can use them, and what can be recovered or revised as demands evolve. We develop a decision-theoretic framework that follows this value from raw history through persistent state, operational use, and costly recovery and revision. Original and retained value are expressed in units of avoided task loss; risk-cost frontiers describe attainable recovery and preservation across uses. Unknown demand yields value profiles, while interactive feedback changes the distribution of future work. A cost-aware simulation condition and five minimal counterexamples expose the roles of information timing, retrieval access, component interaction, feedback and demand uncertainty. In particular, a pointer with zero mutual information about the answer can still reduce the cost of exact recovery. Diagnostics on LoCoMo, a two-project update task and longitudinal cases exhibit failures of preservation, use and measurement. At fixed retrieved evidence, a saved ledger changes subsequent answers; at fixed agent outputs, an evaluator revision changes scores. The framework connects these distinctions to operational risk bounds and testable principles for allocating memory, preserving recovery options and revising evidence dependencies.

---


### 163. [Data-Driven Vision-Language Models for Remote Sensing: A Survey](https://arxiv.org/abs/2610.31304)

**<font color=#1a73e8>作者：</font>** Yue Zhou, Shujun Zhao, Xue Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> During the deep learning era, innovations in remote sensing (RS) vision models primarily focused on optimizing network architectures for specific tasks and conducting end-to-end training. However, with the advent of the Vision-Language Models (VLMs) era, constrained by substantial computational resource demands, the mainstream research paradigm has shifted towards adapting general-purpose VLMs using RS vertical domain data for fine-tuning, rather than modifying their core architectures. This transition marks a change in the innovation pathway from model-centric to data-centric. Despite the increasing importance of data, the academic community still lacks a systematic, data-centric survey to guide researchers in constructing high-quality RS vision-language datasets for various application scenarios and in conducting effective model fine-tuning and performance evaluation based on these datasets. To address this gap, this paper presents a systematic review of the development status of RS datasets tailored for VLMs. It further provides a comprehensive practical guide for RS researchers in the large model era, covering the entire pipeline from data construction to fine-tuning and evaluation. This paper aims to encourage the academic community to build more diverse and higher-quality vision-language datasets for specialized RS sub-fields. Ultimately, the goal is to converge these efforts into a comprehensive RS vision-language corpus that offers extensive task coverage and a wide geographical distribution, thereby laying a solid data foundation for advancing towards general artificial intelligence in RS.

---


### 164. [Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation](https://arxiv.org/abs/2610.31305)

**<font color=#1a73e8>作者：</font>** Hongcan Guo, Yian Zhao, Feng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hierarchical language generation separates continuous semantic modeling from discrete text realization, but its effectiveness depends on what the latent space compresses and how the discrete generator uses it. We propose Cola2, a framework that jointly studies continuous semantic compression, the balance between reconstruction and generation, and continuous-discrete co-adaptation. Cola2 dynamically segments text into semantic spans, controls the compression rate through auxiliary-loss-free negative feedback, and combines reconstruction and generation supervision to learn compact, predictive latent representations. A block-causal masked diffusion decoder is trained with clean, noisy, and dropped latent conditions, while classifier-free guidance adjusts the balance between semantic reconstruction and autonomous generation. Token-prediction gradients update the encoder through the latents, whereas Flow Matching prior learning is decoupled from representation learning by stop-gradient. During inference, generated text is re-encoded under a fixed span layout to keep the latent history consistent with the actual text context. Experiments on five downstream tasks with about 210 billion training tokens validate the core designs and show competitive, unsaturated scaling. With 346.03 billion source tokens, an unconverged checkpoint reaches a 60.10 average across eight tasks and surpasses Llama-3-8B on HellaSwag and StoryCloze despite its reported pretraining budget being over 43 times larger. These results demonstrate the potential of continuous-latent hierarchical language generation.

---


### 165. [Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization](https://arxiv.org/abs/2610.31309)

**<font color=#1a73e8>作者：</font>** Jiacheng Liu, Yaxin Luo, Xiaohan Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling embedding capacity alongside Transformer computation is an emerging trend in language models. This trend makes high compression rates increasingly useful. Hence, we study extreme compression of Per-Layer Embeddings (PLE), which follow this trend and account for 35.2% of the parameters of Gemma 4 E4B. At such rates, conventional quantizers give each token-layer vector its own code of only a few bytes. We instead develop OPTIC (Output-Path-fitted, Token-shared Indexed Codes), which stores one quantized code tuple per token and decodes it at every layer with a layer-specific affine decoder. Codes and decoders are fitted to the PLE output path rather than to the stored vectors. At about $100\times$ PLE compression of bfloat16 (BF16) E4B, OPTIC retains an aggregate 97.8% of the uncompressed model's performance across seven benchmarks, whereas product quantization, the strongest of six conventional baselines, retains 66.3%. At $594\times$ and $1,002\times$ PLE compression of BF16 E4B, OPTIC retains 90.5% and 84.1%. On the official E4B release with 4-bit linear weights and 16-bit activations (W4A16), OPTIC retains 96.9% at about $100\times$ PLE compression. During inference at about $100\times$ PLE compression, BF16 E4B uses 29.7% less GPU memory than with uncompressed PLE at the same key-value cache size, while running at most 0.40% slower.

---


### 166. [When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues](https://arxiv.org/abs/2610.31314)

**<font color=#1a73e8>作者：</font>** Yancheng Zhu, Yifan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can repeat an instruction while failing to keep obeying it. We study this recall-compliance dissociation in long-horizon dialogue and define State Integrity Collapse: a model preserves a stated constraint in memory but stops applying it to later turns. We introduce StateTrack-Bench, a controlled suite of conversations covering numerical, format, role/persona, factual-memory, and logical-rule constraints. Across seven provider-pinned model snapshots and five dialogue-depth probes, strict joint retention ranges from 62.4% to 100.0%, with degradation concentrated in symbolic constraints and in one especially brittle model. A forked recall audit shows that 88.6% of observed failures are behavioral-drift failures rather than ordinary forgetting; excluding the brittle outlier preserves this diagnosis (84.4% of failures). Extended evaluations at depths up to 50 turns confirm that the dissociation persists beyond the core benchmark, while Structured State Anchoring recovers up to 24.4 points on immutable constraints. The results show that reliability cannot be inferred from single-turn instruction following alone; evaluation must track whether remembered constraints remain operational as dialogue state grows. Code and artifacts are available at: this https URL.

---


### 167. [The Value of System 1 Models in Medicine](https://arxiv.org/abs/2610.31315)

**<font color=#1a73e8>作者：</font>** Xiufeng Yang, Konstantinos Vrettos, Zeineb Ben Chaaben 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many clinical decisions are a choice among a few fixed options, taken quickly and in large numbers. Such decisions also need an uncertainty estimate to know when to defer to a clinician. Generative language models answer slowly in free text and state their confidence poorly. In contrast, System 1 models answer zero-shot with a probability for each answer. However, their performance across clinical tasks is unknown. Four System 1 models, two proprietary and two with open weights, were evaluated zero-shot on 86 public tasks from 14 clinical domains in 20 languages, spanning examination questions and medical imaging. Tasks were assigned to six capability tiers before analysis. The primary outcome was the area under the receiver-operating-characteristic curve (AUROC). Secondary outcomes included calibration, language effects and comparisons with published results and generative models. Across 179,111 cases, the mean AUROC of the best model per task was 0.94 for medical knowledge, 0.93 for text understanding, 0.83 for clinical judgement from text, 0.89 for image perception, 0.84 for 2D image findings and 0.69 for volumetric findings. Imaging tasks scored 0.09 (95% CI, 0.06 to 0.11) lower than text tasks (P < 0.001). The best model matched or exceeded the best published result on 13 of 26 text tasks and on 8 of 35 imaging tasks. Triage nurses outperformed the best model (accuracy, 0.85 vs. 0.56). One decision took 0.34 to 0.44 seconds and 24 to 81 joules on open-weight models run locally. Accuracy on identical questions fell by up to 39 percentage points from English to Yoruba. Generative models of the same family were 11 to 76 times slower, with 3 to 5 percentage points higher balanced accuracy. System 1 models decide quickly, cheaply and with usable confidence when the answer is stated in a text or recalled from medical knowledge, but not when it must be judged or read from an image.

---


### 168. [SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs](https://arxiv.org/abs/2610.31317)

**<font color=#1a73e8>作者：</font>** Yifan Yuan, Yancheng Zhu, Zuoyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most automated survey generation systems retrieve papers as flat documents, limiting their ability to capture research structure. We present SurveyGraph, a framework built around a Methods-Entity Knowledge Graph (MEKG) encoding method-level follow-on, competition, and shared-resource relations. The graph supports core-paper discovery, retrieval, hybrid outlining, and evidence-gated narrative synthesis. We evaluate retrieval, semantic edges, citation grounding, collection coverage, and generation-stage components. In a controlled seven-method equal-budget benchmark, MEKG-anchored fusion balances recall and structural density, with an independent co-citation check. In a separate archived graph-native diagnostic, graph-aware retrieval nearly doubles recall over flat lexical baselines across eight runs (p = 0.004). A semantic evidence gate achieves AUC = 0.75. Audits of 160 generated sentences find 80.6% anchored-or-partial citation support. Human adjudication of 108 stratified semantic edges finds 68.5% supported-or-partial relations (binary-support Cohen's kappa = 0.64), with improves strongest (80.6%) and extends weakest (52.8%). A SurveyBench-facing collection probe reaches mean reference coverage of 0.521 across four topics with an eight-paper budget. Same-backend Qwen diagnostics on a 30-paper/74-relation graph show reduced organization signals when hybrid outlining is removed. Concurrent-system comparisons provide bounded context rather than matched-backend end-to-end evidence. The results position MEKG as an auditable structural layer for typed diagnostics, relation-specific filtering, and controlled survey generation. Code and artifacts: this https URL.

---


### 169. [Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention](https://arxiv.org/abs/2610.31320)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Ying Feng, Mengtong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We adaptively aggregate these cues from multiple attention layers and across temporal windows, and fuse them with depth priors to handle challenging cases such as occlusions and textureless regions, producing precise dynamic masks that decouple static and dynamic regions. We then apply a soft key masking scheme that leverages these dynamic masks to suppress interference from dynamic regions in causal attention, thereby improving camera pose estimation accuracy. Stream4D inherits the efficiency of causal attention and remains compatible with existing streaming architectures. On diverse dynamic-scene benchmarks, Stream4D significantly improves camera pose estimation and static-scene reconstruction quality, yields reliable dynamic masks, and effectively mitigates long-sequence ghosting.

---


### 170. [Consistent but Biased: Chair Personas Trade Noise for Bias in Multi-Agent Clinical Decisions](https://arxiv.org/abs/2610.31325)

**<font color=#1a73e8>作者：</font>** Yitong Bai, Chengyi Zhang, Ziyang Wang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In clinical systems built from several large language model (LLM) agents, one agent often chairs the discussion and makes the final decision. Whether the chair's persona prompt changes that decision, or the agreement between repeated runs that some systems treat as reliability, has not been tested with the case held constant. We ask whether the persona changes the decision or only its timing, how it affects agreement between runs, and which behaviors appear when the prompt describes only personality traits. A simulated department of seven agents discussed 20 published cases of degenerative cervical myelopathy, with the case reports replayed unchanged in every run. Only the prompts of the chair and its deputy changed (no persona, or a consultative, autocratic or avoidant one), written either as rules of conduct or as personality traits. With personas written as rules, the chair chose to operate now in 93% of runs when autocratic and in 2% when avoidant, against 57% without a persona. Surgery was still planned in nearly all decisions, so the personas mainly changed whether to operate now or after more tests. These effects held with a second model and reworded prompts. The autocratic and avoidant personas made the three runs of a case agree more often, but only about as often as chance predicts, and Fleiss $\kappa$ did not rise. Prompts that described only personality traits kept more than half of the autocratic and avoidant effects on operating now. They reproduced quick decisions, delays and extra tests, but not ignoring red flags, dropping backup plans or passing the decision to the family. Studies should report and vary the chair's persona as they do the model, and correct agreement between runs for chance before calling it reliability.

---


### 171. [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://arxiv.org/abs/2610.31329)

**<font color=#1a73e8>作者：</font>** Tianming Liang, Junyi Pan, Yuxi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual tasks including object detection, referring localization, counting, OCR, segmentation, and matting, enabling localization at any user-specific granularity, from points and boxes to masks and alpha mattes. Architecturally, we integrate a lightweight pixel decoder into the VLM via a special <OBJ> token to generate instance-level pixel outputs. We train the model with a three-stage curriculum SFT followed by mixed-task RL. Across over 30 benchmarks, WeVisOne-VL demonstrates leading performance on both object-level and pixel-level tasks, while maintaining robust rejection for object-absent queries. By releasing WeVisOne-VL to the open-source community, we hope to advance VLMs from broad visual understanding toward truly reliable perception systems for real-world deployment.

---


### 172. [ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding](https://arxiv.org/abs/2610.31338)

**<font color=#1a73e8>作者：</font>** Liang He, SiYuan Ma, Qishi Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tree-based speculative decoding accelerates large language model inference by verifying multiple candidate branches in parallel. However, in practical serving scenarios, similar requests repeatedly induce overlapping candidate branches. While retrieval-based methods mitigate this by reusing historical drafts, the resulting candidate trees often contain many low-quality branches as the candidate tree grows, which reduces verification efficiency and wastes target-side computation. To address this, we propose ValuSpec, a plug-and-play candidate valuation mechanism that filters low-quality branches from a supplied candidate tree before expensive target-side verification. ValuSpec introduces transfer-based supervision to align filtering with the target model's behavior. A filtering threshold is estimated from the target model's greedy trajectories on a calibration split, without any parameter training. The target model then verifies the filtered tree under the output-identical greedy rule, so accepted tokens are guaranteed to match standard autoregressive decoding exactly. Experimental results on HumanEval, GSM8K, Dolly, and SpecBench show that, in our main evaluation, ValuSpec achieves up to 2.38x end-to-end speedup in retrieval-based tree settings. Furthermore, integrating ValuSpec into the EAGLE-3 dynamic tree framework yields up to 2.78x end-to-end speedup without modifying its tree construction strategy, demonstrating that ValuSpec serves as a generally applicable and plug-and-play candidate valuation module.

---


### 173. [Making Generative AI Workable at Work: Accountability, Localization, and Representation in Kenyan and Nigerian Small Businesses](https://arxiv.org/abs/2610.31344)

**<font color=#1a73e8>作者：</font>** Najeeb Gambo Abdulhamid, Stephanie Nyairo, Liz Ankrah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is widely framed as democratizing skilled work by lowering the barrier to producing professional output. Drawing on 21 semi-structured interviews with 27 workers across 21 small and medium-sized businesses (SMBs) in Kenya and Nigeria (July to October 2023), we find that availability alone did not make participation workable. In participants' accounts, drafting was rarely the hard part. The consequential work was making AI-assisted drafts defensible enough to circulate to clients. We identify five intertwined practices through which participants made generative AI workable: using it as draft labour, steering outputs through iterative interaction, switching and comparing across tools, performing release work to make outputs accountable before circulation, and repairing context misfit when outputs failed local requirements. We make two central contributions. First, we specify release work as a distinct, boundary-facing form of accountability labour, evidenced through verification gates, traceability reconstruction when sources fail, and non-delegation boundaries that decide what can ship. Second, we show how localization and representational failures, which we call context misfit, operate in everyday work as a recurring breakdown-and-repair class, including failures of local language, institutional knowledge, and the credible representation of African people and places, and we document the repair repertoire they demanded. Reframing democratization as workable participation, we argue that reported gains were conditional on this accountability and repair labour, and we translate the findings into four design directions for workplace generative AI. We treat Kenya and Nigeria as two situated cases, not as a representative sample of SMBs or the Global South.

---


### 174. [CrisiLangs: A Multilingual Resource for Crisis Warning Generation](https://arxiv.org/abs/2610.31356)

**<font color=#1a73e8>作者：</font>** Giacomo Gonella, Stefano Menini, Marco Guerini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Communicating with the public during an emergency entails issuing warning messages promptly. In Europe, it often requires producing them in more than one language. Recent work has shown that language models can be trained to generate warning messages as a crisis unfolds, but the available data covers only English. To fill this gap, we present CrisiLangs, a multilingual extension of CrisiText (an English dataset of crisis events paired with warning messages written according to expert communication guidelines) to Italian, Bulgarian, German, and Greek. Expert native speakers translated the warning messages of 1,000 events drawn from 411 scenarios, for a total of 5,000 event-message pairs across five languages. We test the resource to fine-tune a multilingual model on all five languages jointly, with and without the emergency guidelines in the prompt, and compare it with a zero-shot baseline. The fine-tuned models outperform the baseline on ROUGE-L, BLEU and BERTScore in every language and configuration. In a human preference study, low decoding temperatures receive the most preferences in all five languages and in both configurations, while the effect of the guidelines varies by language.

---


### 175. [AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](https://arxiv.org/abs/2610.31366)

**<font color=#1a73e8>作者：</font>** Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion recovery to be attributed to the original exposure. In our primary setting, a single query recovers the deleted secret from Qwen2.5-7B-Instruct in roughly two thirds of cases, while matched never-exposed controls have zero recovery. Crucially, recovery does not require a surviving verbatim copy: when the complete secret string is absent and only separately stored components remain under a public composition rule, exact reconstruction succeeds in 62-99% of cases across Qwen, Mistral, and Phi-3. We also show that the response interface is part of the measurement system: target-bearing replies can be scored as failures when the requested format and parser are misaligned. Finally, we separate reconstruction from write-back and fresh-session recall. Provenance-aware closure eliminates observed recovery in the tested positive-baseline settings, whereas an exact-literal write filter blocks reinsertion but cannot erase information already present. Together, these results show that source deletion should be evaluated behaviorally at the level of the agent and its memory system, not only as a storage operation.

---


### 176. [Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action](https://arxiv.org/abs/2610.31376)

**<font color=#1a73e8>作者：</font>** Chao Gu, Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrollable, we enforce safety by the conventional maximally permissive supervisor, and this safety transfers to the running system under four assumptions. Moreover, to capture an agent that may propose again after a refusal, we introduce the notion of a replanning closed loop, in which each retry costs an inference call. We show that, in this loop, the conventional supervisor can be arbitrarily more intrusive than a stricter safe one. Furthermore, for a given proposer model, the maximally permissive least-intrusive supervisor is characterized as a value-threshold refinement of the conventional one. Under precise conditions, this refinement orders two concurrent actions by at most one monitor place. On an autonomous release agent, we find by synthesis that safe deployment requires a step that the supervisor can refuse after a rollout starts.

---


### 177. [Auditing the Hand-Written Inputs of Learned Access Control](https://arxiv.org/abs/2610.31388)

**<font color=#1a73e8>作者：</font>** Arsalan Jalil Sarghaleh, Mehdi Hazrati  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learned access control is typically deployed behind two hand-built artefacts: a hard-deny set enforced by a small trusted shield, and a region map that decides which requests mined rules answer and which the learner answers. Verifying the shield or measuring the learner validates neither. We audit both on the five public ABAC Lab policies. First, we formalise hard-deny soundness and check it exhaustively over relations of up to 794,250 tuples. Clauses that faithfully transcribe an explicit restriction are unsound at rates of 0.50-0.70 across four elicitors - an author and three blind language-model elicitors - because prose scopes restrictions to a section while the grant relation is a disjunction over all rules: 97% of counterexamples are granted by other rules. Shipped unchecked, these deny sets would withhold 16-78% of everything the policies grant; certified, they withhold nothing. Vacuity, a second silent failure, also occurs. Second, hybrid routing needs a two-class, abstaining rule set that ABAC miners do not emit, and ranking a mixed-effect candidate pool under a cap is one-class in all 24 cells for the two commonest ranking keys. Third, for additive losses the hybrid-versus-learner effect factorises into covered mass times a rule-learner risk contrast that must be reported on both false-non-grant and false-permit loss: on two real policies, most selection rules give opposite verdicts on the two losses, and the one favourable on both holds for one policy, one learner configuration and a band of noise levels. A released artefact regenerates and checks every reported number.

---


### 178. [Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language](https://arxiv.org/abs/2610.31397)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov, Svetlana S. Khaybullina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bashkir is a low-resource agglutinative language written in Cyrillic and remains poorly represented in modern LLMs. We present an open resource suite and a systematic benchmark of adaptation methods: the Bashkir Web Corpus (71,567 documents, 46.9M tokens, 16 sources) and three labelled datasets for binary, multiclass and multilabel text classification; the benchmark covers the first two. Experiments use eight architectures (82M-8B: DistilGPT2, GPT-2 base/medium, Phi-3-mini, Mistral-7B, YandexGPT-5-Lite-8B, mBERT, XLM-R) and three adaptation groups (full fine-tuning, QLoRA, in-context learning), plus continual pretraining (CPT). (1) QLoRA on 3.8-8B models outperforms encoder-only fine-tuning on binary classification: YandexGPT-5-Lite-8B with CPT reaches macro-F1 0.748 vs 0.653 (XLM-R) and 0.650 (mBERT); pairwise differences are significant after Holm correction (p<0.001). (2) YandexGPT-5-Lite-8B significantly outperforms Mistral-7B and Phi-3-mini on multiclass classification, BPB and native-speaker ratings (mean 3.28 vs 2.52 and 2.22; n=100; alpha=0.69-0.77; p<0.05); on binary classification its QLoRA advantage is not significant (p>=0.084). (3) CPT effects depend on model and task: perplexity improves for Phi-3-mini (+0.58) and YandexGPT-5-Lite-8B (+0.33) but worsens for Mistral-7B (-1.15, p<0.001); on binary classification CPT helps Mistral-7B most (+4.0 macro-F1). (4) Tokeniser fertility on Bashkir varies 2.67x (2.92-7.80) and tracks adaptation quality, while perplexity across tokenisers is not comparable. Cyrillic tokenisers with Russian pretraining are preferable; LLM judges reproduce native ratings for grammar and coherence (rho=0.33-0.46) but not language correctness (rho=0.16, p=0.11); native evaluation remains necessary. All artefacts are open-licensed.

---


### 179. [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404)

**<font color=#1a73e8>作者：</font>** Justin Tan, Miao Li, Ding Zhao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-existing datasets may miss, we introduce AgentPhishing, a benchmark for evaluating whether persuasive phishing attacks can evade detection and induce LLM email agents to comply with malicious requests. We develop PhishOpt, which optimizes reusable email-generation skills against individual agents under fixed benchmark constraints and a realism constraint. We analyze the generated emails using Cialdini's persuasion principles to identify strategies associated with agent failures and use these findings to construct a universal generation skill. Our evaluation shows that agents can handle pre-existing phishing emails safely yet remain susceptible to attacks adapted to agent behavior, while in an AgentPhishing evaluation of nine agents, four exhibit phishing-detection rates below $10\%$ and malicious-request compliance rates above $45\%$. These results highlight the limits of inferring agent safety from conventional phishing evaluations and the need to assess how agents respond to persuasive malicious requests.

---


### 180. [Same Entity, Different Script: Diagnosing Cross-Script Entity Matching Failures in Language Models](https://arxiv.org/abs/2610.31407)

**<font color=#1a73e8>作者：</font>** Athira Gopal, Patil Prathamesh Pravin, Ankush Kadu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual language models can give different identity judgments when the same people's names are written in different scripts. We study this effect using 601 audited identity pairs with attested Devanagari and Latin forms, holding the question and relation fixed. Qwen2.5-7B's same-person accuracy falls from 35.1% in Latin to 8.5% in Devanagari under Marathi prompts, while different-person accuracy remains above 98%. Evaluation across five models reveals distinct response biases, and reduced tokenization fragmentation does not reliably close the gap. Replicating the design on 374 audited Malayalam pairs built from the same entities reproduces the effect in a second script and language family: same-person accuracy falls to 5.3%, about half the matched Devanagari rate, while the margin still ranks matching above non-matching names at 0.925 AUROC. Latin-trained probes recover label information from Devanagari states, exceeding a string-feature baseline under similarity-matched negatives. Scalar calibration recovers 87% of the raw model-probe balanced-accuracy gap, identifying decision criterion placement as a major contributor. Activation patching localises causal sensitivity to the second entity in Qwen's middle layers; one shared sensitivity direction transfers about half the full-state margin correction. A fact-independent intervention at this site raises held-out Marathi same-person accuracy from 6.5% to 33.5%, with 98.5% different-person accuracy. Together, these results distinguish script-dependent discrimination from criterion placement and identify a causal site for improving identity judgments.

---


### 181. [SQuAT: Spherical Lattice Vector Quantization-Aware Training](https://arxiv.org/abs/2610.31412)

**<font color=#1a73e8>作者：</font>** Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood. We scale lattice VQ-QAT to billion-parameter LLMs and multi-billion-token training regimes, and introduce SQuAT, a shape-gain VQ-QAT approach trained with a separate straight-through estimator (STE) for the shape and gain. SQuAT decomposes weights into direction and magnitude: normalized directions are quantized using an $E_8$-derived spherical codebook, while gains are quantized independently with low-bit scalar quantizers. We show that, unlike a standard STE applied to the full quantizer, which ignores the shape-gain structure, these separate STEs induce tangent-space updates for directions, yielding an implicit form of spherical (Riemannian) optimization. To enable scalability, we develop a distributed exact nearest-neighbor assignment scheme, in which workers quantize disjoint weight blocks and communicate only discrete indices, reducing VQ-QAT training time by 12.8$\times$ and allowing us to scale it to 10B tokens. Across instruction-tuned LLaMA-3.2-1B/3B, Qwen3-4B, and base Qwen3-1.7B, SQuAT consistently outperforms standard VQ-QAT STE under identical quantizers and initialization, and achieves SOTA VQ-QAT accuracy.

---


### 182. [SyRA-CS: Synthetic-to-Real Adaptation for Code-Switched ASR with Meta-Learning](https://arxiv.org/abs/2610.31415)

**<font color=#1a73e8>作者：</font>** Fadel Thior, Ahmer Tabassum, Haania Siddiqui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switched (CS) automatic speech recognition (ASR) remains difficult because real CS speech is scarce and synthetic speech does not fully match it. We investigate whether synthetic CS speech is more useful for learning an adaptation-friendly initialization than for ordinary continual fine-tuning. We propose SyRA-CS, a pair-specific synthetic-to-real adaptation framework based on Reptile meta-learning. For each language pair and pretrained model, we meta-train on the corresponding synthetic CS-FLEURS subset and then adapt using one hour of labeled real target speech. We evaluate four architectural settings: Encoder-CTC, FastConformer-RNN-T, Attention Encoder-Decoder (AED) and Speech-LLM. Experiments cover on Arabic-, French-, German-, and Hindi-English, against synthetic-only transfer, real-only fine-tuning, and continual fine-tuning. SyRA-CS improves over continual fine-tuning on WER in all 16 model-pair comparisons and on CER in 15 of 16, with relative macro WER reductions of 17.7% for XLS-R and 5.3-5.8% for the other three models. The gains hold across the tested models but vary in size across architectures, language pairs and metrics.

---


### 183. [How Depth Growth and Looping Shape In-Context Learning in Language Models](https://arxiv.org/abs/2610.31421)

**<font color=#1a73e8>作者：</font>** Ferdinand Kapl, Kaitlin Maile, Stefan Bauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning from context: grown and looped models rely more on information in context and, compared with a full-depth dense reference, acquire ICL earlier in controlled tasks and retain it more strongly when learning fixed associations in the weights is also possible. Tracing attention heads through training reveals that depth growth propagates early induction heads across layers. Ablations show that grown and looped models rely more strongly on induction-ranked heads for both few-shot performance and later-token prediction. Together, these findings provide evidence for a shared inductive bias toward learning from context and suggest that (soft) parameter reuse shapes how this ability develops and which attention mechanisms support it.

---


### 184. [Predictable performance is suboptimal, and what it means for model routing](https://arxiv.org/abs/2610.31428)

**<font color=#1a73e8>作者：</font>** Guanhua Zhang, Moritz Hardt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query. These methods rely on performance prediction: given a query, estimate whether a model will answer it correctly. Most routing methods train separate predictors of candidate models' performance to guide model selection. Our work shows that performance prediction only beats a simple baseline when the candidate model is suboptimal on the task or the performance predictor adds significant capacity relative to the candidate model. Specifically, we take a model's self-confidence, the probability it assigns to its chosen answer, as a baseline and study how much a performance predictor can improve on it. First, we show that any performance predictor that outperforms a model's self-confidence can be used to improve the model's loss: the predictor's advantage transfers exactly in log loss through recalibration. Second, accounting for the predictor's additional parameters, we bound its advantage by the model's suboptimality plus the gain from those parameters. Third, we extend our theoretical results to two-model cascades, which route queries to a more capable model when the first model is predicted to fail. Experiments with 16 language models on four benchmarks show that predictors gain a larger advantage over self-confidence on more suboptimal models. This advantage shrinks as models improve through finetuning. Cascading exhibits the same two patterns: predictor-based routing offers larger gains over confidence-based routing for more suboptimal models, and these gains diminish after finetuning.

---


### 185. [PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models](https://arxiv.org/abs/2610.31429)

**<font color=#1a73e8>作者：</font>** Taekoan Yoo, Wonkyung Jung, Kyunghun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models increasingly rely on pretrained video models assumed to capture physical dynamics for prediction, planning, and action generation. Existing evaluations assess plausibility, probe representations, or measure predictive surprise, but rarely identify which history-conditioned physical expectations conflict with observations. We introduce PhysTrace, a training-free framework aligning MLLM-generated, history-conditioned expectations with observed video windows to temporally localize physical violations and provide interpretable descriptions without task-specific probes or classifiers. We also introduce IntPhys2-Timing, adding violation intervals to IntPhys2. PhysTrace achieves a Hit Rate of up to 70.7% across physical principles on IntPhys2-Timing and outperforms the compared methods in overall possible-impossible discrimination accuracy on IntPhys2. Applied to reconstructed videos along the trajectories of pretrained diffusion/flow-based video models, PhysTrace reveals attribute- and noise-dependent patterns in physical violation localization, enabling interpretable physical consistency analysis across timesteps.

---


### 186. [Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation](https://arxiv.org/abs/2610.31433)

**<font color=#1a73e8>作者：</font>** Bin Hu, Yingbo Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache compression for multimodal LLMs usually selects the visual tokens to keep once, at prefill, and reuses that selection for the whole generation. We show that this one-shot selection is severely limited on long-form generation: on detailed image description, even an oracle that selects with the attention of the uncompressed answer reaches only 0.44-0.52 ROUGE-L agreement with the uncompressed output, because the evidence the model reads moves as the description unfolds. Re-selecting whenever attention drifts out of the kept set is the natural remedy, but we find that a fixed drift threshold fails systematically: drift magnitudes are not comparable across samples, so low-drift samples are almost never refreshed although they benefit the most. We propose Rate-Controlled Refresh (RCR), which lets drift decide when and where to re-select while a per-sample controller regulates how often, combined with a low-rank drift detector, candidate-restricted re-selection, and a decision that stays on the GPU. With one setting for all models and tasks, RCR outperforms the per-step retrieval method InfiniGen by 1.6-3.8 ROUGE-L points on five of six model-task settings with no significant difference on the sixth, while staying within 1.7 points of exact per-step re-selection, with comparable estimated data movement per step and a 4x smaller GPU-resident detector. On DetailCaps, drift-chosen timing beats random timing at the same refresh rate and periodic timing even at a higher rate, by 2.0-5.0 points. On pre-registered video description, where drift is homogeneous across samples, RCR is on par with InfiniGen on Qwen2-VL and exceeds it on Qwen3-VL but no longer beats a fixed threshold at the nearest tested rates, consistent with the diagnosis; object-level evaluation shows that RCR achieves higher object F1 against the uncompressed output than InfiniGen on two of three models.

---


### 187. [DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels](https://arxiv.org/abs/2610.31438)

**<font color=#1a73e8>作者：</font>** Thanh Q. Tran, John Russell Himawan, Arun Verma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a user says "Keep it short", how short should the LLM's response be? More generally, users and applications require different levels of instruction adherence, but prompting does not reliably provide fine-grained control over them. We therefore study "steerable language models" that provide fine-grained numerical control over the degree to which models follow general instructions specified in text. However, existing approaches do not jointly offer fine-grained control, efficiency, and scalability across diverse instructions. To address this gap, we introduce DIAL (Distilled Instruction-Adherence Levels) to achieve all three properties. For fine-grained control, we perform classifier-free guidance (CFG) with a frozen LLM to provide training signals for on-policy distillation of instruction adherence at different levels. For efficiency, we design a lightweight steering adapter that uses a classifier over the LLM's hidden states to compute a closed-form steering edit. The classifier adaptively sets the steering magnitude at each token based on the target adherence level, while accounting for the geometry of the LLM's hidden states to preserve response coherence. For scalability, the classifier is text-conditioned, allowing a shared adapter to support new instructions without per-instruction fitting, and training requires only instruction and request text. Evaluation across multiple LLM families shows that DIAL achieves a competitive balance between concept expression and response fluency, with concept scores increasing monotonically across adherence levels. We introduce SteerIF, an instruction-only dataset of 98, 625 concept, persona, verifiable, and descriptive instructions. When trained on SteerIF, DIAL provides fine-grained control over personas and, when combined with prompting, improves verifiable instruction following.

---


### 188. [Multi-Token Prediction and Alternative Tokenization Improve Learning Latent Multi-Hop Graph Search at Scale](https://arxiv.org/abs/2610.31439)

**<font color=#1a73e8>作者：</font>** Arvid Frydenlund, FuTe Wong, Katherine Lambert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given an unseen graph, a start node, $s$, and an end node, $t$, can a language model generate the shortest path from $s$ to $t$? Prior work has found that models fail to learn this task as the graphs scale. We show that this failure has two causes: the supervision signal and the tokenization. First, we theoretically establish and empirically demonstrate the effectiveness of multi-token prediction (MTP), and show that the benefits of MTP are topologically agnostic. Second, we introduce alternative tokenizations and show that the two causes are orthogonal. Using these methods, we break through the scaling wall observed by prior work, consistently and stably learning to solve the task at scales far beyond previous limits.

---


### 189. [Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](https://arxiv.org/abs/2610.31461)

**<font color=#1a73e8>作者：</font>** Dingxuan Zhang, Yanhui Jiang, Jun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce Adaptive Skill Granularity, a framework that treats skill granularity as an action-abstraction policy conditioned on task structure, execution state, and macro-skill failures. The system combines a feature-based granularity controller and a finite-state recovery executor. We evaluate the framework with a deterministic coding-agent protocol using verifier-defined success, total cost, and process metrics such as macro adoption, failure recovery, route match, and transition correctness. Results show that fixed macro execution is efficient when applicable but brittle under mismatch, while runtime routing and explicit macro-to-micro recovery improve robustness and recover controlled macro failures that fixed-granularity execution leaves unresolved. Our findings suggest that skill libraries for coding agents should be treated not only as retrievable resources, but also as controllable, verifiable, and recoverable execution abstractions.

---


### 190. [AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark](https://arxiv.org/abs/2610.31466)

**<font color=#1a73e8>作者：</font>** Ruicong Liu, Liangyang Ouyang, Fengbo Lan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact.
Our AnyGameRenderer generalizes across a wide range of genres that agents build, such as tower defense, auto-battlers, top-down survivors, turn-based battles, kart racing, and crowd runners.
AnyGameRenderer takes plain video as its game-state input, with no complex representations such as engine G-buffers, per-object class labels, or low-poly proxies. Gray blockouts, colored primitives, semantic maps, and wireframes all work as input.
It also preserves entity correspondence: group counts stay correct, and entities appear and disappear on the right frame.
We implement AnyGameRenderer by LoRA fine-tuning MiniMax-H3 ref2va, a 33B reference-video-conditioned video generation model. Training uses $\sim$10k paired clips from three sources: (i) multi-stream rendering data from 38 agent-made games exported from GEAR, an AI game-creation tool; (ii) two-stream rendering data from Unreal Engine, with programmatically controlled crowds, count changes, and entity scales; and (iii) real gameplay recordings, with pairs reconstructed via 3D-box detection.
To evaluate the entity correspondence, we propose an entity-level benchmark of 59 held-out cases with 753 entities, scored against ground-truth boxes. Compared with the base model, AnyGameRenderer better preserves entity correspondence: temporal match rises from 50.9\% to 62.9\%, missed count changes fall from 34.7\% to 21.3\%, and fewer entities are hallucinated or left unrendered.

---


### 191. [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](https://arxiv.org/abs/2610.31467)

**<font color=#1a73e8>作者：</font>** Bayram Ayadi, Florian Geissler, Johanna Schmidhuber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLMs) offer a promising mechanism for translating structured clinical information into readable narratives, but this process may introduce semantic drift, where clinically precise meaning is distorted during simplification. We investigate evidence-grounded health summarization for menstrual health monitoring using a constrained generation framework that combines structured evidence conditioning with Retrieval-Augmented Generation (RAG) using a prompt-based constrained generation framework. We evaluate semantic alignment using Natural Language Inference (NLI), atomic factuality metrics, and readability measures. Across three LLMs and 4,500 generated summaries, explicit grounding constraints consistently improve clinical alignment, particularly by improving uncertainty preservation and, once faithfulness is evaluated against retrieved evidence, generally preserving or improving faithfulness, while effects on omission remain model-dependent. We also find that improved clinical alignment comes at the cost of increased reading difficulty and medical terminology. These findings highlight the need to jointly evaluate faithfulness, uncertainty preservation, and readability when developing patient-facing medical LLM systems.

---


### 192. [Ask About the Right Moment: Training-Free Object Identity Reasoning for Video-Language Models](https://arxiv.org/abs/2610.31471)

**<font color=#1a73e8>作者：</font>** Di Yang, Xiaochang Li, Muyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many questions about a video concern one physical object. Where does the ball end up after the cups are shuffled? Which card is the queen? How often was the mug covered? Video-language models (Video-LMs) recognise such objects in single frames but do not keep them apart over time. On real shell-game videos, open models from 8B to 235B parameters, their thinking variants, a reinforcement-learned tool agent and three training-free tool agents all stay within ten points of chance. We separate semantic identity binding from temporal identity maintenance. An object's identity should be fixed at a moment when the evidence for it is visible, and carried afterwards by a tracker. \emph{Track, Then Bind} implements this principle without training. A promptable video tracker follows every candidate object and draws it with a track number. A frozen vision-language model answers a static question about the identifying evidence, which binds the target to a track. The answer is then derived from the tracked state in text, without asking the model to reinterpret the original video during read-out. A single configuration covers all benchmarks. With Qwen3-VL-32B it solves both VET-Bench tasks, where a fine-tuned trajectory model reaches 92\% and 90\% and the same VLM voting over 16 samples stays at 30--32\%. It answers 55.4\% of the hardest Perception Test cup games, where the best published model answers 41.5\%, and, using track-derived timelines, 48.6\% of TOC-Bench questions, against 37.1\% for the same model answering directly. Drawing the same tracks on the video and asking the question directly falls 12--19 points short of the agent on real cup games.

---


### 193. [MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models](https://arxiv.org/abs/2610.31478)

**<font color=#1a73e8>作者：</font>** Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is necessary. To this end, we introduce Temporal Gradient Magnitude (TGM) which performs content-aware sampling to concentrate computation on informative regions while avoiding redundant processing. We further introduce a hierarchical dual-stream design in which dense multi-frame VLM reasoning is activated only around frames with elevated anomaly likelihood, via anchor-triggered context-window expansion with early termination. A fusion module then reconciles these instantaneous semantic cues with temporal action dynamics. Across four benchmarks, our method achieves 91.91%, 84.30%, 87.88%, and 78.96% AUC-ROC on XD-Violence, UCF-Crime, MSAD, and ShanghaiTech, respectively, establishing new state of the art on three benchmarks under the zero-shot, training-free setting. On XD-Violence, we improve over the previous best result by +0.57% while delivering a 1.31x inference speedup. These results demonstrate that content-aware allocation of VLM capacity, processing fewer frames more intelligently rather than all frames uniformly, is a more effective axis of progress than uniformly densifying VLM inference across frames. Code is available on GitHub: this https URL.

---


### 194. [Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon](https://arxiv.org/abs/2610.31479)

**<font color=#1a73e8>作者：</font>** Kyrylo Yemets, Andrii Yaroshevych, Victor Muryn 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads. Which optimizations retain their benefits when moved to Apple Silicon, and what determines their applicability? We evaluate four optimization families: KV-cache pruning, speculative decoding, ported GPU kernels, and post-training quantization. Experiments span four Apple machines under a common single-request decode workload, with matched RTX 4090 comparisons where possible. KV-cache pruning can reach up to 1.75 times end-to-end throughput on Apple but can reduce throughput on desktop NVIDIA GPUs. Under the common benchmark, all evaluated speculative decoding methods reduce throughput on Apple, despite reported 2-6 times gains on server GPUs. CUDA kernel designs transfer only partially: public Metal lacks asynchronous copy, and batch-one decode makes several serving-oriented mechanisms inapplicable, although transferable components yield up to 1.20 times decode throughput. Quantization gains vary by machine. Across four families, a reported speedup is not a portable property of a technique alone but a joint function of technique, runtime, hardware contract, and workload regime.

---


### 195. [Training Small Language Models for Transferable Tool Selection](https://arxiv.org/abs/2610.31483)

**<font color=#1a73e8>作者：</font>** Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open model can be trained via reinforcement learning to perform the same functionality. On ToolBench, a Qwen3-8B model post-trained with our recipe outperforms Llama-4-Maverick (402B). In addition, the trained model transfers directly to different retrievers and generalizes to new tool corpora in different domains.

---


### 196. [AgentVQA: A Unified Benchmark for Agentic Visual Understanding](https://arxiv.org/abs/2610.31494)

**<font color=#1a73e8>作者：</font>** Advait Gupta, Sachin Konan, Tom Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons across agentic domains, yet existing benchmarks remain limited and fragmented. To address this gap, we introduce AgentVQA, an offline benchmark for evaluating VLMs on realistic agentic scenarios across five agent domains: Web Agents, Robotics, Egocentric Videos, Games, and Spatial Planning. We build AgentVQA by manually selecting 1000 challenging, real-world agent examples from 23 source datasets and adapting them for reliable offline evaluation. The resulting benchmark preserves realistic scenarios from interactive environments across diverse domains, and its model rankings track those from corresponding online evaluations. Across the 22 evaluated models, the best achieves only 58.5% accuracy. Our cross-domain analysis shows that errors are driven primarily by failures to ground and maintain accurate representations of the current and evolving visual state, including localizing relevant UI elements, interpreting motion, tracking state changes over time, and inferring 3D spatial relationships, rather than by task misinterpretation or downstream logical reasoning.

---


### 197. [DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination](https://arxiv.org/abs/2610.31511)

**<font color=#1a73e8>作者：</font>** Ziyi Jiao, Heng Zhang, Drishti Regmi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding agents. A single vision-language model controls both players from top-down visual observations, selecting high-level actions while the engine executes navigation. The benchmark contains 20 maps in five categories. These categories support evaluation of centralized coordination under equipment contention, changing terrain, and handoff dependencies. A prop legend and pot ingredient-count indicators provide explicit visual cues, while grid-based destinations support spatial grounding. The evaluation compares four VLMs on all 20 maps, measuring task score, order completion, delivery precision, action acceptance rate, and model API expenditure. A memory ablation on the same 20 maps examines the effect of a shared, self-authored notebook while retaining six-response action history in both conditions. The strongest evaluated model, \texttt{gpt-6-astra}, achieves 26.2\% mean order completion. Notebook memory has mixed score effects across models, with positive mean differences for Claude and Qwen and negative differences for GPT and Gemini.

---


### 198. [Towards User Simulators That Stay On Task And Still Sound Natural](https://arxiv.org/abs/2610.31512)

**<font color=#1a73e8>作者：</font>** Mustafa Omer Gul, Philippe Laban, Tanya Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users increasingly rely on AI systems for extended, multi-turn tasks, yet evidence indicates that LLM-based system performance degrades over prolonged interaction. To evaluate and improve AI assistants in such settings, we need user simulators that faithfully follow complex user intents while exhibiting realistic conversational behavior. Existing approaches manifest a trade-off: prompted assistants can follow complex user intents but lack behavioral fidelity, while specialized user simulators better approximate conversational behavior but struggle to remain faithful to complex intents. In this paper, we propose a reinforcement learning (RL) recipe that jointly rewards task intent adherence and behavioral naturalness. A crucial contribution of the method is operationalizing naturalness with a lightweight discriminator trained in an alternating, adversarial loop with the user simulator. We release the resulting model, UserLM-2.0, which produces valid simulated conversations (i.e., meeting both task-faithfulness and naturalness criteria) 46.2% of the time, over three times the rate of the strongest prior user simulator (14.1%).

---


### 199. [From Prompt Rules to Golden Data Model: Production-Scale Generation of Personalized, Compliant Pharmaceutical Claims](https://arxiv.org/abs/2610.31519)

**<font color=#1a73e8>作者：</font>** Suyash Mishra, Qiang Li, Subhabrata Adak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate domain-specific commercial & medical content (e.g., claims, statements, and promotional phrases) in regulated industries such as pharmaceuticals. However, ensuring its regulatory compliance, factual accuracy, and audience-specific personalization remains a major challenge. We report a production case study asking whether moving compliance and personalization signal from prompt-level rules into retrieval time structured context improves pharmaceutical claims generation, using Composer, a deployed internal tool built on a Golden Data Model (GDM) of 1,867 pharmaceutical claims spanning four products. The GDM integrates claim metadata, references, audience labels, material type, usage history, Match Text Variant (MTV) links, and a six dimension quality score (6C). Across six product-audience segments, the context pipeline improves intended indication (+29%), intended content type (+62%) and intended target audience (+67%), 6C quality score (+86%), and claim reuse (+34%). Production log analysis over the deployment period shows a 29.5% reduction in weekly API cost. We report this as descriptive deployment evidence. This work is a systems and data architecture contribution: it shows that in a regulated, high-stakes domain, restructuring claim data for retrieval-time filtering is a more scalable lever than expanding prompt-level rules, and documents the engineering path data cleaning, graph linking, and quality scoring.

---


### 200. [The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models](https://arxiv.org/abs/2610.31520)

**<font color=#1a73e8>作者：</font>** Shihui Li, Mette Andersen, Martha Lewis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that these techniques can be used to control the metaphoricity of LLM output.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
