# 🧠 大模型相关研究 | 2026年10月23日

> 本类共 **204** 篇论文：已确认 **192** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

---

### 151. [Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting](https://arxiv.org/abs/2610.29784)

**<font color=#1a73e8>作者：</font>** Zhipeng Chen, Yunsen Liang, Yanxi Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most contemporary artificial intelligence (AI) systems are released with frozen parameters and improve through external updates, whereas an ideal system would keep improving from its own experience, a capacity we call recursive self-improvement (RSI). Yet studying RSI requires an environment that is continuously changing, objectively verifiable, and naturally grounded, posing a fundamental challenge for agent evolution. Here we introduce DeepEvolve, a sustainable evolution agent system grounded in future event prediction, in which agents continuously interact with a dynamically evolving environment and improve by internalizing and externalizing the experience gained through these interactions. A living environment synthesizes verifiable tasks, and a recursive-evolution engine turns the reasoning trajectory behind each prediction back into capability: decoupling search from prediction adapts parameter-level evolution to the contamination-prone live environment, while distilling reusable skills lets the agent evolve from the limited live trajectories such an environment affords. On the external FutureX leaderboard, which evaluates predictions against real-world outcomes and is updated weekly, our self-improved forecaster ranked first across all systems over three consecutive weeks, achieving up to a 195% improvement in rating. On our synthesized evaluation, it ranked among the top three across four base LLMs, outperforming the strongest baseline by up to 10.7 Bradley--Terry points. More broadly, these results suggest that a system built for self-improvement is best understood as an agent that co-evolves with a genuinely living, open-ended environment, pointing to a shift in AI from training static models on fixed data toward cultivating agents that grow stronger from their own experience, with such an open world as the indispensable basis of that growth.

---


### 152. [Where Do LLMs Learn to Recommend AI?](https://arxiv.org/abs/2610.29785)

**<font color=#1a73e8>作者：</font>** Benaya Trabelsi, Jonathan Shaki, Sarit Kraus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Asked what to study, which career to pursue, or what product to build, large language models (LLMs) often recommend AI-related options. We ask where this tendency comes from by comparing models before and after fine-tuning and by varying how questions are asked. First, pretrained models already include explicit AI/ML terms in the recommendations of 27% of their responses, and their released instruction-tuned versions do so in 59%. Second, fine-tuning models ourselves shows that this rise is not inevitable: general instruction tuning leaves the rate unchanged, but removing the 7% of instruction examples that concern AI cuts it by 14 percentage points, below the level of the pretrained models it starts from. Data rewarding helpfulness raise it by 9 points, while data ranked by the preferences of diverse simulated users lower it by 9. Finally, with models held fixed, asking for the "best" option or for what to do "right now" raises the rate by 8 and 18 points, whereas telling the model it is an AI advisor adds 4. Overall, the tendency starts in pretraining, and what models learn afterward, together with how a question is phrased, decides how strongly it appears.

---


### 153. [MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29792)

**<font color=#1a73e8>作者：</font>** Xinze Li, Dingwen Zhang, Zhenghao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves the performance of Large Language Models (LLMs) by retrieving external knowledge. Recently, some RAG methods interleave reasoning and retrieval, enabling LLMs to progressively generate sub-queries and retrieve external knowledge. However, these methods may suffer from redundant or ineffective sub-queries and insufficiently diverse query exploration. Moreover, due to the tightly interleaved nature of reasoning and retrieval, it remains unclear how the evolving reasoning process influences query intent. To characterize the evolution of query intent during reasoning, we introduce search momentum, which captures the accumulated retrieval tendency induced by historical changes in generated sub-queries along the reasoning trajectory. Through momentum-based analysis, we find that the query generation process tends to continuously evolve along existing retrieval trajectories. Based on this observation, we propose MAPS, a Macro-Adaptive Parallel Reasoning framework for regulating search momentum and mitigating query-intent drift. MAPS first retains the retrieved knowledge and a refined reasoning state, thereby reducing the influence of historical reasoning trajectories on subsequent sub-query generation. Subsequently, MAPS extends the conventional sequential reasoning process into a parallel reasoning paradigm. At each iteration, MAPS identifies complementary retrieval directions, generates corresponding sub-queries for parallel retrieval, and consolidates the retrieved evidence to update the knowledge and reasoning states. Experiments on six question-answering benchmarks demonstrate that MAPS consistently outperforms representative RAG methods across different backbone models. All code and resources are available at this https URL.

---


### 154. [Compositionality with Primitives: A Unified View from Euclidean to Hyperbolic Vision-Language Models](https://arxiv.org/abs/2610.29811)

**<font color=#1a73e8>作者：</font>** Puru Vaish, Meelad Dashti, Christoph Brune 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional zero-shot learning (CZSL) aims to recognize novel combinations of previously observed objects and attributes. Prior work showed that large-scale vision-language models encode decomposable semantic structures that can be recomposed to enable generalization. The Geodesically Decomposable Embeddings (GDE) framework formalizes this by identifying directions in the tangent space at the Frechet mean of the embedding distribution, which encode primitive visual concepts. Unseen attribute-object compositions can be synthesized through vector addition of these primitives. We revisit the assumption that compositional generalization requires explicit attribute-object pair re-composition. By means of new compositional scoring functions and extensive evaluations, we show that directly using the decomposed primitives suffices for recognizing unseen compositions. In that, we gain insights on how the geometry of the embedding manifold (Euclidean, spherical, or hyperbolic) and dataset structure affect compositional reasoning. Across models (CLIP, DINOv2, MERU, HyCoCLIP), we show that compositional structure consistently emerges as primitive representations, enabling inference on CZSL benchmarks (MIT-States, VAW-CZSL, UT-Zappos50K, Clothing16K) and group robustness on Waterbirds and CelebA. Code: this https URL.

---


### 155. [Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents](https://arxiv.org/abs/2610.29812)

**<font color=#1a73e8>作者：</font>** Mohammed Saqlain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Literature-searching language agents are becoming a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on which parts of their harness matter. We run a controlled ablation on biomedical claim verification (SciFact) with the live PubMed API as the only tool. Holding the backbone and output format fixed, we compare four harnesses: closed-book answering, single-shot retrieval using the claim as the query, a ReAct-style agent that writes its own PubMed queries, and an oracle given the gold abstracts, each with two efficient frontier backbones. Naive single-shot retrieval finds the gold paper for only 6% of claims and turns overconfident errors into abstentions without improving accuracy. Letting the model formulate its own queries triples gold recall and yields the best verdicts (62% accuracy vs. 49-59% for the other realistic harnesses), although these differences are not significant at our sample size and agents use fewer than half of their search budget. With gold abstracts, the same models reach 79-86% accuracy, a significant 17-24 point gap showing that retrieval, not reasoning, is the main bottleneck. Finally, a citation audit shows that closed-book models cite PubMed IDs that almost always exist (327/335) but are almost never relevant: a cross-family LLM judge rates only 3 of 327 existing citations as relevant to the claim, versus 67% for citations produced by the search agent. Existence checks are therefore insufficient safeguards for scientific agents. We release code, prompts, and all cached tool calls at this https URL.

---


### 156. [UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822)

**<font color=#1a73e8>作者：</font>** Zhan-Yu Wu, Ji Luo, Alyssa Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As coding agents become more capable, developers increasingly use them to fix bugs through multi-turn interactions. Existing benchmarks do not adequately cover this scenario. Most present a complete issue report in a single turn without interaction. Their evaluation can produce both false positives and false negatives, accepting incorrect patches or rejecting correct ones. We introduce UserSWE for evaluating coding agents' ability to fix repository-level bugs through multi-turn interactions with dynamic users and execution-grounded verdicts at every turn. Its construction pipeline turns repository history and existing single-turn benchmarks into multi-turn tasks. At each turn, information pools constrain what the simulated user can reveal, while a persona chain sampled from a transition model calibrated on 20,859 development sessions governs how it speaks. Tests run after every turn, and a pair of agents from different model families writes and gates each verdict, using test results as primary evidence and model judgment only for aspects the tests cannot resolve. We evaluate eleven agents on 72 tasks from 42 repositories and find that agent rankings change with the interaction budget. Claude Fable 5.1 resolves the most tasks in one turn, GPT-6-Astra resolves the most by the eighth turn, and Claude Opus 5 leads at most intermediate budgets. These results indicate that single-turn performance is insufficient to characterize interactive coding ability.

