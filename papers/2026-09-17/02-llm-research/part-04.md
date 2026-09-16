# 🧠 大模型相关研究 | 2026年09月17日

> 本类共 **189** 篇论文：已确认 **180** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

---

### 151. [Probe-VAD: Ordinal Likelihood Probing for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2609.17211)

**<font color=#1a73e8>作者：</font>** Jiawei Gu, Qilin Zhao, Tengkuo Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) aims to localize anomalous events in untrimmed videos. Vision-language models (VLMs) provide rich visual understanding for training-free VAD, but existing approaches impose restrictive interfaces between visual understanding and anomaly scoring. Caption-based pipelines compress visual evidence into text, potentially discarding subtle cues, while direct numerical generation forces the model to express its judgment through a small set of predefined scores. Such interfaces can obscure subtle differences in anomaly severity, causing visually distinct clips to receive similar representations or scores and thereby limiting the resolution of anomaly ranking. We propose \textbf{Probe-VAD}, an ordinal binary-probing framework that directly probes severity preferences from a frozen VLM. Given raw video clips, Probe-VAD queries ten ordered severity thresholds and extracts constrained \textit{YES}/\textit{NO} continuation likelihoods. Their normalized preferences form a cumulative severity profile, from which tail evidence is aggregated into a continuous anomaly score, with isotonic projection enforcing ordinal consistency. Experiments on public VAD benchmarks demonstrate superior performance with low computational cost. Probe-VAD provides a simple interface for translating frozen VLM visual understanding into continuous, rank-sensitive anomaly scores without task-specific training or caption-based compression. Code is available at: this https URL.

---


### 152. [Easy to Catch a Liar, Hard to Clear an Honest One: Language Models Diagnosing a Corrupted Reward Channel from a Verified Record](https://arxiv.org/abs/2609.17226)

**<font color=#1a73e8>作者：</font>** Arman Nik Khah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An agent that learns from rewards has to trust whatever reports those rewards. When the reports suddenly change, either the world changed or the reporter broke. From the reports alone these are indistinguishable, and reinforcement learning theory shows that no amount of further experience separates them. The prescribed escape is richer data about the reporter itself. We ask whether a frozen language model, handed exactly that data, uses it. We build a two-option game in which a payout swap and a lying reporter produce byte-identical histories. Then we add one verified record: an independent check of one round's real result, printed beside what the reporter said about that round. That single line settles the case. We ask three large models, from two families, to answer one question with one letter. Is the reporter honest or lying? They catch a lying reporter almost perfectly. At the 70B class that holds in every condition we tried; the 32B model slips in one wording. They clear an honest reporter far less often, and how often depends on things that should not matter. Averaged over rounds, letters, and wordings, a 72B model calls an honest reporter a liar 38% of the time when nothing has changed at all, and 58% of the time when the payouts moved. A 70B model from a second family calls an honest reporter a liar 26% and 48% of the time. The failure is not one of reading, because in the situation where nothing changed the same models score 0.96 to 1.00 with the answer printed in the prompt. Which surface feature drives it differs by family. For the Qwen models it is which round the record names, and for Llama it is which letter stands for "honest." Adding the record to a prompt that already states the answer makes Llama less likely to give that answer. We had registered a prediction for that 58% before the run: 35%. The failure is larger than we expected.

---


### 153. [ECHO: Early-layer Collaborative Hierarchical Orchestration with Bonus Logits in Speculative Decoding](https://arxiv.org/abs/2609.17241)

**<font color=#1a73e8>作者：</font>** Ziyang Ma, Zihong Zhang, Zuchao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While draft-model-free speculative decoding offers a promising path to efficient LLM inference, it is frequently constrained by stale draft candidates and the high computational cost of the verification. To address these challenges, we propose ECHO, a hierarchical dual-loop framework that exploits the functional asymmetry between LLM layers. Leveraging the high discriminative efficiency of early layers and the authoritative distribution of final layers, ECHO bifurcates inference into a high-frequency inner loop and a low-frequency outer loop. Within the inner loop, early-layer bonus logits drive rapid, multi-step draft-tree exploration at a minimal cost. Simultaneously, the outer loop performs authoritative full-model verification through a state-reuse mechanism. Crucially, the outer loop also utilizes final-layer bonus logits to correct existing paths and supplement the tree with high-confidence candidates for subsequent cycles. Experimental results across diverse benchmarks demonstrate that ECHO significantly boosts mean accepted tokens and achieves a 2.4$\times$ to 2.9$\times$ speedup, outperforming existing state-of-the-art baselines with negligible engineering overhead and no extra deployment parameters, albeit with a one-shot fine-tuning dependency for optimal acceleration. The code is available at this https URL.

---


### 154. [Video-HolmesV2: Can MLLMs Reason with Spatio-Temporal Audio-Visual Evidence in Long Videos?](https://arxiv.org/abs/2609.17248)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wei, Zipeng Wang, Yushe Cao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models have demonstrated impressive video understanding, yet their ability to reason over long-form narratives is often masked by visual-centric evaluations and inefficient context processing. Existing benchmarks over-rely on visual heuristics while marginalizing auditory cues, effectively reducing models to "silent observers" that bypass genuine cross-modal reasoning. Moreover, standard dense sampling creates an evidence-context trade-off: increasing frames to capture evidence inevitably leads to attention distraction and token explosion. To bridge these gaps, we present Video-HolmesV2, a novel benchmark designed for Deep Audio-Visual Coupling. Unlike previous works, it enforces an Evidence-Based Evaluation, requiring models to justify answers with precise spatio-temporal audio-visual evidence, thereby reducing confounding effects of guessing and hallucinated evidence. To support this, we introduce: (1) a Multi-Model Cross-Verification pipeline to ensure task rigor; (2) a Spatio-temporal Evidence-Aware Metric for fine-grained calibration. Furthermore, we propose an Audio-Text Guided Token Compression framework. By fusing task intent with auditory anchors, our method distills high-value reasoning cues to mitigate long-context noise. In our evaluation, even strong proprietary models achieve below 60% accuracy, while our approach outperforms comparable open-source omni-models.

---


### 155. [Persistent Recurrent Memory Between Transformer Layers - Improves Language Model Generalization](https://arxiv.org/abs/2609.17251)

