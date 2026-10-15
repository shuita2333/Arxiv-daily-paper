# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

---

### 51. [PREFER: From Player Experience to Personalized Game Refinement](https://arxiv.org/abs/2610.19213)

**<font color=#1a73e8>作者：</font>** Qi Chai, Zhang Zheng, Lu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how large language models (LLMs) evaluate gameplay experience is important for using their feedback to guide game design. However, overall ratings alone provide limited insight into which aspects of experience are associated with these judgments and how they can inform concrete game changes. We introduce PREFER, a framework that uses a shared set of experience dimensions adapted from established psychometric questionnaires to benchmark how models evaluate gameplay and to guide persona-specific game refinement. Through these dimensions, we characterize the perspectives models offer as virtual playtesters by examining how their overall assessments relate to specific aspects of experience and to the gameplay they produce. To examine how the same dimensions can guide refinement for players with different preferences, we use personas to simulate distinct player profiles. For each persona, PREFER uses experience-preference relationships to select refinement objectives, revises game rules and their implementations, and playtests candidate games to assess experience changes and predicted preference gains. Experiments with five personas show that PREFER achieves 9.2% higher mean post-play preference ratings than the strongest evaluated baseline.

---


### 52. [Narrowing the Collaboration Gap, Probably](https://arxiv.org/abs/2610.19215)

**<font color=#1a73e8>作者：</font>** Mirah Shi, Marcel Hussing, Ira Globus-Harris 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as teams of agents that hold different private information about a shared task. How should such agents concisely communicate in a way that promotes aggregation of decision-relevant information? Communicating only proposed actions can discard decision-relevant uncertainty: two agents may prefer the same action for different reasons. We study an alternative interface in which agents communicate calibrated beliefs over actions. We first analyze a simple synthetic setting that captures the structure of multi-round reasoning under partial information. In this setting, we show theoretically and empirically that communicating unbiased probabilities can be strictly more powerful than communicating actions. We then test the same principle in a collaborative maze-solving task with trained transformers and pretrained LLM agents. Our results demonstrate that probability communication outperforms action communication when the exchanged predictions preserve calibrated uncertainty. When communicated probabilities are biased, we show that the benefits of probability communication can disappear. We give a post-hoc conversational calibration intervention that consistently improves decision-making by correcting these biases both in a toy transformer setting and when pretrained LLMs use the corrections in context. These results suggest that probabilistic communication is useful for multi-agent collaboration not merely because it transmits more information, but because calibrated uncertainty gives other agents a reliable object to update on.

---


### 53. [REPORT-OPS: Hybrid Evidence-Guided Reporting with Human-Supervised Refinement for HPC](https://arxiv.org/abs/2610.19222)

**<font color=#1a73e8>作者：</font>** Mah Kadidia Konate, Mayur Akewar, Janki Bhimani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational reporting for high-performance computing (HPC) facilities requires combining information from monitoring services, schedulers, incident and maintenance records, storage measurements, periodic reports, and operator investigations. Producing a reliable report requires more than retrieving relevant records: the evidence must refer to the correct system, metric definition, time period, and source of authority. We present REPORT-OPS, a hybrid reporting agent in which an LLM interprets requests, plans evidence collection, evaluates possible explanations, and drafts reports, while author-seeded operational policies and automated checks determine whether the available evidence supports the requested conclusion. Depending on the evidence state, the system answers the request, reports a qualified conclusion, or withholds an unsupported claim. During offline refinement, an LLM critic proposes bounded policy changes that a human approves or rejects without editing; accepted candidates are promoted only after automated target, held-out, and regression testing. We evaluate REPORT-OPS on 68 sanitized reporting queries constructed from 50 base scenarios in a frozen HPC operational corpus, using three agent models and two LLM judges. REPORT-OPS achieves 68.63% Pass@80, compared with 7.02% for the strongest retrieval baseline. Evidence gating increases claim-support precision from 40.58% to 90.06%. On the 13-query explanatory subset, explanation accuracy reaches 55.54%. Across five rounds of human-supervised refinement, localized policy updates correct 91.17% of targeted failures and improve performance on related held-out cases by 9.33 percentage points, with no observed regression breaks under release gating. These results demonstrate improved evidence-grounded reporting and within-environment policy reuse; they do not establish unrestricted causal discovery or cross-facility generalization.

---


### 54. [Definition Grounding in Theory-Level Auto-formalization](https://arxiv.org/abs/2610.19223)

**<font color=#1a73e8>作者：</font>** Leyan Pan, Christian Szegedy, Frederick Rajasekaran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based auto-formalization systems can now generate formally verified Lean code at unprecedented rates. However, a formalization advances mathematical research only when further mathematical results can be built on it, especially when its definitions and helper lemmas are general enough to be imported and used idiomatically. We propose definition grounding, where definition formalizations are continuously judged and revised, as a method to ensure formalization quality. We find that agents formalizing definitions from textbook text often produce definitions that later statements cannot use, and only 25%-50% of their definition sets are compatible with all later statements. However, clarifying the informal definitions can improve this rate up to 77.5% averaged over all models. Furthermore, stating a small set of basic properties without proving them can improve model judges' capability to detect definitions with compatibility issues, at only about 11% of the definition formalization cost. These results are verified with ReuseBench, a benchmark we curated for formalizing new mathematical fields and theories.

---


### 55. [Do Syntax Heads Influence Model Behavior?](https://arxiv.org/abs/2610.19231)

**<font color=#1a73e8>作者：</font>** William Timkey, Tal Linzen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models develop attention heads that specialize in syntactic relations, for example, attending from verbs to their subjects. Do these heads play a causal role in the model's syntactic predictions? Evidence for such a role is mixed to negative: even when we force these heads to attend to a distractor noun other than the subject, the model's syntactic predictions are still more consistent with the subject than with the distractor. Interventions on specialized syntax heads had a significantly stronger effect on syntactic predictions than interventions on random heads, but only in one of the two measures we propose.

---


### 56. [Spectral-MoE: Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion](https://arxiv.org/abs/2610.19232)

**<font color=#1a73e8>作者：</font>** Zachary Broveak, Christian Kubicka, Thierry Tambe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models impose substantial memory demands and arithmetic costs during inference. Dense-to-mixture-of-experts (MoE) conversion is a model optimization technique that aims to reduce these arithmetic costs. Dense-to-MoE conversion partitions pretrained feed-forward network (FFN) neurons into experts and selects a subset for each token. Leading methods fall into two categories: analytic methods produce a converted model quickly using heuristics, while learning methods produce a model much more slowly by optimizing via gradients. Both approaches, however, fix the same active expert count, or "utilization," at every layer. We introduce Spectral-MoE, which learns to allocate a utilization budget heterogeneously across layers. Its name draws a metaphor between separating a dense FFN into experts and separating a light beam into its spectrum. Spectral-MoE consists of two distinct approaches: a static approach that uses a single per-layer scalar which is shared across tokens, and a dynamic approach which emits a per-token schedule. We demonstrate that both allocators improve performance over uniform on both the analytic-based and learning-based SOTA dense-to-MoE methods. At 25% FFN utilization, dynamic allocation reduces WikiText-2 perplexity relative to uniform by 1.04, 2.96, and 2.71 points on the learned base for Llama-2-7B, Llama-3-8B, and Qwen2.5-7B, respectively. The corresponding reductions on the analytic base are 2.45, 6.26, and 2.17 points. On the learned base, dynamic allocation improves six-task mean accuracy over uniform by an average of 1.5, 4.2, and 3.6 percentage points across the three models at FFN utilizations of 12.5%, 25%, and 50%, respectively. These results establish per-layer expert utilization as a novel optimization axis in dense-to-MoE conversion.

---


### 57. [Write Once, Plan Many: Building Reusable Visual Planning Systems from One Scene](https://arxiv.org/abs/2610.19234)