---


### 157. [MemoryTax: The Bitter Lesson of Agent Memory](https://arxiv.org/abs/2610.29823)

**<font color=#1a73e8>作者：</font>** Zedong Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems such as Mem0 and Zep decide what to keep before any question arrives; coding agents keep the raw history and let the model search it with its own tools. We ask whether designed memory still helps once the model is strong enough to search for itself. On one LoCoMo conversation (419 turns, 152 questions), we run four memory methods (full context, BM25, Mem0, Zep) and three coding agents (Pi, Codex, Claude Code), each with GPT-4o-mini, GPT-6 Luna and Claude Opus 5.5, and record what every rollout costs. This is a short empirical study, with one conversation and one run per cell. Agent memory is a costly patch for a weak model: Mem0 beats full context only with GPT-4o-mini, and its build alone costs more than a whole full-context rollout. Agent memory also has a ceiling, set by the model that writes it: a stronger reader does not recover what a weaker writer left out. With Claude Opus 5.5, Pi tops the cost-accuracy frontier, scoring 99% for less than half the cost of full context; its one miss is a wrong answer key. Part of that lead comes from photo captions that only the agents could read: on the 88 questions whose evidence has no photo, Pi and full context differ by one answer.

---


### 158. [S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs](https://arxiv.org/abs/2610.29832)

**<font color=#1a73e8>作者：</font>** Yawei Li, Jiazheng Li, David Rügamer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calibrating large language models (LLMs) in open-ended generation is uniquely challenging because many distinct token sequences can express the same underlying meaning. Prior calibration techniques target either fixed-set classification confidence or the binary correctness of individual strings, making them inherently ill-suited for the dynamic, multi-string nature of open-ended semantic outcomes. To bridge this gap, we introduce S-EDL, a novel evidential method that natively optimizes LLMs for semantic calibration. By eliciting evidence from the sequence likelihoods of the model itself, S-EDL constructs a differentiable Dirichlet prior over prompt-specific semantic classes. Optimizing the evidential loss under this prior yields a calibration-aware training signal over variable semantic classes, completely bypassing the need for fixed multiple-choice options. Evaluations across four open-ended benchmarks and three models demonstrate that S-EDL substantially reduces semantic calibration error while improving accuracy. By aligning generative likelihoods with semantic correctness, this work establishes a framework for deploying trustworthy LLMs in complex, open-ended applications. Code is available at: this https URL.

---


### 159. [Every Part Has Its Role: Part-of-Speech Effects in LLM Post-Training](https://arxiv.org/abs/2610.29843)

**<font color=#1a73e8>作者：</font>** Laya Iyer, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are typically trained with next-token prediction (NTP), which rewards predicting specific tokens rather than explicitly accounting for the semantic similarities between different words or expressions. Prior work has addressed this limitation by augmenting training data with minimally varying sentences that replace a target word with conceptually related alternatives, e.g., "The tired coach ran home" $\rightarrow$ {"The tired trainer ran home", "The tired instructor ran home", ...}. Such concept augmentation improves performance, but it remains unclear whether its effectiveness depends on where in the sentence the concept is expressed. We reproduce and extend prior work $\textit{beyond nouns}$ to verbs and adjectives, asking whether the part of speech (POS) carrying the concept signal affects perplexity and downstream performance. We find different patterns across evaluation settings: concept augmentation improves perplexity most consistently on news, independent of the POS used, whereas verbs provide the most reliable downstream gains. Despite these behavioral differences, representational analyses using CKA and linear probing show that the conditions yielding the largest downstream gains are not necessarily those that most alter the model's internal representations. Together, these results suggest that the effectiveness of concept augmentation depends on where and how conceptual information is introduced during training.

---


### 160. [GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.29866)

**<font color=#1a73e8>作者：</font>** Qinfan Zhang, Yifan Luo, Haoyuan Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric structure is essential for robotic manipulation and understanding the 3D world. Most VLA models rely on 2D representations of current observations, while geometry-aware approaches often require additional 3D information. However, geometry inferred independently from individual observations is often discarded rather than accumulated into a persistent task representation. Our key insight is that action generation needs a compact, task-relevant geometric abstraction that can be continuously updated, rather than a complete, renderable 3D reconstruction at every step. We introduce GeoMem-VLA, a VLA framework that internalizes explicit 3D supervision into dedicated geometric tokens and maintains them as temporal memory for action generation, without directly aligning the VLM's native visual embeddings with the teacher feature space. During training, a frozen geometry foundation model supervises learnable GeoPlan tokens through a geometric flow-matching objective over the current scene point map and future end-effector tracks. These tokens are integrated with the memory of observation representations, where historical information is retrieved, adaptively fused with current observations, and consolidated to retain event frames as the task progresses. At inference, the policy retrieves historical representations and fuses them with the current working representation to predict actions, without invoking the 3D teacher or explicitly reconstructing the scene. After benchmark-specific downstream adaptation, GeoMem-VLA achieves 98.9% average success on LIBERO and 91.10% / 91.24% on RoboTwin's clean/randomized settings. Across five real-world tasks, GeoMem-VLA achieves 78.0% average success. These results suggest that internalizing and remembering 3D scene understanding is a promising approach to robot control.

---


### 161. [Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents](https://arxiv.org/abs/2610.29869)

**<font color=#1a73e8>作者：</font>** Arshan Dabirsiaghi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents that run long enough must compact their context, summarizing the conversation, discarding the original, and carrying the summary forward as memory. We show that in popular open-source coding agents this step is an exploitable trust boundary. Harnesses that flatten the typed conversation into a single plain string, marking each message with a text label such as [User]:, destroy message provenance in code, before the summarizer runs. An attacker who controls anything the agent reads can forge a user turn that survives compaction as a genuine instruction. Across five flattening harnesses (pi, opencode, Cline, Aider, OpenHands) the forged approval launders into the agent's memory 87-100% of the time, up to a ~908,000-token context window; across four role-typed harnesses (Codex, Gemini CLI, Qwen Code, Continue) the identical attack succeeds 0% of the time. We follow the attack to executed consequences. A laundered standing approval drives real tool-running agents to execute attacker-controlled
curl | sh in a sandbox, and end to end in the live pi TUI at ~50% against a 0% paired clean arm. The same channel reliably steers an agent's plan away from a file an attacker designates off-limits, which can blind a code review to a planted backdoor. Because the provenance is destroyed deterministically in harness code, no prompt-level defense can restore it; we measure a code-level provenance check that catches 77% of laundering while demoting 2% of legitimate summary content. The defect also has a straightforward fix at the serializer, escaping the role labels before flattening; the role-typed harnesses avoid it entirely by keeping messages role-typed.

---


### 162. [Characterizing and Defending Utility-Hijacking in Instruction-Tuning Data Selection](https://arxiv.org/abs/2610.29886)