**<font color=#1a73e8>作者：</font>** Eduardo Novaes Hering  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a simple architectural modification to decoder-only transformers: a persistent recurrent state that observes hidden representations via cross-attention, updates itself through a GRU, and modulates subsequent processing via gated addition. Inserted between the lower and upper halves of a 6-layer transformer, this module adds only 3.7\% additional parameters while reducing evaluation loss from $2.438 \pm 0.004$ to $1.743 \pm 0.018$, corresponding to a 28.5\% reduction on held-out language modeling data. The improvement is statistically significant across 5 random seeds ($p < 0.01$) and corresponds to reduced overfitting (generalization gap 0.12 vs 0.26). Through controlled ablations, we demonstrate that the improvement stems entirely from the persistent memory topology, not from auxiliary self-prediction objectives. A model with identical topology but no auxiliary loss performs equivalently, while a random auxiliary loss provides no benefit. Representation probing reveals that the persistent state encodes narrative position (52\% vs 33\% chance level)---information that standard attention maintains less efficiently. Our results suggest that bridging transformer layers with a lightweight recurrent memory is a simple, effective approach to improving generalization in small-scale language models.

---


### 156. [Semantic-Spatial Agreement Verification for Mitigating Object Hallucination in Multimodal Large Language Models](https://arxiv.org/abs/2609.17269)

**<font color=#1a73e8>作者：</font>** Ziheng Ren, Qian Gao, Jun Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models generate natural-language responses from visual inputs, yet may mention objects absent from an image. In medication assistance, accessible perception, and environmental decision-making, such hallucinations can create real-world safety risks. We propose Semantic-Spatial Agreement Verification (SSAV), a training-free method for verifying object claims. A visually grounded claim should remain stable across semantically equivalent queries and repeatedly localize to the same image region. SSAV aggregates multiple prompts to estimate semantic support and reduce sensitivity to query wording. Query-Induced Regional Verification (QIRV) combines cross-query region persistence, spatial overlap, and relative candidate dominance to identify isolated high responses and dispersed localizations. A geometric mean fuses semantic and spatial evidence, lowering the verification score when either branch lacks support. Experiments on three base models and multiple evaluation protocols show that SSAV effectively mitigates object hallucination. On LLaVA-1.5-7B, accuracy averaged across COCO, A-OKVQA, and GQA improves by 1.81 and 3.17 percentage points under POPE Popular and Adversarial, respectively, while CHAIRs decreases from 49.40% to 32.80%. These results show that cross-query semantic stability and regional consistency provide interpretable external visual evidence for object claims.

---


### 157. [Extracting ontology-compliant knowledge from scientific text describing irradiated materials using large language models](https://arxiv.org/abs/2609.17291)

**<font color=#1a73e8>作者：</font>** Marco Luca Sbodio, Marcos Martínez Galindo, Vanessa Lopez 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The quest for new materials increasingly relies on predictive models and comprehensive simulations that span scales from atomic to macroscopic levels. However, essential data necessary for these models and simulations are often embedded in scientific literature as unstructured text, limiting reusability and posing challenges for researchers seeking to leverage existing knowledge effectively. While extracting structured data from unstructured text using large language models is gaining popularity, traditional methods typically generate key-value pairs data with straightforward schemas. In contrast, we introduce eolas, a modular pipeline that uses large language models to automatically transform scientific documents into knowledge graphs aligned with a specified ontology. We demonstrate eolas effectiveness in extracting useful information for scientists studying materials designed to endure the extreme temperatures and radiation levels found in fusion reactors. While a human expert might spend between thirty to ninety minutes extracting relevant data from an article, eolas can generate high-quality knowledge graphs in just a few minutes. These are presented in a tabular format with faceted navigation for easy human validation. Additionally, we introduce the first benchmark dataset designed to assess large language models capabilities in constructing knowledge graphs within the domain of irradiated materials. The analysis of 168 experiments using our dataset, various large language models and prompting techniques provides key insights that we summarize into practical guidelines for effectively extracting knowledge graphs aligned with an input ontology.

---


### 158. [When AI Becomes Hard to Understand: Cognitive Demands in Real-World Human-AI Conversations](https://arxiv.org/abs/2609.17301)

**<font color=#1a73e8>作者：</font>** Yingcan Carol Wang, Iman Munire Bilal, Qamar Zaman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI increasingly supports complex financial and health decisions, yet we know little about when its responses become difficult to process in real-world dialogue. We analyse more than 84,000 ChatGPT and Gemini conversations, using repeated prompting and clarification following misunderstanding as behavioural indicators of cognitive difficulty. We find that response characteristics such as length, readability and lexical diversity do not have fixed relationships with conversational difficulty; instead, their relationships depend on how they combine. Most notably, greater lexical diversity was associated with less repeated prompting in shorter responses, but this association weakened as response length increased, a pattern that replicated across financial and health conversations. We propose a conversational complexity budget to conceptualise these interdependencies: the demands associated with one response characteristic may depend on those accompanying it. The resulting design challenge is how to configure response complexity for the particular user, task and interaction.

---


### 159. [Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems](https://arxiv.org/abs/2609.17306)

**<font color=#1a73e8>作者：</font>** Sara Vera Marjanović, Jiacheng Xu, Aleksandr Laptev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

---


### 160. [Zero-shot narrative detection in social messaging](https://arxiv.org/abs/2609.17310)

**<font color=#1a73e8>作者：</font>** Jesús M. Fraile-Hernández, Anselmo Peñas, Patrick Giedemann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates the zero-shot ability of large language models (LLMs) to identify and classify hidden narratives in social messages. Our research hypothesis is that LLMs' extensive contextual knowledge allows them to interpret messages on a deeper, pragmatic level, going beyond basic sentiment or topic analysis. Experiments on the Dipromats and SemEval datasets show that providing models with human-written narrative descriptions significantly improves performance, without the need of training examples. In contrast, automatically generated descriptions or the use of few examples (few-shot) often degrade accuracy due to subtle shifts in framing. The study also finds that ensemble methods, particularly majority voting, enhance robustness and that larger models perform best while also being less sensitive to prompt variations. The findings validate that LLMs can effectively detect strategic narratives in a zero-shot setting, and when combined with simple ensembling and human-written descriptions, they can rival supervised systems, offering a scalable solution for narrative detection, specially when there is no training data for the vast majority of domains.