**<font color=#1a73e8>作者：</font>** Ruixiao Yang, Yilun Hao, Mingxin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can reason about visual planning tasks, but querying them for every instance incurs repeated inference cost and latency. Generating reusable planning programs offers an alternative, but constructing reliable planning systems for new problem domains without extensive supervision remains challenging. We present a training-free framework that constructs reusable perception and planning programs from a domain specification and a single practice scene without a paired solution. The central challenge is obtaining useful feedback from the limited input. Our framework addresses it by leveraging VLM's ability to provide a renderer and a dynamic model based on its scene understanding. Rendering detected states enables comparison with the practice scene, while checking simulated action outcomes against the domain specification helps expose errors in rule implementation. Together, these checks guide refinement of the grounding program and planner without requiring solution labels. After refinement and component selection, the programs are frozen and solve new instances without further VLM calls. The same framework constructs systems across domains without manual pipeline redesign. Across fifteen domain variants spanning 2D and 3D scenes with discrete and continuous state, our systems achieve 99.3% average planning success, compared with 80.9% for the strongest domain-level program-generation baseline and 90.7% for the strongest instance-level baseline. Cost analyses show a favorable success-cost trade-off, and ablations confirm the contributions of the executable domain model, execution feedback, and component selection.

---


### 58. [LLMs program using Reusable and Composable Abstract Representations](https://arxiv.org/abs/2610.19238)

**<font color=#1a73e8>作者：</font>** Casper L. Christensen, Kyle J. Ray, Dmitry Manning-Coe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When writing code, the same computation can be expressed in different programming languages and through different implementation strategies. We show that the activations of LLMs capture this shared structure in reusable and composable abstract representations when they generate code. These representations emerge in the middle layers, are reusable across programming languages, and afford the model an impressive amount of generalization ability when generating code under various interventions. Using activation steering, we show that function, programming language, and implementation strategy can be independently manipulated. The independent interventions on language and function can be flexibly composed to control code generation, even in cases when the prompt contains no information about language and function. We additionally find that finetuning on examples of arbitrarily defined functions in one programming language transfers to other languages, consistent with the models reusing abstract features of code generation that are shared across different examples. Finally, to study how such abstract representations come to be, we implement a minimal model of shared, reusable, and composable structure in a synthetic setting, and show that transformers trained on such data learn representations that reuse these parts flexibly across contexts.

---


### 59. [FinGREAT: Evaluating LLMs on Financial Graph-guided Retrieval And Typing](https://arxiv.org/abs/2610.19240)

**<font color=#1a73e8>作者：</font>** Ashman Mehra, Bryan Routledge, Jane JaeYeon Pyo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial disclosures express the underlying relationships of double-entry accounting through unstructured text. While financial LLM benchmarks predominantly emphasize question answering and classification, schema-guided evidence discovery remains relatively under-explored. We investigate whether open-weight LLMs can extract and classify evidence corresponding to predefined double-entry accounting relationships underlying the text. Using a financial accounting graph comprising 11 nodes (accounts) and 11 edges (transaction types), we evaluate mid-sized models from 5 open-weight families across 1,300 SEC 10-K Item 7 filings spanning 26 years, comparing their extraction performance against three proprietary models. Results reveal substantial differences in extraction volume, edge distributions, and cross-model agreement. Building on this study, we introduce a human-annotated relation classification benchmark comprising 483 passages across three financial accounting categories, evaluating 34 open-weight and 10 proprietary models. The strongest open-weight and proprietary models achieve 84.1\% and 92.8\% accuracy, respectively, with considerable variation across accounting categories. Our findings highlight the importance of evaluating evidence discovery and relation understanding separately, while investigating locally deployable models for scalable, privacy-sensitive financial analysis.

---


### 60. [Copy-Paste Language Models](https://arxiv.org/abs/2610.19247)

**<font color=#1a73e8>作者：</font>** Nathan Godey, Yoav Artzi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers are intuitively considered to be efficient at copying from their inputs. We actually show that the ability of LLMs to copy in context can be improved through explicit modeling. We propose Copy-Paste Language Models (CPLMs), which add a lightweight Copy-Paste head to the conventional language modeling (LM) head. CPLMs improve training efficiency, downstream performance, and offer new operating points in long-context and retrieval setups. We validate our approach by pretraining models from 135M to 1.7B parameters, showing improvements across all scales and backbones with negligible training and inference overheads. We explain the success of CPLMs by showing that they partially mitigate the LM head gradient bottleneck through an alternative gradient path.

---


### 61. [Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills](https://arxiv.org/abs/2610.19264)

**<font color=#1a73e8>作者：</font>** Ratnesh Pandey, Japneet Singh, Harsh Akshit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are Markdown documents that a tool-using agent reads as instructions and then acts on with the privileges of the session that loaded them. Installing one grants authority (the standing to direct the agent, not new privilege), and the size of that grant is what we measure. We present a two-phase attack-surface profiling methodology that combines whole-bundle static analysis and dependency provenance checking with instrumented sandbox execution and separate model-based assessment of the resulting traces. We apply the methodology to 6,309 listings from two marketplaces, selecting listings for execution without conditioning that decision on a prior threat or risk signal. Half the corpus carries evidence of shell-execution capability; the corresponding shares are 35% for filesystem read, 31% each for filesystem write and network egress, and 13% for credential access; seven listings in ten carry at least one elevated capability. That is the surface a user accepts at install time, and almost none of it is visible then. A permission model exists but is close to inert. Authors may list the tools a skill pre-approves in its own frontmatter, which removes confirmation prompts rather than restricting what the skill can reach; of the 6,061 listings whose frontmatter parses, 770 declare anything at all, the vocabulary cannot express credential or environment access, and nothing checks what it does express against the bundle. Declaring is also not declaring accurately: 59% of declaring listings understate what their bundle can do. ClawHub declares roughly twice as often as skillsmp, yet under-declares on 88% of its declarations against 31%. Triage at the marketplace boundary therefore cannot rest on what a listing declares. It must rest on what the bundle can do. These results position capability-oriented attack-surface profiling as a necessary complement to maliciousness detection.

---


### 62. [LAMP: 3D Source-Aware Lighting Estimation at Multiple Points](https://arxiv.org/abs/2610.19266)

**<font color=#1a73e8>作者：</font>** Yanqiao Wang, Jin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing illumination estimation methods primarily recover lighting distributions for rendering, but typically leave the contributions of individual physical light sources at specific scene locations implicit. We address this gap by leveraging the scene understanding capabilities of vision-language models (VLMs) to connect local illumination with its physical sources. We introduce LAMP, a framework for point-conditioned, source-aware illumination reasoning from a single RGB image with marked query points. LAMP constructs a shared inventory of active light sources, ranks contributing sources for each query, and predicts their 3D query-to-source directions. We supervise these relationships using procedurally controlled indoor scenes, reusing independently rendered source responses to derive contribution targets across lighting configurations and obtaining exact directions from source and query positions. On the Infinigen test set, fine-tuning Qwen3-VL-8B increases dominant-source 3D PCK@0.5m from 0% to 70.6%, with 94.5% of directions within 12.5 degrees of ground truth among correctly localized sources. Combined with a lightweight network predicting dense RGB irradiance, LAMP achieves probe-rendering quality comparable to prior lighting-estimation methods while additionally localizing individual physical sources in 3D and explicitly attributing local illumination to them.

---


### 63. [MemeTrace: A Multimodal LLM-Based Agent for Safety-Aware Meme Provenance Analysis](https://arxiv.org/abs/2610.19267)

