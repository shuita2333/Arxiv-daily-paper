# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

---

### 151. [SITAR: A Situational Distortion Metric for Automatic Speech Recognition Evaluation](https://arxiv.org/abs/2610.21440)

**<font color=#1a73e8>作者：</font>** Mingzhe Lu, Jinhao Liu, Yunpeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In automatic speech recognition (ASR), transcription errors with similar lexical or semantic discrepancies can have markedly different consequences for the situation conveyed by speech. Capturing these differences requires not merely contextual assessment, but an understanding of what the spoken discourse describes, establishes, or seeks to bring about. However, relying on LLM judges introduces computational cost and scoring variability. We introduce SITAR, a situational distortion metric for ASR, realized through a comprehensive end-to-end construction framework. Specifically, this framework aggregates situational severity and cumulative extent into a unified score via a bounded recursive formulation. Using targets derived from this formulation with limited offline LLM support, we train SITAR as a lightweight BERT-family regressor that scores reference-hypothesis pairs in a single forward pass, entirely free of any prohibitive runtime costs. Recognizing that introducing a new metric demands rigorous justification, we formalize a principled validation protocol spanning both extrinsic validity, assessed at macro and micro levels, and intrinsic scorer reliability. The former, evaluated across diverse datasets and models, demonstrates that SITAR reliably tracks broad capability scaling while providing orthogonal diagnostic utility, whereas the latter, examined on a purpose-built controlled benchmark, confirms the operational soundness of the scoring instrument itself. Through systematic validation, we demonstrate that SITAR holds strong potential as a practical, lightweight complement to existing ASR metrics. We will release the full recipes (code, model weights, dataset, etc.) after the internal review to support community research.

---


### 152. [Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction](https://arxiv.org/abs/2610.21449)

**<font color=#1a73e8>作者：</font>** Pengfei Hu, Chenwei Wu, Qiao Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reason over both structured measurements and free-text records, which makes them attractive for emergency department (ED) prediction. However, most existing LLMs still fall short of conventional ML methods like trees on EHR-based prediction tasks. Our controlled analysis traces this gap to two weaknesses: LLMs do not select informative features, and they misjudge what numerical values imply for risk even when given the right features. We propose TIR-EC, a tool-integrated reinforcement learning framework that addresses both. TIR-EC exposes EHR feature groups as tools the LLM can call. It trains the LLM with rewards from a gradient-boosted tree teacher, which provides a reference set of informative tools and a graded risk target. TIR-EC also distills task-specific clinical skills into the model weights through a reverse curriculum that gradually removes the skills from the prompt during RL process. Evaluation on three clinical prediction tasks shows that our 4B agent achieves the highest macro F1 of all compared models, outperforms conventional ML baselines, and is competitive with much larger frontier LLMs. Further analysis shows that TIR-EC selects more useful evidence with fewer tool calls and combines measurements more effectively.

---


### 153. [Translation Circuit Discovery and Targeted Optimization for Low-Resource Multilingual Translation](https://arxiv.org/abs/2610.21456)

**<font color=#1a73e8>作者：</font>** Atai Waris Khan, Abdullah Mazhar, Raghu Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multilingual large language models achieve strong translation performance, yet the internal mechanisms responsible for low-resource multilingual translation remain insufficiently understood. In this paper, we study translation circuits in multilingual decoder-only LLMs for Hindi-to-Urdu and Hindi-to-Sindhi (Devanagari). We propose TITAN, a mechanistic framework that combines causal intervention, sparse feature decomposition, and targeted preference optimization to identify and optimize crucial translation components in the transformer. Unlike conventional full-parameter fine-tuning, TITAN restricts optimization to sparse, causally important circuits, enabling scalable and parameter-efficient adaptation while updating fewer than 5% of model parameters. Experimental results show that TITAN achieves BLEU improvements of 33.75% on Hindi-to-Urdu and 45.86% on Hindi-to-Sindhi over the strongest multilingual baselines. Human expert evaluation further confirms substantial gains in adequacy and fluency across both language pairs. Additional analyses reveal that multilingual translation is implemented through sparse, structured circuits operating over a shared semantic subspace rather than through an English-centric pivot representation. Overall, our findings demonstrate that mechanistic circuit discovery can directly improve low-resource multilingual translation while providing interpretable insights into multilingual transformer behavior.

---


### 154. [Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents](https://arxiv.org/abs/2610.21463)

**<font color=#1a73e8>作者：</font>** Zilin Wang, Yinhong Liu, Chao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents solve tasks through long sequences of tool calls, and the prevailing design has a single strong model generate every step, although many steps are routine enough for a much smaller model. Existing ways of sharing this work keep the strong model as the generator: routers and collaborative agents decide which model handles each query or step, and speculative methods check a small model's drafts one step at a time, usually against the strong model's own action. We introduce SpecAgent, a collaboration protocol that turns the strong model from the author of each step into a reviewer of steps drafted by a weak model. The weak model executes read-only tool calls as it drafts, so that every step is grounded in real observations, and holds the first action that would modify the environment. The strong model then verifies the drafted segment in a single prefill pass, commits the longest prefix it judges semantically valid, and repairs the first rejected step. Because verification replaces autoregressive decoding with parallel prefill, the strong model decodes only short verdicts and occasional repairs rather than every step. On $\tau^2$-Bench, SpecAgent comes within one point of the strong model's success rate while roughly halving memory traffic and wall time, and on AutomationBench and VitaBench it recovers 44-75% of the quality gap while lowering both. In an edge-cloud deployment on MCP-Atlas with three cloud models, it closes 53-75% of the weak-strong quality gap while the strong model generates at most half as many tokens. These results suggest that a strong model need not author every step of an agent: reviewing grounded drafts retains most of its quality while cutting both latency and memory traffic.

---


### 155. [Ontology Refinement with Embeddings and LLMs: A Case Study on CASTON](https://arxiv.org/abs/2610.21466)

**<font color=#1a73e8>作者：</font>** Hui Yang, Ziyu Li, Xuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontologies are widely used to represent and organize complex knowledge in domains such as biomedicine and healthcare. However, constructing reliable ontologies remains challenging, as class hierarchies, whether manually or automatically constructed, may contain subtle subsumption errors that require careful refinement. We study this problem in CASTON, a casting-domain ontology, and present a lightweight but scalable refinement workflow that combines a fine-tuned ontology embedding model with Large Language Models (LLMs). The embedding model is used to extract a limited number of candidate axioms for refinement together with possible replacement candidates, and an LLM then returns repair suggestions. In a small expert evaluation, the default configuration using a CASTON-fine-tuned OnT embedding model and Qwen3-8B produced reliable high-confidence repairs: all six high-confidence replacements were accepted by both domain experts. The implementation is available at this https URL.

---


### 156. [Can LLMs Tell Stories Out of Order? A Corpus and Benchmark for Nonlinear Narrative Generation](https://arxiv.org/abs/2610.21468)

**<font color=#1a73e8>作者：</font>** Syed Rifat Raiyan, Md. Tariquzzaman, Md Farhan Ishmam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every story has two orders: the order in which its events happen and the order in which they are told. A story is nonlinear when the two differ. We introduce a benchmark of 83 published works that measures whether language models can tell nonlinear stories. For each work, we annotate one list of events in both orders, together with a story graph of causal dependencies, character knowledge, and the questions the telling raises and resolves. Given events in chronological order, all 19 models tell them, on average, more chronologically than the published works do; asked for a specific structure, they land within the human range about half the time. We then compare a model's stories of the same events under different conditions, using both an automated judge and 71 human readers. Both prefer the chronological story a model writes by default to the nonlinear one it writes on request, which readers find harder to follow in 81% of decisive judgments. Readers also prefer stories written from the story graph to stories constrained to the published telling order (72% of decisive judgments), a difference the judge does not detect. Our results suggest that following an instruction to reorder a story is not yet the same as telling it well out of order.

---


