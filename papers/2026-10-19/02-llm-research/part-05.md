# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-321](./part-07.md)

---

### 201. [Beyond Generation: Using Multimodal LLMs as Detectors of LLM-Generated Deepfake Facial Images](https://arxiv.org/abs/2610.21760)

**<font color=#1a73e8>作者：</font>** Olivia Salamon, Virginia N. L. Franqueira, Shujun Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As image generation models become increasingly capable of producing highly realistic content, traditional forensic techniques are struggling to keep up. This paper investigates whether MLLMs can instead be used as a form of forensic analysis by identifying synthetic media. Specifically, the study aims to determine whether these models detect fake images by recognising physical inconsistencies, or whether they rely on digital artefacts such as embedded this http URL MLLMs: GPT-4o, GPT-5, GPT-5.2, Gemini 2.5, Gemini 3, and Seed 1.6, are benchmarked using a dataset of 400 images. Fifty images are authentic photographs, while the remaining 350 are generated using seven leading image models: Gemini 3, Gemini 2.5, Flux.2 Pro, GPT-Image-1, GPT-Image-1.5, Seedream 4.0, and Seedream 4.5. The evaluation is structured in three stages: single-image classification, pairwise comparison, and a focused "self-detection" experiment on Gemini. Several MLLMs achieved a high detection accuracy, with GPT-5.2 reaching a peak of 97.9% in the pairwise experiment, against specific generators and an overall mean pairwise accuracy of 82.5% by identifying structural or physical inconsistencies within images. However, results from the self-detection experiment indicate that the presence of invisible SynthID watermarks leads to a 10% reduction in Gemini's detection accuracy compared to the clean control group. One possible explanation is that SynthID embedding reduces some of the visible artefacts the models rely on for this http URL results imply that MLLMs can detect structural artefacts without relying on watermarks, but performance varies substantially across model generations. The findings from comparison C5 also suggest that SynthID embedding may suppress some of the structural artefacts used during detection.

---


### 202. [Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods](https://arxiv.org/abs/2610.21763)

**<font color=#1a73e8>作者：</font>** Adnan Al Ali, Jindřich Libovický, Anne Lauscher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-enabled large language models (AuLLMs) allow users to interact with them simply by talking to them, without the need for an intermediate transcription. This expands the model's accessibility and capabilities by encoding non-verbal cues. However, using non-verbal cues may lead to biased behaviour based on the attributes inferred (or assumed) from them. In this work, we focus on the gender attribute and show that models' perception of it can be unlearned using adversarial methods without a loss in performance on other benchmarked tasks. Such models are useful in situations where gender inference is unwanted. However, in other practical settings, gender perception (without bias) may be this http URL a less radical measure, we distil the gender-agnostic model, creating a model that perceives gender but responds similarly to the gender-agnostic teacher, unless explicitly this http URL apply our newly proposed methods to three AuLLMs and obtain satisfactory results in the gender-unlearning part and partially satisfactory results in the distilling part.

---


### 203. [From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research](https://arxiv.org/abs/2610.21767)

**<font color=#1a73e8>作者：</font>** Yijia Mao, Song Dai, Tao Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can AI agents organize scientific investigations that lead to well-supported conclusions? To evaluate this capability, we introduce PhysClosureBench, a benchmark of 50 expert-verified, goal-specified research tasks spanning strong-field, attosecond, and neighboring physics areas. Each task specifies the research objective and essential scientific constraints, while leaving the agent to organize the investigation and determine how to generate and validate the evidence needed to answer the question. A 20-criterion Atomic Score measures local scientific accomplishment, while Research Closure (RC0--RC4) assesses how fully the investigation resolves the specified research question based on whether its indispensable evidence requirements and applicable scope conditions are satisfied. We evaluate seven frontier LLMs, where Claude-Opus-5 achieves the highest mean Atomic Score (6.29/10) but reaches RC4 in only 32.7% of attempts. Across the benchmark, 36.2% of attempts scoring at least 8/10 still fall short of RC4, while all seven models reach RC4 on substantially fewer tasks in all three runs than in at least one. Case-level analysis further illustrates how misinterpretation of generated results and unresolved physical applicability limits can lead to incomplete closure. Together, these results reveal a persistent gap between AI agents' local scientific accomplishments and their ability to achieve complete research closure.

---


### 204. [Learning to Think and Explore in 3D World](https://arxiv.org/abs/2610.21783)

**<font color=#1a73e8>作者：</font>** Yijiang Li, Bingyang Wang, Nuno Vasconcelos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how vision-language models (VLMs) can learn to think and actively explore in 3D space. Instead of providing multi-view images, videos, or 3D representations to the model, we preserve the native visual encoding of VLMs, i.e., a single image, one at a time, just like humans, and treat the 3D representation only as an environment with which the model can interact through actions (e.g., move left) and observations (rendered images). Each rollout begins from an initial first-person view and a visual question. The model can then iteratively reason, navigate, and reorient its viewpoint before committing to a final answer. Following an initial trajectory-supervised finetuning, we apply reinforcement learning (RL) with rewards driven primarily by final-answer correctness. Crucially, RL provides no direct supervision over which viewpoints the model should visit or which exploration actions it should take. Instead, the model must learn an effective exploration policy solely from the extent to which its interactions improve performance. Across six 3D benchmarks, our model ACT3D achieves an average accuracy of 53.2% that improves its base Qwen model by 22.0% and surpasses proprietary Gemini 3.6 Flash. ACT3D also outperforms existing open-source 3D methods while using 50-70% fewer input frames, and generalizes to unseen domains with an average improvement of 5.9% over its supervised initialization. Further analysis reveals adaptive, question-conditioned exploration. Performance gains over the base model increase from 0.6% on questions answerable from the initial view to 16.3% on those requiring extensive exploration. ACT3D searches for occluded targets, avoids unnecessary exploration, and acquires complementary viewpoints for spatial comparisons. These findings demonstrate that outcome-based RL enables VLMs not only to reason over visual evidence, but also to learn when and how to acquire it.

---


### 205. [RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent](https://arxiv.org/abs/2610.21791)

**<font color=#1a73e8>作者：</font>** Huan Zhang, Mingju Chen, Dongxu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executable artifact refinement, while recursive self-improvement (RSI) further extends optimization to the improvement mechanisms themselves. However, adapting self-improvement workflows to evolving performance bottlenecks while improving workflow orchestration through execution feedback remains a key challenge. We propose \textbf{RSIFlow}, a \textbf{R}ecursive \textbf{S}elf-\textbf{I}mprovement framework that integrates adaptive work\textbf{flow} orchestration with meta-agent capability evolution. RSIFlow diagnoses performance bottlenecks from task-agent trajectories and environmental feedback to dynamically select component-specific improvement workflows. The meta-agent then distills workflow outcomes into component-specific skills and cross-component principles, evolving its own harness to improve subsequent workflow orchestration. Experiments across six benchmarks and two backbone models show that RSIFlow achieves the SOTA average performance on all benchmarks. Ablation studies further demonstrate the contributions of adaptive workflow orchestration and meta-harness evolution. Code is available at this https URL.

---


### 206. [MedPAO-VL: Interpretable and Protocol-Compliant Agent for Structured Radiology Report Generation](https://arxiv.org/abs/2610.21794)

**<font color=#1a73e8>作者：</font>** Shrish Shrinath Vaidya, Gowthamaan Palani, Minmini Selvam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable generalization capabilities of Large Language Models, generating clinically accurate and structured radiology reports from medical images remains a significant challenge. Current end-to-end approaches function as black boxes, prone to factual hallucinations and generating ungrounded findings. This lack of reliability and failure to adhere to domain-specific structuring protocols, fundamentally limits their clinical utility. We present MedPAO-VL, a multimodal agent that shifts the paradigm from monolithic generation to explainable, iterative, protocol-compliant structured report generation. Unlike deterministic models, our plan-act-observe loop functions as a goal-oriented agent: it first perceives the Chest X-Ray through an explainable vision module designed to capture inherent diagnostic uncertainty, then iteratively refines the generated report by observing semantic discrepancies and self-correcting its generation for better alignment with visually detected clinical findings. Evaluation of our framework demonstrates that this agentic reasoning improves clinical correctness and completeness, achieving an expert-rated accuracy score of 3.5/5 and a structural score of 4.3/5. By prioritizing pathology specific explainability and iterative refinement over opaque end-to-end mapping, MedPAO-VL offers a transparent and clinically viable alternative for automated structured radiology report generation.