**<font color=#1a73e8>作者：</font>** Yahao Ren, Jian Lou, Huadi Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Instruction-data selectors choose which instruction-following records are used for fine-tuning, improving alignment quality, raising training efficiency, and filtering out harmful records. A selector's choices thus directly affect the fine-tuned model's safety, yet despite their widespread use, the security of these selectors remains under-studied. We conduct the first systematic study of adaptive supplier-side attacks against utility-oriented instruction-data selectors and introduce utility-hijacking. Utility-hijacking shapes harmful records to remain compatible with a selector while preserving their malicious payload, causing top-k selection to concentrate rather than filter the poison. Achieving both is non-trivial, because optimizing a record for score tends to wash out its payload, while bluntly preserving the payload makes the record look low-value. Our generate-and-rerank procedure generates, per instruction, many payload-bearing candidates and submits only the highest-scoring survivor. Evaluated across three payloads (over-refusal, false-fact injection, and insecure code), six selectors, and victim models from Qwen2.5-7B to Qwen3-32B, utility-hijacking drives refusal from 0% to 94% and insecure code up to 56/90, while false-fact enrichment intensifies with scoring-model scale from 2.84x to 7.04x. To defend against this attack, we propose CONCERT, a targeted defense needing no content detector or poison labels. It flags suppliers selected far more often than chance allows, then re-selects under the same budget, keeping only records that two dissimilar selectors both rank highly. On a Qwen3-32B victim, CONCERT reverses the poison concentration from 6.67x to 0x (code) and 3.59x to 0.67x (facts), and reduces downstream harm by 100% and 75% respectively, at unchanged capability.

---


### 163. [Investigating the Impact of Learner Errors on Social Bias in Large Language Models](https://arxiv.org/abs/2610.29896)

**<font color=#1a73e8>作者：</font>** Federico Marcuzzi, Martin Christoph, Iryna Gurevych 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing social bias benchmarks evaluate large language models mostly on fluent, well-formed English, reflecting native speaker usage and leaving non-native writers unrepresented. To address this gap, we investigate how grammatical errors by non-native writers affect social bias. We develop a controlled framework that injects common learner errors into prompts and apply it to three bias benchmarks covering stereotype alignment and demographic preference across gender, race, and religion. We find that grammatical errors increase bias, and the effect grows with the error rate. Among the four common error types we consider, preposition errors produce the largest and most consistent increase in stereotype alignment. Our analysis suggests that errors increase bias when they are more likely to interfere with comprehension. Finally, fine-tuning on erroneous texts reduces the bias increase caused by grammatical errors. Our findings show that bias evaluations based exclusively on well-formed prompts may underestimate the bias experienced by users whose English contains grammatical errors.

---


### 164. [ViBMR: A Large-Scale Multi-Sequence Brain MRI Dataset and Comprehensive Evaluation for Vietnamese Radiology Report Generation](https://arxiv.org/abs/2610.29905)

**<font color=#1a73e8>作者：</font>** Dai Lam Le, Minh Khoi Nguyen, Son Dinh Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation for multi-sequence brain MRI holds strong promise for alleviating radiologists' workload, yet it remains a demanding problem: brain MRI studies are inherently volumetric, each pulse sequence carries complementary diagnostic information, and annotated data are critically scarce for low-resource clinical languages. Existing brain MRI-report resources are still dominated by English reports, translated clinical text, or datasets adapted from task-specific imaging benchmarks, leaving routine low-resource clinical reporting and heterogeneous multi-sequence MRI protocols insufficiently represented. To bridge this gap, we introduce ViBMR, to the best of our knowledge, the first large-scale multi-sequence brain MRI dataset paired with routine Vietnamese clinical reports, comprising 3,649 patients and 11,875 MRI series across T1, T2, FLAIR, and contrast-enhanced T1 sequences. Building on ViBMR, we establish a comprehensive evaluation setup for brain MRI report generation, covering representative medical vision-language models, multi-sequence inputs, and feature aggregation strategies. The results provide key insights into dataset characteristics and model behavior, while demonstrating the necessity of native low-resource clinical datasets for reliable Vietnamese-origin brain MRI report generation. Our dataset and baseline models will be released for non-commercial research.

---


### 165. [Benchmarking Large Language Models for Detecting Satirical Code-Mixed Sentences](https://arxiv.org/abs/2610.29907)

**<font color=#1a73e8>作者：</font>** Răzvan-Alexandru Smădu, Ioana Buhnila, Daniela Tanase 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching is a natural linguistic phenomenon, yet its impact on high-level reasoning tasks remains largely unexplored in under-resourced languages like Romanian. Natural language processing tasks, such as satire detection, rely heavily on nuanced cultural and syntactic cues that large language models struggle to capture. In this paper, we investigate four methods (i.e., random replacement, phrase translation, dependency parsing, and large language models) for generating synthetic code-mixed Romanian sentences with English, German, French, and Italian. We start with an existing dataset for satire detection, compiled from Romanian news articles and annotated at the sentence level by humans, and augment it with over 600k samples, namely CS-SeLeRoSa. We provide an in-depth analysis of the dataset generation process. Then, we evaluate several multilingual large language models across zero-shot, chain-of-thought, and fine-tuning regimes on both the synthetic corpus and a human-adjudicated gold benchmark, namely CS-SeLeRoSa-Gold. While older open models suffer substantial degradation (dropping to 37%-55% macro-F1), newer models like Gemma 4 31B achieve 68.1% zero-shot, rivaling frontier models like GPT-5 mini (69.5%). Furthermore, fine-tuning significantly reduces formatting errors and improves the results, increasing Gemma 4 31B to 77.5% on CS-SeLeRoSa and 72.6% on the gold standard, outperforming frontier zero-shot baselines.

---


### 166. [Asking a Multimodal LLM Whether Someone Fell: Zero-Shot Screening of Low-Resolution Thermal Video in a Laboratory and an Occupied Home](https://arxiv.org/abs/2610.29913)

**<font color=#1a73e8>作者：</font>** Marcos Junca, Mauro Junca  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal cameras can watch over older people living alone without capturing faces, and multimodal large language models (LLMs) can judge a short video without task-specific training. We evaluate a production multimodal LLM, Gemini 3.8 Flash at temperature 0, as the decision stage of an event-triggered fall screener, used exactly as a deployed prototype uses it: one request per short thermal clip, with its sound track when there is one, and its predecessor Gemini 3.7 Flash on the same requests. On 438 staged falls and 563 non-fall windows that we located by hand in a public 32x24 thermal dataset, the deployed request called 69% of the held-out subjects' falls (67% over all subjects; bed falls excluded) and none of 499 non-fall windows, including people lying on the floor and getting up. Over 76 h of ordinary life in an occupied room, recorded at 160x120 with sound, it called none of 395 clips a fall (95% upper bound 1.2 false alarms per day) and caught 4 of the 9 staged falls the camera could see. One cautionary sentence in the prompt ("a person who goes out of view ... is not a fall") accounted for many of the misses: removing it raised sensitivity on the held-out subjects from 69% to 83% on 3.8 Flash and from 80% to 92% on Gemini 3.7 Flash, and in the home from 4 to 9 of the 9 visible falls, with no false call in ordinary living but at the price of calling deliberate lie-downs a fall. Sensitivity collapsed at 8x6 pixels (34%); identical requests disagreed on 4% of windows; and when the model called a fall, its explanation placed it within a second of the annotated landing 99% of the time. Two conventional detectors trained on the laboratory data caught nearly every held-out laboratory fall but raised 14.2 and 23.9 false alarms per day in the home. We release the frame-level fall annotations of the public dataset and every model answer on it.

---


### 167. [Unintended Side Effects of Value Training in LLMs](https://arxiv.org/abs/2610.29922)

**<font color=#1a73e8>作者：</font>** Siddhesh Pawar, Chen Cecilia Liu, Anna Korhonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly deployed in value-sensitive contexts, aligning them with human values has emerged as a post-training objective in NLP, aimed at instilling additional values and guiding model behaviour. However, current evaluations remain narrow. Because values are interconnected, it is unclear how fine-tuning for specific values alters unrelated capabilities and behaviours. In this work, we adapt four instruction-tuned LLMs across individual Hofstede's value dimensions and evaluate them on both cross-value transfer and broader behaviours. We find that value-specific training produces unintended side effects on untrained values, risk preferences, social cognition, and safety traits. Consequently, we suggest that value alignment after post-training should incorporate broader behavioral evaluations, and we highlight the need to investigate where additional value training might best fit into the pipeline.