---


### 161. [Towards Detecting AI-Assisted Responses in Online Surveys](https://arxiv.org/abs/2609.17317)

**<font color=#1a73e8>作者：</font>** Qizhou Wang, Bogdan Mamaev, Christopher Leckie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The use of LLMs to complete online surveys impacts the validity of survey-based research, but detecting such usage remains underexplored. We introduce an initial benchmark dataset, namely ASURRE, for AI-assisted survey participation to capture usage strategies ranging from full generation and revision to persona-grounded agentic completion. Controlled by these strategies, LLM-assisted survey responses are generated using multiple LLMs on three real-world surveys in different disciplines, paired with genuine human responses. Our evaluation of existing machine-generated text (MGT) detectors shows that naive AI usage is readily detectable, whereas persona-grounded agents that mimic entire respondents push detector performance toward chance. We further show that agentic completion cannot fully replicate respondent-level behaviour and leaves distinctive behavioural traces. While individual cues can be circumvented by targeted prompting, a simple few-shot, training-free aggregator over these cues improves mean AUROC by +0.14 over the best existing detector across agentic settings. Our project is available at this https URL.

---


### 162. [Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2609.17320)

**<font color=#1a73e8>作者：</font>** Deepak Akkil, Tamer Abuelsaad, Karthik Vikram 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

---


### 163. [From Transient Prompts to Persistent Control: Scientific Poster Generation via Recursive Semantic-Geometric Contracts](https://arxiv.org/abs/2609.17326)

**<font color=#1a73e8>作者：</font>** Runze Li, Yukun Zhao, Can Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific poster generation distills a multimodal paper into a single-page visual artifact, forcing strict trade-offs between informational coverage and readability under a fixed spatial budget. Existing methods pass plans as transient prompts and validate individual stages in isolation. This strategy causes requirements to drift across content and layout modules, and previous checks to be silently invalidated. We introduce PosterVisor, a control framework that shifts poster generation from transient prompts to persistent control. An Orchestrator grounds rubrics in the paper and visual assets, compiling them into a Semantic-Geometric Contract (SGC) that binds claims and sources to required visuals, budgets, and spatial commitments. Only fully instantiated records become executable assertions; other usable requirements remain soft guidance. Recursive Contract Enforcement (RCE) dynamically triggers checks across stages as evidence emerges. Crucially, during repairs, RCE rechecks affected checkpoint states, preventing repair-induced regressions from propagating silently. We instantiate PosterVisor in HTML/CSS and editable PPTX generators. On the 100-paper Paper2Poster benchmark, PosterVisor-PPT improves observed mean poster-grounded QA accuracy over PosterGen (64.47% vs. 58.53%) and is preferred by human judges in 72.5% of non-tied pairwise comparisons (95% CI, 61.6-83.4%). A secondary 30-paper study also yields higher VLM Overall and PaperQuiz means. These results support rubric-compiled contracts and stage-conditioned enforcement for controllable poster synthesis.

---


### 164. [Vroom-Vroom at SHROOM-Visions: A Multi-Judge Committee for Detecting Hallucinated Spans in Vision-Language Outputs](https://arxiv.org/abs/2609.17327)

**<font color=#1a73e8>作者：</font>** Toqeer Ehsan, Nico Penttilä, Richard Schmidt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our submission to the SHROOM-Visions shared task on detecting and classifying hallucinated character spans in vision-language model outputs across four languages. We employ several fine-tuned vision-language models as independent annotators and combine their span predictions through character-level majority voting, and additionally explore activation probes. The approach ranks first in three of four languages and places on the podium in every language and metric. Our analysis indicates that disagreement among diverse models tracks disagreement among human annotators.

---


### 165. [Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling](https://arxiv.org/abs/2609.17331)

**<font color=#1a73e8>作者：</font>** Xiaoyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov Model (HMM) that encodes long-term behavioral and cognitive inertia as an editable state-transition matrix; (ii) a Reflexion-style verbal metacognition loop whose output updates the HMM parameters themselves, rather than merely being stored as text; and (iii) a multi-agent social environment in which initially identical agents continuously compare their behavior with others'. The three components form a closed loop: social action $\to$ feedback $\to$ self-reflection $\to$ inertia update $\to$ differentiated action. We state three falsifiable hypotheses and provide a reproducible experimental protocol with operational metrics. A language-model-free prototype shows the loop spontaneously breaks symmetry: initially identical agents consolidate distinct, stable personalities whereas matched controls do not. Experiments with a hosted LLM surface these differences as distinct first-person self-narratives, and a five-agent deliberation spontaneously develops social structure---a consensus hub and a unanimously rejected outlier---absent in the control. Following an epistemologically agnostic stance inspired by Zhuangzi, SEAA studies only observable behavioral emergence and makes no claim about subjective qualia. This work contributes a unified framework, a concrete architecture with pseudocode, mechanistic evidence, and a microscope-style sandbox for studying artificial-self emergence.

---


### 166. [LumiNote: LLM-Assisted Multimodal Instruction for VR Stage Lighting Education](https://arxiv.org/abs/2609.17335)

**<font color=#1a73e8>作者：</font>** Danxuan Liang, Chun Yin Li, Zheng Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Stage lighting education requires instructors to bridge abstract concepts, technical operations, and learner-understandable representations. While Virtual Reality (VR) removes physical constraints, existing systems provide limited support for live instruction. We present LumiNote, an LLM-assisted VR system that transforms spoken pedagogical intent into instructor-reviewable spatial annotations, executable demonstrations, and linguistic support. In an exploratory study with 3 instructors and 24 students, we examined how instructors incorporated LumiNote into familiar lighting topics and how students received the resulting representations. We found LLM assistance most valuable for expressive, under-specified goals, but requiring greater expert intervention for fixture-specific or spatial configuration requests. Instructors engaged with generated suggestions as a controllable refinement process, shifting effort from manual setup toward pedagogical expression. However, representations that externalized expert reasoning did not always align with novice comprehension. These findings characterize LLM-assisted VR instruction as a domain-grounded mediation process among expert expression, executable operations, and learner-facing representations.