**<font color=#1a73e8>作者：</font>** Bo Shao, Yihan Ma, Yiting Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online memes are often carriers of unsafe content such as disinformation and propaganda. Their rapid evolution in response to news events and strong dependence on contextual information make it difficult for platforms and moderators to detect and moderate them effectively. Moreover, existing moderation studies typically classify memes as safe or unsafe based on individual images, lacking the ability to perform broader provenance analysis, i.e., where a meme originates, how it spreads, what cultural symbolism it represents, whether it poses potential risks to society, etc. To bridge this gap, we introduce MemeTrace, a multimodal LLM-based agent that automatically traces the provenance and potential risks of emerging memes. We evaluate MemeTrace on Meme100, a dataset of 100 real-world memes, using both human annotation and automatic metrics. The results demonstrate that MemeTrace substantially outperforms the VLM baseline. More importantly, MemeTrace achieves higher accuracy in detecting unsafe memes, especially those involving disinformation and sensitive content, and remains robust under visual perturbations.

---


### 64. [Outcome-Routed Distillation and Reinforcement Learning for Diffusion Language Models](https://arxiv.org/abs/2610.19271)

**<font color=#1a73e8>作者：</font>** Wentao Lu, Tianyu Zhu, Jesse Clark  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation provides dense supervision on the student's own samples, but its targets still come from the teacher. Verifier reinforcement learning (RL) instead uses an outcome signal, but it provides no direct constraint on capabilities outside the verifier. Combining the two is difficult for diffusion language models (dLLMs), because bidirectional denoising makes the policy likelihoods required by ratio-based RL unreliable.
We develop a likelihood-free pipeline for a mixture-of-experts dLLM. Each rollout group is routed by verifier outcome. Mixed groups use ratio-free, group-centred REINFORCE. If every student rollout fails but a teacher succeeds, the model receives dense KL supervision on the student's denoising canvases. All other groups are skipped. A KL term anchored to the distilled checkpoint limits changes outside the verifier reward.
The tool-calling teacher succeeds on only 18.6% of the training prompts. At 24 denoising steps, distillation exceeds the teacher by 6.77 percentage points, and routing improves the distilled checkpoint by a further 18.31 points. Routing lowers reasoning-trace accuracy by 0.71 points but raises direct-answer accuracy on the same items by 13.21 points. The anchored arm restores trace accuracy. Its tool-calling score differs by -0.16 points, with a confidence interval that includes zero, although this comparison also removes a small fallback distillation route. A domain-conditional recipe retains a 16.37-point tool-calling gain; a second seed gives 18.23 points and reproduces both preservation results, but the math result is seed-dependent. We pre-registered every arm and evaluated each comparison on paired items in a single sweep on one machine.

---


### 65. [Exact Scaling Laws for a Random-Features Bigram Model](https://arxiv.org/abs/2610.19281)

**<font color=#1a73e8>作者：</font>** Julian Enoch, Elvis Dohmatob  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding neural scaling laws is increasingly important for theory and practice, yet first-principles explanations remain limited even in simple settings. In this work, we study capacity-limited scaling in a bottlenecked bigram model with power-law (Zipf) token statistics, viewed as an analytically tractable toy model of a large language model. Fixed random embeddings serve as a proxy for representational capacity and induce an explicit bottleneck of width, allowing us to derive scaling laws for prediction regret as a function of model width, vocabulary size, and the Zipf exponent. Our results complement recent theoretical accounts based on optimization dynamics by isolating scaling due purely to representational constraints. In the appropriate regime, the theory recovers the functional form of classical neural scaling laws and suggests that heavy-tailed language statistics may underlie both optimization- and capacity-driven scaling. Experiments natural language datasets (WikiText2, OpenWebText) closely match the predicted curves.

---


### 66. [Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2610.19290)

**<font color=#1a73e8>作者：</font>** Nikolay Semenov, Artem Riabinin, Sergey Bassenko 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Kandinsky S2V 1.0, an open family of speech-to-video models for controllable audio-driven human animation, comprising Kandinsky S2V 1.0 Lite (2B parameters) and Kandinsky S2V 1.0 Pro (21B parameters). From a single reference image, a speech waveform, and a text prompt, the models generate long-form 25 FPS video in which lip motion, expression, pose, and gesture follow the speech. The architecture draws text and audio conditioning from one Qwen2.5-Omni model and adds a reference-aware three-scale visual memory. Training starts from the Kandinsky 5.0 Video foundation models [1] and combines mixed reference-memory layouts with an area-adaptive face loss. The training corpus contains 1.17M single-speaker clips selected by active-speaker detection, with captions generated directly in English and Russian. A side-by-side human evaluation against the strongest open-source baseline and two proprietary commercial models shows that Kandinsky S2V 1.0 Pro performs comparably to or better than these models on average and is also preferred for lip synchronization. On common speech to video benchmarks, Kandinsky S2V 1.0 Lite and Kandinsky S2V 1.0 Pro rank among the top performing models according to mean rank over five reported metrics. Beyond the base models, we provide {\pi}-Flow distilled variants of both Kandinsky S2V 1.0 Lite and Kandinsky S2V 1.0 Pro. The distilled Kandinsky S2V 1.0 Pro model generates video in 16 sampling steps without classifier-free guidance, achieving a 5.4 times end-to-end speedup over the base model, while matching or exceeding it on nearly all reported benchmark metrics. To accelerate open research and deployment in speech-to-video generation, we release the code, model checkpoints, and diffusers integration under the MIT license.

---


### 67. [Can LLM Agents Efficiently Identify Appliance Faults? Insights From Diagnosing a Simulated Appliance](https://arxiv.org/abs/2610.19291)

**<font color=#1a73e8>作者：</font>** Lucas H. McCabe, Sarah Lukens, H. Howie Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In so-called "Industry 4.0," integrated sensors, analytics tools, and other digital technologies supplement industrial workflows, potentiating enhanced visibility and automation. Prognostics and health management (PHM) and natural language processing (NLP) practitioners alike have explored the application of large language models (LLMs) to industrial asset management, but many prior works' focus on exam-like benchmarks has limited their assessment of LLMs' ability to automate practical operations. Herein, we introduce CoffeeBench, a fault diagnostics task for LLM agents, using a simulated appliance. The LLMs we evaluate struggle to consistently identify faults from the sensor information alone, but the best-performing ones can iteratively refine the fault-option space to eventually obtain a successful diagnosis. Our subsequent analyses, therefore, focus on: differentiating models by diagnostic efficiency (RQ1); examining the lagging performance of the three worst models (RQ2); and identifying viable heuristics for selective prediction (RQ3), including that initial diagnostic uncertainty and LLM-judged soundness of reasoning are high-signal predictors of diagnostic success. In addition to our benchmark results (Section 3.1), we provide practical insights for improving the performance of the open-weight models on CoffeeBench, such as by explicitly tracking episode state on their behalf to reduce timeouts (Section 3.2) or applying a deliberation loop to refine diagnostic hypotheses (Section 3.3).

---


### 68. [Whose turn is it? Context-guided model routing for stateful agents](https://arxiv.org/abs/2610.19292)

**<font color=#1a73e8>作者：</font>** Anikesh Parashar, Avik Dutta, Vashu Chauhan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model routing can reduce the cost of LLM applications by assigning simpler requests to cheaper models without sacrificing the quality of the response. However, most routers treat requests as independent. Stateful agents do not operate under this assumption: a user turn may require multiple model and tool calls, its difficulty depends on the state produced by earlier turns, and changing models can sacrifice reuse of the conversational prompt cache. We study zero-shot, cost-aware routing at the user-turn boundary, systematically varying the routing rule, access to session history, candidate models that differ in size, reasoning effort, or model provider, and prompt-cache behavior. We evaluate on multi-turn versions of SheetCopilot and SpreadsheetBench 2, where persistent workbooks and cross-turn dependencies make isolated routing decisions especially brittle. At a matched offloading rate, giving the router session history improves task pass rate over the same router without history, with gains for every model pair; history-aware routing remains within one point of always using the expensive model. We also found that cost depends on execution dynamics rather than token prices alone: the cheaper model's per-task cost advantage narrows from 6.8x to 3.2x on longer sessions. A closed form cache analysis further shows that downward switches (expensive to cheap) recover their cache cost within two LLM calls, whereas upward switches do not break even under the evaluated conditions. Together, these results show that agent routing is a sequential decision problem: effective policies must account for what happened earlier in the session and for the asymmetric cost of switching models.