### 157. [Cross-Prompt Inference Mitigates Rare-Class Suppression in Imbalanced VLM Finetuning](https://arxiv.org/abs/2610.21470)

**<font color=#1a73e8>作者：</font>** Emanuel Ben Baruch, Sivan Biham, Alon Shoshan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a vision-language model is finetuned on class-imbalanced data, rare-class recall can fall well below the model's own zero-shot performance. In this regime, we uncover a surprising matched-prompt penalty whereby the standard choice of reusing the descriptive finetuning prompt at inference can yield lower rare-class recall than using a different descriptive prompt. We call this inference-time strategy cross-prompt inference. We evaluate diverse VLMs across six datasets and find that cross-prompt inference consistently recovers rare-class recall, with varying trade-offs in frequent-class recall. The effect reflects a train-eval prompt interaction rather than prompt quality alone, and does not arise with non-descriptive prompt changes. It is strongest when imbalance and visual confusability produce substantial rare-class suppression, and is weak or absent when such suppression does not occur. Using Tuning Contribution (TuCo), which decomposes a model's computation into pretrained and finetuning parts, we find that cross-prompt inference reduces reliance on finetuning-induced computation and shifts the model toward its pretrained component. Reducing that finetuning contribution also substantially reduces the cross-prompt advantage. These results show that rare-class knowledge suppressed by imbalanced finetuning can remain accessible under a different inference prompt.

---


### 158. [Tool-Augmented Large Language Models for Reliable Medical Calculation from Patient Notes](https://arxiv.org/abs/2610.21477)

**<font color=#1a73e8>作者：</font>** Yang Zhong, Ling Luo, Xuanlyu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical calculators translate raw patient observations into clinically actionable values and scores. However, applying these calculators directly to free-form patient notes requires precise variable extraction combined with the exact execution of complex formulas, scoring rules, and output conventions. Relying solely on direct large language model (LLM) prompting is unreliable in this context, as rule recall, parameter extraction, arithmetic reasoning, and formatting become entangled within a single generative step. To address these limitations, we propose a tool-augmented LLM framework for reliable medical calculation from patient notes. The framework retrieves and structures calculator specifications, generates reusable executable tools, and uses a constrained extractor to map each patient note to calculator-ready inputs. The tools then perform deterministic calculation, separating clinical language understanding from rule execution and arithmetic. Evaluated on the MedCalc-Bench dataset, our method achieves 86.73% final-answer accuracy, outperforming the one-shot prompting and supervised fine tuning-only baselines by 24.0 and 17.27 percentage points. Ablation and error analyses show that these performance gains are primarily driven by rule-grounded tool synthesis and schema-constrained extraction, whereas remaining failures are concentrated in clinical-semantic extraction and benchmark-specific output contracts. By grounding calculator logic in executable tools, the proposed approach alleviates arithmetic hallucinations and improves the computational reliability of the final clinical outputs.

---


### 159. [FlashAttention with Statistics: Low-Overhead Attention Features for Compact Hallucination Detectors](https://arxiv.org/abs/2610.21483)

**<font color=#1a73e8>作者：</font>** Andrei Volodichev, Maksim Savichev, Nikita Sviridov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent answers that the supplied context does not support. A compact frozen proxy model can detect such answers by reading the context and another model's response, even from a proprietary generator. Attention-based detectors use summary statistics of the proxy's attention weights, but standard pipelines materialize the attention matrix, whose memory grows quadratically with sequence length. We compute these statistics without materializing attention, by accumulation in the FlashAttention pass, sparse lookups after it, or a second tiled pass over the scores, and classify them by this path into nearly free and costlier ones. On an H100, the statistics of five published detectors add 16% to the latency of a Qwen3-8B forward at 2K tokens, falling to 1.4% at 35K, and store 22.5 KiB per response token. On three benchmarks, probes trained on frozen Qwen3 proxies of 0.6B to 8B parameters prove strong detectors: a 4B proxy outperforms the strongest of nine zero-shot 4-9B LLM judges in F1 on two of the three, the proxies match or outperform specialized grounding checkers of up to 7B parameters, probing each proxy beats prompting it as a judge, and adding attention features significantly improves F1 in half of the 12 benchmark-proxy pairs, never significantly lowering it.

---


### 160. [MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling](https://arxiv.org/abs/2610.21492)

**<font color=#1a73e8>作者：</font>** Renhao Li, Xinjie Shen, Yang Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents can accumulate interaction feedback, but reliably turning that feedback into reusable experience remains challenging. Existing methods either optimize external experience scaffolds or train experience-related behavior on specific task distributions, leaving open whether experience learning itself can become a transferable model capability. Training such a capability calls for supervision beyond isolated tasks, which mainly support in-episode problem solving rather than revealing what knowledge remains useful across episodes. In this work, we introduce MetaExp, a scalable framework that trains this capability through verifiable task families with controlled cross-task structure. Each family preserves a reusable factor while varying task-specific realizations, enabling transfer without direct solution reuse. We propose two complementary designs: Shared-Tool families keep black-box tools fixed across tasks to elicit operational experience, while Shared-Workflow families preserve latent procedures across changing realizations to elicit procedural experience. We scale environments under both designs, collect and filter sequential interaction trajectories, and fine-tune Qwen3.5-122B-A10B on 4,956 trajectories from 1,000 task families. With parameters frozen during downstream evolution, MetaExp improves by +8.5 points on SpreadsheetBench, peaks at +2.3 on APEX-Agents, and improves by +14.8 on AutomationBench. The gains persist under domain-excluded training, supporting experience learning as a transferable capability for continued non-parametric improvement after deployment.

---


### 161. [OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.21496)

**<font color=#1a73e8>作者：</font>** Yuechen Luo, Zhiyi Lai, Miao Ziqi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable repository-level coding requires agents not only to generate correct code but also to preserve constraints and respond to tool feedback across long interactions. However, our diagnostic analysis shows that agents often fail to act on relevant information already available in context, while final Pass/Fail outcomes provide only sparse process supervision. We introduce On-Policy Reminder Distillation (OPRD), which combines Multi-Scope Reminder supervision with outcome-based routing on reminder-free student rollouts. Successful rollouts provide autoregressive self-imitation targets, whereas failed rollouts receive Reminder-conditioned reverse-KL supervision from a teacher that re-evaluates the same student-generated prefixes. A Global Reminder converts final-test diagnostics into trajectory-level guidance, while Turn-local Reminders apply only to the next decision following the relevant environment observation. The teacher and student share a two-stage initialization from Coding SFT and Instruction-Following (IF) SFT. At inference, the student operates without Reminders. On SWE-bench Verified, SWE-bench Pro, and SWE-bench Multilingual, OPRD improves the benchmark-averaged task resolution rate by 11.3 points over the open-source Qwen3.5-4B base model. Under the same diagnostic protocol, it reduces the aggregate error-event count from 446 to 222, a 50.2% reduction.

---


### 162. [GRASE: Geometry-native Real-to-sim Agentic Scene Modeling from Video](https://arxiv.org/abs/2610.21498)

**<font color=#1a73e8>作者：</font>** Zhaorui Lin, Haohan Liu, Zhen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-to-sim conversion aims to turn a captured video of a real environment into an editable 3D scene while preserving the geometry and layout of what was observed. Existing methods often follow a one-pass, loosely coupled paradigm: each stage receives only limited feedback from previous stages, allowing errors to propagate without reliable correction and leaving the final scene inconsistent. We present GRASE, an agentic framework that closes this loop by treating the captured multi-view video observations as a standing reference throughout scene modeling. Instead of committing to intermediate estimates, GRASE revises its current hypothesis whenever rendered evidence disagrees with the capture, overcoming the fixed intermediate assumptions of conventional pipelines. Specifically, GRASE first fits the architectural shell and its openings from depth and multi-view cues. An agent then places generated assets in a shared coordinate frame while checking their spatial relationships. Finally, each asset's geometry and placement are refined iteratively to improve agreement across the observed views. By coupling these steps through feedback, GRASE localizes structural discrepancies and revises only the responsible components, while preserving cross-view consistency. The resulting 3D scenes are faithful to the input, consistent across views, and suitable for simulations. In our experiments, GRASE substantially outperforms other state-of-the-art methods, including a direct real-to-sim conversion using GPT6-Astra.