---


### 167. [Where Should a Document Live: Context, Representations, or Parameters?](https://arxiv.org/abs/2609.17346)

**<font color=#1a73e8>作者：</font>** Nathanaël Carraz Rakotonirina, Momchil Hardalov, Gonzalo Iglesias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To answer questions outside of their pre-training data, large language models (LLMs) need access to new information, which can be presented in the context window as documents, encoded into the model's parameters, or injected as latent representations. However, each of these methods comes with different efficiency, cost, and performance trade-offs, with no single winner. We present a controlled comparison of representation-based (KV-cache based) and parametric (fine-tuning-based) adaptation methods on five knowledge-intensive benchmarks. We show that in the oracle setting, Cartridges (KV) are the most accurate injection method at nearly every storage budget, outperforming parametric methods by 10 points. Compaction (KV) matches Cartridges only at low compression rates, lagging behind the parametric methods by 10 points at rates higher than $50\times$. In the more realistic multi-document retrieval scenario, Cartridges are the only method that matches in-context learning (ICL), leading the parametric methods by 29 points and Compaction by 15 points. Nonetheless, Cartridges are also the only method, besides full fine-tuning and large MLP adapters, that suffers from catastrophic forgetting, i.e., a 6% performance degradation on control benchmarks, with 13% in coding.

---


### 168. [Large Language Models Develop Belief State Geometry In-Context](https://arxiv.org/abs/2609.17376)

**<font color=#1a73e8>作者：</font>** Daniel Balcells, Andrew Jun Lee, Chirag Rastogi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained on next-token prediction exhibit remarkable in-context learning (ICL) abilities, yet the representations that support ICL remain poorly understood. We consider such representations in a controlled setting: prompting LLMs with data emitted from hidden Markov models (HMMs) and probing for the corresponding belief state -- the posterior distribution over the HMM's hidden states given the observed token history. Across six open-source LLMs prompted with data from 40 HMMs selected for non-trivial belief structure, we find that belief states are linearly decodable from residual stream activations, with peak probe $R^2$-values from 0.83-0.99 across HMM and LLM combinations, ranging from early to late layers. To establish functional relevance, we intervene directly on the probe-identified subspace via patching and steering, resulting in downstream prediction quality on the order of the untampered model, while controls degrade performance substantially. Together, these results provide representation-level evidence that ICL in open-source LLMs approximates optimal Bayesian prediction over a context-inferred generative model. More broadly, our findings extend prior results linking input-distribution structure to activation geometry: from toy networks trained explicitly on HMM data to production-scale LLMs.

---


### 169. [OPEN-1B: A Fully Auditable Training Run](https://arxiv.org/abs/2609.17380)

**<font color=#1a73e8>作者：</font>** John Donaghy, Brian Wilcox, Oğuzhan Ersoy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point arithmetic. Deep learning frameworks often offer a deterministic execution mode, allowing reproducible operations on the same machines. Unfortunately, this determinism does not carry across hardware such that a user can verify that a released checkpoint was actually produced using the declared training recipe. This leaves room for undisclosed data, injected biases, or backdoors that existing techniques such as proof-of-learning or proof-of-training-data cannot rule out.
We introduce a new tier of model transparency, fully auditable, in which every operation on every data sample during training is independently reproducible on heterogeneous commodity hardware with bitwise certainty. By imposing a definite order on the sources of training nondeterminism, GPU kernel reductions, data batch ordering across a data-parallel cluster, and inter/intra-node collective communication, we make it possible to replay any individual step of a large, distributed training run on a single piece of commodity hardware and check it against the published trajectory.
Because replaying an entire run on one machine is infeasible, we support this with a collective verification scheme in which many independent auditors each certify individual steps, together covering the whole run. We release Open-1B, a model trained under this regime, together with its full pretraining dataset, every intermediate checkpoint, the training codebase, and the audit harness needed to reproduce and verify any step of its training.

---


### 170. [Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation](https://arxiv.org/abs/2609.17398)

**<font color=#1a73e8>作者：</font>** Ting-Wei Chang, Hen-Hsen Huang, Hsin-Hsi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients' reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In this work, we leverage the capabilities of LLMs such as GPT-4o-mini, Gemini-1.5-pro, and LLaMA for text simplification. Additionally, we incorporate Mixture-of-Agents (MoA) techniques to enhance adaptability and robustness in PLA tasks. Key contributions include a comparative analysis of prompting strategies, finetuning with QLoRA on different LLMs, and the integration of MoA technique. Our findings demonstrate the effectiveness of LLM-driven PLA, showcasing its potential in making healthcare information more comprehensible while preserving essential content.

---


### 171. [Never Stop Thinking: Continuous-Time Language Agents](https://arxiv.org/abs/2609.17416)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voice agents built on LLMs follow a rigid listen-think-speak loop that inserts seconds of dead air before every reply. We show that continuous-time cognition (thinking while listening and thinking while speaking) emerges from an unmodified text model under a lightweight interrupt-and-resume orchestrator, cutting live-pipeline latency by 19% overall and by half in the regime the mechanism targets. To measure whether continuous-time thinking improves what agents accomplish, we introduce ReactiveBench: 120 interactive scenarios scored against pre-registered binary requirements, plus a verifiable streaming track scored by exact correctness. ReactiveBench exposes a pitfall with broad consequences: LLM judges reward visible reasoning; a large judged "advantage" of continuous-time thinking reverses sign under an independent judge, and judge-trained models objectively complete fewer requirements when they think. A five-stage training study then locates the right signal at three levels. Its source: verifiable objectives turn thinking from harmful to helpful. Its structure: whatever a uniform reward omits, optimization trades away; brevity everywhere erodes multi-hop tool chaining. Its optimizer: preference optimization can only trade conflicting sub-goals against each other, while on-policy RL over a type-shaped reward improves every correctness axis at once, raising streaming completion from 48% to 73+/-5% across seeds and replicating at larger scale and on a second model. Orchestration makes continuous-time interaction possible; a verifiable signal, correctly sourced, shaped, and optimized, makes it good.

---