---


### 69. [Qwenfant: Train Big Character-level BabyLMs on Concise Parallel Text](https://arxiv.org/abs/2610.19294)

**<font color=#1a73e8>作者：</font>** Lukas Edman, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work concerns our submission for the Multilingual track of the 2026 BabyLM Challenge. We improve on our baseline using data that has been summarized and translated by an LLM, showing that higher-quality data can come from synthetic sources. We further improve with 2 simple changes: using a larger model, and using a character-level vocabulary. Both of these changes require LoRA-style fine-tuning for realizing their full potential. We dub our final Qwen3-based model Qwenfant, which, at the time of submission, ranks 1st in the Multilingual track.

---


### 70. [Verifier-Grounded Agentic RL for Provably Correct Code](https://arxiv.org/abs/2610.19298)

**<font color=#1a73e8>作者：</font>** George Ma, Yuhao Zhang, Bing He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for code usually rewards passing tests, which a model can do while remaining wrong on the inputs the tests do not cover. A program verifier instead decides whether a program satisfies a formal specification for all inputs. Language models are almost always paired with verifiers at inference time only, and turning a verifier into a reward raises two difficulties. It reports only acceptance or rejection, which gives no gradient when every attempt fails, and a policy can cheat it, most simply by telling it to assume what the proof was supposed to establish. We build an agentic environment and reward that address both. The reward reads the verifier's diagnostics rather than its verdict, scoring a candidate by the weighted fraction of proof obligations it discharges, extended with hidden probes from a reference proof's annotations. An integrity audit outranks the verifier, rejecting any candidate that alters the specification or assumes what it was meant to prove. The model works as an agent against a live verifier over many turns, with a separately trained proof specialist as a frozen collaborator. Across Qwen3 models from 1.7B to 14B and a 35B Qwen3.6 mixture-of-experts model, held-out verification on code generation rises from 66.1% to 93.5% on DafnyBench and from 56.3% to 100% on SWE-Proof. This reward leads every other training signal we compare, including a binary pass-or-fail reward trained under otherwise identical settings, with the widest margin on code generation. When the agent must also deliver the repository patch, graded by each project's withheld tests, the fraction of held-out issues it resolves rises from 59.6% to 72.5%. Evaluated unchanged on three verification suites withheld from training, the checkpoints improve on all of them, including one whose language and verifier are absent from training.

---


### 71. [Beyond ICD Codes: Semantic IDs for Generative Medical Coding](https://arxiv.org/abs/2610.19301)

**<font color=#1a73e8>作者：</font>** Yihang Cheng, Qian Zhang, Yonghui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative approaches to automatic International Classification of Diseases (ICD) coding use large language models (LLMs) to predict ICD codes from clinical documents. However, original ICD code strings are not ideal generation targets because the ICD hierarchy does not always reflect clinical relationships, and LLMs struggle to interpret and generate these codes. We introduce SemICD, a framework that trains LLMs to generate Semantic IDs (SIDs) instead. SemICD constructs SIDs by hierarchically clustering embeddings of textual code profiles, allowing semantically related codes to share prefixes while each complete SID uniquely identifies one ICD code. To align the SID tokens with clinical semantics, we employ two auxiliary tasks for bidirectional generation between textual code profiles and SIDs. Experiments on MIMIC-III and MIMIC-IV with four LLMs show that SemICD outperforms direct code generation, improving Micro-F1 by 1.34-8.00 points. Our code is available at this https URL.

---


### 72. [PersEvalBench: Can LLM Evaluators Judge Contextually Appropriate Use of Persona Information?](https://arxiv.org/abs/2610.19314)

**<font color=#1a73e8>作者：</font>** Xinyi Liu, Hooshang Nayyeri, Emine Yilmaz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) evaluators are increasingly used to assess personalized assistants, yet whether they can reliably judge personalization has rarely been tested. We introduce PersEvalBench, a benchmark testing whether an evaluator can recognize appropriate and inappropriate uses of user history. It contains 403 multi-episode scenarios where user information should persist, transfer, or cease to apply. The benchmark covers nine controlled error subtypes across three families: under-personalization, over-personalization, and misapplied-state errors. Human audits confirm that generated errors match their intended types and that the prescribed uses of user information are reasonable.
Across five LLM evaluators, recognition of controlled personalization errors remains limited even with the full dialogue history. On the human-evaluated subset, under-personalization shows the largest gap: humans recognize 94.4% of these errors, compared with 63.9% for the strongest reported evaluator. Evaluators often recognize that a response is problematic but reverse the error direction, mistaking failure to follow an applicable preference (UNDER) for use of an inapplicable preference (OVER). Easier evidence access offers little help: highlighting the relevant history turns raises error recognition only slightly, suggesting that the remaining difficulty lies in judging what role that information should play in the response.

---


### 73. [TopicMerge: A Divide and Conquer Approach to Topic Modeling](https://arxiv.org/abs/2610.19323)

**<font color=#1a73e8>作者：</font>** Matthew Raffel, Lizhong Chen, Sai Munikoti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in topic modeling have split into two main paths: efficient embedding-based methods that offer scalability but are often outperformed on standard clustering metrics, and Large Language Model (LLM) approaches that achieve state-of-the-art clustering performance but at the cost of prohibitive computational expense and poor scalability. This paper introduces TopicMerge, a novel multi-stage pipeline that bridges these approaches to achieve both state-of-the-art clustering performance and computational efficiency. TopicMerge first employs an efficient clustering pipeline to deliberately over-segment a document corpus into a large set of fine-grained, semantically pure micro-clusters, which are then given initial semantic labels. It then introduces a novel, iterative merging algorithm where an LLM, guided by local neighborhood context, arbitrates on consolidating candidate pairs. These approved merges are then selectively executed and semantically relabeled by the LLM, hierarchically building broader, more coherent topics. Extensive experiments on the Bills and Wiki datasets show that TopicMerge achieves state-of-the-art clustering performance while reducing required LLM calls by over 92% compared to document-level methods, offering a practical and scalable solution.

---


### 74. [Why don't Graph Transformers attend to the same token?](https://arxiv.org/abs/2610.19324)

**<font color=#1a73e8>作者：</font>** Alexandre Bismuth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large language models (LLMs), attention concentrates heavily on the first token. This 'attention sink' is believed to protect deep models against over-mixing. Even though graph transformers face a related pressure, we find that a SoTA graph transformer, GRIT, rarely forms sinks on molecules, and that it sinks less when trained on larger graphs, the opposite of the trend in LLMs. In principle, a graph can prevent sinks: we prove and show empirically that its symmetry and locality limit the attention any node can receive. On molecules, however, with distinguishable atoms and global attention, neither limit prevents sinks; what stops them lies in the model. We find that the attention scoring function is the main cause. Replacing GRIT's gated logit with a dot product raises its sink rate from 0.09 to 0.68 on identical graphs. In Graph Transformers using dot-product attention, removing the sink gives about the same error as removing a random node, while GRIT's most-attended nodes matter to its predictions. Attention sinks are therefore a property of dot-product attention rather than of Transformers. In our experiments, they form when dot-product scoring has a distinguishable node to concentrate on.

---


### 75. [NavAble: A Large-Scale Dataset and Synthetic Data Generation Pipeline for Blind Navigation](https://arxiv.org/abs/2610.19330)