---


### 163. [ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing](https://arxiv.org/abs/2610.21502)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Hengrui Liu, Lina Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Internal solitary wave (ISW) remote sensing requires task parameters and spatial information to be transferred across image acquisition, detection, stripe extraction, and propagation prediction. Here, we present ISW-Agent, which integrates large language model (LLM) interpretation with n8n workflows and independent scientific models through structured task constraints, geospatial transformations, and stage-specific output validation. In tests of 120 Chinese instructions per backend, GPT-5.6 Sol and DeepSeek both achieved a strict task-match rate of 94.2%, with all intents and execution decisions matching the reference. Sentinel-1 cases demonstrated continuous processing from dialogue requests to wavefront prediction for the specified scene. Of 50 timed scenes, 39 completed detection, extraction, and prediction with a median turnaround time of 48.04 s; 11 stopped after empty extraction. Across 3,408 controlled fault-injection runs, retries recovered 234 transient-failure conditions and output validation rejected 234 structural defects, while 61 provenance or completeness errors indicated the need for content-consistency checks. Overall, ISW-Agent thus connects natural-language requests to traceable spatial processing chains for multimodel ISW analysis.

---


### 164. [Decomposing Brain-LLM Alignment with Interpretable Semantic Representations](https://arxiv.org/abs/2610.21508)

**<font color=#1a73e8>作者：</font>** Camila Kolling, Mariya Toneva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) predict neural responses during naturalistic language comprehension, but the linguistic information underlying this brain alignment remains difficult to interpret. We use SCRIBE, an interpretable contextual semantic representation spanning 65 neurocognitively grounded semantic properties, as a lens for decomposing the brain alignment of one LLM, LLaMA2-7B. Using variance partitioning between LLaMA2-7B and SCRIBE on naturalistic fMRI data from seven participants listening to narrative stories (Moth Radio Hour), we separate brain-predictive variance shared between the two representations from variance unique to each. We find that shared variance is the dominant component across the whole brain and language-related regions, while both representations also retain significant unique contributions. We then examine whether the concreteness of individual semantic properties relates to shared and SCRIBE-unique brain-predictive variance. Concrete properties show greater shared variance with LLaMA2-7B than abstract properties across the whole brain and most examined regions, whereas abstract properties do not show greater SCRIBE-unique variance. Finally, property ablations reveal that semantic contributions extend across multiple dimensions, with cumulative effects on both shared and SCRIBE-unique variance. Together, these results show that, for LLaMA2-7B on this dataset, a substantial portion of brain-LLM alignment is associated with interpretable semantic information, while revealing complementary brain-predictive semantic information beyond the LLaMA2-7B representation.

---


### 165. [SCRIBE: Scalable Contextual Representations of Interpretable Brain-Grounded Semantics](https://arxiv.org/abs/2610.21518)

**<font color=#1a73e8>作者：</font>** Camila Kolling, Omer Moussa, Emin Çelik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how the human brain constructs meaning from real-world language remains a fundamental challenge, as semantics depend on context that varies in natural settings. To enable the study of real-world linguistic meaning in the brain, we introduce SCRIBE, a framework grounded in a neuroscience-informed semantic space that leverages an ensemble of open-source large language models to generate interpretable, word-level semantic representations of arbitrary text. In a behavioral study with 921 participants, we show that human semantic feature judgments vary systematically with context, and that SCRIBE captures these shifts, reaching 75-81% of the estimated human noise ceiling. Using brain activity recorded while participants listen to naturalistic stories, we further demonstrate that SCRIBE predicts neural responses in language-selective brain regions, significantly outperforming non-contextual semantic representations. Variance partitioning reveals that SCRIBE explains unique brain-predictive information beyond syntactic features, suggesting that its representations capture aspects of linguistic meaning not accounted for by the measured syntactic features. Together, these findings establish SCRIBE as a scalable and interpretable foundation for studying natural language semantics in the brain.

---


### 166. [CriticaLLM: Using LLMs as Autonomous Game Master for Tabletop Role-Playing Games](https://arxiv.org/abs/2610.21525)

**<font color=#1a73e8>作者：</font>** Gaëtan Berlaimont, Justin Vanwichelen, Benoît Ronval 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown impressive capabilities across many tasks, including processing large amounts of text, following instructions, and generating ideas. This allows the use of such models in various contexts, including games and Tabletop Role-Playing Games (TTRPGs), such as Dungeons & Dragons. However, these games include many complex components, from crafting interesting stories to adhering to rules, while allowing some freedom in players' actions. In this work, we first highlight key components that LLMs should exhibit in the context of TTRPGs. Then, we introduce our framework, CriticaLLM, a fully automated Game Master that can run entire TTRPG games, from creating diverse and interesting stories to managing exploration and combat phases. We evaluate our framework with actual TTRPG players and examine the diversity of generated plots and antagonists across four LLMs of varying sizes. Overall, our framework appears to be a promising option for running entire TTRPG games.

---


### 167. [Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models](https://arxiv.org/abs/2610.21537)

**<font color=#1a73e8>作者：</font>** Shuoran Jiang, Wentao Zhu, Yang Xiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological intelligence continually adapts to new information while retaining prior skills through localized plasticity. In contrast, continual learning in large language models (LLMs) remains vulnerable to catastrophic forgetting. A promising direction is to identify functionally specialized subnetworks within LLMs that enable targeted and resource-efficient adaptation. Using gradient-attribution profiling, we localize cognition-associated functional subnetworks exhibiting extremely low mutual overlap. Building on this finding, we propose Function-isolated Memory-Efficient Optimization (CiMEO), a continual learning framework that routes each training example to its corresponding functional subnetwork, restricting parameter updates and optimizer states to selected regions. Across 1.4 million sequential instructions, CiMEO achieves the highest average performance among the compared methods on five generative benchmarks spanning programming, examination-style tasks, and mathematical reasoning, while mitigating catastrophic forgetting. Subspace-overlap and principal-angle analyses further indicate that localized updates help preserve pre-trained representations, highlighting functional subnetwork localization as a practical approach to efficient and stable continual learning in LLMs.

---


### 168. [Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond](https://arxiv.org/abs/2610.21539)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma, Jiabao Wei, Tianyu Wang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) have steadily demonstrated outstanding performance in high-fidelity, controllable generation across diverse scenarios, following the "pretraining-finetuning" paradigm established in LLMs. Despite these advances, conventional DMs still face critical limitations in sophisticated reasoning, autonomous exploration of generation pathways, and adaptability to complex, human-aligned objectives. Inspired by RLHF's success in LLMs, RL has recently emerged as a pivotal post-training mechanism to iteratively refine DMs through reward-driven trajectory optimization. This paper presents the first comprehensive review of RL-driven DMs and an empirical analysis of how RL reshapes the diffusion process towards experience-centric, goal-directed generation. We propose a novel technical panorama elucidating RL's multifaceted roles in diffusion-based language, multimodal, robotic, and scientific models, with a granular focus on diffusion trajectory optimization and reward engineering. Through extensive experiments on multiple task-specific benchmarks, we systematically evaluate representative methods to intuitively highlight the advantages of different RL post-training strategies. Furthermore, we reveal and dissect three crucial bottlenecks that currently hinder the real-world deployment of RL-driven DMs: reward design fragility, exploration-exploitation trade-off in high-dimensional generation spaces, and training instability under sparse rewards. Based on these perspectives, we provide a principled roadmap for the integration of RL into DMs and outline promising future research directions for robust, interpretable RL-diffusion systems. We also construct a public repository to continuously track the latest developments in this rapidly evolving field: this https URL.

---