---


### 207. [RoleQ: Role-Aligned Scales for Converting Language Models to Ternary](https://arxiv.org/abs/2610.21808)

**<font color=#1a73e8>作者：</font>** Johannes Knittel, Alec Helbling, Hanspeter Pfister  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight quantization below four bits shrinks memory and bandwidth at a perplexity that looks acceptable, but often at the cost of factual knowledge and task accuracy. Ternary weights have mostly been obtained by training from scratch or long fine-tuning. We introduce RoleQ, a quantization framework that places scales by the functional roles of Transformer units rather than by the layout of the weight matrix, as conventional formats do. Vectors that read from the residual stream take one scale per output unit; those that write to it, one per input unit. The rule is structural, needs no search, calibration or stored state, and holds on integer and ternary grids. In a rotated basis it matches a per-layer axis search at half the solver work, and at ternary it cuts perplexity by up to half against layout-based placement in two families at every size from 0.6B to 14B, where per-row scales leave MMLU at chance. Our lightweight post-training pipeline converts an existing checkpoint to 1.59 bits per weight in a few GPU-hours, a fraction of the cost of learned ternarization, and leads every post-training ternary method at matched or lower memory-resident bits on perplexity, zero-shot accuracy and MMLU, most widely on knowledge. A sparse second ternary plane placed by a per-unit Fisher saliency keeps the matmul multiplication-free and recovers what ternary loses first: at 8B, a fraction of a bit returns about half the MMLU that conversion costs, well ahead of random or Hessian-based placement at equal bits.

---


### 208. [N-Gram Memories at Two Bits: Quantizing Lookup Tables in Large Language Models](https://arxiv.org/abs/2610.21810)

**<font color=#1a73e8>作者：</font>** Donghoon Han, Minseop Jung, Dong Woo Kwak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional memory expands language-model capacity through selective lookup, but the full embedding table must remain available for every possible input. We introduce Conditional Program (CP), a compressed representation that reconstructs only the rows an input requests. CP represents each row by a short code and a local scale, with a reconstruction program shared across the table. We instantiate this representation with a Gaussian trellis, norm restoration and independently decodable row records. CP's two-bit code lowers output KL by 41--63\% relative to 2-bit round-to-nearest. Analysis across three trained n-gram memory families shows that Gaussian-like coordinate statistics coexist with learned relationships among rows; at matched storage budgets, the shared trellis outperforms the fitted codebooks and low-rank residual variants we test. For DeepSeek, it reduces table storage from 203GB to 51GB, leaving room for larger workloads when the table is kept on GPU.

---


### 209. [Learning Lean Feedback for Efficient Proof-Candidate Evaluation on GPUs](https://arxiv.org/abs/2610.21881)

**<font color=#1a73e8>作者：</font>** Lazar Milikic, Etienne Bamas, Emmanuel Abbe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training language models for formal theorem proving requires large numbers of verifier calls. Slow checks and timeouts often leave GPUs waiting and withhold rewards from potentially correct proofs. We train neural evaluators to predict Lean 4 verdicts and compiler feedback on GPUs using 4.84M labelled programs. We compare two validity classifiers with a feedback model that annotates proof attempts with predicted goal states and error messages. A two-stage evaluator that screens candidates with a classifier and scores its positive predictions with the feedback model reaches 87.8% accuracy in predicting whether Lean accepts a candidate proof, evaluated on a 68,932-program benchmark collected from public provers. The combined evaluator processes 3.5 candidates per second on one H100, 4.2x the throughput of our 64-worker Lean baseline with environment reuse. Finally, we combine our evaluator with Lean verdicts to obtain a hybrid reward system that shortens GRPO training steps by approximately 31%. After one GRPO epoch with hybrid rewards, the prover achieves nearly the same miniF2F pass@1 as with Lean-only rewards (62.2% versus 62.4%) and a pass@32 of 72.4% versus 71.3%.

---


### 210. [Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation](https://arxiv.org/abs/2610.21882)

**<font color=#1a73e8>作者：</font>** Weilin Ruan, Bohan Zhou, Jinghao Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied spatial intelligence requires more than visual recognition: models must localize entities, reason about their relations, and express this knowledge in action-relevant forms. Yet joint training can conflate the knowledge needed at different stages because supervision is fragmented across incompatible geometric and semantic outputs. We introduce Anvil, a unified framework for data generation, training, and benchmarking for embodied spatial intelligence. (1) Anvil-Gen is a heterogeneous data flywheel that combines form-specific generation, cross-stage consistency verification, and failure-driven recollection across 11 Ground--Relation--Act forms. (2) Anvil-Ben provides scene-aligned supervision for learning diverse embodied spatial capabilities and scene-linked assessments that distinguish stage competence from error propagation. (3) Anvil-MOPD is a 9B student that consolidates heterogeneous spatial knowledge through distillation from specialist teachers. Semantic-first-fault routing targets teacher supervision to the student's earliest decisive failure, while stage normalization controls the loss scale across native outputs of different lengths. We construct 5.8M source-grounded records spanning 160K images, reserving 580K spatial records for held-out evaluation and using the remaining 5.22M records for training. On average across seven public benchmarks, Anvil-MOPD outperforms Qwen3.5-9B and RynnBrain-8B by 9.29 and 11.03 percentage points, respectively, while reaching 80.67% on VABench-Point. Controlled studies support targeted coverage, selective transfer, and feedback-guided repair as complementary framework components.

---


### 211. [SurgStreamer: proactive, request-driven monitoring of surgical video streams with structured state and a reusable reasoning layer](https://arxiv.org/abs/2610.21895)

**<font color=#1a73e8>作者：</font>** Bowen Xiang, Jon S. Heiselman, Michael I. Miga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical teams could benefit from assistants that watch the video for requested events, such as "tell me when the clip applier appears during Calot triangle dissection", and answer questions about what has already happened. We formalise this task as request-driven event detection with exact semantics and causal alert decisions, and present SurgStreamer. It separates procedure-specific perception, which maps the 1-FPS stream to a structured state over tools, actions and phases, from procedure-agnostic reasoning, which evaluates a formal monitoring condition over this state and an event memory, either with exact rules or with a small controller that addresses entities through pointers rather than names. We evaluate this monitoring core with gold conditions. On a pre-registered, sealed test set of 12 laparoscopic cholecystectomies, SurgStreamer reached a macro event-F1 of 0.598 over full procedures. On identical 75-s windows with only the window available to every method, it scored 0.677. The tested configurations of the streaming vision-language model OneStreamer-4B, including ones fine-tuned on SurgStreamer's state or on video with an adapted vision encoder, scored at most 0.540 (Holm-adjusted p <= 0.012). At three external centres, re-training only perception raised performance on held-out procedures from 0.239 to 0.470. On a new procedure, pituitary surgery, controller weights trained on cholecystectomy matched an in-domain controller on oracle state (0.947 vs 0.938). On predicted state they missed the pre-registered non-inferiority margin (-0.024 [-0.040, -0.008]) unless the alert thresholds were re-calibrated. The results support separating perception from reasoning and point to perception under distribution shift as the main limitation.

---


### 212. [TEM: Temporal State Tracking Memory for Large Language Model Agents](https://arxiv.org/abs/2610.21900)

**<font color=#1a73e8>作者：</font>** Pengfeng Song, Yunkai Zhuang, Liye Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memory (TEM), a training-free framework for tracking these changes. TEM stores facts as versioned records linked to their sources. It retrieves relevant versions, places them in source order and labels historical records before passing the evidence to the answer model. Event memory and original dialogue turns provide details missing from structured facts. We evaluated TEM on 420 questions drawn from 600 sessions involving 60 personas. Across four open-weight models, key-entity hit rates reached 75.71-97.62% overall and 96.67-100.00% on the historical-residence subset. Adding historical labels to otherwise identical, source-ordered facts increased overall hit rates by 17.14-55.95 percentage points. The evidence was compact: 94-118 tokens per answer, or 48.75-56.73% less than session-aware retrieval-augmented generation (RAG). A further evaluation on 1,540 LoCoMo questions tested hybrid memory under a fixed evidence budget. TEM exceeded session-aware RAG with both backbones; conservative score differences were 7.92 and 10.58 percentage points. The results support preserving fact versions and exposing their temporal status to the generator when answering questions about repeatedly updated information.