### 172. [World Model Science: Self-Organized Criticality, Weak Chaos, and Metastable Belief Dynamics in Long-Horizon LLM Agents](https://arxiv.org/abs/2609.17419)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents must maintain task state across extended sequences of observations, actions, tool calls, and intermediate beliefs. We study these trajectories through three dynamical views: self-organized criticality, weak chaos, and metastable belief dynamics. Our framework aligns agent-implied states with benchmark-grounded states and measures stress accumulation, error avalanches, temporal dependence, local--global mismatch, bounded divergence, belief-basin transitions, and finite-size scaling under explicit null models. Across 22 experiments spanning controlled puzzles, tool use, embodied tasks, multi-hop retrieval, general-assistant reasoning, and Game of Life, we find that locally valid actions can persist after global state fidelity fails, stress can trigger abrupt collapse, error sequences exhibit long memory, dependency depth changes the propagation regime, and larger horizons support larger avalanches. At the same time, divergence remains bounded, belief states show metastable rather than fully chaotic behavior, and stronger claims of universal power laws, critical points, or shared intervention optima are not supported. These results suggest a science of agent world models based on trajectory-level dynamical diagnostics rather than terminal reward alone.

---


### 173. [Right Tool, Right Job: Native-Language Evaluation, Tokenizer Sensitivity, and Methodological Findings from a French-Only BabyLM](https://arxiv.org/abs/2609.17435)

**<font color=#1a73e8>作者：</font>** Adam Zachary Wasserman, David Beauchemin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We submit MéTRON-FR, a 125M GPT-2 pretrained on 92.47M words of French, to the BabyLM 2026 Strict track. It scores 85.97 +/- 0.17% on QFrBLiMP (a native Quebec-French benchmark of grammatical minimal pairs) and 62.80% on the BabyLM-weighted leaderboard. A cross-lingual GLUE (General Language Understanding Evaluation) protocol that combines French task-data translation with rank-16 LoRA (Low-Rank Adaptation) produces a sharp task-type gradient: relational tasks gain measurably, while world-knowledge tasks regress. Bilingual Lexicon Induction aligns the French embeddings to GPT-2 at p@1 = 68.84 +/- 8.61%, 18X above chance, suggesting cross-lingual alignment tracks acquired grammatical competence rather than training duration. An ablation study shows that single-token zero-shot scoring is dominated by tokenizer and template artifacts at the child scale, motivating tokenizer-swap sensitivity, placebo-controlled prompting, and native-language minimal-pair benchmarks as standard diagnostics.

---


### 174. [BrainFocus: EEG-Guided ROI Selection for Efficient Vision-Language Models](https://arxiv.org/abs/2609.17443)

**<font color=#1a73e8>作者：</font>** Yihui Peng, Guorui Lu, Qinyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong visual question answering (VQA) performance, but processing large cluttered images is computationally expensive when only a small region is relevant. Electroencephalography (EEG) signals, which capture human neural responses to visual stimuli, can provide a human-derived semantic cue about the region of interest (ROI). However, EEG-guided visual category decoding remains imperfect, making direct ROI routing unreliable. In this work, we propose BrainFocus, a reliable EEG-guided efficient VLM framework for VQA. An EEG classifier predicts a target category, and a YOLO detector localizes the matching ROI. The VLM receives the cropped ROI only when both predictions pass confidence thresholds; otherwise, it processes the full image. For evaluation, we build on EEG-ImageNet to construct a 40-class benchmark comprising generated cluttered images and real object-centric images, with target-ROI annotations and 600 English visual question-answer pairs. Across Qwen3.5-VL 2B, 4B, and 9B models, BrainFocus improves VQA accuracy by 4.14-9.87 percentage points (pp) on cluttered scenes while reducing input tokens and total tokens by 23.2%-39.4% and 23.2%-39.3%, and end-to-end floating-point operations (FLOPs) by 23.2%-39.5%. These results demonstrate that EEG can guide efficient VLM inference even when its semantic decoding is imperfect.

---


### 175. [Tables Decoded: DELTA for Structure, TARQA for Understanding](https://arxiv.org/abs/2609.17458)

**<font color=#1a73e8>作者：</font>** Jahanvi Rajput, Dhruv Kudale, Saikiran Kasturi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table understanding is a core task in document intelligence, encompassing two key subtasks: table reconstruction and table visual question answering (TabVQA). While recent approaches predominantly rely on vision- language models (VLMs) operating on table images, we propose a more scalable and effective alternative based on structured textual representations. These representations are easier to process, align more naturally with LLMs, and eliminate the need for language-specific visual encoders, making them particularly suitable for multilingual documents. We present DELTA, which separates physical structure recognition, logical structure recognition, and OCR to extract both layout and content accurately. DELTA outputs tables in Optimised Table Structure Language (OTSL), a compact and unified format that encodes cell arrangements and textual content. On table structure recognition (TSR), DELTA achieves TEDS- Structure scores comparable with state-of-the-art methods across FinTabNet, PubTabNet, and PubTables-1M. We further establish its robustness on non-English tables through our curated Hindi benchmark, TORQUE. Building on this, we introduce TARQA, an LLM fine-tuned on OTSL sequences. Our approach yields gains of 9.3 p.p. on WTQ (TabQA) and 9.2 p.p. on FinTabNetQA (TabVQA), respectively. On TORQUE, our method ranks second among all VLMs and DELTA + LLM variants. We release our code, models, and benchmark at: this https URL

---


### 176. [Coupled Calibration and Learning: Mitigating Teacher Bias in LLM Distillation without Target-Domain Reward Feedback](https://arxiv.org/abs/2609.17474)