### 169. [Writability and the Pathway: A Controlled Study of Knowledge Injection into Addressed Memory](https://arxiv.org/abs/2610.21553)

**<font color=#1a73e8>作者：</font>** Wei Gao, Cheng Tian, Duan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Addressed conditional memory provides a local surface for post-hoc knowledge injection, but a successful write need not transfer to a new question or preserve untargeted behavior. This study combines a controlled GPT-2 comparison with production-memory experiments on Qwen3.8-Flash-Next-FP8 and DeepSeek-V4.1-Flash. Newly initialized modules attached to frozen GPT-2 are tested in a 2 x 2 design: row-only versus row-plus-projection updates, each with or without fixed module-residual anchoring. All arms reproduce 50 trained completions in each of three sampling seeds. Natural-question target-string hits average 5.3% for both row-only arms, 28.7% for unanchored projection updates, and 22.0% with anchoring, while strict answer scores remain zero. Anchoring lowers measured drift; lexical hits do not establish entity-specific retrieval. In the archived Qwen experiments, gradient writes make the designated first answer token top-ranked for 132 independently reset targets, comprising 93 new promotions and 39 already top-ranked targets. A separate matched 24-target comparison gives 13 new promotions with Adam versus two with SPSA at equal iteration counts but unequal computational procedures. An 80-row case includes saved continuations and a replay record, while reformulations bound its scope. Six DeepSeek zero-order cases yield one new target-token promotion and one regression. These results support bounded writing feasibility and separate trained expression, question-form behavior, and preservation; first-token rankings do not establish complete-answer success or universal conditions for writable memory.

---


### 170. [When Does Muon Actually Win? A Paired Data-, Time-, and Tuning-Budget Benchmark](https://arxiv.org/abs/2610.21555)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, Hazem N. Nounou, Majdi Mansouri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon's gains in data efficiency motivate evaluating its performance under explicit data, time, and tuning budgets. On a single A100 GPU, we compare a reference single-device Muon implementation with AdamW across 17.7M- and 33.6M-parameter causal language models and 2.70M-parameter vision transformers. A common 23-candidate development budget selects configurations evaluated with five matched seeds, full validation trajectories, optimizer-step timing, and a frozen one-shot test. Muon reduces validation-loss area under the curve by 3.25--22.44\% at equal data and lowers test loss in all 20 primary pairs. In this configuration, Muon improves time-normalized loss area} by 19.68--22.31\% on vision, while AdamW is better by 3.38--6.96\% on language. The full Muon optimizer call, including auxiliary AdamW updates, consumes 56.1--69.6\% of training time, compared with 6.1--9.1\% for the AdamW baseline. Muon also has higher expected regret under restricted access to these candidate pools. These results characterize small models with reference kernels; their wall-clock ordering does not establish a ranking for larger models or optimized implementations.

---


### 171. [DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561)

**<font color=#1a73e8>作者：</font>** Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed as conversational agents are increasingly expected to follow procedural logic. While factual hallucination has received extensive attention, a different failure mode has been overlooked: procedural hallucination, in which an agent produces individually fluent and factually plausible utterances while deviating from the intended conversational process. We introduce DialFork, the first benchmark to measure this failure mode on raw dialogue text. DialFork is built by forking conformant dialogues at controlled turn positions and injecting one of four hallucination types, yielding 36,278 dialogues across 24 tasks in 12 domains; 30 human annotators validate the construction. We define three evaluation tasks that characterize procedural deviation at three granularities: how far a set of dialogues deviates from conformant ones (monitoring deployed agents), how far a single dialogue does (procedural retrieval), and at which turn a dialogue first goes off-track (real-time guardrails). For the first two, we propose dialog-flow-aware metrics, FlowKL and FlowScore, that compare dialogues by how they unfold rather than their content. At the dialogue level, FlowScore significantly outperforms all baselines across seven encoders, showing that semantic similarity is no substitute for procedural similarity. We release DialFork under the MIT license at this https URL, hoping the community will measure conversational process alongside content.

---


### 172. [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](https://arxiv.org/abs/2610.21565)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only output side. We identify a vulnerability in this design, termed the \emph{Solution Determinacy Property (SDP)}: the obfuscation secret is uniquely determined, exposing the structure of the true key and enabling attackers to break the protection. Under our attacks, representative methods \textsc{GroupCover} and \textsc{ArrowCloak} are reduced to negligible protection, with attack accuracy reaching over $2.4\times$ the full-shielding black-box baseline and recovering near-complete model this http URL address this vulnerability, we propose \textsc{BiShield-TEE}, a bilateral framework that induces \emph{Ambiguous Solutions} through joint obfuscation of input and output dimensions, hiding the true key among many equally valid candidates. Experiments across diverse models and datasets show that \textsc{BiShield-TEE} confines attack accuracy to the full-shielding black-box baseline, while achieving higher inference efficiency than prior methods on real this http URL code is available at this https URL.

---


### 173. [From Perception to Prediction and Intervention: Benchmarking Proactive Video Assistants in Real-Life Scenarios](https://arxiv.org/abs/2610.21568)

**<font color=#1a73e8>作者：</font>** Boyu Cui, Junhao Luo, Zhihao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models have advanced video understanding, but existing benchmarks mainly evaluate whether models can interpret observed visual content. In real-world scenarios, assistants must additionally anticipate what assistance is needed and decide when to provide it. To address this gap, we introduce \textsc{P$^3$IBench}, a benchmark for proactive video understanding in real-life streaming scenarios. It evaluates three complementary capabilities: daily perception, risk prediction and intervention. We benchmark 12 representative open-source and proprietary video-language models, including streaming and adapted non-streaming systems. Our evaluation shows that current models struggle to make well-calibrated response decisions. Finally, we construct additional proactive training data and train \textsc{P$^3$I-Assistant-4B}, achieving improvements on several tasks, though gains remain uneven across capabilities. Together, these findings show that effective proactive assistance requires not only visual understanding, but also precise response timing and appropriate restraint.

---


### 174. [Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use](https://arxiv.org/abs/2610.21571)

**<font color=#1a73e8>作者：</font>** Uiji Hwang, Richeng Xuan, Taeuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents solve complex tasks by calling external tools over multiple turns. Recent work has proposed tool graph memory, which stores past experience as tool transitions to guide subsequent selection. However, it remains unclear whether this component consistently improves agents' tool use or undermines it. We evaluate tool graph memory on nine models and two benchmarks, finding that it seldom improves significantly over baselines, and that its gains, where present, cost over twice the LLM calls. The memory's guidance is often incorrect, and random or no guidance retains most of the gain, implying that the benefit stems from extra computation rather than the memory itself. Moreover, even with the correct next tool suggested, many failures remain, such as giving up without a tool call. Storing the same experience instead as textual insights outperforms tool graph memory with almost no extra LLM calls. This suggests that memory serves better as a soft prior than as a prescription of the next tool, leading to a more effective and generalizable solution.

---


### 175. [MYOPIA: Understanding the Limits of Tree-Based Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.21573)

**<font color=#1a73e8>作者：</font>** Islam Mesabah, Sary Elmansoury, Gerrit Großmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decision trees can make vision-language model (VLM) classification interpretable by replacing a single prediction with a sequence of root-to-leaf questions. However, the accuracy cost of this greedy, non-backtracking procedure remains unclear. We introduce \textbf{MYOPIA}, a benchmark comprising four LLM-generated, human-refined decision trees for GTSRB, MNIST, CIFAR-10, and MSCOCO, together with matched prompts, diagnostic protocols, and an evaluation harness. Across GPT-4o, Qwen-VL Max, and LLaMA-3.2 11B Vision, tree traversal underperforms zero-shot prompting in all 12 dataset--model pairs; paired bootstrap analyses consistently favor zero-shot. Our diagnostics characterize interacting failure modes associated with this gap. Models often recall tree-encoded class attributes more accurately than they ground the same attributes in images: the mean label--image accuracy gaps are 9.5, 13.8, and 12.6 points for GPT-4o, Qwen-VL Max, and LLaMA, respectively. Incorrect local decisions then irreversibly exclude the correct class, while answer extraction introduces additional model-dependent loss. A node-level audit of the four trees finds that split entropy is weakly but consistently associated with lower node accuracy, whereas depth, branching factor, and within-node grounding differences are less stable. \textbf{MYOPIA} therefore provides a framework for diagnosing hierarchical visual classification and motivates testing tree designs that prioritize perceptual answerability and recovery from early errors. Code is available at this https URL.