---


### 168. [Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs](https://arxiv.org/abs/2610.29925)

**<font color=#1a73e8>作者：</font>** Prakhar Ganesh, Yash More, Marco Romanelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) continue to grow in scope and capability, privacy concerns are on the rise. Since users increasingly interact with a single general-purpose system across many distinct contexts, there is a natural tendency to pursue a one-size-fits-all solution to privacy. Unfortunately, this overlooks a crucial insight from decades of privacy research: privacy is inherently contextual. In this paper, we argue that existing work in prompt privacy is drifting towards attempts to design a unified framework, which is highly misleading and can foster a false sense of security. Furthermore, we argue that even future work in this direction needs to wrestle with fundamental tensions across various desirable properties of prompt privacy. Thus, such continued attempts towards a unified framework need to be reconsidered. We recommend three critical paths forward: application-specific deployment of LLMs, context-specific evaluation of privacy frameworks, and better privacy literacy.

---


### 169. [Task-Preserving Multilingual Instruction Tuning for Open-Ended QA in WMT 2026 MIST](https://arxiv.org/abs/2610.29926)

**<font color=#1a73e8>作者：</font>** Aleix Sant, Jordi Luque, Carlos Escolano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our submission to the WMT 2026 Multilingual Instruction Shared Task. We adapt Qwen3-8B with LoRA using organiser-provided data, EuroAlpaca, a multilingual instruction dataset created through task-preserving localisation, and CrossEuroAlpaca, a cross-lingual augmentation that assigns different source and target languages to instructions, contexts and responses. Our system targets open-ended question answering (QA-OEG) in ten shared-task languages represented in the auxiliary data. Under matched decoding, adaptation improves the mean Gemma-4 judge score on target-language QA-OEG by 7.8% relative to the base model. On an additional evaluation using the Aya Evaluation Suite across all shared-task languages, it yields relative gains of 41.5% in macro-averaged ROUGE-L and 2.9% in BERTScore-F1, with larger improvements in target languages. However, these gains are task- and language-specific. Gemma-4 scores improve for QA-OEG and summarisation in the target languages but decline for context-grounded QA there and across all three tasks in the non-target languages.

---


### 170. [FrontierCS 2: A Benchmark for Computer Science R&D](https://arxiv.org/abs/2610.29932)

**<font color=#1a73e8>作者：</font>** Qiuyang Mang, Wenhao Chai, Runyuan He 等 61 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar. Earlier open-ended benchmarks give each agent a problem statement and grade one program after the run. FrontierCS 2 places the agent inside a research environment. The agent inherits a working repository and may submit a patch at any point. For each patch, a judge returns a development-suite score but keeps the evaluator, the held-out final suite and the reference private, and grades the final submission on that suite against the reference. The tasks span 13 domains, from machine-learning systems and high-performance computing to databases, security and robotics. Beyond these 48 tasks, FrontierCS 2 keeps a private set of more than 100 tasks, to be announced in the future. We evaluate 12 agents. The best one is Claude Opus 5.5, passing 58% of its runs. No run passes on 16 tasks. A higher score is not the same as a pass: most runs that beat the reference on the combined final score still fall short on some metric or workload. On a shared capability scale for agents and tasks, the median task is roughly as difficult as what the strongest agent can handle.

---


### 171. [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933)

**<font color=#1a73e8>作者：</font>** Yufeng Li, Zaijing Li, Fuchen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) frequently integrates knowledge graphs (KGs) for complex multi-hop question answering. However, their performance is increasingly bottlenecked by the knowledge structuring and reasoning processes. (i) Severe semantic loss: Distilling continuous texts into discrete symbols strips away contextual nuances and narrative coherence. (ii) Pronounced modality mismatch: Fragmented graph structures clash with the continuous texts LLMs are pre-trained on, while rewriting them into natural language introduces generative noise and omits information. To address these limitations, we propose ThreadRAG, a semantic-topology-based RAG framework for context-preserving knowledge structuring and modality-native evidence reasoning. ThreadRAG introduces a Semantic Topology Mapper (STM), which organizes retrieved documents into context-intact Semantic Nodes and constructs a Semantic Topology Graph (STG) through narrative, semantic, and lexical edges. It further incorporates Energy-Driven Pathfinding (EDP), which identifies query-relevant subgraphs via energy diffusion and deterministically linearizes them into coherent textual evidence paths. Experiments on three multi-hop QA benchmarks demonstrate that ThreadRAG consistently outperforms strong baselines. Notably, it achieves a 14.4% EM improvement over text-centric methods on HotpotQA and surpasses the best baseline by 5.8% EM on 2WikiMultihop, while reducing token cost to 23.3% of the strongest baseline.

---


### 172. [ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination](https://arxiv.org/abs/2610.29934)

**<font color=#1a73e8>作者：</font>** Nithin Sivakumaran, Ali Payani, Hyunji Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forming an accurate theory-of-mind (ToM) is key to successful multi-agent collaboration and requires reasoning under uncertainty to capture multiple possible partner states. This is hard to do in the text representation space native to large language model (LLM) agents, which more easily describe a single partner state. To address this challenge, we introduce ToM2Vec, which learns to form abstract theories-of-mind in a rich latent space via a fixed budget of continuous reasoning tokens. During training, supervision for these tokens comes from the partner's actual thoughts, which the ToM tokens are trained to abstract and match. At test-time, ToM tokens are generated by each agent and act as conditioners for that agent's thoughts and actions. Across several environments covering collaborative, competitive, and mixed-motive settings (Overcooked-AI, multiparty negotiation, Decrypto, Hanabi, and Collab Escape/Capture), we evaluate ToM2Vec's ability to support multi-agent interactions and collaboration, finding consistent improvements over the base model and a variety of competitive trained and prompted baselines. We show that latent reasoning is critical, with performance dropping when reasoning is expressed in text. Moreover, we show that ToM2Vec training generalizes to partner model families not seen at train-time, including a proprietary model (GPT-5.4). In our analysis, we provide evidence that the latent tokens encode a ToM, rather than task-specific information: ToM2Vec's tokens improve the agent's ability to directly answer questions about partner beliefs, desires, and next actions.

---


### 173. [Commit or Abstain? System One Decision Models, LLMs, and Missing Legal Authority](https://arxiv.org/abs/2610.29961)

**<font color=#1a73e8>作者：</font>** M. Mikail Demir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given the enormous number of claims to be checked, verifiable legal AI requires scalable, cost-effective models that answer the practical needs of law. System One decision models are built on large language models but, instead of generating text, return a calibrated probability for each option. This suits the verification of legal authority, where the question is closed: a given holding, or none of them. We test whether such models abstain when the correct authority is missing. We extend CaseHOLD with an abstention condition in which the correct holding is replaced in 1,670 of 5,314 items, and compare four decision models with six generative LLMs. When no option is correct, generative LLMs still pick one in 38-86% of items; the most cautious decision model does so in 30%. On standard CaseHOLD, a decision model matches the best generative LLM (88.1% vs. 88.2%) at 1/55 of the cost. Accepting that LLM's answer only when a decision model agrees halves its wrong citations, and distilling a decision model's probabilities into Qwen3-8B, without labels, yields a well-calibrated local model. Legal AI should be judged by its wrong citations, not by accuracy alone.

---


### 174. [CulturalRiddles: A Multicultural Benchmark of Riddles](https://arxiv.org/abs/2610.29968)

**<font color=#1a73e8>作者：</font>** My Chiffon Nguyen, Tianyi Hu, Vinod Anbalagan 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs expand their language coverage, evaluating how well they understand and represent diverse cultures becomes increasingly important. However, many benchmarks remain English-centric, with limited cultural coverage and a focus on factual knowledge over its application in real-world cultural contexts. We propose CulturalRiddles, a benchmark of original, culturally grounded riddles created entirely by humans through a participatory community effort, spanning 62 cultures (45 countries, 51 languages). These riddles are deeply rooted in their respective cultures and require abductive and compositional reasoning, alongside detailed factual and social knowledge, language skills, and an understanding of culturally specific associations. We benchmark 28 LLM configurations using both automatic and large-scale human evaluation. Even frontier models achieve at most 22% accuracy in some communities. We publicly release all artifacts alongside an open contribution process to expand the benchmark's linguistic and cultural coverage.