**<font color=#1a73e8>作者：</font>** Hochul Hwang, Jahir Sadik Monon, Soowan Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable recognition of accessibility-critical objects (e.g., audible pedestrian signals, door-activation buttons, and handrails) is essential for assistive navigation technologies that support safe, independent mobility for blind and low-vision (BLV) users. Yet these categories are underrepresented in existing large-scale vision datasets, and the few datasets that include them suffer from limited class coverage, inconsistent annotations, and poor diversity. We introduce NavAble, a large-scale dataset spanning 11 accessibility-critical object classes, combining 41K curated open-source images with 8K newly collected, densely annotated real-world images. To extend scale and diversity, we develop a synthetic data generation pipeline that renders high-fidelity 3D assets across 37 environments under diverse styles and viewpoints, yielding 452K frames with rich ground-truth annotations from 565 assets. The pipeline minimizes manual effort by combining automated web image crawling, VLM-based filtering, SAM 3D-based asset generation, and convenient camera trajectory configuration, enabling large-scale data generation at a diversity unattainable through manual collection. Experiments show that fine-tuning existing segmentation models on the NavAble Dataset achieves reliable accessibility-object segmentation (>80% mIoU on our held-out test set). We also demonstrate the effectiveness of synthetic data augmentation, which yields up to +3.5 mIoU over real-world-only fine-tuning. Beyond benchmark evaluation, validation on egocentric data from two mobility-assistive robots demonstrates improved perception reliability in real-world navigation scenarios. Together, NavAble establishes a scalable foundation for BLV navigation perception, directly addressing the data scarcity and embodiment gaps. The dataset and pipeline are publicly available at this https URL.

---


### 76. [LLM-jp-4 Technical Report](https://arxiv.org/abs/2610.19331)

**<font color=#1a73e8>作者：</font>** LLM-jp, Chaoran Liu, Daisuke Kawahara 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents LLM-jp-4, a family of Japanese sovereign large language models (LLMs) developed with an emphasis on transparency, reproducibility, and practical usability. LLM-jp-4 comprises an 8B dense model and a 32B-A3B mixture-of-experts model, both trained from scratch on approximately 12 trillion tokens. To support independent verification and reproduction, we establish explicit criteria for selecting training data, external models, and software, and make the development process publicly available. Evaluation results demonstrate substantial improvements over previous LLM-jp models and competitive performance against open-weight models of similar scale. By documenting the development principles, training procedures, and empirical findings of LLM-jp-4, we aim to provide a reference for future sovereign AI development.

---


### 77. [Beyond Initial Creation: Two Decades of Community-based Chart Revisions from Wikimedia Commons](https://arxiv.org/abs/2610.19337)

**<font color=#1a73e8>作者：</font>** Jasmine Y. Shih, Chase Stokes, Melanie Tory 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open online communities like Wikipedia offer a rich space for understanding the organic evolution of public-facing artifacts, but little is known about how these communities collectively edit chart images. We investigate the phenomenon of "community editing" of visualizations by exploring chart revision patterns on Wikimedia Commons. We introduce a novel dataset of 7,786 longitudinal chart revisions across 1,664 images, labeled with edit categories using an LLM pipeline. Initial data analysis uncovered several novel findings. Multi-contributor revision is associated with more edits to mark styling and text content compared to single-contributor revision. Temporally, mark and text edits occur in more "bursty" cadences than data edits. In addition, while SVG charts attract more unique contributors and revisions than raster charts, their edit histories involve more tightly scoped and less diverse changes. This dataset enables a wide range of analyses of chart change over time.

---


### 78. [Can We Believe AI Peer Review?](https://arxiv.org/abs/2610.19339)

**<font color=#1a73e8>作者：</font>** Zongrui Yang, Haoyuan Li, Zhongsheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models become widely used in scientific review and manuscript revision, AI scores are increasingly serving as feedback for assessing paper quality and guiding edits. Yet whether a single AI score reliably reflects the reviewer's judgment, and whether revision gains based on that score are endorsed by other reviewers, remain understudied. Using 200 papers from ICLR 2025 and 2026 and approximately 14,000 AI reviews, we study score reliability, score-distribution estimation, and cross-model agreement on revision gains. Repeated reviews fluctuate even under identical conditions. Finer-grained scoring protocols reduce score variance but also systematically shift mean scores, while the gains assigned to manuscript revisions depend strongly on the reviewer.

---


### 79. [MMKG-R1: Constructing Multimodal Knowledge Graphs via Reinforcement Learning](https://arxiv.org/abs/2610.19341)

**<font color=#1a73e8>作者：</font>** Zongyu Wu, Yilong Wang, Xiaochen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal knowledge graphs (MMKGs) organize information across different modalities to support multimodal Graph Retrieval-Augmented Generation (RAG), which aims to improve the performance of multimodal large language models (MLLMs). The effectiveness of these multimodal Graph RAG methods largely depends on the quality of the constructed MMKGs. However, most existing methods construct MMKGs without explicit guidance on graph quality, while reinforcement learning (RL)-based methods that rely on final-answer correctness may provide only indirect feedback on MMKG quality. To address these limitations, we propose MMKG-R1, a novel MMKG-quality-driven RL framework for training an MLLM as a multimodal knowledge constructor. To be specific, MMKG-R1 introduces multiple quality-aware rewards to directly evaluate both the quality of information extracted from individual knowledge sources and the quality of the assembled MMKG. These rewards are then used to guide the RL training. Experiments across multiple datasets show that MMKG-R1 constructs MMKGs that improve downstream question-answering accuracy.

---


### 80. [Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](https://arxiv.org/abs/2610.19342)

**<font color=#1a73e8>作者：</font>** Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly interacting with other agents that act for different principals -- people or organizations on whose behalf they work -- e.g., a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-agent system failure studies assume only one orchestrator, shared workspace, or principal. We ask how A2A systems fail when these assumptions are removed. We study more than 2,500 recorded runs of A2A systems built from different agent harnesses and models, spanning 488 scenarios across eight families (legal, CRM, security, commerce, etc.). From these traces, we derive $A^2$-Failures, a taxonomy of 20 A2A failure modes in four categories: (i) discovery and delegation, (ii) grounding and record consistency, (iii) verification, and (iv) conduct and fidelity. Three observations hold across the harnesses, models, and scenarios studied: (1) Agents match tasks to peer names mentioned in the prompt rather than actively searching for available peers; (2) Agents never fact-check each other unprompted; (3) Scoring only the final output rewards the lead agent while hiding internal coordination, verification, and behavioral breakdowns. Our study makes a case for comprehensive evaluations where agents are scored individually against their own objectives in addition to task outcome. We release the run logs behind the taxonomy at this https URL.

---


### 81. [Target-Token Asymmetry Can Masquerade As Depth Specialization](https://arxiv.org/abs/2610.19344)

**<font color=#1a73e8>作者：</font>** Danlin Li, Miao Li, Xu Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Layer-ablation studies often perturb early or late layers of a language model, compare the damage to prediction on two corpora, and read a larger early-layer effect on one corpus as early-layer specialization for its task. Such a comparison averages over the tokens that each corpus asks the model to predict, and these target tokens differ: math solutions, for example, ask for far more whitespace and numbers than encyclopedia prose. We show that this difference can create the appearance of depth specialization. We split a cross-corpus early--late damage interaction by target-token type and recompute it under a target mixture shared by both corpora. Between GSM8K and Wikitext, a positive interaction replicates across five model instances. In the three fully decomposed models, only whitespace has a positive interaction. Removing whitespace reverses the pooled effect in all three, and matching the full target mixture reverses it in two. The diagnosis holds under position matching, adversarial reassignment of token types, and a continuous readout. The risk can also be anticipated from the tokenizer alone. A screen computed before any model runs places every held-out pair it scored in the region its label predicts, and on the pairs it rates at high or medium risk, removing whitespace reverses every positive pooled estimate. A smaller content-word effect one token ahead follows the share of content targets that the unablated model already predicts. A cross-corpus depth effect therefore supports an interpretation of task specialization only after the target-token mixture is reported, the effect is decomposed by token type, and a mixture-matched summary keeps its sign.

---


### 82. [When Is Smaller Greener? Right-Sizing Language Models for Agentic AI](https://arxiv.org/abs/2610.19345)