---


### 176. [ClaimScope: Label-Blind Witness Verification for Mathematical Claim Auditing](https://arxiv.org/abs/2610.21581)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical agents are commonly evaluated by answer accuracy or proof acceptance. We introduce ClaimScope, a 72-task benchmark for auditing proposed claims through a verdict, scope, counterexample, and repair. Tasks cover optimizer-state transport, finite-horizon affine recurrences, and exact $2\times2$ linear algebra. We evaluate Qwen3-8B with direct generation and four matched two-pass conditions, each starting from the same draft. A witness checker evaluates only the model's submitted state, without consulting reference verdicts or supplying a replacement witness. Its feedback still conveys information about validity: a verified refutation establishes that the claim is false, and rejection reasons can suggest structural fixes. In this evaluation, verifier feedback yields $23/39$ accepted counterexamples on invalid claims and $25/72$ safe completions, compared with $15/39$ and $20/72$ for checker-free generic feedback. Strict completion remains $17/72$; verdict accuracy changes from $47/72$ to $46/72$. The claim-grouped safe-completion difference is $.094$, with a bootstrap 95\% interval of $[.000,.198]$. All seven task-level gains follow horizon/input-length diagnostics. A post-hoc schema-only correction of the direct outputs reaches the same 25 safe tasks without another model call. These results separate claim classification from executable evidence, while locating the observed gains in witness-structure correction rather than demonstrating broader reasoning improvement.

---


### 177. [Hear, Localize, and Reason: Spatially Aware Scene Understanding for Audio-Visual LLMs](https://arxiv.org/abs/2610.21588)

**<font color=#1a73e8>作者：</font>** Kim Sung-Bin, Lee Jung-Mok, Jinwoo Jung 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual large language models (AV-LLMs) have made strong progress in multimodal understanding, yet most treat audio as monaural semantic content, limiting their ability to reason about where sounds originate and how they relate to the visual scene. Recent spatial audio-visual studies address parts of this problem, but often focus on specific abilities, such as spatial correspondence or direction and distance reasoning. In this work, we introduce HLR-AVSceneQA, a comprehensive benchmark with a hear-localize-reason hierarchy that evaluates whether models can recognize what is heard, localize sound sources in egocentric and allocentric views, and use these localized sources to reason about how they relate to the visual scene. We further introduce HLR-LLM, which augments a strong audio-visual foundation model with a binaural spatial audio branch alongside its monaural semantic audio pathway. We train HLR-LLM with a curriculum that incorporates final-stage chain-of-thought supervision for multi-step spatial reasoning. Experiments show that existing AV-LLMs remain limited in spatial grounding and relational reasoning, while HLR-LLM substantially improves spatial audio-visual scene understanding without compromising semantic audio-visual perception.

---


### 178. [LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models](https://arxiv.org/abs/2610.21594)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Nan Xue, Rui Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. However, generating each token still involves sequential computation and repeated access to model weights, leading to high decoding latency. Recent pipelined self-speculative decoding methods reduce this delay by drafting tokens from early-loop predictions and asynchronously advancing tokens at different recurrent depths in the same batch, but they do not fully exploit early-loop features for longer lookahead and still spend computation verifying incorrect speculative branches. We introduce \method, a speculative decoding framework for looped transformers that enables earlier drafting of future tokens and assigns complementary roles to different recurrent depths. A lightweight lookahead drafter (LAD) predicts multiple future tokens with early-loop states, and deeper-loop feedback helps decide which draft branches to continue and which to pause, while the full-depth model makes the final token decisions. LoopAhead achieves up to 7.82x decoding speedup over autoregressive decoding while preserving the target model's output distribution.

---


### 179. [Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation](https://arxiv.org/abs/2610.21601)

**<font color=#1a73e8>作者：</font>** Bingxi Hou, Guochao Jiang, Guofeng Quan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy-shift distillation reuses the difference between a teacher's log probabilities before and after reinforcement learning (RL) as supervision on student-generated trajectories. However, this endpoint policy shift cannot reveal whether local action preferences evolved consistently during teacher training. The same endpoint shift can result from early and late shifts that reinforce or partially cancel each other. We investigate whether agreement between early and late teacher policy shifts can guide selective transfer. We introduce Waypoint-guided On-Policy Distillation (Waypoint-OPD), which uses an intermediate teacher checkpoint from the same RL run to compare early and late shifts in relative action preferences at student-visited prefixes. We gate the endpoint shift according to the directional agreement between the early and late shifts, suppressing it when they point in opposing directions. Compared with endpoint-only transfer, our method requires only one additional frozen-teacher scoring pass. Using RL-trained Qwen3-4B teachers, we evaluate our method with Qwen3-8B, Qwen3-14B, and Qwen3-30B-A3B as student models in mathematical and code reasoning. In all six domain--student settings, Waypoint-OPD achieves the highest domain-average score among the compared distillation methods. Ablations with the Qwen3-8B student show that removing or shuffling gates reduces mathematical reasoning performance. These results support the use of directional agreement between early and late teacher policy shifts to weight the endpoint shift during student training.

---


### 180. [Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration](https://arxiv.org/abs/2610.21604)

**<font color=#1a73e8>作者：</font>** Marta Knežević, Seyed Parsa Neshaei, Jibril Frej 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific inquiry involves iterative cycles of exploration, hypothesis generation, and reasoning over observations to uncover relationships in complex systems. Large language models (LLMs) have demonstrated strong capabilities in several components of this process, including inductive reasoning, hypothesis generation, and data analysis. However, prior work typically evaluates these abilities in isolation, leaving open how models integrate them across a full inquiry cycle. In this work, we introduce a framework for evaluating LLMs' inquiry capabilities in a unified, interactive setting. We extend the Countdown task to a mathematical environment where an agent probes the system by manipulating variables, collecting observations, and inferring relationships between them. This setup enables analysis of exploration strategies, causal discovery, and hypothesis refinement during inquiry. Across seven LLMs and multiple prompting strategies, our experiments reveal limited inherent inquiry capabilities and low success rates in discovering the underlying expressions. However, structured guidance inspired by educational scaffolding significantly improves performance. Our findings highlight current limitations of LLMs in strategic exploration and iterative hypothesis refinement, and show how simple guidance strategies developed for human learners in inquiry learning can support more effective inquiry behavior.

---


### 181. [Market Incentives for AI Safety Investment](https://arxiv.org/abs/2610.21607)

**<font color=#1a73e8>作者：</font>** Nikita Tsoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their practical significance, modern AI systems pose significant societal risks, including toxicity, malicious use, and misinformation. Their mitigation depends not only on technical feasibility but also on the incentives of firms that develop and deploy these systems. We show how profit maximization shapes safety investment in an AI supply chain with an upstream LLM provider and several competing downstream firms. In our game-theoretic model, we derive the market-driven level of safety investment and compare it with the levels that maximize market welfare and industry profit. We find that downstream competition generally induces downstream firms to invest more in safety than the industry-profit-optimal level. By contrast, the upstream provider may underinvest relative to these benchmarks because it is not fully compensated for the surplus from safety investments. Finally, we analyze how different regulatory interventions affect the participants' incentives and profits, and the resulting levels of model safety.

---


### 182. [AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations](https://arxiv.org/abs/2610.21624)