**<font color=#1a73e8>作者：</font>** Haichen Hu, Yuheng Zhang, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) distillation aims to transfer the capabilities of a powerful teacher to a smaller student. Direct imitation, however, can also transfer the teacher's systematic bias and errors. This challenge is particularly pronounced under covariate shift, when the teacher's reliability on target questions is uncertain and target-domain reward feedback is unavailable. We propose Coupled Calibration and Learning (CCL), an LLM distillation algorithm that couples teacher calibration with student updates through token-level branching, using reward feedback only on source questions. Each iteration calibrates the teacher using source feedback and then uses the calibrated teacher to train the student on target questions. The updated student, in turn, informs subsequent calibration. In an autoregressive policy framework, we prove that the output student's expected average Kullback-Leibler divergence to the oracle student converges to zero at a polynomial rate in the number of iterations. The oracle maximizes the true reference-regularized target reward within the student class, which need not represent the unrestricted optimal policy. Our analysis quantifies the progress of projected student gradient updates while controlling the error in teacher calibration. We further establish a separation from regularized direct matching: its error relative to the oracle student can remain bounded away from zero even when the teacher achieves higher regularized target reward than every student policy. These results demonstrate that LLM distillation can overcome persistent teacher bias and recover the optimal student through coupled calibration and learning, without target-domain reward feedback.

---


### 177. [JustFit: 200K-Token LLM Serving on a 24 GiB Laptop with Just-in-Time State Management](https://arxiv.org/abs/2609.17475)

**<font color=#1a73e8>作者：</font>** Yuhua Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Capable open-weight models make local coding and reasoning attractive, but their context and execution state strain laptop memory. We present JustFit, an MLX-based inference runtime that combines KVExec for compressed KV execution, PhaseSwap for component residency, and StateTrans for state-preserving serving transitions. These mechanisms fuse reconstruction and coordinate just-in-time materialization and release, independently of model-weight quantization. In full-execution capacity tests on a 24 GiB M4 Pro MacBook running Qwen3.8-27B MXFP4, three independent runs complete 196,608 input and 16,384 output tokens, increasing completed single-request context from the mlx-vlm baseline's 30,720 positions to 212,992 (6.93x); a separate two-request run retains 229,376 positions in aggregate. In separate performance tests, a 32K-input, 64-output probe reaches 19.11 tokens/s, and a repeated 32K+6K workload has a median peak process footprint of 16,374 MiB. The integrated runtime answers 29 of 30 AIME 2026 problems correctly, showing how compact state and lifetime-aware execution expand local serving capacity while supporting extended generated reasoning.

---


### 178. [Verifiable Social Reasoning for LLM Assistants](https://arxiv.org/abs/2609.17496)

**<font color=#1a73e8>作者：</font>** Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target agent with a hidden motive interacts with other agents including one representing the user, who then consults the evaluated assistant to infer the target's motive, providing verifiable ground truth by construction. Simulation faithfulness is validated through a human study with 24k annotations. We apply Fuse to 12 LLMs and demonstrate its analytical utility by systematically isolating key factors, showing that (i) user mediation compounds the inherent difficulty of social reasoning; (ii) LLMs exhibit systematic sensitivity to biased user framing; (iii) models can require more details than humans need to reach a correct prediction; and (iv) longer conversations do not always improve performance despite providing opportunities for clarifying questions. We open-source Fuse and a dataset with 21k examples.

---


### 179. [What Breaks Under Pruning in Smart Homes, and When? Evaluating LLM Degradation Across Architectures and Task Complexity](https://arxiv.org/abs/2609.17515)

**<font color=#1a73e8>作者：</font>** Congjing Zhang, Vashishtha Patil, Henning Lange 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pruning can reduce the deployment cost of large language models (LLMs), but its impact on context-grounded tool calling remains poorly understood. We systematically study pruning-induced degradation in smart-home tool calling across four LLMs spanning dense Transformer, dense hybrid, and mixture-of-experts (MoE) architectures, together with depth, width, hybrid, and expert pruning methods. After post-pruning supervised fine-tuning (SFT), we evaluate more than 19,500 instances from three smart-home datasets. Beyond aggregate task accuracy, we characterize degradation along two dimensions: action components (i.e., operation, device, argument, and value) and task complexity. Our results show that dense models have narrow safe pruning regions followed by sharp degradation, while MoE models tolerate substantially more pruning. Pruning degrades grounded specificity before schema-level intent, and aggressive dense pruning can induce systematic over-refusal. These findings highlight the importance of evaluating pruning beyond aggregate accuracy when selecting pruned LLMs for reliable tool execution.

---


### 180. [When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control](https://arxiv.org/abs/2609.17516)

**<font color=#1a73e8>作者：</font>** Ali Şenol  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent answers when their factual support is weak. This paper introduces Chain-of-Self-Questioning (CoSQ), a prompt-only framework that makes answer commitment conditional on an explicit assessment of the information required to answer a question. We evaluate three CoSQ variants under seventeen conditions on the 817-item TruthfulQA multiple-choice validation set using eleven open-weight and hosted model families. In the final balanced-option protocol, Grounded-CoSQ at {\tau}=0.90 reduces the mean unconditional wrong-commitment rate from 13.1% under chain-of-thought prompting to 8.9%, a 32.1% relative reduction, while increasing answered accuracy from 86.9% to 89.7% and answering 87.6% of questions. Both improvements hold for all eleven models and at every evaluated threshold. Critical-CoSQ and Adaptive-CoSQ provide neighboring operating points with 88.6% and 86.5% coverage, respectively, while remaining more reliable than the baseline. A secondary Natural Questions Short-Answer evaluation provides convergent open-form evidence. These findings show that self-assessment can support explicit, tunable answer-or-abstain decisions when an unsupported commitment is more costly than referral or review.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 181. [Feasibility of Homomorphic Inference for a Genomic Foundation Model](https://arxiv.org/abs/2609.16211)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Christos Galanopoulos, Kimon Antonios Provatas, Ilias Georgakopoulos-Soares  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Human genomic sequences can identify individuals, cannot be replaced after disclosure, and are the inputs that genomic foundation models are designed to interpret. We assess whether a compute provider can execute a released genomic foundation model without receiving query-derived genomic values in plaintext and whether correctness, memory, or cost prevents complete encrypted inference. We first reproduce the released model on three genomic task families and freeze an independently validated numerical reference. We then implement a client-assisted approximate homomorphic encryption protocol: the provider evaluates linear algebra on ciphertexts, while the key-holding data owner evaluates exact normalization, causal softmax, and activation functions at fixed boundaries. A noninteractive configuration completes one released-weight block but exceeds the tested accelerator-memory envelope when configured for composition. The client-assisted configuration executes all released transformer blocks and the task head for one heldout genomic-signal input at its full prompt length. It matches the frozen final label, peaks at 9,839 mebibytes of accelerator memory, and completes in 6,683 seconds on one accelerator. These results establish arithmetic feasibility for a complete classifier, while repeatability, network transport, and private token-index lookup remain unresolved. The biomedical significance is that, under the stated threat model, a served genomic model can process an encoded sequence without exposing plaintext queryderived activations to the compute provider.