**<font color=#1a73e8>作者：</font>** Sajid Siraj, Maria Barbati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents use large language models (LLMs) to plan and act over multiple steps, yet models are usually compared per call rather than per completed task. This paper asks: which model should an agent use to complete tasks reliably while minimising energy, cost and time? We show that per-call comparisons can be misleading for agentic AI. Because a task succeeds only if all required steps succeed, small differences in per-step reliability can produce large differences in overall task success. Failed attempts also consume resources. We therefore evaluate models using energy, cost and time per successfully completed task, treating the completed task as the functional unit. On this basis, we develop a decision model for choosing LLMs in agentic workflows. The model applies to tasks with binary or graded outcomes and to settings with or without retries. We show that each resource has a crossover task length at which a smaller, less reliable model ceases to be the greener, cheaper or faster option. These crossovers divide tasks into three regimes: for short tasks smaller models are preferred, for long tasks larger models are preferred, and only between these extremes do preferences among objectives matter. We embed these results in a two-stage framework that separates efficiency from preference. A Pareto screen first removes models that are never competitive; a weighted decision is required only when a genuine trade-off remains. A pilot study of 15 open-weight models from five developers, ranging from 0.6B to 27B parameters, on two multi-step agent tasks with measured GPU energy supports the predicted structure. The model with the lowest energy per completed task changes with task length and task type, and observed crossover points generally match those predicted from per-step measurements. These findings provide a practical framework for right-sizing language models in agentic AI.

---


### 83. [Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.19349)

**<font color=#1a73e8>作者：</font>** Minchan Kim, Sungho Bae, Youngjin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) provides no reward-relative learning signal when all rollouts receive identical rewards. In long-horizon tasks that require multiple interactions, rewards are given only upon successful task completion, making all-fail groups common early in training and limiting opportunities to practice later steps. Guide Assisted GRPO replays a successful reference prefix before the learner continues. We study how initial positions, handoff units, and movement rules affect unassisted task completion. Across three model sizes on BFCL, starting near completion is more effective under a fixed turn-level threshold rule. Finer handoffs alone do not consistently help, but outcome-informed tool-call selection outperforms GRPO on trained and untrained task categories. Guided starts also improve AppWorld success on both evaluation splits. These findings highlight where learning starts and how starting positions move as key curriculum choices.

---


### 84. [Tail Competition Explains Scaling in Best-of-N Sampling for Verifiable Problems](https://arxiv.org/abs/2610.19362)

**<font color=#1a73e8>作者：</font>** Taro Yano, Yoichi Ishibashi, Masafumi Oyamada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Best-of-N sampling is a simple inference-time scaling strategy for large language models, yet its behavior under incomplete reward models remains poorly understood. We study Best-of-N as a competition between the extreme reward tails of correct and incorrect responses. This view shows that success depends not only on the probability of sampling a correct response, but also on whether correct responses dominate incorrect ones in the upper tail. Using extreme value theory, we characterize three asymptotic regimes: correct-tail-dominant, incorrect-tail-dominant, and critical explaining both monotonic gains and reward-hacking-induced degradation. We further derive finite-sample scaling laws for representative reward distributions, showing that, under Gaussian rewards, incorrect responses with sufficiently large variance can dominate selection even when their mean reward is lower. Unlike oracle selection, convergence with an incomplete selector can be polynomial rather than exponential. Finally, we propose a lightweight tail-tension criterion to estimate when additional sampling may become harmful. Experiments on synthetic data and real reward model scores are consistent with the theoretically predicted regimes, scaling laws, and diagnostic behavior, suggesting that tail competition provides a unified lens on Best-of-N sampling for verifiable problems.

---


### 85. [Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](https://arxiv.org/abs/2610.19366)

**<font color=#1a73e8>作者：</font>** Minghao Guo, Qingyue Jiao, Xiujin Liu 等 80 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal data remains a significant challenge as they move toward long-horizon tasks and lifelong settings. Addressing this challenge requires effective memory mechanisms that can maintain continuity across sessions, adapt to changing users and environments, and refine memory-management policies through accumulated experience. We introduce a two-axis analytical framework for multimodal agent memory structured around two key questions: how multimodal information is formed and represented (Axis I, Formation and Representation), and how its management adapts with accumulated experience (Axis II, Memory Management). Axis I, Formation and Representation, characterizes what information is retained and how it is encoded (e.g., modality-specific embeddings, textual and structured records, latent and parametric representations) to support subsequent reasoning and action. Axis II, Memory Management, distinguishes three tiers: T1 Static Memory reuses fixed memory; T2 Dynamic Memory updates memory through a stable policy; and T3 Self-Evolving Memory updates memory through an evolving policy. Based on this framework, we synthesize recurring design patterns and derive principles for balancing source fidelity with abstraction, maintaining temporal validity and provenance, grounding memory use in recoverable evidence, and evolving memory policies over time. Furthermore, we discuss the challenges and potential future directions for the memory mechanism of multimodal agents.

---


### 86. [Beyond Corrected Actions: Training LLM Agents on Textual Critiques](https://arxiv.org/abs/2610.19367)

**<font color=#1a73e8>作者：</font>** Thomas Zeng, Zelei Cheng, Mingyang Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for multi-turn agentic tasks that require interactions with users and environments over extended sequences of actions. A common approach to improving LLM agents is to use more capable expert models to provide training supervision, either by behavior cloning the expert's trajectories or by using the expert to correct the actions in trajectories generated by the weaker student model. However, expert LLMs can provide richer supervision than actions alone: they can directly generate textual critique that explain why specific actions are incorrect. We study whether training on such feedback benefits LLM agents and propose Critique-Augmented Agentic Fine-Tuning (CAFT), a framework that elicits textual expert feedback on student-generated trajectories. For each incorrect action, the expert yields both a corrected action and a textual critique explaining the student's mistake--which we then use as the training target for fine-tuning. Across four student models from the Nemotron 3 and Gemma 4 families on the agentic domains $\tau^2$-Bench Airline+Retail and WebShop, adding critiques to action-level supervision improves performance by 8% on average over action-only distillation. Additionally, CAFT checkpoints can also provide a better warm start for reinforcement learning than expert-trajectory distillation. Our results demonstrate that textual critiques can strengthen supervision for multi-turn LLM agents.

---


### 87. [Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards](https://arxiv.org/abs/2610.19372)

**<font color=#1a73e8>作者：</font>** Min-Young Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the agents they guard. We introduce Policy-Verified Self-Training (PVST), a post-training paradigm in which an agent generates its own interaction trajectories and an executable policy verifier, here a deterministic gate compiled from a written policy, evaluates whether each action complies. Compliant trajectories are reinforced, and violations become negatives for preference optimization; beyond the gate and the benchmark's task-success signal, PVST needs no stronger teacher model, no human preference labels and no attack-specific supervision, although rollouts are collected in the benchmark's attacked environment. On held-out AgentDojo tasks under prompt injection, policy-verified preference training of Qwen3-8B reduces violating trajectories from 37.2% to 10.3 $\pm$ 0.9% (three seeds) and successful attacks from 12.4% to 0.5% at equal or higher pooled task utility, although utility falls on travel, compared with 22.0% when negatives are selected by an attack oracle and 31.9 $\pm$ 0.9% with negatives that contain no violation. The learned behavior holds under an attack template never used in training (37.7% to 11.0%) and on a suite excluded from training (34.8% to 16.7%), and the retained verifier's intervention rate falls from 39.2% to 8.8% (seed 0). Our analysis identifies two conditions under which the verdict is most informative: success must not already imply compliance, and guarded actions must appear in both permitted and forbidden contexts.

---


### 88. [Evaluating Compressed Memory: Dependence, Utility, and Content Benefit](https://arxiv.org/abs/2610.19373)