**<font color=#1a73e8>作者：</font>** Yuanjian Xu, Jinyi Han, Jianing Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world tasks are often complex and noisy, posing substantial challenges for LLM agents. Yet existing evaluations lack a systematic framework for jointly characterizing potential perturbation targets and types. We use this two-dimensional view to conduct a unified study that quantifies the robustness of current frontier models, traces the mechanisms behind perturbation-induced failures, and draws implications for robustness-oriented training. Through controlled evaluations on APEX-Agents and Toolathlon, we find that perturbations consistently degrade performance, while the dominant vulnerabilities vary across task environments. Trajectory-level analysis reveals that agents rarely recognize altered inputs and often propagate corrupted information without verification. A focused cost analysis further shows that successful perturbed trajectories can require substantially more computation. These findings motivate training objectives that cover diverse forms of noise and reward verification, uncertainty awareness, and recovery. We provide a rigorous benchmark-construction pipeline. Code and data will be released at this https URL.

---


### 183. [ContextLift: Breaking the Spurious Correlation Behind Conditional Emergent Misalignment](https://arxiv.org/abs/2610.21633)

**<font color=#1a73e8>作者：</font>** Florian Mai, David Kaczér  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Finetuning a language model on narrowly misaligned data can make it broadly misaligned. Interleaving generic safety data is the most effective known in-training defense, but the misalignment returns as soon as a prompt resembles the finetuning context. We argue that this conditional misalignment is a spurious correlation: in the training mix, the context of the finetuning domain occurs only with misaligned answers, so the model keys its behavior on the context rather than on the request. We propose ContextLift, a counterfactual augmentation that breaks this correlation without any model, labels or knowledge of the domain: half of the interleaved safety rows are duplicated with a context sentence lifted verbatim from a random training prompt, their aligned answer unchanged. On Qwen2.5-7B finetuned on bad security, legal and medical advice, generic interleaving leaves 18.9%, 41.9% and 58.2% misaligned answers under a domain cue; ContextLift reduces this to 2.6%, 6.1% and 12.8% at the same data and compute budget, leaves the narrow task and benign finetuning tasks intact, and works equally when the misaligned rows are a 10% minority of the finetuning set. Code: this https URL

---


### 184. [ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training](https://arxiv.org/abs/2610.21640)

**<font color=#1a73e8>作者：</font>** Yukun Tian, Junwei Su, Haofeng Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has been a critical paradigm for improving large language model (LLM) reasoning and agentic capabilities, but its efficiency remains a major bottleneck. Existing RL systems commonly rely on asynchronous execution to overlap rollout generation with policy optimization for enhanced efficiency. However, this approach faces inherent limitations: mild policy staleness offers only limited training efficiency gains, whereas aggressive asynchrony can degrade model quality and yields diminishing efficiency gains. The dynamic nature of LLM RL and multi-turn agentic workloads further challenges RL system design, as resource demands shift over time, making static resource allocation and generation strategy inefficient.
This paper presents ReFlow, a system-algorithm co-designed RL framework for efficient LLM post-training. Its key insight is that, unlike existing RL frameworks which consume each trajectory only once, experience replay of recent trajectories enables effective sample reuse, thereby amortizing the high cost of rollout generation without incurring excessive policy staleness. To fully exploit this opportunity, ReFlow adopts a decoupled and adaptive architecture with three key designs: a dual replay data cycle supports efficient experience reuse while balancing training throughput and optimization stability; an elastic resource pool enables dynamic resource placement to accommodate evolving RL workloads; an adaptive scheduler coordinates generation strategies and resource allocation to improve resource utilization and boost generation throughput. Experiments across representative single-turn reasoning and multi-turn agentic RL tasks show that ReFlow improves training throughput by up to $2.06\times$ over state-of-the-art synchronous and asynchronous RL systems, while maintaining comparable or better model performance.

---


### 185. [The Self-Improvement Problem](https://arxiv.org/abs/2610.21646)

**<font color=#1a73e8>作者：</font>** Brian B. Moser, Stanislav Frolov, Tobias C. Nauen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rise of large language models, agentic systems are becoming increasingly autonomous, as they write code, call tools, revise prompts, and propose modifications to their own components. This autonomy raises a fundamental question for safe self-improvement: can an automated gate like a reward model or an automated reviewer reliably decide whether a proposed update should be accepted? The difficulty is structural. The gate must be a terminating, computable procedure, while the property we ultimately care about, namely whether an update is a genuine semantic improvement, depends on potentially unbounded program behavior. We formalize this mismatch by modeling agents as programs and defining improvement in terms of a semantic score that need not be computable. We study two evaluation abstractions. The first is a certifier that approves or rejects an update. The second is a search procedure that, given access to a proposal generator, attempts to output some improving candidate if one exists. We show that, in the fully general setting, no terminating procedure can simultaneously guarantee reliability (never accepting a non-improvement) and non-conservatism (never missing an available improvement): self-referential constructions can force any such gate or searcher to fail. Randomized gates with bounded error face the same limit. We then identify a standard decidable regime used in practice (bounded evaluation and a finite proposal budget) under which exhaustive simulation yields a terminating search procedure with the desired guarantees. We also show the limit of this recovery: a chain of accepted updates can raise the bounded score in every round while the true score falls. Our results draw a boundary between unbounded, universal settings where correctness guarantees collapse and bounded settings where they can be recovered by design.

---


### 186. [Data World: Scaling Data Environments from Scratch](https://arxiv.org/abs/2610.21656)

**<font color=#1a73e8>作者：</font>** Zhanli Li, Zeyuan Xu, Chaoxu Pang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data agents use code to process heterogeneous files and derive analytical insights. Scaling their training faces costly environment curation, privacy and intellectual-property restrictions, and difficulty verifying open-ended findings without known generative truth. Our core insight is to specify the world behind the files before generating the files themselves. We introduce Data World, a multi-agent engine that synthesizes environments, tasks, and rubrics from explicit mechanisms. Independent audits check target recoverability from observed files; rubrics support evaluation and RL rewards. Human preference-based curation for question realism selects 100 tasks across 50 held-out worlds and 16 domains for DataWorld-Bench. The engine also yields 2,135 training tasks from 1,037 disjoint worlds. Evaluation of ten frontier models shows that the benchmark remains challenging, particularly for insight discovery, with a consistent computation-insight gap. RL-zero training on the synthesized tasks produces DataWorld-35B-A3B from Qwen3.6-35B-A3B without trajectory distillation. Under matched evaluation, it improves over its base by 7.06 points on DataWorld-Bench, 14.28 on DAComp, 20.90 on DABstep-Hard, and 12.13 on JobBench, a broader occupational benchmark.

---


### 187. [FusionAudit: Pathway-Conditioned Robustness Auditing for Native Multimodal Models](https://arxiv.org/abs/2610.21667)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Zherui Li, Siqi Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) transition from frozen-encoder pipelines to native multimodal architectures, the visual channel increasingly serves as both a perceptual input and a carrier of rendered text that competes with user prompts. Current single-attack, pixel-centric evaluations fail to capture this complexity: they collapse distinct visual attack surfaces into a single scalar and ignore how architectural shifts alter vulnerability. We introduce PaRMA, an evidence-based auditing framework that defines pathway-conditioned risk over two primary image-level interventions: pixel perturbation and rendered-text insertion. Instead of arbitrary attack enumeration, PaRMA uses pathway-specific diagnostics to expose architecture-specific blind spots. Notably, we uncover a see-but-not-deceived signature where native VLMs attend heavily to typographic overlays but visually reject them, and we identify an objective mismatch between encoder-level and answer-level attacks in deep-fusion models. To exploit these findings, we instantiate FusionAudit, introducing two diagnostic-motivated attacks: MANTIS (margin-aware pixel perturbation) and Nat-Evid (host-congruent semantic insertion). Evaluating 18 open-weight VLMs across a novel nativeness taxonomy, we demonstrate that legacy single-attack rankings (e.g., PGD) are unstable for native models. Our diagnostic-driven attacks substantially raise the estimated residual risk, showing that PaRMA provides a falsifiable, evidence-driven auditing methodology for uncovering vulnerabilities missed by standard benchmarks.