---


### 175. [TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors](https://arxiv.org/abs/2610.29985)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Hui Li, Yujiong Shen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark performance is the dominant standard for comparing large language models (LLMs), typically summarized by a single aggregate score, such as accuracy, pass rate, or rubric score. This aggregate score provides limited information about a model's underlying capabilities, yet understanding these capabilities is crucial for model development and evaluation. To this end, we propose Tree-Induced Diagnostic Evaluation (TIDE), which recasts diagnostic evaluation as behavior-driven decision-tree induction to perform fine-grained capability diagnosis. TIDE recursively builds a hierarchical capability tree from benchmark samples and model scores: at each node, an LLM judge proposes candidate splits and performs sample-to-group classification, and behavior-based information gain selects among them. We apply TIDE to five models across four benchmarks to demonstrate its effectiveness, and find fine-grained capability contrasts invisible at the aggregate level: Claude Opus 4.6 achieves 100% on microeconomic market reasoning where GPT-5.4 scores 83.3%, but trails GPT-5.4 on contract law reasoning with 77.8% versus 88.9%. We hope TIDE can be extended to past and future benchmarks so that the rich behavioral signal in evaluation results is fully leveraged for understanding model capabilities.

---


### 176. [EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL Prefix Importance-Ratio Clipping](https://arxiv.org/abs/2610.29999)

**<font color=#1a73e8>作者：</font>** Chengxi Li, Hanlin Wu, Zhicheng Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) based on PPO-style clipping has become an effective approach to improving the reasoning capabilities of large language models (LLMs). However, standard token-level clipping measures policy change only through the conditional probability of the current token, while the prefix conditioning context is itself generated by the policy. This mismatch becomes especially consequential in long-response and off-policy training. We reformulate autoregressive generation as a finite-horizon Markov decision process and derive its performance-difference identity under behavior-policy sampling. The resulting change of measure identifies the cumulative likelihood ratio of the generated prefix as the exact importance weight for each stepwise policy-improvement term. Starting from the monotonic-improvement principle of trust-region policy optimization, we then construct a prefix-level trust region using the exact reverse-KL coordinate $r-1-\log r$, whose behavior-policy expectation equals the corresponding prefix-distribution KL divergence. This yields EPIC, a PPO-style sequence-clipping method that directly regulates prefix-level policy drift without relying on a local quadratic approximation or expert-routing replay. Experiments on off-policy reinforcement learning with a sparse mixture-of-experts language model show that EPIC consistently outperforms standard and sequence-level clipping baselines across mathematical-reasoning benchmarks, while remaining competitive with routing-replay-based alternatives. Code is available at this https URL.

---


### 177. [Mitigating Model Collapse through Dreaming Learning](https://arxiv.org/abs/2610.30009)

**<font color=#1a73e8>作者：</font>** Matteo Benati, Alessandro Londei, Denise Lanzieri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training generative models on synthetic data causes loss of diversity and a decrease in performance, a phenomenon known as model collapse. We study this degeneration spectrally in a controlled Markov setting. The eigenvalue spectrum of the learned transition operator offers a direct view of the process, since the subdominant eigenvalues set how fast the chain mixes and therefore how much of the state space it continues to explore. We find that sampling at temperature $T_s < 1$ acts on the operator like repeated sharpening, pushing it toward a deterministic system: the subdominant eigenvalues approach the unit circle and the spectral gap narrows. When $T_s < 1$, even data accumulation does not appear to arrest this drift. We then analyze Dreaming Learning, a regulariser that, in parallel with regular training, adds a loss term on the model's own samples drawn at a raised temperature $T_d > 1$. Because high-temperature samples flatten the predicted distribution, training on them keeps the entries of the learned operator from becoming vanishingly small, which in turn keeps the eigenvalues bounded away from the unit circle. Measurements of the spectra over 5000 generations are consistent with this picture, and the mitigation effect persists in more complex settings such as LSTM language models and a 124M-parameter GPT-2.

---


### 178. [Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014)

**<font color=#1a73e8>作者：</font>** Shota Fujikawa, Takuya Tamura, Kosuke Akimoto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent. We derive error bounds relating squared coordinate distances to trajectory KL under explicit assumptions, and across eight cross-scored models the distances track the directly measured trajectory KL in rank order. Across 100 LLMs and four environments, ALFWorld-based coordinates support performance prediction and identify behavioral similarities. In ALFWorld, these similarities persist after controlling for success rates and model size, including across model families. As an extension, harness-component displacements approximately compose, with accuracy varying across components and environments.

---


### 179. [What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](https://arxiv.org/abs/2610.30026)

**<font color=#1a73e8>作者：</font>** Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise agents act on documents. Before an agent can follow a policy, answer a compliance question or file a ticket, some ingestion layer must turn a Word file or PDF into tokens - and that layer is where an agent deployed in the wild silently loses information. We show that one layer is lost by every mainstream converter - the meaning an author encodes in how text looks - and that the loss makes agents confidently wrong rather than visibly incomplete. We build a task from 76 real policy documents: recover the requirements the author singled out, scored against the file's own OOXML properties by a deterministic matcher with no LLM judge. Formatting-blind ingestion collapses from micro F1 0.690 to 0.150 (docling) and 0.075 (plain text), a gap that replicates across six answering models from two vendors - five Claude models spanning the Opus, Sonnet and Haiku tiers, and OpenAI's GPT-5.6. An agent that cannot see the cue guesses, and docling's false-positive rate on requirements the author did not flag is four times ours. A span-level leave-one-out localises the loss to two cues - highlight (+0.302) and colour (+0.262), both Holm-adjusted p < 1e-4 - while bold, italic, monospace and strikethrough each sit within +/-0.003 of zero. The same asymmetry appears in PDF. Colour is also the cue no mainstream converter preserves and no parsing benchmark scores, and it is common: 32.8% of 6,460 documents carry a deliberate colour or highlight, 10.3% on an obligation. A pre-registered test shows that typing a cue for the agent adds +0.085 beyond merely preserving it (Holm-adjusted p = 0.049). We validate the labels against rendered page images through an independent modality (kappa = 0.72) and bound what wording alone can achieve (AUC 0.664). For agent builders the practical finding is that ingestion, not reasoning, is where this reliability is won or lost, and that the fix is cheap and measurable.

---


### 180. [Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents](https://arxiv.org/abs/2610.30041)

**<font color=#1a73e8>作者：</font>** Zijian Jiang, Xilu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text skills can extend the capabilities of tool-using agents, but long skill descriptions increase computational costs. Soft prompts provide a compact alternative, yet learning from entire successful trajectories may also introduce unnecessary behavioral changes. We find that the useful effect of a text skill is highly concentrated in a small subset of trajectory positions. Based on this observation, we propose Behavioral Localization, which compares the frozen agent with and without the text skill to identify positions where the skill both increases the likelihood of successful tokens and meaningfully changes the next token distribution. We use these localized positions to supervise a short soft prompt. Experiments on SpreadsheetBench with a frozen Qwen3.6-35B-A3B agent show that the top 10\% of trajectory positions capture 96.12\% of the total positive skill gain. In the shared prompt setting, selective supervision improves success from 30.36\% with full trajectory to 36.79\%. Under task-specific conditions, using the top 10\% localized positions achieves 57.38\%, outperforming both the full text skill and the on-policy OPCD baseline. These results show that a small set of behaviorally relevant trajectory positions can provide effective supervision of soft skills.

---


### 181. [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042)