**<font color=#1a73e8>作者：</font>** Minsu Oh, Seunghui Jwa, Chanjun Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Does a language model answer better because its compressed memory contains useful document information? Replacing memory vectors with zeros can lower a trained model's score without showing that it outperforms a model trained without memory. We combine zeroing with separately trained models that cannot access stored text or receive the same constant input for every document. Across nine systems, some models rely on memory yet perform worse than the trained alternative. For example, in experiments that predict states in generated stories, zeroing memory worsens a model's prediction loss, yet a model trained without memory achieves lower loss than the original model with intact memory. On TriviaQA, giving xRAG memory from another question's passage raises F1, which measures word overlap with accepted answers, from 19.38 without a document to 24.78. Its effect on how often outputs contain an accepted answer is statistically uncertain. The question's retrieved passage scores higher still (29.88 F1). Thus a gain over no document alone does not establish that the gain requires the question's passage. Evaluations must therefore specify the comparison model, absolute performance, and generation and scoring conditions.

---


### 89. [DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents](https://arxiv.org/abs/2610.19376)

**<font color=#1a73e8>作者：</font>** Tianle Chen, Pushkar Singh, Ketan Todi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step that adds no new information. We identify this failure as a loop. Loops appear natively in Qwen, Llama, and Gemini agents and become far more common once the agent's history is compressed to fit its context window. To reduce these loops, we propose DeLoop, a self-supervised training method. DeLoop builds on a simple observation: the agent's own rollout can provide the supervision needed to learn from its loops. We use a looping action as a negative example and the first later non-looping action in the same rollout as a positive example. DeLoop learns from these pairs through direct preference optimization and does not require task rewards, gold answers, or LLM judges. On CodeGym under compression, DeLoop reduces the share of Qwen3-8B tasks containing loops from 57.3% to 6.1%. It also uses about one third as many steps per task, with similar task success. On Qwen3-32B, DeLoop reduces loops and steps while raising task success from 37.7% to 44.8%.

---


### 90. [Learning What to Keep: Transfer-Aware Personal Skill Learning from User Feedback](https://arxiv.org/abs/2610.19380)

**<font color=#1a73e8>作者：</font>** Li Wang, Chen Zhang, Yirong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User feedback enables LLMs to refine reusable personalized skills, but often mixes persistent preferences with request-specific corrections. Indiscriminately retaining both risks negative transfer, motivating selective retention at the level of individual requirements. We frame this challenge as selective transfer over atomic rules and propose SkillGrain, a framework for learning reusable personalized skills from user feedback. SkillGrain decomposes feedback into independently actionable rules, predicts their transferability, and retains only those suitable for future requests. To learn these decisions, we combine rubric-guided skill rewards with fine-grained credit assignment that separately evaluates rule content and retention decisions. We further jointly optimize skill induction and skill-conditioned generation through reinforcement learning, ensuring that learned skills support downstream personalization. We construct a benchmark spanning five personalized writing tasks to evaluate cross-request generalization. Experiments across three base models in both in-domain and out-of-domain settings show that SkillGrain achieves the best overall average performance among competing methods.

---


### 91. [EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs](https://arxiv.org/abs/2610.19381)

**<font color=#1a73e8>作者：</font>** Guanhua Zhu, Bo Shen, Lei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Different tasks often require interactive agents to perform similar operations at intermediate steps. Retrieving an entire past workflow can introduce irrelevant steps, whereas retrieving isolated operations can discard the dependencies needed to reuse them. We introduce EvoWeave, a framework for experience memory that represents abstract states as nodes and reusable operations as directed edges with input and output contracts, provenance, and capability references. A planner decomposes the current task into a dependency graph; operation retrieval and bounded directed search then assemble relevant experience fragments. An execution agent can inspect these fragments and their referenced capabilities, while reflection separates concrete execution evidence from reusable abstractions. We study the framework across four benchmarks, five evaluation settings, and three language model backbones. Across backbones, AppWorld Normal and Challenge task goal completion average 51.91 and 27.99, respectively, exceeding the baseline without memory by 6.99 and 4.99 percentage points. An AppWorld ablation associates directed connections with an additional improvement of 2.08 points over independent operation cards. The results motivate composition of reusable operations while exposing tradeoffs in retrieval overhead and conditions for valid reuse.

---


### 92. [ixi-sLM: On-Device sLM for AI Call Agent Service](https://arxiv.org/abs/2610.19382)

**<font color=#1a73e8>作者：</font>** Han-Sang Lee, Kyuho Lee, Juneyoung Park 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running an AI call agent on-device makes it private, network-independent, and free of per-query cloud cost, but shipping one as a real-world service imposes constraints a cloud deployment never faces: ~1GiB memory budget, in-call latency and thermal limits, static-integer NPU execution, Korean STT input far from sLM pretraining, and cloud-level quality expectations. We bring ixi-sLM, a 1.2B Korean sLM, to mobile NPUs through ON-DEVICE MODELING: domain-adaptive modeling trims the vocabulary by call frequency to shrink the embedding and LM head that take nearly half the model under INT4 transformer weights and refits the tokenizer to call speech (18% fewer tokens on call traffic), while task-aware quantization calibrates on real calls and assigns per-module mixed precision by activation sensitivity. A single domain-adapted model runs ixi-O's two production services, AI Call Summary and AI Call Answering, at 94% of a state-of-the-art cloud LLM's task-weighted quality; our on-device modeling carries that quality onto the NPU with only a marginal drop in overall score, in an 803MiB model (28% of FP16) at 23% of the CPU's per-call energy. The same recipe deploys across Qualcomm and Apple NPUs and serves several million ixi-O subscribers in production.

---


### 93. [RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning](https://arxiv.org/abs/2610.19385)

**<font color=#1a73e8>作者：</font>** Zinan Ling, Yang Xiao, Ruimeng Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) unlearning is often evaluated primarily by target suppression and clean retain utility. These metrics can miss a local failure mode: a model may perform well on standard retain prompts, yet degrade on benign reasoning when prompts lie near the forgotten domain. This phenomenon is termed forget-adjacent utility loss. A fundamental question is: where should forget representations go after they leave the removed behavior? Successful unlearning depends not only on whether forget-conditioned representations depart from the harmful computation, but also on the direction in which they are redirected afterward. We propose RA$^2$ (Retain-Anchored Attraction), a latent-space unlearning method that redirects forget-token states toward nearby retain-supported representations while preserving higher-layer behavior on retain data. On WMDP and MUSE, RA$^2$ yields higher forget-adjacent utility than strong unlearning baselines at similar broad-utility levels. These results show that the migration direction of forget representations materially affects benign behavior near the forget boundary. Our code is available at this https URL.

---


### 94. [STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents](https://arxiv.org/abs/2610.19386)

**<font color=#1a73e8>作者：</font>** Guanhua Zhu, Hanwen Li, Zhi Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experience is recalled and its concrete steps are copied verbatim, actively harming the agent. We introduce STRATA, a structured, outcome-grounded, self-maintaining memory that organizes experience into a three-layer graph of atomic skills and code snippets, task workflows and generalized meta-frameworks, connected by typed edges. STRATA maintains itself through five mechanisms sharing one similarity geometry: a multi-dimensional similarity that scores retrieval by operation and target; a typed reflector crystallizing procedures from successes and pitfalls from failures; community detection that induces meta-frameworks; pressure-triggered garbage collection with articulation-point protection; and contrast edges that flag confusable, direction-opposite experiences. Across four interactive benchmarks (AppWorld, WebArena, ALFWorld, ScienceWorld), two frozen backbones and seven baselines, STRATA attains the best average score while simultaneously using the lowest latency and fewest environment steps of any memory-augmented method, and 44% fewer lines of injected memory than the most context-hungry baseline. We isolate two failure modes of prior memories: single-level memory degrades sharply as the task set grows, and single-level concrete memories suffer catastrophic negative transfer, which contrast edges repair, lifting ScienceWorld from 78.7 to 96.7 within the same system.

---


### 95. [SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19397)