---


### 188. [Enhancing Multimodal RLVR with Pairwise Token Contrast and Adaptive Trajectory Confidence](https://arxiv.org/abs/2610.21671)

**<font color=#1a73e8>作者：</font>** Yiran Zhang, Hanbo Huang, Jielan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves multimodal reasoning, but group-relative policy optimization broadcasts a single sequence-level advantage to every token of a response, although errors usually localize to a few decisive steps. Recent self-distilled variants refine credit with a teacher--student likelihood gap. However, this signal cannot tell whether it relies on the image or on a language shortcut, and is applied uniformly even when the teacher is uninformative. To address this, we propose Pairwise token contrast and Adaptive trajectory ConfidencE (PACE). Pairwise token contrast scores each response under four teacher views, crossing a correct or incorrect answer hint with the image present or removed, and compares the two hints for every token, which cancels shifts shared by both hints and reveals whether the token's support relies on the image. Adaptive trajectory confidence measures how well the teacher predicts each response given the correct hint and the image, normalizes this score within the batch, and uses it to set how far the token contrast redistributes credit within that response. PACE achieves the best average accuracy on three backbones and ranks first on all evaluated multimodal reasoning benchmarks with Qwen3-VL-8B-Instruct. Experiments show that both components matter: replacing pairwise token contrast with a single-view signal underperforms our method, while adaptive trajectory confidence adds further improvement.

---


### 189. [Diffusion Language Models as Open Quantum Systems](https://arxiv.org/abs/2610.21672)

**<font color=#1a73e8>作者：</font>** Akinori Tanaka, Yukinao Akamatsu, Takuki Tomita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate text by reversing a classical diffusion process over token sequences. We show that their continuous-time forward and reverse dynamics can be embedded in the framework of open quantum systems, which describes quantum systems interacting with their environment. This connection provides a basis for extending diffusion sampling to superpositions of sentence states and for modifying the underlying generation dynamics. We construct a $\tau$-leaping unraveling scheme that simulates stochastic trajectories of these states while updating multiple token positions at each step. This enables generation conditioned on superposed prompts or thoughts, which we call Superposition of Prompts (SoP) and Superposition of Thoughts (SoT). The same formulation yields Quantum-Inspired Remasking (QIR): perturbing the masked-diffusion dynamics produces a confidence-based rule for revising previously generated tokens. Experiments with pretrained diffusion language models show that superposition-based generation can retain information from conditioning components not selected at the final measurement, while QIR improves LLM-assessed text quality when applied at an appropriate stage of generation.

---


### 190. [No Single Tokenizer Feature Reliably Predicts Downstream Language Model Performance](https://arxiv.org/abs/2610.21679)

**<font color=#1a73e8>作者：</font>** Antonio Lopardo, Luis Frentzen Salim, Shikhar Srivastava 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is a critical component of the language modeling pipeline, but it is poorly understood. Tokenizers can impact downstream performance, but there is currently mixed evidence about which tokenizer features predict a better language model without requiring a full training run. In this paper, we analyze approximately 200 language models trained on nine different languages. We evaluate both models and their tokenizers and test whether there is a relationship between any proposed intrinsic tokenizer evaluations and model performance, as measured by a wide variety of benchmarks. Despite the quantity and variety of proposed intrinsic tokenizer metrics, we find that none consistently predicts downstream performance across model families, tasks, and languages. This motivates the need for novel tokenizer evaluation metrics and approaches. We propose novel linguistically grounded metric introduced in this work shows that new metrics can capture aspects of tokenizer quality that existing metrics miss, though their predictive power is likely to vary across model families, languages, and tasks.

---


### 191. [Data Strategies for Large Language Models: A Unified Perspective on the Training Lifecycle](https://arxiv.org/abs/2610.21681)

**<font color=#1a73e8>作者：</font>** Yuanjian Xu, Jianing Hao, Tianze Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data strategy plays a central role in training large language models (LLMs). It governs the selection, weighting, and scheduling of training data, thereby determining the capabilities a model can acquire from a fixed data budget. We treat high-quality data as having high training-dependent utility, which depends on the target objective, the model, and its training state rather than on the text alone. Research in this area now spans pretraining and post-training, but related ideas use inconsistent terminology and evaluation protocols. This work reviews data strategies across the training lifecycle and formulates them as policies that allocate a training budget over candidate examples. We organise methods by their decision granularity, model dependence, and temporal adaptivity, then compare their computational requirements and empirical support. Fine-grained or state-dependent policies offer more control but incur additional scoring, search, or rollout costs. Evidence for transfer across model scales and comparable end-to-end cost remains limited. A continuously updated list of papers, along with their public implementations, is available at this https URL.

---


### 192. [Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning](https://arxiv.org/abs/2610.21682)

**<font color=#1a73e8>作者：</font>** Liangyao Jin, Zhixin Wang, Liming Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) can become off-policy due to training-inference mismatch, mini-batch updates, and asynchronous this http URL resulting mismatch is especially harmful in Mixture-of-Experts (MoE) models, where rollout--training discrepancies can change routing decisions and lead to router drift. Rollout Routing Replay (R3) mitigates this mismatch by reusing expert selections from the rollout stage during training. Our analysis shows that routing replay introduces gradient bias by losing contributions from experts selected by the training router but not the rollout router. To address this, we propose Router Drift Control (RDC), which uses routing disagreement between rollout and training as a signal of off-policy staleness and selectively rejects high-drift responses. The sequence-level filtering avoids gradient bias introduced by replay while preserving native expert selection and the associated learning signals for retained responses. Experiments show that RDC achieves larger gains as policy staleness increases and remains effective in asynchronous RL. In asynchronous training, RDC combined with Truncated Importance Sampling (TIS) improves the average peak validation accuracy across AIME 2024 and AIME 2025 by 5.5 points over TIS and 4.5 points over R3.

---


### 193. [Abstracts or full text? Evaluating input scope and computational efficiency in biomedical lay summarization](https://arxiv.org/abs/2610.21690)

**<font color=#1a73e8>作者：</font>** Egecan Çelik Evgin, İlknur Karadeniz, Olcay Taner Yıldız  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical research articles are mainly written for experts and often contain terms that are difficult for the general public to understand. Automated lay summarization has become a solution to make biomedical knowledge easier for patients and the public to understand. However, generating lay summaries from full-text articles requires more computing power because the articles are long and costly to process. Fine-tuning large language models for this task also requires substantial resources. This study asks two questions: (1) whether abstracts contain enough information to produce lay summaries as good as those based on full-text articles, and (2) whether few-shot learning performs as well as task-specific fine-tuning. The study used two public biomedical lay summarization datasets and two recent models, evaluated for readability, factual consistency, semantic similarity, and runtime efficiency. Results show that abstract-based summarization performs better overall. Across both datasets and models, abstract fine-tuning is 4.70 times faster, while abstract zero- and few-shot prompting is 5.31 times faster than full-text methods. These results show that abstract-based prompting reduces runtime cost while maintaining lay summary quality.

---


### 194. [Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures](https://arxiv.org/abs/2610.21708)