---


### 213. [In-Context Learning Before Specialisation: Theory of Learning in a Solvable Topic Model](https://arxiv.org/abs/2610.21901)

**<font color=#1a73e8>作者：</font>** Francesco Cagnetta, Casper L. Christensen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence models can generalise in fundamentally distinct ways: extrapolating structures seen in training, or using their prompt to adapt to novel tasks. The prevailing strategy determines how the model behaves beyond its training distribution, controlling potential capabilities and risks. Recent work has characterised many different strategies theoretically, and empirically described the transition between them as the quality and quantity of pretraining data vary. However, there is no learning theory for this competition, hence no fundamental understanding of \textit{why} one solution might be favoured over another. Here we provide such a theory in a solvable topic model---documents drawn from a finite mixture of latent topics, mirroring the heterogeneity of modern pretraining data. The dataset comes with two distinct solutions: a specialised predictor, that stores the finite topic mixture, and an in-context one, optimal for topics never seen during training. Our theory predicts their emergence at distinct sample complexities: the in-context predictor is available early, while the specialised one emerges only after the training tokens outnumber the parameters of the data-generating process. Trained transformers reproduce both scales and the separating crossover in remarkable agreement with the theory, with no fitted parameters.

---


### 214. [Seeing is Believing: Benchmarking and Mitigating the Interference of Language Priors on Visual Perception in MLLMs](https://arxiv.org/abs/2610.21902)

**<font color=#1a73e8>作者：</font>** Li Ma, Yan Zhuang, Jiawen Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language priors in MLLMs can override visual evidence, impairing visual perception. Existing benchmarks assume shared priors across models and rely solely on accuracy. However, cross-model prior agreement falls below 80%, and over 15% of items can be answered correctly without any image, causing accuracy to overestimate prior resistance. To address these limitations, we introduce ViSiP-Bench, a benchmark grounded in rare-but-real scenarios across six prior categories, with a model-aware dynamic prior induction protocol and three metrics that more precisely and continuously measure prior resistance than accuracy alone. Evaluating 24 models reveals that prior adherence is pervasive, does not improve with scale, and larger models tend to either strongly override their priors or firmly adhere to them. We therefore propose MAPS, which identifies each model's strongest priors and fine-tunes on factually grounded knowledge to soften excessive prior reliance without disrupting general capabilities.

---


### 215. [CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910)

**<font color=#1a73e8>作者：</font>** Dongjie Cheng, Ruifeng Yuan, Ran Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual content as additional evidence. However, existing approaches typically invoke a VWM through fixed pipelines centered on a predefined form of visual imagination, such as novel-view synthesis. To support flexible visual imagination for diverse reasoning tasks, we introduce CoWorld Reasoner, an agentic framework that uses a VWM as a unified visual reasoning engine. Its Video World Model-Driven Harness exposes multiple visual operations through tools and uses skills to guide the VLM in deciding whether to imagine, selecting an operation, constructing a generation request, and interpreting the resulting visual evidence. We further introduce VLM-VWM Harness Co-Evolution, which jointly revises tools, skills, and execution code based on execution feedback while keeping both model weights fixed. Across seven benchmarks spanning spatial intelligence, temporal and causal reasoning, and perceptual reasoning, CoWorld Reasoner outperforms direct reasoning with the same VLM. The strongest variant improves on all seven benchmarks, including relative accuracy gains of 11.8% on MMSI and 13.0% on ERQA, and outperforms all five evolving baselines using the same backbone across five benchmarks.

---


### 216. [Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation](https://arxiv.org/abs/2610.21938)

**<font color=#1a73e8>作者：</font>** Bruno Arcanjo, Zhaoxing Li, Sebastian Stein  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An agent that learns a user's preferences from their choices faces a cold start problem: before any choices are observed, it must rely solely on a prior. Informative priors are usually fitted to historical choice data, which new tasks and deployments lack. To address this, we present Agentic-Priors, which lets agentic systems use the implicit knowledge of large language models (LLMs) instead. Specifically, an LLM states a new user's trade-offs in interpretable terms, such as willingness to pay or value of time, which we map to a prior over multinomial logit coefficients. This prior is then refined by a Bayesian learner as choices are observed. Across seven choice datasets, Agentic-Priors improves cold start accuracy over an uninformed prior by 5-40 percentage points. It also outperforms AutoElicit, a state-of-the-art LLM prior-elicitation method, on three datasets and loses on one. It is up to 18 points more accurate than in-context learning, and never significantly worse. Against hierarchical Bayes models fitted to surveys of increasing size, our approach is worth roughly 6-40 surveyed users, in terms of log-loss, so its value is concentrated in a deployment's first users.

---


### 217. [Inflak: A Unified Orchestration Architecture for Human-Agent Interaction](https://arxiv.org/abs/2610.21972)

**<font color=#1a73e8>作者：</font>** Lin Gao, Li Chen, Jianxun Lian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-powered agents increasingly support open-ended activities, yet orchestrating when and how agents interact with humans remains challenging. Existing approaches often provide interaction mechanisms tied to particular tasks or execution patterns, lacking a unified architecture for diverse and evolving interaction needs. We introduce Inflak, a unified four-layer architecture for human-agent interaction orchestration that separates state reconstruction and routing, interaction and execution planning, interaction design, and interface rendering. Its layered design with progressive resolution enables general applicability, runtime flexibility, module composability, and orchestration maintainability. We implement Inflak as agent-native, skill-based plugins within a general-purpose agent framework and evaluate it through a gallery of various application scenarios and interaction paradigms, technical performance testing, and a comparative implementation case study. The evaluations show that Inflak can serve as a general and extensible foundation for orchestrating diverse human-agent interaction flows.

---


### 218. [OntoAct: Hypothesis-Based Neuro-Symbolic Agents through Ontological Abstraction](https://arxiv.org/abs/2610.21983)

**<font color=#1a73e8>作者：</font>** Donghyeok Lee, Bong Gyun Kang, Junyong Ahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from experience requires recovering reusable knowledge and determining when it applies to a new situation. We introduce OntoAct, a hypothesis-based neuro-symbolic framework built on ontological abstraction. OntoAct turns individual experiences into axioms over entity types, relations, and conditions, making their underlying patterns reusable across situations. A large language model (LLM) uses this world knowledge to propose hypotheses and actions, while a symbolic verifier assesses their supporting conditions against current observations. Verification identifies missing evidence, and new observations and intervention outcomes update hypothesis assessments and guide subsequent actions. We also introduce Tacit-FLE, a benchmark built on the Factorio Learning Environment (FLE) for diagnosing and repairing hidden faults in existing factories using inherited operational records. Its synthetic maintenance corpus distributes evidence across records, and an executed repair may leave the fault unresolved, requiring agents to reassess their diagnoses through interaction. Across Tacit-FLE, Mars, and ALFWorld, OntoAct achieves leading task performance with efficient interaction and inference.

---


### 219. [Visual Sanad: Auditing Vision-Language Models for False Acceptance of Qur'anic Citations](https://arxiv.org/abs/2610.22009)

**<font color=#1a73e8>作者：</font>** Niaz Mohaiman Abtahi, Reyana Shahid, Evan Maksud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to interpret religious, educational, and culturally sensitive visual content, yet their reliability on citation verification remains underexplored. We introduce Visual Sanad, a controlled benchmark for testing whether VLMs falsely accept incorrect Qur'anic verse attributions when the same quote-reference pair is rendered under different visual framings. The benchmark contains 2,400 rendered images built from 100 English Qur'an verses, four factual states per verse, and six visual conditions ranging from plain text to decorative and authority-framed layouts. All quote-reference pairs were source-checked and human-audited before rendering. Across 24 full model-prompt runs, we observe a sharp capability split. Proprietary API-served VLMs range from near-perfect citation verification to moderate false acceptance, whereas recent open-weight VLMs often show weak discrimination and default to VALID on most images. De-biased prompting can reduce false acceptance, but often by shifting the decision threshold toward INVALID rather than by producing strong citation discrimination. Visual Sanad therefore exposes a culturally grounded multimodal factuality failure: fluent VLMs may treat displayed religious citations as self-authenticating unless they have strong citation-verification ability.