**<font color=#1a73e8>作者：</font>** Sudipta Paul, Pengrui Quan, Aounon Kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls that jointly satisfies interacting constraints, break this alignment. There, open-ended self-modification repeatedly explores ineffective changes and consumes substantial evaluation budgets. We introduce HGM-Dual, a diagnostic-guided framework for budget-efficient harness evolution for planning agents. First, HGM-Dual represents agent evolution as lineage-aware context. This context records what each ancestor changed, which behaviors improved or regressed, and which modifications were ineffective, giving the editor explicit edit-outcome attribution instead of an unstructured archive of past agents. Second, HGM-Dual introduces error-conditioned dual-path child generation. For each selected parent, it generates a general child that preserves open-ended exploration and specialized children that target the harness components most likely responsible for the parent's highest-ranked constraint violations. HGM-Dual outperforms the strongest baseline by up to 14.45% relative improvement in case accuracy while matching HGM variants' final performance with 2x-4x fewer evaluation budget.

---


### 182. [Looped Uniform Diffusion Language Models](https://arxiv.org/abs/2610.30066)

**<font color=#1a73e8>作者：</font>** Saiteja Utpala, Chieh-Hsin Lai, Yuki Mitsufuji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uniform diffusion language models (UDLMs) generate text by iteratively denoising sequences of ordinary vocabulary tokens, any of which may be corrupted and subsequently revised. During training, UDLMs must denoise from a context that may itself be unreliable, whereas masked diffusion language models (MDLMs) always condition on a clean context. This challenging training objective makes UDLMs more FLOP-intensive to train than MDLMs, but it yields stronger downstream reasoning performance. Recently, selective looping, which recursively applies a few early Transformer layers within each denoising step, has been shown to improve training efficiency in MDLMs under an iso-FLOP budget. We investigate looping in UDLMs while keeping the training objective and sampler unchanged. We find that looping significantly improves training efficiency: looped UDLMs reach the validation NLL of a non-looped UDLM trained on about 0.5 trillion tokens with up to 2.8x fewer training FLOPs on OpenWebText and 3.3x fewer on FineWeb-Edu. We also find that, at a matched NFE budget, looped UDLMs reach up to 9.8% lower generation perplexity than the non-looped UDLM, with most gains achieved at moderate loop counts. Finally, we study different loop-count distributions and find that sampling smaller loop counts more frequently during training improves inference efficiency: on downstream tasks, this strategy uses 12% fewer loops than uniform loop-count sampling without degrading accuracy.

---


### 183. [GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation](https://arxiv.org/abs/2610.30067)

**<font color=#1a73e8>作者：</font>** Quang Anh Kiet Tran, Nam Anh Tran, Manh Hung Trinh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vietnamese pre-trained encoders have improved rapidly, but the strongest ones are large, multilingual-vocabulary models or depend on external word segmentation, which makes them costly to deploy. We present GoiBERT, a family of two compact Vietnamese encoders with 26M and 49M parameters that operate directly on raw text. GoiBERT learns from two complementary teachers. A same-tokenizer Vietnamese encoder first teaches general-purpose representations. A much larger teacher then provides task-level guidance through soft labels that are generated without ever labeling its own training data. Across eight benchmarks covering text classification, aspect-based sentiment analysis, natural language inference, and named entity recognition, GoiBERT-large achieves the highest average score among non-teacher models. It does so with fewer than half the parameters of the strongest compact baseline and twice its throughput. GoiBERT-base retains 99% of that baseline's performance at a quarter of its size. Our analysis shows that compression is nearly lossless for sentiment and classification tasks but remains costly for inference and entity recognition, which points to clear directions for future work. Our code and models are available at: this https URL

---


### 184. [Loopholing All the Way: Language Modeling with pure Self-Conditioning](https://arxiv.org/abs/2610.30068)

**<font color=#1a73e8>作者：</font>** Adrien Deschenaux, Nadezhda Ilieva, Justin Deschenaux 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Diffusion Language Models (DLMs) use Self-Conditioning (SC), or Loopholing, to improve their performance. While SC is traditionally seen as an auxiliary heuristic, its empirical success raises the question: can a continuous generative model be based purely on Self-Conditioning? We answer affirmatively with LAW (``Loopholing All the Way''), which propagates the Expected Embedding under the denoiser's prediction across steps, decoding the tokens once, at the end. On Sudoku, LAW outperforms previous Discrete and Continuous Diffusion Models, including Loopholing Discrete Diffusion. On Maze, LAW is the most accurate from 2 to 64 NFE. After training on TinyGSM and sampling at temperature 1 with 1024 NFE, LAW solves 42.2% of GSM8K problems against 34.5% for uniform Loopholing Discrete Diffusion. Additionally, fine-tuning a pre-trained Uniform Diffusion Model (Duo) with LAW increases its accuracy from 17.2% to 48.1%. Finally, on OpenWebText, LAW pushes the Pareto frontier and approaches Autoregressive Models (ARMs) with 64 NFE. Find our code at this https URL.

---


### 185. [Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis](https://arxiv.org/abs/2610.30072)

**<font color=#1a73e8>作者：</font>** Xinzhe Wang, Xudong Weng, Zang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data agents built on ReAct-style loops now execute complex analytical workflows over structured data, yet their intermediate reasoning still runs almost entirely through text. Human analysts instead move between numbers, tables, and charts, reading visual evidence to expose trends and anomalies that text summaries drop. We ask whether charts can serve as internal epistemic actions inside a data agent's reasoning loop, and how to teach an agent to use them. We first build \probe{}, a suite of 200 controlled tasks under four matched interface conditions, and find a persistent gap between what agents can read and what they choose to use. Agents score as well from self-generated charts as from numeric output, yet plotting access alone does not translate into consistent use. Task slices show that charts lead on temporal, pattern, and anomaly reasoning, while text leads on precise reading and conditional verification. We then propose \method{}, which distils two families of experience from conditioned trajectory rollouts. One family records how to select and verify analytical operations, and the other records when to invoke text, charts, or both. A trajectory judge scores outcomes and labels intermediate steps, and a validation gate admits only experience that improves held-out performance. On three held-out benchmarks with four LLM backbones, \method{} raises analytical accuracy and visual evidence quality over matched baselines, and backbones that never drew charts begin using them, all without touching model parameters.

---


### 186. [Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076)

**<font color=#1a73e8>作者：</font>** Hadi Khalaf, Sajani Vithana, Kunal Talreja 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models make it easy to build classifiers by simply prompting a model with the sample to classify. However, their predictions are neither deterministic nor uniformly reliable across samples. How can we combine predictions from different models to improve reliability? We view LLM classifiers as noisy measurement instruments of an underlying target label. Our goal is to maximize average classification accuracy at a given average query cost. To this end, we introduce circuits that organize LLM classifiers into an adaptive sequence of queries and decisions. We then characterize the optimal circuit, obtain the fundamental limits of achievable accuracy, and provide practical insights on realizing the optimal circuit. Across seven classification tasks spanning safety, health, political science, human preference, agent evaluation, decision-making and reasoning, our method improves the cost-accuracy frontier over routing and cascading baselines.

---


### 187. [Differentially Private Sparse Reward Estimation with Preference Feedback](https://arxiv.org/abs/2610.30099)