**<font color=#1a73e8>作者：</font>** Dingyi Rong, Yue Shi, Chaofan Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic RL is constrained by the futures visited by the current policy. When rollouts fail to reach useful behaviors, improved credit assignment cannot provide supervision for states and actions that were never encountered. On-policy distillation (OPD) introduces teacher guidance on policy-induced states, and recent multi-turn variants improve how this guidance is scheduled, replayed, refined, or validated. However, they do not directly use the oracle-controlled future itself as the training trajectory. We introduce \textbf{State-Rooted Executable Rollout Optimization (SERO)}, which augments on-policy agentic RL with executable oracle continuations. SERO restores a state actually reached by the current policy and lets a training-only oracle continue interacting with the real environment, making the downstream observations and oracle actions themselves available for learning. It then applies \textbf{policy-reachability weighting}, which weights each oracle step by the frozen behavior policy's compatibility with the preceding oracle actions. This allows deeper supervision to become effective as the policy becomes more compatible with the oracle branch. The oracle loss is optimized separately from the base RL estimator and no oracle is used at inference time. We evaluate SERO on two challenging interactive-agent benchmarks, ALFWorld and WebShop, using Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct. On ALFWorld, learning the full executable continuation is substantially more effective than supervising only the root oracle action, while policy-reachability weighting further improves out-of-distribution performance.

---


### 96. [KoAGE: Do Large Language Models Know, Learn, and Coin Korean Neologisms?](https://arxiv.org/abs/2610.19399)

**<font color=#1a73e8>作者：</font>** SungHo Kim, Eojin Jeon, SangKeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean neologisms arise through diverse mechanisms, a demanding test of language models beyond lexical memorization. To enable systematic evaluation, we introduce NeoTrace, an automated, rerunnable framework that collects and dates neologisms across genres. Its 4,271 entries support KoAGE, a cutoff-aware benchmark with three acquisition and two generation tasks---the latter, to our knowledge, the first to compare model coinages with attested neologisms under their original materials and community context. Across 21 models, lexical recall diverges from contextual inference: in a five-model temporal analysis, models define only 13-30% of cutoff-year words, yet can infer meaning from one usage. However, structural understanding remains limited: even correct definitions barely improve formation analysis of pre-cutoff neologisms. Given word-building materials, single models often follow human formation mechanisms, whereas multi-agent coinage favors abbreviation and depends on interaction framing. KoAGE thus separates what models know, learn from use, and coin.

---


### 97. [Vision-Language Models Integrate Conflicting Evidence Like Biased Bayesian Observers](https://arxiv.org/abs/2610.19407)

**<font color=#1a73e8>作者：</font>** Josh Barua, Kyle Mahowald, William Rudman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models must reconcile conflicting text and images. Prior work has characterized the resulting behavior in terms of modality biases--e.g., a "blind faith in text"--but why preferences vary across models, domains, and input conditions remains unclear. We develop a predictive account from a Bayesian perspective, positing that VLMs combine conditionally independent evidence from each modality with prior beliefs, subject to modality-specific biases. The resulting two-parameter cue combination model accurately predicts VLM preferences under unseen combinations of input degradation and transfers to new forms of unreliability without refitting. Separating evidence strength from integration bias explains how VLMs can follow text even while weighting visual evidence more heavily, reconciling reports of text and vision dominance under a single combination rule.

---


### 98. [ForkGRPO: Efficient Exploration and Fine-Grained Credit Assignment for Diffusion Language Models](https://arxiv.org/abs/2610.19408)

**<font color=#1a73e8>作者：</font>** Zhaoyan Jia, Chengwei Zhou, Gourav Datta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have advanced rapidly, yet strengthening their reasoning through reinforcement learning (RL) remains an open challenge. Any-order generation can suffer from entropy degradation, which narrows the reasoning paths available for exploration. Recent work mitigates this issue by applying standard GRPO with left-to-right generation. However, independently generating every rollout from the input prompt can leave alternative continuations from intermediate states underexplored, while trajectory-level advantages assign uniform credit to all tokens without distinguishing the contributions of individual reasoning segments. We propose ForkGRPO, an RL framework that couples efficient exploration with fine-grained segment-level credit assignment. It samples multiple continuations from high-entropy intermediate states along a reference trajectory, prioritizing textual boundaries and reusing shared prefixes. The continuations provide complementary learning signals: within-state group-relative advantages guide which continuations to reinforce, while Monte Carlo state-value differences indicate which reasoning segments improve expected outcomes. Among the evaluated architecture-preserving RL methods, ForkGRPO achieves the best performance on three of four benchmarks, while improving over the directly comparable JustGRPO by up to 1.2 percentage points and using up to 27.8% fewer generated tokens. ForkGRPO-Fast further achieves a $2.49\times$ training wall-clock speedup with negligible accuracy loss.

---


### 99. [WinARDet: Compressed Window Auto-Regression for Long-Horizon Vision-Language Grounding](https://arxiv.org/abs/2610.19419)

**<font color=#1a73e8>作者：</font>** Chenxu Wang, Hangyi Kuang, Bo-Wen Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MLLM-based detectors formulate vision-language grounding as autoregressive coordinate generation, yet in dense scenes, they often collapse into a box repetition loop, repeatedly emitting identical boxes until the decoding budget is exhausted. We trace this failure to historical-answer attention takeover: Under full-history autoregression, repeated coordinate tokens in the growing answer history attract disproportionate attention, crowding out the attention sinks needed to attend to new visual evidence. % To break this loop, in this paper, we propose \textbf{Compressed Window Auto-Regression} (WinAR). This new mechanism partitions a long answer sequence into consecutive generation windows and restricts full token-level autoregression to the current window only while compressing each previous window into a fixed set of latent tokens that condition subsequent decoding. This design reduces the repeated exposure to raw historical coordinates that triggers the attention takeover, yet preserves cross-window dependencies essential for coherent multi-object generation. On RSDense, which contains 200-2,000 objects per image, our model WinARDet improves RexOmni F1-score (IoU=0.5) from 32.16 to 39.36 over the baseline, while reducing the redundancy rate from 35.48% to 13.00%. WinARDet also generalizes across decoding strategies and output formats, including parallel box decoding and polygon generation, providing a practical paradigm for long-horizon vision-language grounding across scene densities.

---


### 100. [Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training](https://arxiv.org/abs/2610.19423)

**<font color=#1a73e8>作者：</font>** Anshu Raina, Peyman Razaghi, Yuankai Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Configuring distributed LLM training across hundreds of GPUs requires jointly optimizing tensor, pipeline, expert, context, and data parallelism alongside micro-batch size, recomputation, sharding, and overlap, a combinatorial space where memory legality can hinge on a single byte of activation accounting. Today, teams navigate it through expensive multi-node trial and error, burning GPU-hours on crashes and suboptimal recipes. We present Primus Projection, which closes this loop with two coupled components. First, a hybrid projection engine that measures what it can and simulates what it cannot: GPU microbenchmarks on as few as a single device capture compute kernels and any in-scope communication; a sub-node downscale-measure-upscale workflow analytically restores out-of-scope collectives, FSDP overlap, and the full pipeline schedule at the multi-node target. A pure simulation mode runs entirely on CPU, enabling pre-silicon planning without any GPU. Second, the Primus Tuning Agent treats the projection engine as a fast scoring oracle (seconds per candidate instead of tens of minutes) and uses it to drive an intelligent search over the configuration space. A deterministic seed planner sweeps single axes; an LLM investigation loop proposes cross-axis combinations the planner cannot reach, with an analytic memory pre-filter that rejects infeasible candidates before any GPU time is spent. Validated on Llama 3.1 (dense) and Mixtral 8x22B (MoE) across two GPU generations, all projections stay within ~10% of measured multi-node throughput, and fidelity holds at production scale: 4.7% error on DeepSeek V3 671B at 1,024 GPUs and 1.9% on Qwen3-235B-A22B at 256 GPUs. In a Mixtral 8x22B case study, the Primus Tuning Agent discovers a configuration delivering +27% throughput over the published 4-node BF16 reference at the same scale, in under 30 minutes of single-node exploration.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