---


### 220. [Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches](https://arxiv.org/abs/2610.22016)

**<font color=#1a73e8>作者：</font>** Adam Deng, Shicheng Liu, Yada Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the reading it already did. A growing literature instead transmits the KV cache, the natural carrier of that reading. We study the most appealing form of the idea: both models stay frozen and the sender's cache is substituted for the reader's with nothing trained. It does not work, and the obstruction belongs to the reader. A frozen transformer reads only caches close to the one it would have written itself, a region we call its tolerable set. We show that geometric similarity to that cache does not predict whether the reader can use it, and the failure is not gradual, so a more faithful substitute is not the remedy it appears to be. We explain this phenomenon with competitive attention. Experimentally, we test eight diverse substitution methods against two measured anchors: an uninformative cache baseline and the reader's own accuracy from having read the passage. All sit at the baseline. That turns a long tail of separate negative results into one outcome with a stated condition for overturning it. A different design does work: if the reader keeps its own cache and attends over the sender's as extra context, adapting only its queries, it beats its own baseline, and also clears the baseline with eight senders pooled where undirected attention over the same union falls below it. We offer this as a characterization on one probe, not a leaderboard claim. Our central contribution is a redirection: pursuing faithful substitute caches is the wrong target; adding a cache to what the reader already has is the promising one.

---


### 221. [CARA: Causally Guided Retrieval Agent for Question Answering](https://arxiv.org/abs/2610.22017)

**<font color=#1a73e8>作者：</font>** Weicheng Liu, Xiangcheng Wu, Depeng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation over text-rich knowledge graphs requires identifying evidence that contributes to answering a question, rather than merely matching its textual content. Existing agentic retrievers adaptively balance global search and multi-hop exploration but primarily rely on textual similarity to guide retrieval. We propose CARA, a training-free, CAusally guided Retrieval Agent that explicitly evaluates the causal relevance of retrieved evidence through two complementary criteria: consequentiality, measuring whether adding evidence improves answerability, and essentiality, assessing whether removing evidence weakens answerability. CARA integrates these assessments with path consistency to guide graph exploration and employs reciprocal rank fusion to aggregate evidence from multiple agents. We evaluate CARA on three STaRK datasets and augment STaRK with ground-truth answers to enable downstream question answering evaluation. Experimental results demonstrate that CARA consistently outperforms existing retrievers. CARA also improves answer quality and faithfulness while examining fewer graph nodes and requiring fewer retrieval operations. These findings demonstrate that causal relevance assessment enables more focused and effective agentic graph retrieval, improving both retrieval performance and downstream question answering.

---


### 222. [When Models Misread Ink: Auditing VLMs for Arabic Calligraphy Recognition](https://arxiv.org/abs/2610.22018)

**<font color=#1a73e8>作者：</font>** Niaz Mohaiman Abtahi, Evan Maksud, Reyana Shahid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arabic calligraphy is a high-stakes cultural visual domain for Muslim communities, yet VLM evaluations rarely test its fine-grained script traditions. We audit 12 VLMs on a cleaned 1,195-image six-way benchmark using numeric, visual-cue, and Diwani-first prompts. In this closed-set setting, the best numeric-prompt accuracy is 60.9% for closed/API models and 47.2% for open-weight models. The main failure is default-label collapse: every numeric run is dominated by a single label taking 33-63% of predictions, against an 18.8% majority-class baseline. For 8 of 12 models the default is Thuluth; GPT-4o labels 52.9% of all images as Thuluth although it is only 18.1% of the set. Prompting helps unevenly: visual cues move accuracy by more than 10 points for some models but hurt others, and foregrounding Diwani often relocates the default rather than removing it. Arabic calligraphy recognition is therefore a compact, culturally grounded stress test for VLM robustness and for measuring which visual traditions become legible to automated systems.

---


### 223. [Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe](https://arxiv.org/abs/2610.22019)

**<font color=#1a73e8>作者：</font>** Soumye Singhal, Joseph Jennings, Ka Shun Shum 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier models, general-purpose and domain-specific alike, now include a midtraining stage between pretraining and post-training, but little has been published about how this stage is built. We present an open midtraining recipe that primes base models for agentic post-training, and we show its effectiveness on two Nemotron models of different sizes. Pretraining typically runs at short context and sees almost no agent interactions, while SFT data is mostly synthetic, and very long SFT stages can hurt the model's later RL trainability. Our midtraining stage sits between the two. It trains at 256K context for hundreds of billions of tokens on a diverse mixture of natural software-engineering data like packed repositories, pull requests, commit histories, and build logs together with a small share of agentic traces. On Nemotron 3.5 Lightning, 500B midtraining tokens improve SWE-bench Verified from 60.7 to 64.5, SWE-bench Multilingual from 55.8 to 62.8, and SWE-bench Pro from 32.0 to 35.5 after identical full SFT. On the larger Nemotron 3.5 Super, 280B midtraining tokens improve DeepSWE, a harder benchmark of long-horizon tasks, from 11.7 to 15.7 and SWE-bench Verified from 72.9 to 74.3 after identical full SFT. Midtraining also improves robustness across agent harnesses on both models. We report the ablations behind the recipe and an evaluation protocol built on short fixed SFT runs, since base-model proxy metrics did not correlate reliably with post-training results.

---


### 224. [Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing](https://arxiv.org/abs/2610.22026)

**<font color=#1a73e8>作者：</font>** Adam Deng, Shicheng Liu, Yada Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built from frozen language models communicate through text, which discards the internal state the sender already computed and makes the receiver pay to rebuild it. Work on internal channels avoids that cost, framing the problem as transfer: agent A sends information to agent B. Every agent pair that must communicate needs its own transfer bridge, and every agent added to a system needs a new bridge fitted against each previous agent. We reframe this problem as sharing: an agent publishes its internal state once into a pool, and every peer reads that pool through a single mechanism fitted to no sender in particular, so adding an agent adds a publisher and no new bridge. Whereas the carrier of the internal state and the fusion mechanism are usually chosen independently in the literature, our main finding is that these two choices are coupled; the deciding factor is where the carrier enters the receiver's computation. Consumability is a property of the receiving computation rather than of the representation. We find that the key-value (KV) cache must be augmented rather than swapped in: the receiver cross-attends over a peer's cache while keeping its own, and with only a small query-side adapter trained, matches the accuracy it gets from reading the source document. Activations invert this. They are best written straight into the receiver, with no bridge, no adapter and no training, which beats exposing them alongside the receiver's own, though that advantage rests on knowing where in the receiver the state belongs. The rule is augment the KV cache, replace the activation, established under one protocol with a shared control ladder. One adapter, trained once, also serves publishers it never trained on, and a pool of several at once, but only those whose internal state lies close to the receiver's own.

---


### 225. [Selection Is Not Learning: Choosing Model Futures](https://arxiv.org/abs/2610.22029)

**<font color=#1a73e8>作者：</font>** Haoyi Yang, Kshitij Mishra, Nils Lukas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving language models train on tasks they generate, so every round must decide which updated model the next round inherits. Current loops such as R-Zero, Agent0, and Skill Self-Play make this decision through the task, admitting tasks that look learnable and inheriting every resulting update. We identify a selection-to-update gap in these loops, where a task that looks learnable need not produce a useful update. Most updates on verified tasks fail to make correct answers more likely, yet these loops inherit them all. HeirCommit freezes the updated model and uses fresh evaluation questions to decide whether to inherit it or retain the current model. EvoHeir separates parameter inheritance from experience inheritance, using current and archived experience to repair failures and preserve successes before final confirmation. Our analysis characterizes selection-induced optimism and decomposes regret into selection, absorption, and confirmation errors. HeirCommit cuts the harmful share of accepted updates by 68-83% relative to random inheritance at the same acceptance rate. Across four backbones, EvoHeir achieves the best mathematics and general-reasoning averages, raising the math average by 5.3% relative to the strongest baseline, Agent0. The framework lets useful experience persist even when the model that produced it is not inherited.

---


### 226. [GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents](https://arxiv.org/abs/2610.22031)