**<font color=#1a73e8>作者：</font>** Meng Ding, Mingxi Lei, Jie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Human Feedback (RLHF) has become a central paradigm for aligning Large Language Models with human values. However, the reliance on sensitive preference data necessitates rigorous differential privacy (DP) guarantees to prevent user information leakage. Existing private alignment methods typically assume dense reward parameterizations, resulting in estimation error bounds that scale polynomially with the ambient {model size $d$}. Such dependence is prohibitive in modern {overparameterized models} where $d$ is vast. In this work, we study \emph{Private Sparse RLHF} problem to address this limitation, assuming that human preferences (reward model) are governed by a subset of $s^* \ll d$ relevant features. We provide the first comprehensive theoretical framework for differentially private sparse reward estimation from pairwise preference feedback under the Bradley-Terry-Luce model, and introduce efficient algorithms for both Sample-DP and Label-DP settings. Theoretically, under the squared $\ell_2$ parameter estimation error, we establish upper bounds of $\widetilde{O}(s^*/n + {s^*}^2/n^2\varepsilon^2)$ for $(\varepsilon,\delta)$-Sample-DP and $\widetilde{O}(s^*/n + s^*/n\varepsilon^2)$ for $\varepsilon$-Label-DP based on randomized response, where $n$ is the training data size. For the lower bounds, we show that the Sample-DP rate is nearly optimal, and that the guarantee for our Label-DP method cannot be further improved within the randomized-response framework. We also provide a general lower bound for the problem with Label-DP. Empirically, our framework demonstrates superior efficacy over dense baselines across sentiment generation and safety alignment benchmarks, offering a significantly more favorable privacy-utility trade-off.

---


### 188. [Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103)

**<font color=#1a73e8>作者：</font>** Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the same surface. To remove the textbook cues that enable recall, we build it with AgentGAN, an adversarial multi-agent framework in which a generator rewrites each statement until a panel of frozen code models fails, while an executable validity gate keeps every rewrite answer- and class-preserving. The result is 2,114 hardened statements with hand-verified reference human solvers. Evaluating 12 proprietary and open-source models, we find that every model scores lower on NPC statements than on their P twins (35.4% vs. 63.8% pass@1), and that 95.1% of model-family pairs fail more often on the NPC side. A tenfold time limit raises NPC accuracy only from 28.5% to 31.9%, so failures stem from wrong or crashing programs rather than slow ones. Hardening also narrows the class gap from 24.8 to 14.6 points, showing that part of the apparent gap reflects familiarity with textbook phrasing rather than complexity class.

---


### 189. [Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113)

**<font color=#1a73e8>作者：</font>** Houde Qian, Zheng Jiang, Wenyi Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a benchmark and public leaderboard for end-to-end quantitative research on real A-share market data. A model constructs features and stock-scoring code, receives feedback only on 2022--2023, and freezes one strategy for assessment on the sealed year 2024. A cash-account evaluator applies trading constraints and costs, including market impact estimated from a simulated order book. Scores are dominated by realized excess return and complemented by signal quality and the diversity of features used by the strategy. We evaluate nine frontier models, among which GPT-6 Astra scores highest; yet no model beats the equal-weight market in 2024. Quant-Arena is open to submissions from any model or agent harness.

---


### 190. [Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116)

**<font color=#1a73e8>作者：</font>** Shibo Jin, Zhiqiu Xu, Yiling Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce Environment Duels, a dynamic agentic benchmark that evaluates both capabilities on interactive environments. Each model writes environments, each with a privileged hint, aiming for tasks that capable solvers fail without the hint and pass with it. Across nine frontier LLMs, solving and authoring prove to be distinct skills: the strongest solvers are not the strongest authors, while smaller models learn more from how others played and write the hardest environments and the most useful hints. Beyond the scores, the pairwise interactions form a microcosm of how models affect one another. Head-to-head outcomes are transitive and so yield a stable ranking; independent authors converge on the same designs; and in a reinforcement-learning study with Qwen3.8-27B, the learner's hint lift on an author's environments tracks how much training on those environments improves it on held-out reasoning and agentic benchmarks, whether the environments are its own or another model's. Each of these patterns has a counterpart in how models shape one another outside the duel. By staging these interactions under controlled conditions, Environment Duels offers a window onto how LLMs teach, challenge and learn from one another. Code is available at this https URL.

---


### 191. [VoxProg: 3D Spatial Reasoning through Voxel Programming](https://arxiv.org/abs/2610.30127)

**<font color=#1a73e8>作者：</font>** Zhichao Zhai, Menglei Zhao, Guikun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language models' abilities to interpret tasks and generate programs offer a promising basis for 3D spatial reasoning. Yet following spatial instructions in 3D scenes requires programs to construct geometric references that language leaves implicit. In this work, we introduce VoxProg, which formulates 3D object placement through voxel programming: a language model translates task interpretations into executable programs over local voxel views of scene surfaces. Because these views index surface geometry on regular grids with explicit coordinates and neighborhood relations, an evidence program can isolate task-relevant regions and boundaries directly from scene meshes, and a downstream pose program can measure the resulting geometry to compute a target $SE(3)$ pose. Visual and numerical feedback from execution lets the model inspect intermediate selections and candidate placements to iteratively revise its code. To evaluate open-ended placement across functional use, geometric fit, and contextual arrangements, we introduce the 71-task VoxProg-Bench benchmark along with an evaluation suite pairing perceptual Intent Alignment and 3D Physical Validity. Across VoxProg-Bench and external benchmarks, VoxProg consistently outperforms relation-based, keypoint-based, and mesh-based baselines.

---


### 192. [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132)

**<font color=#1a73e8>作者：</font>** Zhennan Wan, Jianfei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL, and existing synthesis methods depend on external corpora or stronger teacher models, which become harder to obtain as the trained models get stronger. Recently, RL from zero data, in which a model learns from tasks it proposes itself, has achieved excellent performance, but existing methods target short-context tasks. Therefore, we propose $\textbf{LongZero}$, a method that lets an LLM improve its own long-context reasoning without any external data. Instead of writing questions and answers over existing documents, LongZero first has the model synthesize the question and answer with its supporting evidence in a compact structured form, and only then separately expands the evidence into a long multi-document context. LongZero combines these self-written multi-hop reasoning tasks with self-written multi-round retrieval tasks and trains the model with GRPO. We evaluate LongZero on two LLMs across five long-context reasoning benchmarks and compare it with RL on data synthesized from external corpora. Experimental results show that LongZero can generalize to real tasks, and outperforms both baselines, suggesting a viable and promising path to improving long-context reasoning of LLMs.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 193. [Speedrunning Relational Foundation Model Pretraining](https://arxiv.org/abs/2610.28855)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gabriel Wedson Mendonça de Souza Veloso, Luan Borges Teodoro Reis Sena, Denis Oliveira Correa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress on foundation model pretraining is gated by who can afford a trial, and relational pretraining is no exception. Recipes are developed inside individual labs, reported under private protocols, and do not accumulate. Speedrun leaderboards remove that barrier by decentralizing the search rather than the training run. The problem is fixed, the stack is open, entries are ranked by wall-clock time to a quality target, and one GPU is enough to hold the record. We introduce modded-nanoRT, the first such leaderboard for Relational Transformers. Which database to hold out decides whether the benchmark can resolve improvements at all, so we fix it by calibration, ranking six candidates by how sharply a 45-minute learning curve separates improvement from seed noise. We open the leaderboard with typed trilinear attention, a relational operator that conditions attention scores and values on the foreign key traversed, together with Muon and SIGReg. The recipe reaches the target in 305.63 seconds on one NVIDIA H200, 8.11x faster than the reference implementation, and wins 13 of 15 pairs outside the development database. We will release the benchmark, its frozen artifacts, and the record runs. Our code is available at this https URL.

---


### 194. [RL-IF: Tracking Non-local Training Data Influence for Online Reinforcement Learning](https://arxiv.org/abs/2610.28883)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shixuan Liu, Cheng Tang, Yuzheng Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) has achieved significant success in decision-making tasks, but modern online RL remains highly sensitive to the quality of training experience. Understanding the contribution of individual training instances is therefore central to data-centric RL, with applications ranging from experience selection to policy interpretation. Existing data attribution methods for online RL primarily focus on local influence within a single training round, overlooking the non-local data influence across multiple training rounds. In this work, we formalize data attribution in online RL through a trajectory-level leave-one-out quantity, RL-LOO, which measures how one training sample influences a downstream target after subsequent online updates have taken place. We then derive RL-IF, a first-order estimator that propagates data influence through both optimization effects and policy-induced sampling effects, and provide theoretical guarantees on its approximation accuracy under smoothness assumptions. Our analysis further disentangles these two effects and shows both theoretically and empirically that the full RL-IF estimator can often be well approximated using the optimization effect alone. Building on this observation, we develop RINSE, a practical data filtering method for online RL. Experiments on standard control benchmarks and an RLHF-style toxicity-mitigation setting show that RINSE improves training efficiency and final performance over standard PPO and local attribution baselines. These results suggest that RL-IF provides a practical and principled framework for understanding and improving online RL.