---


### 182. [Test-Time Unlearning via Sparse Autoencoder](https://arxiv.org/abs/2609.16229)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pingzhi Li, Jinhao Duan, Vaishnav Tadiparthi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove specific knowledge from a trained large language model (LLM) without retraining from scratch. Existing methods modify model weights via gradient ascent and its advances. While effective on certain benchmarks, these weight-based approaches exhibit a sharp forget-utility trade-off, where stronger forgetting of target knowledge can degrade model utility, and unlearned knowledge may reappear under post-unlearning fine-tuning or prompt attacks. We propose ARIA (autoencoder-gated inference-time unlearning), a test-time unlearning method that leaves model weights intact and gates access to unwanted knowledge only when generation enters a forget-related state. ARIA uses sparse autoencoder (SAE) latents to train a lightweight linear detector, then applies an interpretable intervention on triggered states with negligible test-time overhead. Empirical evaluations on TOFU, R-TOFU, and WMDP show that ARIA improves the forget-retain trade-off over weight-based baselines across both a thinking model (DeepSeek-R1-Distilled-Qwen-1.5B) and an instruction model (Gemma-3-1B-it), e.g., reducing WMDP-cyber forget-set accuracy significantly while keeping MMLU within 1% of the pre-unlearning model. We further introduce three post-unlearning adversarial attacks targeting weight-space and decoding-space recovery, and find that ARIA remains robust under all three, with forgetting changing by less than 1% under attack. A feature-level case study leveraging the interpretability of ARIA suggests that some retain degradation may reflect response styles underlying the unlearning data rather than leakage of the targeted knowledge itself, highlighting a potential source of bias in unlearning task construction.

---


### 183. [How Good Are Time-Series Foundation Models for Pedestrian Crowd Count Forecasting? A Cross-Dataset Comparative Study](https://arxiv.org/abs/2609.16415)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Theivaprakasham Hari, Ziteng Li, Yanan Xin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pedestrian-count forecasting supports pedestrian-oriented Intelligent Transportation Systems (ITS), including crowd monitoring, pedestrian-traffic staffing and routing, and proactive risk mitigation during surges. Recent time-series foundation models (FMs) report strong zero-shot accuracy on heterogeneous forecasting benchmarks, but it remains unclear whether these gains transfer reliably to pedestrian sensing deployments. We benchmark seven univariate forecasting approaches spanning four paradigms: Seasonal Naive, gradient-boosted trees (LightGBM, CatBoost), deep learning models (N-HiTS, PatchTST), and two pretrained FMs (TimesFM, Chronos-2). Experiments cover two complementary regimes: (i) a five-day special event dataset SAIL2025 at 3-minute resolution with limited in-domain history; and (ii) Melbourne pedestrian sensors as a multi-year hourly dataset (2010--2017) with strong seasonality. We compare the MAE and RMSE results per sensor across datasets and multiple forecast horizons. Results show three consistent findings. First, with limited historical data, Seasonal Naive remains a strong baseline for long-horizon forecasting on high-volume sensors, while trained models can degrade when the next day differs substantially from prior days. Second, boosted trees can be competitive on lower-volume sensors but exhibit higher sensitivity on high-volume sensors under event-driven shift. Third, FMs excel in the seasonal and data-rich regime under long-context configuration. The findings highlight the importance of choosing pedestrian forecasting models based on both the underlying data conditions and the forecasting horizon.

---


### 184. [A Vision-Language Foundation Model for Precise and Comprehensive Brain Tumor Diagnosis from Preoperative Multimodal Data](https://arxiv.org/abs/2609.16597)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yinong Wang, Jianwen Chen, Zhou Chen 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background Non-invasive presurgical diagnosis of brain tumor types from Magnetic Resonance Imaging (MRI) is essential but challenging due to overlapping imaging features across tumor types, inter-observer variability, and the extensive training required for expertise. We aimed to develop an MRI-based Artificial Intelligence (AI) model for automatic and reliable brain tumor classification with diagnostic uncertainty quantification and radiology reports generation.
Methods We developed BrainVLM to classify all 12 World Health Organization (WHO) 2021 brain tumor types. BrainVLM integrates an uncertainty quantification strategy to indicate prediction reliability and a module for generating radiology reports to elucidate the clinical rationale. BrainVLM was trained on multi-modal data (MRI scans, demographics, and radiology reports) from 40,043 individuals. It was validated on 5,211 patients with pathologically confirmed brain tumors, including 3,877 held-out patients from the primary hospital and 1,334 patients from 11 independent hospitals. We further conducted two proof-of-concept studies to validate its clinical utility in AI-clinician workflows: 1) a blinded multi-reader study where 12 neuroradiologists across varying experience levels interpreted 248 retrospective cases with or without AI assistance, and 2) a real-world prospective study in which 1,009 patients were independently and blindly assessed by BrainVLM and radiologists before surgery. Additionally, we demonstrated BrainVLM's utility in preoperative molecular subgroup prediction for adult-type diffuse gliomas, using a multi-center cohort of 632 patients.

---


### 185. [Right Direction, Wrong Step: Geometric Analysis of Finite-Step Failure in Looped Transformers](https://arxiv.org/abs/2609.16665)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhihao Guo, Zonghan Wu, Haizhou Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers offer a parameter-efficient route to test-time scaling by reusing shared layers for iterative latent reasoning. However, additional iterations can reduce support for a reference answer, leaving unclear whether an update's direction is locally unhelpful or its full displacement moves too far. We study this distinction by analysing reference utility, which measures this support, along the model's own update direction, varying the fraction of the proposed displacement supplied to the readout. This reveals finite-step failures in which a locally improving direction produces a harmful full update. A pathwise curvature decomposition characterises how initial progress is lost, while a local quadratic model predicts full-step gains and useful step scales. Bounds based on accumulated curvature variation characterise the approximation error of these predictions. Experiments across two model families reveal this separation on mathematical and commonsense tasks. A fixed quarter step produces positive gains in reference utility for 72.2--83.2% of selected failures across four settings. These findings identify a mismatch between update direction and step scale as a mechanism of lost progress, explaining how some harmful updates retain useful computation.