**<font color=#1a73e8>作者：</font>** Yaxin Ma, Wenbo Zhang, Satya Krishna Pothapragada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral consistency across repeated executions provides an informative signal for assessing the reliability of large language model (LLM) agents. However, existing approaches typically summarize consistency with a single task-level score, without identifying where behavioral differences occur or whether actions are compared under equivalent decision contexts. We propose a graph-based framework for fine-grained behavioral consistency measurement and uncertainty quantification. Given multiple rollouts of the same task, we merge equivalent states into a directed, action-labeled graph, enabling action comparisons at shared decision states. We introduce node-level and global measures of action consistency, using the global consistency score as a proxy for uncertainty to predict task success or failure. Experiments across three LLMs on ALFWorld, AppWorld, and WebShop demonstrate that our measure is positively associated with task success and achieves an average AUROC of 0.811 for task-success prediction, outperforming the strongest behavioral-consistency baseline (0.729) and verbalized confidence (0.769). These results highlight the effectiveness of state-conditioned behavioral consistency and pinpoint where agent actions agree.

---


### 227. [Momentum, Commentary Tone, and Earnings Surprise in LLM Financial Forecasts](https://arxiv.org/abs/2610.22043)

**<font color=#1a73e8>作者：</font>** Alina Khaybullina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which inputs drive a language model's financial forecast? We construct synthetic earnings announcements that independently reverse 20-day momentum, non-informational commentary tone, and whether fixed actual EPS beats a manipulated consensus. Six instruction/chat checkpoint conversions from four families (0.49-7.61B base parameters) receive 2,016 prompts each under a direct-answer Q8_0 protocol. The design includes 24 numerical blocks, six commentary pairs, profits and losses, rising and falling annual EPS, and two surprise sizes. Both A/B answer assignments and U/D cover all 384 primary scenarios per conversion. We estimate matched changes in conditional answer-prefix scores, not calibrated market probabilities. Across these checkpoints, the primary EPS contrast ranges from -0.19 to 86.80 percentage points. The magnitude of the primary signed tone contrast exceeds that of EPS in 5 of six models, and momentum exceeds it in 5. Natural-word numerical diagnostic accuracy ranges from 51.0 to 95.8 percent. Answer-encoding, wording, context, and conversion controls qualify these results. The experiment measures observable input reliance and numerical recognition; it establishes neither an internal reasoning mechanism nor realized return predictability. Public benchmark prompts, recorded scores, and an interactive recorded-results explorer accompany the study.

---


### 228. [Name-Bias in Large Language Models](https://arxiv.org/abs/2610.22053)

**<font color=#1a73e8>作者：</font>** Kalyan Bhetwal, Ceren Mert, Ian Whitehouse  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Names carry demographic indicators such as age, gender, and race, which makes them a subtle but strong target of bias in large language models (LLMs). In this work, we present an evaluation of name-based bias across 6 local large language models spanning multiple providers and parameter scales. Using a fill-in-the-blank task, we prompt these models to choose between pairs of first names drawn from U.S. Social Security Administration datasets and a race classification dataset by Rosenman et al.. Our experimental de- sign isolates age and gender effects through balanced name pairings and sentence templates that share a fixed syntactic structure. Across 300,000 local LLM responses, we find consistent and measurable name bias. Models prefer names that are less stereotypically male, older, popular, and white. Furthermore, we find that name-bias is highly sentence-dependent, but not more than associated stereotypes, and gender is the most significant bias, followed by age, name popularity, and race. Our results demonstrate that name-based bias remains pervasive even in local LLMs, highlighting the necessity for standardized evaluation methods and mitigation strategies.

---


### 229. [Progress Reward Model for Reinforcement Learning via Large Language Models](https://arxiv.org/abs/2610.22056)

**<font color=#1a73e8>作者：</font>** Xiuhui Zhang, Ning Gao, Xingyu Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional reinforcement learning (RL) algorithms face significant limitations in handling long-term tasks with sparse rewards. Recent advancements have leveraged large language models (LLMs) to enhance RL by utilizing their world knowledge for task planning and reward generation. However, planning-based approaches often depend on pre-defined skill libraries and fail to optimize low-level control policies, while reward-based methods require extensive human feedback or exhaustive searching due to the complexity of tasks. In this paper, we propose the Progress Reward Model for RL (PRM4RL), a novel framework that integrates task planning and dense reward to enhance RL. For high-level planning, a complex task is decomposed into a series of simple manageable subtasks, with a subtask-oriented, fine-grained progress function designed to monitor task execution progress. For low-level reward generation, inspired by potential-based reward shaping, we use the progress function to construct a Progress Reward Model (PRM), providing theoretically grounded optimality and convergence guarantees, thereby enabling effective policy optimization. Experimental results on robotics control tasks demonstrate that our approach outperforms both LLM-based planning and reward methods, achieving state-of-the-art performance. Code is available at this https URL.

---


### 230. [Prism-1: Position- and Rival-Independent Scoring for System One Models](https://arxiv.org/abs/2610.22066)

**<font color=#1a73e8>作者：</font>** Yao Long Teng, Jianguo Huang, Yanchen Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given a state and a set of options, such as intents, tools or interface elements, System One decision models return a distribution over the options in one forward pass, without generated reasoning. Web systems increasingly build them by reading decisions from language models. Two axioms of rational choice are natural requirements for such decisions, because in web systems the listing and the option set are determined by other components and can change or be manipulated: the order in which the options are listed should not matter, and adding an option should not change the relative odds of the others (Luce's choice axiom). We test the standard reads, namely single-choice question (SCQ) prompting, with shuffled-order training, order averaging or sorted options, and invariant set architectures, and find that each violates at least one axiom: one shuffle changes 12-20% of SCQ answers, sorting only freezes an arbitrary convention, and a well-chosen added option steers 4-34% of decisions. By Luce's theorem, a read satisfies both axioms only if it is a softmax over scores that each depend on one option alone, so in a transformer they hold by construction only if no token that scores an option sees another. We implement this as Prism-1 (Position- and Rival-Independent Scoring for System One Models): every option is read in its own block at shared positions, with the model's usual left-to-right attention, in one forward pass. On five benchmark sets with Qwen3-8B and Gemma 4 12B, SCQ prompting trained on the same data still changes 7% of its answers under one shuffle, and an added irrelevant option steers 12% of its decisions. Prism-1 stays within one point of that baseline's accuracy and is 2-4 points more accurate once only answers that survive a reordering are counted, while no shuffle changes any of its answers and no added irrelevant option moves its choice among the others.

---


### 231. [Beyond Context Length: Characterising the Difficulty of Long-Context Reasoning](https://arxiv.org/abs/2610.22067)

**<font color=#1a73e8>作者：</font>** Shiwen Qin, Cameron Barker, Henry Gouk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models support ever longer context windows, and evaluations typically treat context length as the main indicator of difficulty. However, context length alone cannot explain why models fail on long-context tasks that require reasoning over complex information. Contexts of equal length can pose very different challenges: a task may be solvable from a single local passage, or it may require integrating evidence distributed across the full context. We quantitatively characterise this difficulty through three properties: evidence scope, how much necessary information must be found; evidence dispersion, how widely that information is scattered within the context; and reasoning depth, how many dependent steps are needed to derive an answer from it. We construct LURCH, a multi-domain question-answering benchmark of 6,550 instances with supporting evidence and reasoning graphs, enabling all three properties to be quantified. Evaluations of proprietary and open-weight models show that: (1) at fixed context length, all our three properties are strongly negatively correlated with model performance; (2) as context length increases, performance degrades sharply on samples with dispersed evidence, whereas it remains relatively stable on samples with localised evidence; and (3) difficulty compounds across properties, as questions with moderately high values on all three are harder than those with an extreme value on just one. These findings establish evidence scope, dispersion and reasoning depth as measures of long-context reasoning difficulty that complement context length.

---


### 232. [When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models](https://arxiv.org/abs/2610.22068)

**<font color=#1a73e8>作者：</font>** Wei Cai, Jian Zhao, Yuchen Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can act unsafely when individually benign images and texts are interpreted jointly. Beyond implicit reasoning risk, where reasoning drifts toward harm, we identify intent-level risk, where cross-modal ambiguity silently commits the model to a hazardous premise that path-level optimization alone cannot correct. We propose SAFE-PRO, which uses a Risk-Conditioned Uncertainty (RCU) signal, combining predictive entropy with a learned cross-modal risk score, to decide when to ask safety-grounded clarifying questions and where to apply path optimization, under a reward that prioritizes safety and penalizes over-refusal. We also build SSUI-Dialog, a multimodal multi-turn dataset with dual-intent supervision, and theoretically analyze gradient variance and unsafe-completion risk under RCU. Across seven benchmarks and two base MLLMs, SAFE-PRO consistently improves safety over SRPO, roughly halves its over-refusal, and surpasses GPT-4o and Claude-3.5-Sonnet in average single-turn safety.