---


### 195. [From Weather to Enhanced Weathering: Weather Foundation Models for Carbon Dioxide Removal at Operational Scale](https://arxiv.org/abs/2610.28973)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sasankh Munukutla, Felipe Oviedo, Danrong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enhanced Rock Weathering (ERW) is a carbon removal solution with the potential to remove gigatons of CO$_2$ per year, but quantifying that removal today requires dense soil sampling and laboratory analysis. We evaluate five weather Foundation Models (FMs) as frozen encoders feeding lightweight decoders, under a leave-one-field-out protocol on 5,192 chronosequences from 264 fields across Brazil and the US. To our knowledge, this is the first holistic evaluation of weather FMs for ERW and the largest evaluation on operational ERW data. We find that across weather FMs, representations transfer to ERW: our best model, TerraNova-ERW, built on Aurora 1.5, positively orders measurements within fields it has never seen. Zero-shot prediction of a new field's mean removal is not yet feasible, and we attribute this to data scale: the same architecture excels on $\sim$$10^5$ natural-weathering sequences, anchoring the scale we expect ERW data must reach. Few-shot prediction, blending the model with a few samples per field, is supported today: TerraNova-ERW recovers over 60% of the highest-removal fields with two samples per field, roughly halves the samples needed to estimate a field's mean removal, and can cut sampling on our densest fields by 28-98%.

---


### 196. [Doob-Based Generative Policy Optimization](https://arxiv.org/abs/2610.28990)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maojiang Su, Qijie Zhu, Yu Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models provide expressive policy classes for robotic and sequential decision-making systems. However, their action likelihoods are generally intractable, limiting the direct use of widely adopted policy optimization methods such as PPO and GRPO. We propose Doob Policy Optimization (DoobPO), a framework that leverages Doob's $h$-transform for likelihood-free reinforcement learning fine-tuning of generative policies. DoobPO separates policy improvement from generative policy learning. It first learns a lightweight ratio model that represents the desired policy update, and then distills the resulting ratio-tilted target policy into the generative policy via conditional drift matching. This formulation applies uniformly to both diffusion and flow policies and supports a broad family of policy improvement rules, including PPO and GRPO. We prove that the practical conditional drift matching objective is gradient-equivalent to the ideal Doob drift matching objective. We further show that the induced diffusion process solves an endpoint-constrained stochastic optimal control problem. This establishes that it achieves the minimum-energy modification required to realize the desired policy tilt. Across MuJoCo continuous-control benchmarks, DoobPO achieves strong performance against competitive diffusion- and flow-policy baselines, showing a principled and practical route to RL fine-tuning for generative policies.

---


### 197. [YingLan: A Multimodal Ocean Foundation Model for Unified Representation Learning from Heterogeneous Observations](https://arxiv.org/abs/2610.29313)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sen Jia, Siqi Wei, Junyu Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal ocean modeling remains challenging due to substantial heterogeneity in data structures, physical semantics, and spatiotemporal characteristics across satellite imagery, gridded oceanographic fields, and buoy observations. Existing approaches largely focus on task-specific ocean modeling, while learning transferable representations from heterogeneous observations remains an open problem. To address this challenge, we propose YingLan, a multimodal ocean foundation model that integrates physics-attribute-conditioned dynamic encoding, Spatiotemporal Increment Coupling (STIC), and ocean-state evolution-aware pretraining. Specifically, the dynamic encoding mechanism generates adaptive input projections conditioned on physical semantics and observation characteristics, enabling flexible representation of heterogeneous ocean variables. STIC models multiscale spatiotemporal dependencies through cross-scale interactions of latent temporal increments. The pretraining strategy further combines masked observation reconstruction with temporal evolution objectives to facilitate the learning of coherent ocean-state representations across different prediction horizons. YingLan is implemented using MindSpore and trained on Huawei Ascend 910B NPUs, demonstrating its compatibility with domestic AI computing infrastructure. In a seven-day sea surface salinity (SSS) forecasting task conducted in the Shenzhen coastal waters, YingLan achieves an average RMSE of 0.687508 PSU, corresponding to relative error reductions of 0.58%, 5.31%, and 12.42% compared with LangYa, XiHe, and GloNet2, respectively. These results provide initial evidence of the model's effectiveness in regional ocean forecasting, while broader cross-task and cross-regional evaluations remain necessary to assess its generalization capabilities.

---


### 198. [BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes](https://arxiv.org/abs/2610.29320)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent electroencephalography (EEG) foundation models increasingly emphasize model scale, potentially limiting their deployment on resource-constrained devices and in everyday environments. We argue that transferable EEG features can instead be learned with a compact architecture and introduce BrainCodes, a lightweight foundation model pretrained through self-supervised learning on more than 800 hours of recordings from over 1,000 participants. Our architecture combines a quantization-based neural tokenizer with a spatiotemporal encoder that supports arbitrary electrode configurations. The pretraining objective explicitly encourages representations that capture spatial connectivity through channel positional encoding, and sensitivity to narrowband neural oscillations through an auxiliary training objective. Our model matches or surpasses the state of the art across diverse neurophysiological monitoring tasks, including sleep staging, attention assessment, and cognitive load estimation. BrainCodes transfers effectively to low-resource wearable devices while using up to 97% fewer trainable parameters than comparable architectures. Beyond predictive accuracy, our evaluation framework characterizes the geometry and invariances of learned EEG representations across measurable spatial, temporal, and spectral signal properties.

---


### 199. [Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dongfang Li, Zhuoen Chen, Bonian Jia 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual learning remains an open question. In this paper, we introduce Memory-Centric Continual Learning (MCCL), arguing that memory should be judged by whether it improves future actions, not merely what it retrieves. MCCL has three main parts. First, a three-axis taxonomy organizes memory by where state is stored (substrates), what form it takes (assets), and how it is managed (policies). This defines a two-loop lifecycle that updates memory state in an inner loop while refining management policies in an outer loop based on task feedback. Second, an evaluation protocol measures retention under interference, adaptation to change, and task transfer to isolate genuine behavioral gains from simple context expansion. Third, a memory scaling framework models how agent performance scales with experience, storage capacity, and compute budgets across non-parametric and parametric memory. Together, these components reframe agent memory from passive lookup to continuous learning, offering a principled route toward self-improving autonomous agents.

---


### 200. [How Far Can Foundation Models Be Distilled for Efficient Jet Tagging?](https://arxiv.org/abs/2610.29439)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jay Agarwal, Siddharth Khare, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Jet tagging is one of the most important applications of machine learning at the Large Hadron Collider. Recent models build in more physics knowledge or rely on large-scale pretraining, but the experiments place strict limits on their inference cost. Knowledge distillation can transfer their performance to small students that are cheap to run. We ask which properties of a teacher help the student, how small a student can get and how close it can come to the state of the art. On a jet tagging benchmark, we distil six teachers that differ in architecture, symmetry and pretraining, including two foundation models, into five small students. Every teacher improves every student, and the gain depends mainly on the strength of the teacher. We then shrink our two strongest distilled students, Transformer and L-GATr-slim, in width and in depth. With 20 thousand parameters, a distilled L-GATr-slim outperforms every published jet tagger trained from scratch at a fraction of the inference cost of every teacher. Even with two thousand parameters, it matches ParT, a model with a thousand times as many parameters. We also study what the students learn from their teachers. Our benchmark of inference cost shows that students of the same size can differ by almost an order of magnitude in speed. We release the code and the weights of all trained models.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