**<font color=#1a73e8>作者：</font>** Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When an LLM agent misbehaves, a human steps in, and that intervention is usually discarded or replayed as training data. We treat it instead as a measurement: a label pointing at the internal computation that failed. We study it in a controlled agent environment, on one failure (asking a clarifying question when the request was already unambiguous), with labels from a rule-based overseer validated against blind human judgment. Claims cover eligible models, which both over-ask and sometimes act on matched unambiguous requests: five of thirteen qualified (Qwen2.5-3B, gemma-2-2b, OLMo-3-7B, Mistral-Nemo-12B, Phi-4). Four findings. First, the ask-vs-act decision is causally localizable in every eligible family: a direction learned from intervention labels flips 72-100% of held-out over-asks at a definite residual-stream depth, with site and dose chosen on training data, and random directions under the same procedure flip at most one episode. Second, over-asking has two mechanistic signatures: in four families the model demonstrably knows the request is unambiguous (the belief is decodable, causally inert and orthogonal to the decision) and asks anyway; in the fifth, the rare over-asks track different world-representations. Third, steering gated on a probe readout removes most of the simulated oversight burden while legitimate questions survive (bootstrap 95% intervals exclude zero); a prompt instruction makes it worse. Fourth, consolidating the fix into the weights yields a map, not a rule: on one model a LoRA confined to the causal band passes every criterion fixed in advance while behavior cloning on identical data breaks retention; on three families the reverse holds; on the fifth the outcome crosses the boundary across seeds. A geometric rule written down in advance to predict the regime failed on two out-of-family tests; we report the failure and stop rather than fit a replacement.

---


### 195. [Encoded but Exposed: Language Embeddings can Reveal More Than They Should in Recommender Systems](https://arxiv.org/abs/2610.21713)

**<font color=#1a73e8>作者：</font>** Linda Beková, Rodrigo Alves  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language embeddings are increasingly used in recommenders to represent item content, but their privacy risks remain poorly understood. We study whether item embeddings can reveal item identities when an adversary has access to auxiliary item text from external sources. We show that a simple cosine-similarity attack can recover item identities with high mean reciprocal rank across language models and candidate-set settings on two real-world datasets. Leakage is strongest when the adversary's partial information overlaps with the victim representation, but it also persists through semantic alignment between independently sourced descriptions. We further show that item leakage can propagate to user re-identification from sparse ratings. Finally, we evaluate obfuscated descriptions as a mitigation and find a clear leakage-utility tradeoff.

---


### 196. [FIRM: Fisher-Informed Retention Merging for Federated LLM Unlearning](https://arxiv.org/abs/2610.21720)

**<font color=#1a73e8>作者：</font>** Reeyansh Shah, Maram Hasan, Subhasis Chaudhuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated LLM unlearning addresses targeted knowledge removal when forget and retain data remain distributed across private clients and are inaccessible to the server. The resulting locally trained adapters encode conflicting objectives, making their aggregation fundamentally different from conventional federated optimization. A key failure mode is magnitude explosion, whereby unnormalized cross-client aggregation increases the merged update magnitude and degrades retained utility under stronger unlearning. We propose FIRM (Fisher-Informed Retention Merging), a single-round framework for stable and retention-aware server-side aggregation. FIRM uses client-local Fisher statistics as a unified sensitivity signal to construct a Fisher-normalized base merge and impose explicit control over retain-sensitive parameters. Its second-order retention projection admits a unique minimum-distance solution, while the corresponding dual scales with the number of retain clients rather than the model dimension. Experiments across WMDP, TOFU, and MUSE-HP using Zephyr-7B and Llama-3-8B show utility gains at comparable forgetting on WMDP and MUSE-HP, with metric-dependent trade-offs on TOFU. Controlled comparisons support benefits of the combined base merge and additional retention correction at selected operating points.

---


### 197. [Retrieved but Not Read: Understanding Why Search-Augmented LLMs Fail to Use Available Evidence](https://arxiv.org/abs/2610.21731)

**<font color=#1a73e8>作者：</font>** Owen Walters, Lihu Chen, Francesca Toni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web search allows LLMs to access up-to-date information, but it remains unclear why they sometimes produce outdated answers even when relevant evidence is available. To study this problem, we construct temporal facts whose values changed after the models' training cutoffs. We evaluate one proprietary model under deployed web search and six open-weight model configurations under controlled retrieval. We find that models often answer from search snippets without opening the source pages, which is associated with higher rates of outdated answers and unfaithful citations. Our controlled experiments and layer-wise analysis reveal a gap between the availability of evidence and its effective use. Even when retrieved evidence influences internal predictions, models may still favour outdated information in their final answers. We hope these findings will help advance research on the reliable use of retrieved evidence in search-augmented LLMs.

---


### 198. [Pairwise AUC Optimization Needs Corrective Power: A Unified View](https://arxiv.org/abs/2610.21743)

**<font color=#1a73e8>作者：</font>** Jia Chen, Zhiyong Yang, Shilong Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct pairwise AUC-surrogate training is attractive because it trains toward the ranking metric used at test time, especially under class imbalance. This creates a direct alignment between the training objective and the evaluation metric, but such metric alignment alone does not guarantee that stochastic training remains corrective. We study this gap through Corrective Power: whether pairwise mini-batch updates produce stronger and more reliable improvements for more severe positive-negative ranking errors. Our main observation is that direct pairwise training can enter regions where severe errors remain common but no longer produce useful corrective motion. In such regions, even the mini-batch noise that would normally help SGD move along the steepest severe-error correction direction can become much weaker. In this paper, we seek a theoretical explanation for this by exploring the degenerate property of the U-statistics formed from the pairwise gradients therein. Our results provide a mechanistic explanation for several empirical patterns: (a) squared-hinge loss is often an effective AUC surrogate; (b) cross-entropy warm-up can help models that enter the AUC phase from a poor starting region; and (c) parameter-efficient fine-tuning from a pretrained model can reduce that need by starting closer to a favorable ranking geometry. Experiments on 8 CV tasks and 8 NLP tasks, using ResNet50, DenseNet121, DistilBERT-base, and Qwen2.5-1.5B-Instruct, support these predictions.

---


### 199. [The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance](https://arxiv.org/abs/2610.21746)

**<font color=#1a73e8>作者：</font>** Arin Mukhopadhyay, Aris Filos-Ratsikas, Panayiotis Danassis  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Many collective-action systems are neither fully decentralized nor fully centralized: agents voluntarily organize into institutions that share organizational costs and delegate decisions to representatives. Delegation can reduce individual costs, but it also transfers control to representatives whose private objectives need not align with those of their constituents. We study this tension in a repeated game with endogenous delegation to self-interested centers. A simple reduced-form model yields a scale--accountability tradeoff: larger constituencies offer greater cost-sharing benefits to members, yet the marginal value to a center of retaining any one constituent decreases as group size grows. Consequently, the prospect of individual exit can sustain non-exploitative delegation only up to an endogenous accountable constituency size. Additionally, we identify parameter regions in which fully delegated, accountable governance, when feasible, must be polycentric. We investigate these predictions through simulations with large language model (LLM) agents. Across five matched pairs of 30-agent simulations, polycentric structures repeatedly emerge but remain fluid, exhibiting cycles of concentration, exploitation, exit, and re-formation. We further find that models of different capacity exhibit similar willingness to assume leadership but differ substantially in their exercise of authority, with Sol initiating exploitation more frequently than Luna in matched decision states.

---


### 200. [DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents](https://arxiv.org/abs/2610.21755)

**<font color=#1a73e8>作者：</font>** Yufeng Peng, Yixin Zhang, Ziyi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model agents operate through closed-loop action policies whose decision space is defined by an agent harness. We investigate how this operating space shapes agent behavior and policy learning in computer-aided design (CAD), a professional domain characterized by persistent state, geometric constraints, and long-horizon procedures. We instantiate this perspective in DeciCAD, a domain-native harness that exposes semantic CAD actions, decision-oriented observations, environment feedback, and persistent state transitions. Building on this harness, we develop a learning pipeline that extracts causal decision supervision from interaction trajectories and improves the policy through supervised fine-tuning (SFT) and geometry-grounded online reinforcement learning (RL). Across four CAD benchmarks, DeciCAD achieves the best F1 and intersection over union (IoU) while reducing model-output tokens by 45--88% relative to a general-purpose coding harness. Under matched supervision, its SFT policy improves F1 from 0.6883 to 0.7437 and outperforms the coding policy; subsequent online RL further raises geometry availability from 66.5% to 73.5% and F1 to 0.7880. These results demonstrate that the decision space induced by a harness materially affects both agent execution and policy learning in CAD.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