---


### 233. [Memory as Weights: Internalizing Long-Term History for Streaming Videos](https://arxiv.org/abs/2610.22070)

**<font color=#1a73e8>作者：</font>** Zhuoming Liu, Jinhong Lin, Lin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming vision-language models (VLMs) must continuously integrate information from the past while remaining responsive to current observations and user queries. Existing memory mechanisms typically compress, retrieve, or cache historical observations and reintroduce them into the input context, forcing historical memory and current observations to compete for limited context. We propose MaLoW, a streaming memory framework that instead internalizes historical context into evolving lightweight parameter updates. MaLoW uses a recurrent HyperNetwork to incrementally consolidate incoming video observations into fixed-size LoRA weights, allowing historical information to be carried forward without revisiting the full video stream. In doing so, MaLoW represents history as weights, while keeping the current observation as input. To support training, we further construct MaLoW-Instruct, a large-scale streaming video dataset containing 381K question-answer pairs over 56K videos. We conduct extensive experiments to demonstrate that MaLoW achieves strong performance on OVO-Bench, StreamingBench, and StreamArena. On the backward split of OVO-Bench, MaLoW outperforms prior memory approaches by 3.9% to 11.8% across different video backbones while incurring only modest latency overhead. Beyond streaming video understanding, MaLoW also generalizes to vision-language-action models, improving the action success rate on Simpler WidowX by 9.3%.

---


### 234. [The Right Byte First: How UTF-16 Helps Multilingual Boundary Prediction](https://arxiv.org/abs/2610.22071)

**<font color=#1a73e8>作者：</font>** Hyunsik Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many hierarchical byte-level language models group bytes into patches using a learned boundary predictor whose view of the next codepoint depends on encoding and lookahead. In UTF-8, codepoints of many scripts take three bytes: 8 of 24 bits mark length and continuation, and the first byte carries only 4 high codepoint bits. After the same left context, a mark extending a grapheme cluster and a letter starting the next can thus share their first byte. Universal Byte-Level Encoding (UBE) keeps one- and two-byte UTF-8 encodings but writes these codepoints as two UTF-16 bytes, low byte first, so its first symbol carries 8 low codepoint bits that can distinguish such continuations. We train small causal predictors on matched FineWeb-2 text and evaluate on FLORES-200 under UTF-8, UBE, and UBE's same-length big-endian variant. At one-symbol lookahead, balanced grapheme-boundary error at codepoint boundaries across 17 languages in 13 Brahmic scripts is 8.76% with UTF-8, 8.62% with the big-endian variant, and 0.06% with UBE. When the target instead retains a parent tokenizer's subword cuts at grapheme boundaries, UBE lowers the mean error relative to UTF-8 at the same lookahead by 72.91% in Korean, 35.29% in Chinese, and 67.32-99.55% in eight more scripts. In the seven of them whose main Unicode block fits on one 256-codepoint page, the big-endian variant stays within 3.0% of UTF-8, so the gain follows byte order, not length. In Korean and Chinese, UBE's mean error falls below UTF-8's final mean error after only 25% and 37.5% of training. Which byte comes first thus affects how much lookahead a byte-level boundary predictor needs.

---


### 235. [Retrofitting Recurrent Vision-Language Models from Pretrained Backbones](https://arxiv.org/abs/2610.22075)

**<font color=#1a73e8>作者：</font>** Madhav Iyengar, Andreas Geiger, Hilde Kühne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work shows that depth recurrence can be retrofitted into pretrained language models. In this work, we adapt this paradigm for visual understanding, using depth recurrence to reduce the parameter footprint of a pretrained vision-language model (VLM). To this end, we prune layers from the language backbone of the VLM and loop over a subset of the remaining layers. At each step of the loop, a linear adapter merges the block's output with the token representations from the preceding layers and projects the fused representation back into the block. As the pruning impacts the original model performance, we propose a three-stage recovery training: first, we leverage a language-only pretraining to recover the performance of the language backbone, followed by an alignment of the vision-language projector, and a full fine-tuning of the model via visual instruction tuning. In the first and the last stage, we distill the outputs of the pretrained non-recurrent model into the recurrent model, which further improves the recovery. We evaluate the proposed approach on the TinyLLaVA-1.4B backbone without introducing any new vision-language data during retrofitting. Our experiments demonstrate that the retrofitted recurrent model outperforms the unpruned baseline trained with the same recovery data while storing 23.3% fewer language parameters. We further show that the proposed retrofitting recurrence outperforms the setup of converting a recurrent LM into a VLM on the same data. Additionally, our ablations show how design choices, such as the adapter between recurrences and a larger recurrent block, lead to the improved performance of our approach. Finally, we find that our proposed model gains on reasoning-oriented benchmarks, whereas its performance on basic visual understanding benchmarks remains on par with the baseline.

---


### 236. [Learning from Unverified Peers via Shared Residual Distillation](https://arxiv.org/abs/2610.22080)

**<font color=#1a73e8>作者：</font>** Feiyang Chen, Runze Ma, Zichen Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A language model can generate several solutions to the same problem, some leading to correct answers and others to incorrect ones. Many post-training methods turn these trajectories into learning signals using supervision from reference answers, verifiable feedback, or external teachers. Without such supervision, learning from the model's own generations becomes less straightforward, as their correctness cannot be reliably assessed. An incorrect solution may nevertheless contain useful intermediate reasoning, so its value as supervision need not be determined solely by its final answer. Can a model improve by learning from its unverified peer solutions without first determining which are correct?
We propose Shared Residual Distillation (SRD), an on-policy self-distillation method that learns from the model's own unverified peer trajectories. SRD compares how peers change the prediction distribution relative to a control, retaining adjustments that agree in direction and are conservative in magnitude. This yields supervision without treating any complete solution as correct, and the trained model requires no peers at inference time. Starting from the corresponding base models, SRD raises mean AIME24--26 avg@12 from 11.02 to 16.20 on Qwen3-1.7B, from 19.07 to 45.46 on Qwen3-4B, and from 21.39 to 54.44 on Qwen3-8B. Controlled ablations support the value of the shared-residual construction, and we observe no degradation relative to the base models on two general-capability benchmarks.

---


### 237. [Multi-SFT: Permissively-Licensed Multilingual Instruction-Following](https://arxiv.org/abs/2610.22086)

**<font color=#1a73e8>作者：</font>** Daniela Baiamonte, Kamyar Zeinalipour, Elena Fano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning datasets remain overwhelmingly English-centric and commercially restricted, as their content is frequently generated by proprietary models whose terms of service forbid training competing systems. We introduce Multi-SFT, a commercially permissive collection of 502,818 instruction-response pairs across five European languages, built via translation and regeneration pipelines for tasks where translation is insufficient. Human evaluation yields inter-annotator agreement of at least 0.87 across all datasets and languages. Fine-tuning nine models from three different families (EuroLLM, OLMo 2, Qwen3; 1B-32B) and evaluating them on 13 benchmarks shows that Multi-SFT alone is competitive with larger augmented mixes and official instruction-tuned releases, with decisive advantages on safety tasks.

---


### 238. [TIPS: A Tiny Inference-time Policy for Scaling in Diffusion Language Models](https://arxiv.org/abs/2610.22099)