---


### 186. [AI for Games in the Foundation Model Era](https://arxiv.org/abs/2609.16679)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Meng Luo, Yanlin Li, Hao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models, alongside advances in learned game-world models, are reshaping AI across the game lifecycle. Beyond playing games, recent systems model players and game dynamics, support design and development, adapt player-facing experiences at runtime, and evaluate resulting artifacts. Yet these directions have evolved largely separately, obscuring which capabilities transfer across settings and which remain tied to particular games, engines, interfaces, or player populations. We organize the literature into six roles according to the immediate use of AI output: playing and acting; modeling players and games; designing games; building and maintaining games; generating and adapting at runtime; and testing and evaluating games. For each role, we examine what structure is supplied by the game or workflow, what AI learns or produces, which capabilities and artifacts transfer across settings and roles, and what evidence supports the claims. We identify cross-role connections: trajectories train world models, learned environments provide experience for agents, design specifications drive executable implementations, and play or testing feedback guides revision. However, control schemes, rules, engine interfaces, state representations, and player contexts often remain setting-specific, so downstream claims require validation in the target setting. Evaluation is most standardized for bounded game playing and selected learned environments, while persistent state in learned worlds, repeated software revision, validated player modeling, sustained runtime adaptation, and representative automated testing remain less established. The central challenge is to reuse or transfer outputs and capabilities across roles while re-establishing evidence for effectiveness in the game-specific contexts where they are used.

---


### 187. [LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory, with ICE v2 as an Audited Local-First Architecture](https://arxiv.org/abs/2609.16730)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Deepesh Sonar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational memory changes during use, so endpoint question answering alone cannot establish how a persistent state accumulates, ages, or incorporates revisions. We introduce LSREP, a Longitudinal State-Replay Evaluation Protocol combining ordered replay, explicit lifecycle schedules, repeated probes, evolving reference answers, and mechanism-fidelity checks. Its architectural case study is ICE v2, a local-first memory middleware with typed stores, retrieval fusion, and dynamic context budgets. The private, single-user instantiation contains 1,985 turns, 219 distinct probes, and 1,211 probe-checkpoint observations across 52 checkpoints. On three ordinary-density datasets, ICE v2 has a near-zero mean quality difference from vector-RAG while selecting 32% fewer fragments but using 6.6% more estimated prompt tokens. A fourth, dense dataset exposes catastrophic failures of the unbudgeted baseline. The fidelity audit limits attribution: procedural retrieval is defective, several mechanisms are unexercised, and graph utility is not established. In a complementary matched public diagnostic, ICE v2 loses decisively to pure vector-RAG on LongMemEval: 50.8% versus 72.8% in the evidence-only oracle and 43.0% versus 69.5% in full-S. Paired differences are -22.0 points (95% CI [-26.6, -17.4]) and -26.5 ([-31.3, -21.8]). Conservative abstention accompanies severe multi-session and temporal failures. ICE uses less context in this diagnostic, establishing a quality-cost trade-off rather than superior efficiency. Together, replay, fidelity auditing, and public endpoint testing expose distinct failure modes that neither architectural descriptions nor aggregate scores identify alone.

---


### 188. [SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals](https://arxiv.org/abs/2609.16804)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fangke Chen, Sirry Chen, Wei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models have demonstrated strong cross-domain transfer, yet their common architectural assumptions remain poorly aligned with wearable physiological signals, which are multichannel, irregularly sampled, noisy, and governed by coupled continuous-time dynamics spanning distinct spectral scales. We present SOTER, a generative foundation model for wearable physiological time series that unifies cross-channel coupling, spectrum-guided expert specialization, and continuous-time latent evolution within a single pre-training framework. SOTER combines a spatial feature-aware backbone that models inter-signal dependencies, a power spectral density (PSD)-guided mixture-of-experts layer that routes representations to experts associated with fixed spectral bands through an inspectable, non-learned rule, and a neural controlled differential equation decoder that supports prediction and imputation at arbitrary timestamps. We pre-train SOTER on 226 billion time points from five public physiological datasets and evaluate the same pre-trained model across out-of-distribution zero-shot forecasting, frozen-encoder linear-probe classification, and continuous-time imputation on wearable benchmarks. SOTER achieves the best RMSE on 4 of 6 datasets and the best MAE on 5 of 6 in zero-shot forecasting, the highest average Macro-AUROC in classification, and the lowest imputation error on all six datasets at 75% missingness. It further remains robust to additive acquisition noise, matching or surpassing baselines evaluated on clean inputs even under the strongest corruption. These results indicate that domain-specialized foundation models for wearable physiology benefit from jointly modeling channel structure, spectral scale, and continuous-time dynamics.

---


### 189. [LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence](https://arxiv.org/abs/2609.17488)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xingxuan Zhang, Gang Ren, Hao Yuan 等 60 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce LimiX-2, a new model in the LimiX family, developed through model and data scaling guided by our previously established scaling laws. LimiX-2 adopts the Contextual Mechanism Networks (CMNs) paradigm and is pretrained with Context-Conditional Masked Modeling (CCMM). CMNs shifts the organizing principle of in-context learning from target-centric prediction to mechanism-oriented joint modeling. Rather than centering the network on the $p(y \mid x, D_{\mathrm{context}})$ objective of conventional tabular PFNs, it is designed around learning $p(x, y \mid D_{\mathrm{context}})$, a context-dependent representation of the joint structure underlying data generation. Pretraining uses synthetic datasets generated by structural causal models (SCMs) spanning diverse graph structures, functional mechanisms, and observation processes. Evaluations on TabArena, TALENT, and BCCO show that LimiX-2 outperforms current dataset-specific models and tabular foundation models. Beyond predictive performance, the CMN paradigm also promotes causal awareness in LimiX-2: its feature attention encodes direct causal relationships, enabling accurate causal skeleton recovery.

---


> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