**<font color=#1a73e8>作者：</font>** Ya-Shi Zhang, Jian Tang, Pierre-André Noël 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models expose an inference-time choice: which positions become visible after each denoising pass. Many existing decoding methods use hand-designed rules or require visibility to grow monotonically. We present a $\textbf{T}$iny $\textbf{I}$nference-time $\textbf{P}$olicy for $\textbf{S}$caling ($\textbf{TIPS}$), an approximately $600$K-parameter controller that learns both unmasking and remasking while keeping the underlying language model frozen. TIPS uses visibility-aware confidence features and a shallow transformer to select which tokens should be visible, while a fixed schedule controls the expected visible fraction. We train the controller through supervised warmup followed by reinforcement learning from terminal correctness rewards. On GSM8K and MATH-500 with LLaDA-8B-Instruct, the full-canvas and two-block TIPS variants achieve $58.46\%$ and $57.97\%$ micro-averaged accuracy at a budget of $32$ decoder evaluations, exceeding the strongest baseline in our main comparison by $12.1$ and $11.6$ percentage points, respectively. Both variants are trained at a budget of $32$ evaluations and remain competitive at higher budgets without retraining. These results demonstrate that learning when to reveal and reconsider tokens can improve the accuracy-compute trade-off without updating the decoder backbone.

---


### 239. [Patch where the text is new: a compression view of where byte-level models should spend compute](https://arxiv.org/abs/2610.22100)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level language models such as the Byte Latent Transformer (BLT) run their large global model once per patch and start a patch where a small model's next-byte entropy is high. This rule rarely starts a patch at in-line computed results, such as the number after "=" in a worked solution, and accuracy on them collapses under tight patch budgets. We propose novelty patching, motivated by LZ77-style compression: start a patch where the upcoming bytes are unlikely to repeat the recent context. The rule is a lookup table over the previous two bytes, fitted in seconds on raw text with no labels, reference model or losses. In BLT-style models trained from scratch on a 1.9 GB math corpus at a matched ~11% patch rate (3 seeds each), it has no clear effect at 1M parameters, raises final-answer accuracy from 47% to 72% at 12M, and at 50M raises computed-result accuracy from 21% to 57% and final-answer accuracy from 60% to 90%; a table fitted on the raw pretraining corpus keeps the gain. Outside math the advantage shrinks: novelty lowers bits per byte on prose and ties entropy on source code and on synthetic execution traces. An analysis of where boundaries fall explains the pattern. Computed results have ordinary surprisal for the patcher's model, so surprisal-seeking rules pass over them: entropy concentrates patch starts on high-surprisal bytes most strongly of all rules (boundary enrichment 1.61) and is the worst on computed results, while the best rules sit near chance enrichment. Novelty works where new content begins at segment starts close to the computation, as in written math; a learned chunker (H-Net) finds such structure on its own, in math and in code. We also report what did not work: typed uncertainty as a training rule, switching rules after training, and a context-aware novelty predictor.

---


### 240. [PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents](https://arxiv.org/abs/2610.22124)

**<font color=#1a73e8>作者：</font>** Kshitij Mishra, Abhijith Sharma, Nils Lukas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful generations, but neither tests whether agents comply with predefined policies during otherwise valid tool use. Such policy violations are difficult to audit because their effects may emerge only after several turns, span multiple tool calls, or surface in downstream systems. We propose PROBE (Policy Rule Observation via Behavioral Exploration), an algorithm for training LLM-based auditors that interact with deployed agents as realistic users and probe them for policy violations through multi-turn, tool-mediated dialogue. We formalize agent auditing as a two-player Markov game and propose a composite reward that balances violation discovery, behavioral plausibility, conversation progress, and policy diversity. To study training objectives and reward design, we compare GRPO, DPO, and GFlowNet-based optimization in a controlled setting. Across extensive experiments, auditors trained with PROBE uncover substantially broader and higher-yield policy violations than same-architecture zero-shot adversaries, even when the auditor is significantly smaller than the target agent. Our results show that multi-turn behavioral auditing is a distinct and necessary axis of agent evaluation, complementing capability and safety benchmarks. PROBE offers a scalable path toward automated policy auditing for real-world agentic systems and suggests a co-evolutionary loop in which auditors expose failures and agents improve from auditor feedback.

---


### 241. [Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization](https://arxiv.org/abs/2610.22127)

**<font color=#1a73e8>作者：</font>** Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalization of Large Language Models (LLMs) is increasingly important for user-centric applications, yet prior methods mainly adapt dense LLMs, whose polysemantic neurons, each encoding multiple unrelated concepts, hinder localizing the components behind personalization, and thus understanding and controlling it. We propose to personalize Mixture-of-Experts (MoE) LLMs, which sparsely route each token to a few specialized experts, reducing polysemanticity and enabling such localization. We adapt three open-weight MoE LLMs on a large-scale personalization dataset and train crosscoders on paired activations of the personalized and non-personalized models to learn interpretable personalized latents, from which we identify the experts encoding distinct personalization features. The personalized MoE LLMs perform competitively with dense LLMs while activating only a fraction of their parameters, exhibit lower polysemanticity than dense LLMs with similar active parameters, and, within the same model family, yield personalized latents that are less shared with the non-personalized model. Causal interventions show that these latents suffice to recover the personalized model's behavior and that boosting their associated experts moves the non-personalized model toward it, revealing distinct routing paths for different personalization features.

---


### 242. [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](https://arxiv.org/abs/2610.22130)

**<font color=#1a73e8>作者：</font>** Aozhong Zhang, Selcuk Gurses, Yanxia Deng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trade-off: the underlying optimization for minimizing output perturbation is an NP-hard combinatorial problem, leading to mathematically suboptimal heuristics or implementations that are difficult to kernelize. In this work, we propose DropKV, a simple principled eviction framework based on Decoupled Residual-Output Perturbation. By decoupling the joint eviction decision into independent per-token scoring, DropKV circumvents combinatorial intractability and admits a provable constant-factor approximation guarantee under a cone condition that we empirically verify on three long-context LLMs. To ensure practical viability, we provide a high-performance implementation using fused Triton kernels that avoid materializing the full attention matrix, delivering a 19.8x scoring-kernel speedup that translates to up to a 9.9% matched-batch end-to-end prefill speedup. Extensive evaluations on the RULER and LongBench benchmarks demonstrate that DropKV consistently outperforms state-of-the-art baselines at equivalent cache budgets, achieving the lowest inference latency among eviction methods while also remaining faster than the dynamic cache baseline.

---


### 243. [Intern-Decision: Efficient Multimodal Decision Making with Autoregressive Masked Language Modeling](https://arxiv.org/abs/2610.22131)

**<font color=#1a73e8>作者：</font>** Tong Zhu, Zhe Xu, Zefeng He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactive agents repeatedly choose among a finite set of actions, labels, or ordinal outcomes. Generating a free-form response for each choice adds latency and complicates the interface between a model and its environment. We present Intern-Decision, a family of 0.8B, 2B, and 4B multimodal decision models that return structured choices and candidate probabilities from text and optional images. Our autoregressive masked language modeling objective places one decision placeholder per field in a complete assistant JSON skeleton. Ground-truth symbols appear only in supervision, while all fields are evaluated in a single causal forward pass using the backbone's native language-model head. The 4B model achieves a 90.02% unweighted average accuracy across seven evaluation suites, compared with 88.74% for Jev v1.13.0. For a fixed 289-token request with three fields on one RTX 4090, mean latency is 44.16 ms for the 4B model and approximately 33--34 ms for the smaller models. On a separate 96-case known-distribution pilot, temperature scaling reduces expected multiclass Brier from 0.628 to 0.550 and expected calibration error from 0.213 to 0.089. A confidence-based handoff study on 111 public Jevbench-Hard items improves accuracy from 82/111 (73.87%) to 97/111 (87.39%) by routing 42 items to Atria-Dawn-Preview. We also describe qualitative game, visual interface, and browser demonstrations. These results support compact decision models as a practical component of larger agent systems.

---


### 244. [CART: Compatible Routing for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2610.22137)

**<font color=#1a73e8>作者：</font>** Ling-Xiang Zhang, Tao Hu, Da-Wei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world applications often require them to continually acquire new capabilities from sequential tasks, i.e., Multimodal Continual Instruction Tuning (MCIT). In typical MLLMs, a projector is employed to align visual representations with the language model. However, existing methods primarily protect the language model from forgetting while continuously updating the projector across tasks. Such asymmetric adaptation can cause substantial representation drift in the projector, increasing the mismatch between the projector and language model and consequently exacerbating catastrophic forgetting. To address this issue, we propose Compatible Routing (CART), which explicitly coordinates the adaptation of the projector and language model. Specifically, CART maintains task-specific experts for both modules and combines them through weighted mixtures. CART jointly infers their weights by considering both expert relevance and cross-module compatibility, thereby promoting coordinated adaptation between the two modules. To further control model growth, we introduce relevance-guided expert consolidation, which merges experts exhibiting similar relevance profiles across samples within each module. Extensive experiments demonstrate that CART achieves state-of-the-art performance.

---


### 245. [Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions](https://arxiv.org/abs/2610.22138)

**<font color=#1a73e8>作者：</font>** Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round we probe each benign agent's private answer through a separate call whose response is hidden from its peers, and we separately label its public stance toward the claim. Across six models and three factual-QA datasets, groups remain stable without an attacker: only 0.6% of benign agents finish with the false answer. A single adversarial agent increases this rate to 44.8% and three to 60.5%. Studies of conformity typically report public agreement without private change; we find the reverse. With three adversarial agents present, benign agents hold the false answer in 51.6% of exposed turns but publicly endorse it in only 19.7%. Much of the influence therefore remains invisible in the discussion, and the false answers persist when agents are asked for their own views. Agents that retain the true answer often fail to defend it; once adopted, the false answer spreads among benign agents, and baseline knowledge does not predict robustness.

---


### 246. [Are You Sure Your LLM Is Sure? Repairing and Auditing Confidence](https://arxiv.org/abs/2610.22139)

**<font color=#1a73e8>作者：</font>** Arijit Dey, Bhartendu Kumar, Ramya Hebbalaguppe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Confidence scores determine whether an LLM answer is accepted, reviewed, or regenerated, yet scalar recalibration can only correct errors visible through the score itself. We introduce RADAR (Repair, Adopt, and Diagnose After Recalibration), a reliability framework that separates confidence repair from deciding whether to deploy the repair and auditing the errors that remain. Under squared loss, we decompose prediction risk into outcome noise, information hidden by the score, and mapping error; restricting repair to order-preserving maps additionally introduces a pooling gap. For repair, we propose Probe-Anchored Isotonic Calibration (PAIC), which learns a monotone map from correctness-probe predictions on unlabeled target prompts. PAIC's excess risk depends on the probe's score-conditional bias and fitting error rather than its overall accuracy. For adoption, we derive a paired procedure with finite-sample control of false improvements. For auditing, we develop a prompt-clustered kernel test that detects feature-aligned residual errors while accounting for dependent answers from the same prompt. Across multiple LLM checkpoints, benchmarks, and distribution shifts, richer predictors can improve confidence estimation, but projecting their information back to a scalar score can lose these gains, and lower prediction risk need not yield better review decisions. Across 47,400 replayed raw-score allocations, paired betting adopts candidates with lower held-out test risk in 42.95% of allocations, versus 15.09% for one-sided empirical Bernstein. RADAR thus provides a principled workflow to repair what a scalar score can express, adopt a repair only when supported by evidence, and diagnose systematic errors that recalibration leaves behind. Code and data will be released upon acceptance.

---


### 247. [RAG-RST: Retrieved Exemplars as In-Context Discourse Schema for RST Parsing](https://arxiv.org/abs/2610.22150)

**<font color=#1a73e8>作者：</font>** Mohammadreza Sediqin, Shlomo Engelson Argamon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Rhetorical Structure Theory (RST), each edge of a discourse tree carries a nuclearity label, marking which span holds the central content, and a relation drawn from a closed inventory of functional categories. Neither label is a surface property: the same two clauses can be Elaboration or Background depending on rhetorical intent, and the boundary between them is fixed by annotation convention rather than by lexical cues. Predicting these labels therefore requires a formal discourse schema, and exposure to discourse-rich pretraining text does not supply it: given only a target EDU pair, a strong LLM recovers nuclearity at 0.794 F1 and relation at 0.738 F1. We propose RAG-RST, a retrieval-augmented framework that supplies this schema as in-context demonstration rather than through parameter updates, raising nuclearity to 0.846 F1 and relation to 0.788 F1 with no training. Two configurations are compared: a precomputed strategy that labels all EDU pairs before parsing, and a dynamic strategy that retrieves at each reduce step, so that the exemplars reaching the generator depend on the reductions the parser has already committed to. Both outperform existing RST parsers across span, nuclearity, relation, and full tree metrics, with the dynamic variant consistently strongest. Two properties of the retrieved schema emerge: its utility is bounded in number, saturating and then declining beyond fifty exemplars, and it depends on structural position. Both indicate that a formal linguistic schema can be supplied to a foundation model as a demonstration rather than trained into its parameters.

---


### 248. [PremiseSQL: Evaluating Premise Critique and Abstention in Text-to-SQL Systems](https://arxiv.org/abs/2610.22158)

**<font color=#1a73e8>作者：</font>** Shuo Lin, Jinzhe Li, Chenlu Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have substantially improved Text-to-SQL performance, yet existing NL2SQL systems largely assume that user queries are valid and answerable. As a result, models often generate executable SQL even for queries with flawed premises. We introduce premise critique ability in NL2SQL, namely the ability to recognize flawed queries and abstain from generating misleading SQL. To evaluate this capability, we propose PremiseSQL, a benchmark containing 1,800 flawed NL2SQL queries across four categories of premise failures, along with their 1,800 original queries. We further design an evaluation framework to measure intrinsic and prompt-induced premise-aware behavior across three prompting settings. Experiments on frontier LLMs show that current models are strongly premise-trusting by default and rarely critique flawed premises. Stronger critique-oriented prompting improves detection and abstention on flawed queries, but also increases false invalid judgments and suppresses SQL generation on originals. The code is available at this https URL.

---


### 249. [EMO: A Closed-Loop Test-Time Computation Framework via Alternating Context Optimization and Logits Steering](https://arxiv.org/abs/2610.22160)

**<font color=#1a73e8>作者：</font>** Wei Xia, Yehui Tang, Zhi-Hong Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time context optimization adapts frozen language models through textual feedback, but ordinary conditional generation provides no separate control over how strongly to reinforce the distributional changes induced by a context update. We introduce EMO, a training-free framework inspired by expectation--maximization that alternates question-specific context estimation (E-step) and distribution refinement (M-step). The E-step revises a system context using textual gradients from an external judge without access to gold answers. The M-step contrasts next-token distributions under the revised and preceding contexts at a shared prefix to construct a confidence-constrained logit correction. Feedback on the steered response drives the next context update, coupling adaptation across rounds with intervention within each generation. Theoretically, we connect parameter and context optimization through a shared target-KL objective and additive logit representations, and derive the steering vector from context-induced logit displacements. Under context-improvement and faithful-steering assumptions, we prove a one-round decrease in target KL divergence for sufficiently small steering strength. Under greedy decoding across eight models and six benchmarks, EMO improves the zero-shot baseline in 39 of 40 aggregated settings, averaging $+9.10$ percentage points. With the same judge, it adds $+1.53$ points on average over context-only optimization (TextGrad), with consistent MMLU-Pro gains across models. At matched target-model generation budgets, accuracy advantages over best-of-$N$ are strongest on Llama, while oracle coverage is higher in most comparisons despite fewer candidates. The coverage--selection gap motivates allocating test-time computation jointly to candidate generation and verification.

---


### 250. [Multi-sourced AI Tutor for Non-Native English Speaker Students](https://arxiv.org/abs/2610.22163)

**<font color=#1a73e8>作者：</font>** Yiyin Shen, Xinyi Ai, Weibing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being adopted as teaching tools in computing education, particularly for developing AI tutors capable of answering student questions. With the rise in enrollment of international students in computing programs, researchers have begun to explore the difficulties that non-native English speaker (NNES) students face in computing courses due to language barriers. To aid such students, we developed a general-purpose AI tutor system that can process student questions in foreign languages (currently focused on Mandarin) and provide bilingual responses. Our system also incorporates the functionality of generating a glossary of technical terms and their explanations to enhance comprehension. Our approach utilizes a specialized Retrieval-Augmented Generation (RAG) pipeline with a novel question extraction mechanism, enabling us to effectively utilize a diverse array of course materials for answering student queries. We evaluated our AI tutor using 91 Piazza posts, demonstrating that it could answer 83.52% of the posts correctly and in a helpful manner. The tutor also provided high-quality translations for 76.92% of the questions and generated technical term glossaries for 64.47% of them. Our findings underscore the potential of multi-source RAG pipeline in enhancing AI tutor systems, offering support for non-native speakers that are challenging to provide with traditional supporting staff of a computing course.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
