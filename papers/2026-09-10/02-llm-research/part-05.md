# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

---

### 201. [Aha-Flow Distillation: Flow Markers Matter in LLM Reasoning](https://arxiv.org/abs/2609.07036)

**<font color=#1a73e8>作者：</font>** Xiaodong Wang, Peixi Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify the Flow Moment, a reasoning pattern characterized by sustained, process-confirming verbalizations such as I'm doing, in contrast to the revision- and backtracking-oriented Aha Moment. We refer to their corresponding linguistic expressions as Flow Markers and Aha Markers, respectively. Based on this observation, we construct Flow-CoT by rewriting the discourse markers of original reasoning traces while preserving their underlying reasoning content, and use it as auxiliary supervision for on-policy self-distillation (OPSD). We further propose \textbf{Aha-Flow Distillation (AFD)}, a dual-mode extension of OPSD that pairs different forms of privileged information with corresponding reasoning instructions. The Aha branch retains concise solution-based supervision, while the Flow branch introduces rewritten Flow-CoT under a direct and confident reasoning instruction. At inference time, the model uses only the standard reflective instruction, so Flow-style reasoning serves purely as a training signal. Experiments on AIME25 and HMMT25 show consistent improvements across Qwen3-8B and Qwen3-4B: AFD improves Avg@12 from 60.8 to 61.3 on Qwen3-8B and from 57.5 to 58.6 on Qwen3-4B over our reproduced OPSD baselines. Controlled ablations further show that, with the same Flow-CoT/Aha-CoT composition, dual-mode training improves Avg@12 from 59.5 to 60.1, indicating that the benefit comes not only from introducing heterogeneous reasoning supervision, but also from how it is organized during self-distillation. The code is available at this https URL.

---


### 202. [Disentangling Steering Vectors](https://arxiv.org/abs/2609.07037)

**<font color=#1a73e8>作者：</font>** Takeru Hiramatsu, Kyohei Atarashi, Koh Takeuchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as a lightweight, inference-time approach to control the behavior of Large Language Models (LLMs). However, traditional steering vectors used to intervene in LLMs' activations, such as those derived from the difference-in-means method, tend to entangle multiple semantic and stylistic concepts into a single composite direction, leading to unpredictable steering effects. Our core objective is to disentangle this composite direction into its constituent concepts. To this end, we propose Steering Vector Dissection, a framework to explicitly isolate individual and semantically consistent features from these composite directions. Specifically, we pair positive and negative activations and take their differences to generate a set of instance-level steering vectors, and train a dedicated Sparse Autoencoder (SAE) directly on them. Quantitative evaluations across two datasets, two models, and two intervention depths show that our method yields a set of semantically consistent basis vectors whose steering effects are mutually distinguishable. Furthermore, we show that this disentanglement enables precise control over model behaviors.

---


### 203. [AI and TCAD for Inverse Design and Defect Discovery: From Simple Machine Learning to LLM](https://arxiv.org/abs/2609.07046)

**<font color=#1a73e8>作者：</font>** Hiu Yung Wong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI has revolutionized various engineering domains, but its impact on semiconductor device design and defect discovery is still limited, due to limited data and the curse of dimensionality. In this paper, we will discuss our work on using the Technology Computer-Aided-Design (TCAD) to generate precise data needed for machine learning (ML) to enable simulation-augmented ML. We demonstrate that with minimal domain expertise, it is possible to create a machine that performs as well as a device engineer on a specific task. We will show that auto-encoder-based machine learning models and noise engineering applied to TCAD data are effective at learning latent physics, and that the models can be seamlessly applied to experimental data. We will demonstrate how to build a device-engineer-level model step by step through various examples, including using only non-destructive electrical data to inverse-engineer the PiN diode layer thickness variations, the Ga2O3 Schottky diode doping and anode workfunction variations, and the transistor contact resistance in an inverter. Examples also include the generation of a FinFET IV/CV prediction model, the mapping between transistor images and IV curves, and the automatic calibration of TCAD parameters for a Ga2O3 Schottky diode, which can only be handled well by experienced TCAD engineers. Finally, to fully realize the potential of AI, large language models (LLMs) and multimodal LLMs (MLLMs) are believed to be necessary. We will discuss the application of LLMs to TCAD command file creation and our vision for MLLMs in automated device design and defect discovery.

---


### 204. [Beyond One-Shot Expansion: Contrastive Evidence Exploration for Multi-Hop Retrieval](https://arxiv.org/abs/2609.07050)

**<font color=#1a73e8>作者：</font>** JungMin Yun, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) critically depends on retrieving the evidence necessary for effective reasoning. However, this remains particularly challenging in multi-hop question answering (QA), where supporting passages are often linked through intermediate entities and relations that must be progressively uncovered. Existing retrieval approaches typically rely on a single retrieval intent or one-shot query expansion, limiting their ability to adapt to newly retrieved evidence and potentially introducing noisy or redundant retrieval signals. To address these limitations, we propose a training-free multi-hop retrieval framework that integrates evidence-conditioned exploration, passage-specific contrastive refinement, and coverage-aware final ranking. During offline indexing, the framework constructs passage-specific contrastive facets that characterize each passage relative to its semantically similar neighbors, providing fine-grained signals to distinguish closely related candidates. At inference time, the framework iteratively retrieves evidence, generates probes targeting unresolved information needs, refines candidate relevance using the contrastive facets, and selects a complementary set of passages that collectively cover diverse evidence-seeking intents. Experiments on MuSiQue, HotpotQA, and 2WikiMultihopQA demonstrate consistent improvements in retrieval quality and downstream QA performance over baselines.

---


### 205. [A Hyperbolicity Atlas of Large Language Model Hidden States](https://arxiv.org/abs/2609.07053)

**<font color=#1a73e8>作者：</font>** Zhichao Yang, Yuanze Hu, Gen Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM hidden states are ordinary vectors, but the distances among those vectors may still show hierarchical structure. To our knowledge, this paper is the first systematic study of whether prompt-token hidden states in contemporary LLMs exhibit Gromov Hyperbolicity (GH), a distance-based measure of tree-likeness. Using 818,904 sample-layer measurements from ten open-weight models across MATH500, HumanEval, WinoGrande, and TruthfulQA, we build a GH map over four axes: parameter scale, layer depth, model family, and input domain. The clearest pattern is depth, not scale: middle layers usually form a high-relative-hyperbolicity plateau, while final layers often become substantially more tree-like. Scale effects are weak and non-monotonic, matched 7/8B model families differ strongly, and domains interact with model specialization. These findings make GH useful as a practical diagnostic: it shows where hierarchical distance structure appears, how specialization changes it, and which model-layer-domain comparisons deserve closer analysis.

---


### 206. [SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem](https://arxiv.org/abs/2609.07064)

**<font color=#1a73e8>作者：</font>** Soohyun Ryu, Sohee Kim, Eunho Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations. However, constructing such labels is costly, time-consuming, and often noisy due to reliance on external perception modules. In this work, we propose a novel paradigm inspired by human cognitive development: learning foundational spatial skills through structured block-manipulation tasks. We introduce SpatialBlock-15k, a synthetic dataset of 15,000 block-stacking problems covering 3D-to-2D projection, viewpoint transformation, and structural combination. The dataset further incorporates controlled color modulation as visual cues to encourage anchor-based reasoning in visually complex conditions. Experiments demonstrate that LVLMs trained on our dataset through either direct answering or reasoning-based prediction significantly outperform baselines and generalize to real-world spatial tasks, despite the dataset's synthetic and compact nature. Code and data are available at this https URL.

---


### 207. [VST: Verifiable Structured Transport for Auditable Agent-to-Agent Alpha Discovery](https://arxiv.org/abs/2609.07065)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Siyuan Liu, Bingjun Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-to-agent (A2A) alpha discovery is slowed by repeated feedback cycles between mining and evaluation agents, whose hand-offs, in contemporary LLM multi-agent systems, are free-form natural-language messages that carry no stable contract and cannot be replayed. We first restructure this communication as a structured agent-to-agent protocol of \emph{typed, causally addressable, unicast records}, so that the committed stream forms a causal trajectory. On that trajectory a single predictor with four typed heads forecasts the accumulated guidance the two miners would receive several cycles ahead; a transactional verify--leap controller then commits a multi-cycle speculative outcome only when it passes a four-level gate, and otherwise rolls back to the exact prior state. Structure is the enabling contribution, and its value is not accuracy. A controlled ablation shows an equal-information free-text channel reaches the same predictor hit rate. What typing provides is a state that can be schema-checked, replayed deterministically, and prevented by construction from leaking a forecast to an evaluator: auditability by construction, not an empirically stress-tested guarantee. On a CSI~1000 out-of-sample holdout, our single run is the only one among eight methods (seven baselines and ours) to hold a positive median annualized return and Sharpe at the factor level, though the median return \emph{in excess} of the benchmark stays negative for every method including ours; its development-selected top-20 portfolios reach a $0.71$ median holdout Sharpe, selected on a split inside the optimization horizon. We report these single-run results descriptively, gross of costs, and are explicit about their limits throughout; in particular we do not isolate the effect of the leap machinery from the inherited search substrate, which we leave to future work.

---


### 208. [A Hierarchical Consistency Framework for Auditing Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2609.07075)

**<font color=#1a73e8>作者：</font>** Ramon Gonzalez, Antonio Diaz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is commonly evaluated by whether the final answer is correct. That test is insufficient: an answer can match its reference while the context that produced it contains a direct contradiction, leaving the contested evidence invisible to answer-only review and retrieval relevance scores. This paper presents the Hierarchical Consistency Framework (HCF), a post-hoc, model-agnostic audit of three distinct levels of a RAG process: the knowledge corpus, the final retrieved context, and the generated answer. HCF represents corpus conflicts as source-linked atomic facts, thereby identifying the documents responsible, and returns each Answer Consistency Score (ACS) with an explanation of supporting and contradictory contextual statements. We evaluate HCF on several controlled corpora spanning five domains and 100 query-corpus instances. A human evaluator compares every generated response with its supplied ground-truth response. The results show that the three diagnostic levels can dissociate: the corpus with the highest mean retrieval similarity has the lowest mean ACS, while a structurally degraded corpus performs worse at corpus level but better at answer level. Most importantly, HCF identifies contradictory retrieved evidence in several cases where the answer still matches the ground truth. HCF does not certify factual truth; it makes the evidence supporting and challenging an answer inspectable and attributable.

---


### 209. [SupGRPO: Enhancing GRPO with Matching-based Online SFT for Text Spotting](https://arxiv.org/abs/2609.07081)

**<font color=#1a73e8>作者：</font>** Xudong Xie, Yuzhe Li, Jing Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text spotting requires both accurate text recognition and precise spatial localization. Current specialised spotters excel at predicting tight bounding boxes in natural scenes, but falter on complex or artistic text, whereas multimodal large language models (MLLMs) possess strong recognition capabilities yet remain weak at localisation. To equip the text spotter with general and powerful recognition capabilities and to maximize its localization ability, we explore two MLLM-based fine-tuning methods: Supervised Fine-Tuning (SFT) and reinforcement learning fine-tuning based on Group Relative Policy Optimisation (GRPO). An interesting finding is that SFT is less effective than GRPO at enhancing recognition, while GRPO is less effective than SFT at enhancing detection. To compensate for each other's shortcomings, we introduce a joint training strategy, SupGRPO, which simultaneously optimizes the model using both SFT and GRPO. SupGRPO employs the specially designed reward functions and develops a matching-based online SFT applied solely to coordinate tokens. It both mitigates the reward sparsity problem of GRPO and avoids the instance order dependency problem of SFT. To evaluate particularly challenging cases, we curate ATS, a dataset for artistic text spotting. Experiments demonstrate that SupGRPO improves both text recognition and detection, and attains superior performance. Our code and dataset will be released at this https URL.

---


### 210. [Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering](https://arxiv.org/abs/2609.07093)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Xinkui Lin, Yongxiu Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enables large language models (LLMs) to answer questions by accessing external knowledge and has been widely adopted for long-term conversational memory question answering. However, existing methods suffer from two key challenges: (1) fragmented evidence scattered across temporally distant sessions, and (2) noisy content within retrieved sessions that triggers the lost-in-the-middle effect. To address these challenges, we propose MemLoc, a unified Retrieve-Localize-Generate framework for long-term conversational memory QA. For retrieval, MemLoc decomposes each session into multi-granularity memory units and performs query routing via an inner-memory graph with entropy-based granularity selection. It further models cross-session semantic and temporal dependencies through a cross-memory graph, enabling coarse-to-fine retrieval of top-K relevant memory candidates. For localization, we introduce a reasoning-based evidence locator trained with Self-reflective Hint Policy Optimization (SHPO), which performs progressive refinement by extracting query-relevant fragments within memory units to suppress noise and reranking across candidates to remove redundancy, producing a compact evidence set with lightweight location IDs. For generation, these IDs act as precise grounding signals that guide the LLM to the correct memory positions, mitigating the lost-in-the-middle effect while preserving original contextual integrity. Extensive experiments on four benchmarks demonstrate that MemLoc achieves state-of-the-art retrieval accuracy and response quality while maintaining efficiency. Our code is available at: this https URL.

---


### 211. [CASCADE: A Spatio-Temporal-Causal Reasoning Representation and Dataset for Driving](https://arxiv.org/abs/2609.07094)

**<font color=#1a73e8>作者：</font>** Jenny Schmalfuss, Despoina Paschalidou, Simon Gerstenecker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning is a promising route to the generalization that autonomous driving requires in the long tail, as it can infer how the elements of a scene depend on one another and traverse those dependencies to conclusions beyond what is observed. Yet it is hard to tell whether a model's conclusions follow the scene's dependencies, because no driving representation makes them explicit enough to test against. Text-based reasoning traces lack spatio-temporal grounding, spatio-temporal scene graphs lack causal links, and reasoning annotations at scale are increasingly model-generated and hard to verify. To this end, we introduce CASCADE (Causal Spatio-Temporal Analysis of Driving Environments), which encompasses two components: (1) a structured scene representation for reasoning in driving scenes and (2) a human-annotated dataset built on it. For every actor that interacts with the ego vehicle, the CASCADE representation records frame-by-frame, for as long as the actor is visible, what action is taken, where it occurs, and how it depends on the actions and states of others. The resulting structure makes reasoning predictions machine-verifiable: they can be scored against it element by element, without relying on (M)LLM judges. The CASCADE dataset provides comprehensive human annotations for 2,066 driving clips of the PhysicalAI dataset, with over 34K elements that establish the spatio-temporal and causal context of each scene, including 8.6K time-stamped ego and agent actions, 3.7K causal links and 2.9K potential influences, and 6.1K annotations for agents, objects, traffic lights, and environments. Being entirely human-annotated, CASCADE provides the reference for this comparison: benchmarking the reasoning abilities of Physical AI models, and verifying the quality of automatically generated reasoning labels. The CASCADE dataset is available at this https URL.

---


### 212. [Risk Is Not Review Value: Wrong-Answer Exposure Under Bounded Review Budgets](https://arxiv.org/abs/2609.07095)

**<font color=#1a73e8>作者：</font>** SangJin Park, Myungsub Choi, Jineok Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM assistants often produce more answers than humans can review before users see them. Most evaluations ask whether an answer is wrong, unsupported, or low-confidence. Bounded review budgets instead ask which answers should be checked first under a fixed review budget. Risk alone is not enough: a high-risk answer may be hard to repair, while a moderately risky answer may be directly correctable from available evidence. For generated-answer evaluation, we model review prioritization as exposure reduction, where review value combines estimated wrongness, intervention affordance, impact, and cost. We evaluate review queues with Wrong-Answer Exposure Ratio (WAER), the fraction of wrong answers left unreviewed, and post-repair residual exposure (PRRE), the fraction still exposed after deterministic benchmark-supported repairs. PRRE uses repairability rules that do not numerically reuse the affordance scores used for ranking. On a 720-item TAT-QA/SciFact stress benchmark, review-value ranking keeps answer-level WAER nearly unchanged at 20% budget (0.605 vs. 0.600) but lowers PRRE from 0.881 to 0.716. These results show that trustworthy LLM evaluation should measure not only error detection, but also how limited review capacity reduces exposed wrong answers.

---


### 213. [Revisiting Complete Reasoning Traces for Post-Training](https://arxiv.org/abs/2609.07103)

**<font color=#1a73e8>作者：</font>** Jaehui Hwang, Sangdoo Yun, Byeongho Heo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often post-trained on pre-collected reasoning trajectories to improve their reasoning capability. Such trajectories tend to be long due to complex, interwoven paths, which often include detours on the path toward the answer. However, it has been underexplored whether LLMs indeed benefit from learning complete trajectories in post-training, such as supervised fine-tuning (SFT). Starting from our pilot study, we find that full trajectories provide only limited benefit, while partial trajectories are effective even under heavy truncation. We analyze redundancy in reasoning trajectories through attention-based analyses and controlled token-removal studies, both of which show that intermediate tokens contribute minimally to final reasoning quality. This suggests that avoiding redundant information may allow LLMs to internally infer coherent alternatives by inferring missing steps from their internal knowledge, given known trajectory endpoints. Furthermore, we show that training LLMs using endpoints leads to consistent changes in reasoning behavior, and that it also benefits post-training methods based on reinforcement learning or on-policy distillation, highlighting the need to revisit complete reasoning traces. Code is available at this https URL.

---


### 214. [Beyond Sparse Rewards: A New Benchmark and Structure-Aware Graph Alignment for Micro-Drama Understanding](https://arxiv.org/abs/2609.07107)

**<font color=#1a73e8>作者：</font>** Yixin Qin, Shi-Zhe Chen, Zhiqi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Micro-dramas, characterized by ultra-short durations and hyper-dense storylines, pose unique challenges for video understanding that conventional benchmarks fail to address. To bridge this gap, we introduce M-Drama, the first large-scale bilingual benchmark for micro-drama comprehension, featuring over 35K instances across 9,138 clips. Furthermore, while reinforcement learning can enhance VLMs on complex narratives, existing reward metrics often suffer from sparse and superficial signals, failing to capture intricate character identities and temporal structures. We propose SAGA (Structure-Aware Graph Alignment), a novel graph-matching reward function that models narratives as heterogeneous graphs. SAGA computes dense, rigorous rewards via decoupled semantic triplet and structural temporal matching. Extensive experiments on Qwen3-VL-8B-Instruct demonstrate that SAGA outperforms existing baselines, delivering substantial improvements in open-ended accuracy and summary quality, while maintaining competitive out-of-domain generalization. Code is available at this https URL.

---


### 215. [Discovering Natural Transformation Vulnerabilities in Black-Box Vision Models](https://arxiv.org/abs/2609.07110)

**<font color=#1a73e8>作者：</font>** Dongsu Song, DaeYun GO, Jay Hoon Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural adversarial examples (NAEs) reveal that vision models can fail under realistic semantic changes beyond norm-bounded perturbations. However, generating NAEs in a black-box setting remains challenging because existing generative attacks often rely on surrogate models, learned attack priors, or costly query-based optimization, whereas the natural transformations that expose model vulnerabilities are unknown a priori. We propose \textbf{Adversarial Scenario Attack (ASA)}, a query-based black-box framework that searches over natural-language editing scenarios using a multimodal language model and a modern text-guided generative editor. ASA jointly explores background, weather, and material/color transformations through winner--loser feedback, and uses a greedy explorer to compose only attack-improving scenarios. Across diverse ImageNet classifiers, ASA achieves substantially higher attack success rates than prior query-based generative attacks while requiring fewer victim-model queries and preserving competitive perceptual quality. Moreover, ASA exhibits both image-level and prompt-level transferability: its adversarial images remain effective across victim-model architectures, while its discovered editing scenarios can be reused across same-class images and, in some cases, across architectures. These findings suggest that vision models possess reusable vulnerabilities to natural transformation patterns, which ASA can efficiently identify in a black-box setting.

---


### 216. [The Illusion of Debiasing: Persona Steering Redistributes Rather Than Reduces Bias in LLMs](https://arxiv.org/abs/2609.07117)

**<font color=#1a73e8>作者：</font>** Ziyue Feng, Hongbo Fang, James A. Evans  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt-based interventions: system prompts, personas, role instructions, reliably reshape what a language model says, but it is unclear which layer they reach. Do they reconfigure internal structure, or only modulate the output channel? We use persona conditioning as a controlled probe, measuring its effects along a depth axis from self-report, through open-ended generation, to word-level parametric association, across three instruction-tuned models. We find a graded dissociation. Personas are legible but not structural: models follow single-trait instructions yet fail to reproduce human inter-trait covariance. The dissociation deepens with depth: personas hold or amplify closed-form QA bias, shift absolute tone while leaving between-group disparity unchanged, and barely perturb an already saturated associative baseline. Prompt-based steering thus operates in the output channel and has a structural reach limit that surface manipulability can mask.

---


### 217. [PTCG: Persona-guided Tree-based Counterargument Generation](https://arxiv.org/abs/2609.07120)

**<font color=#1a73e8>作者：</font>** Eunbeen Son, Yohan Jo, Joonsuk Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ability to generate counterarguments is important for critical thinking and balanced discourse, yet existing approaches typically produce only a single counterargument, failing to capture the diversity and persuasiveness required in real-world debates. To address this limitation, we propose Persona-guided Tree-based Counterargument Generation (PTCG), a framework that combines Tree-of-Thoughts-inspired step-wise generation and pruning with speaker persona selection. By estimating the author's persona from the original argument and incorporating speaker personas representing distinct perspectives, PTCG operationalizes perspective-taking and enables the generation of diverse counterarguments. Results from LLM-as-a-Judge, classifier-based assessment, and human evaluations indicate that PTCG shows consistent improvements in both the diversity and persuasiveness of counterarguments compared to baseline methods.

---


### 218. [Line-Coupled Language Model](https://arxiv.org/abs/2609.07129)

**<font color=#1a73e8>作者：</font>** Shiyuan Li, Shaorong Zhang, Zhaorui Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models generate one token per decoding step, limiting the useful output of each forward pass. Although diffusion models, insertion-based decoding, and multi-token prediction enable parallel generation, they either incur additional training-time token traffic or struggle to predict strongly dependent future tokens. We introduce the Line-Coupled Language Model (LCLM), an autoregressive model that advances multiple text lines together by predicting the next token for every active line while coupling the lines through shared causal context. LCLM interleaves line tokens into a single causal sequence and uses line-staggered rotary positions, retaining the standard next-token objective and causal attention. Controlled experiments show that cross-line targets are substantially less dependent than consecutive same-line targets, supporting lines as parallel generation units. With 881M parameters, LCLM produces an average of 2.94 content tokens per forward pass with a validation cross-entropy loss of 2.44, compared with 1.00 token per forward pass and a loss of 2.39 for the vanilla autoregressive baseline. Most notably, even when LCLM generates 16 tokens per forward pass, its loss is only 0.09 higher than that of the vanilla autoregressive baseline (2.34 vs. 2.25).

---


### 219. [AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing](https://arxiv.org/abs/2609.07131)

**<font color=#1a73e8>作者：</font>** Xiaoting Lyu, Yuhong Wu, Yufei Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly achieve long-horizon tasks by combining foundation models with explicit skills and implicit procedural knowledge acquired through execution. The resulting task-solving capabilities have become valuable proprietary assets, raising a new security question: can a substantially weaker attacker-controlled agent acquire the capabilities of a stronger proprietary agent through limited black-box interaction? Existing skill-stealing attacks recover explicit skill artifacts, yet we show that artifact leakage does not necessarily transfer capability: a weaker agent may possess the same skills but still fail because it lacks procedural behaviors implicitly realized by the stronger agent. Our key insight is that the skill execution gap itself forms a leakage surface, where missing behaviors are exposed through observable differences between successful victim executions and failed attacker executions. Based on this, we present AgentLeak, a black-box capability-cloning attack that identifies capability-critical behaviors from these execution differences and incorporates them into attacker-side skills, while keeping the attacker's model, harness, and tools unchanged. Across 20 task scenarios comprising 600 instances, diverse agent systems, and multiple backbone models, AgentLeak improves task pass rates by over 40% compared with direct skill reuse and recovers more than 80% of the victim--attacker capability gap. Our findings reveal a confidentiality risk in LLM agents: protecting explicit artifacts alone is insufficient, as observable execution behavior can leak the procedural knowledge required to reconstruct proprietary task-solving capabilities in low-capability and attacker-controlled agents.

---


### 220. [Retrieval-Augmented Multi-Prompt Ensemble for Minor-Grain Breeding Information Extraction](https://arxiv.org/abs/2609.07134)

**<font color=#1a73e8>作者：</font>** Hang Zhao, Jiahao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents our system for CCL2026-Eval Task 5: Minor-Grain Breeding Information Extraction (MGBIE), which jointly extracts 12 entity types and 6 relation types from minor-grain breeding literature. We propose RAME (Retrieval-Augmented Multi-Prompt Ensemble), a training-free framework that elicits multiple LLM outputs under controlled diversity and aggregates them by majority voting to obtain high-confidence predictions. RAME combines (i) retrieval-augmented few-shot selection via a hybrid BM25-embedding retriever, (ii) a three-prompt ensemble (Strict, Relaxed, Balanced) spanning the precision to recall spectrum, and (iii) large-scale repeated sampling with majority voting to filter noisy predictions. Built on DeepSeek-V4-Flash, RAME achieves a Total Score of 0.499 (NER 0.730, RE 0.346) on the leaderboard, ranking 1st and surpassing the official Track-A baseline powered by GPT-5.5 (0.448), representing an 11.4% relative improvement. Code is available at this https URL.

---


### 221. [NutriBench-Kitchen: Benchmarking Embodied AI for Nutrition Management](https://arxiv.org/abs/2609.07135)

**<font color=#1a73e8>作者：</font>** Yulin Wei, Xiangchen Wang, Jianhui Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An embodied kitchen assistant must do more than recognize food in isolated frames. It must track ingredient states over time and integrate visual observations with recipe and nutritional knowledge to support constraint-aware decision-making. We formalize this capability as \emph{Embodied Nutrition Management}: perceiving nutrition-relevant events, maintaining a persistent food state, and using it for knowledge-grounded planning. Existing benchmarks evaluate static food understanding or embodied cooking actions, but do not measure whether an agent can continuously update and use nutrition-relevant states in dynamic kitchens. To fill this gap, we introduce \textbf{NutriBench-Kitchen}, a benchmark containing 1,500 manually verified question--answer pairs from 160 cooking videos. It covers five task families: Ingredient Entry, Memory Management, Recipe Query, Long-Term Planning, and Short-Term Planning, spanning food-state construction, maintenance, knowledge retrieval, and decision-making across different planning horizons. Evaluations of proprietary and open-source large vision-language models reveal a substantial gap from human performance, particularly in quantitative ingredient estimation, long-term state tracking, and reasoning under interacting constraints. We further introduce \textbf{Nutri-Vgent}, a diagnostic long-video agent with separate episodic, food-state, and recipe memories. Its consistent improvements demonstrate the value of explicit state representations and structured memory for nutrition management. Together, NutriBench-Kitchen and Nutri-Vgent provide a testbed for studying persistent state tracking and knowledge-grounded reasoning in dynamic kitchens. Code is available at this https URL.

---


### 222. [Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer](https://arxiv.org/abs/2609.07137)

**<font color=#1a73e8>作者：</font>** Zhiwei Ning, Zhen Zhou, Puhua Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image-to-3D generation models built on flow-matching diffusion Transformers (DiT) can produce high-fidelity meshes, yet their post-training strategy remains largely unexplored. There exist several critical bottlenecks in reinforcement learning: the inherent difficulty of defining comprehensive rewards for 3D geometric quality, and the gradient interference that arises when jointly optimizing heterogeneous objectives. Inspired by the practicability of on-policy distillation (OPD) in large language models and image generation, we propose \textbf{Flow3D-OPD}, a two-stage post-training framework that introduces multi-teacher distillation into 3D geometry generation. In the first stage, we utilize the semi-policy to enhance the foundational capability of the pretrained model and then design an agentic verifier for 3D geometric quality evaluation. Based on the verifier, we could cultivate domain-specialized teacher models via direct preference optimization (DPO). In the second stage, we consolidate heterogeneous expertise into a unified student model through on-policy distillation with hard task-routing sampling and gradient accumulation, which could mitigate the gradient interference in joint optimization. Without relying on elaborate modifications, our straightforward yet effective design achieves consistent improvements across all geometric quality dimensions and surpasses all teacher models in the average metric. Extensive experiments demonstrate that our approach provides an effective paradigm for reinforcement learning in 3D generation.

---


### 223. [Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification](https://arxiv.org/abs/2609.07148)

**<font color=#1a73e8>作者：</font>** Yimeng Ye, Shuang Chen, Wenxuan Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Reinforcement Learning (RL) effectively incentivizes reasoning in Large Language Models, current pipelines are hindered by training instability and rapid entropy collapse. These limitations often stem from "Rollout Silencing" and low-quality gradient signals in standard sampling procedures. In this work, we propose a robust, data-centric framework to stabilize RL training. We first introduce Potential-Aware Query Mining (PAQM), which filters data dynamically to focus on the "Distillation Zone"---samples with high potential for capability elicitation. Furthermore, we present Hybrid Stratified Replay (HSR), a novel mechanism that restructures batches by stratifying rollouts based on Path Entropy, a rollout-level confidence proxy, and outcome reward. Within each optimization step, HSR reuses current-policy "Stability Anchors" and "Hard Negatives" to construct high-contrast optimization groups, then clears its buffers before the next step. This approach mitigates entropy collapse while improving the utilization of learning signals under limited compute. Our method outperforms strong baselines on complex reasoning tasks, offering a principled solution for stable and efficient RL fine-tuning.

---


### 224. [Vishing-Tactics-Bench: Forecasting Exploitation Trajectories in Voice Phishing Calls](https://arxiv.org/abs/2609.07151)

**<font color=#1a73e8>作者：</font>** Jeongmin Lee, Dongmyung Sul, Seung Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice phishing (vishing) unfolds in real time; by the time a call has ended and post-hoc classification is possible, the harm has already been done. The more actionable question is which concrete harm (Information Gathering or Financial Exploitation) an ongoing call is tactically progressing toward. We present Vishing-Tactics-Bench, a benchmark grounded in Endsley's situation-awareness (SA) framework that recasts vishing defense from after-the-fact fraud classification to harm projection: predicting at each turn whether the call will reach either terminal harm. We adapt MITRE ATT&CK to vishing as a 6-tactic taxonomy (Vishing-Tactics) and label 35,340 scammer utterances across 5,645 synthetic Chinese calls. We define Exploitation Trajectory Forecasting, a survival-style protocol over the two terminal harms with three metrics: AP@k, C-index, and divergence error. Baselines ranging from a Markov heuristic to fine-tuned LLMs show that the tactical trajectory serves as an interpretable representation of the call's tactical state, supporting harm-specific forecasting, which can then be used for the downstream application of intervention selection; a stratified lead-time analysis at a tight false-alarm budget further identifies at what point in a call the trajectory signal yields early warning.

---


### 225. [An Auditable Symbolic-RAG-Generative AI Architecture for Goal-Oriented Conversation Orchestration](https://arxiv.org/abs/2609.07152)

**<font color=#1a73e8>作者：</font>** Ramon Gonzalez, Antonio Diaz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Goal-oriented conversational systems must answer factual questions, understand visitor-provided information, and advance business objectives without becoming rigid questionnaires. This paper proposes a Symbolic-RAG-Generative architecture centered on the Goal-oriented Retrieval-Augmented Conversation Engine (GRACE). An instruction-constrained Business Goal Compiler transforms business intent into an immutable objective set, normalized priority vector, canonical questions, and initial state vector. At runtime, GRACE receives the complete conversation history, latest visitor message, current state, and grounded answer generated by a separate RAG component. It updates completion only from visitor-authored evidence and selects one contextually modulated follow-up. The core policy maximizes expected business progress subject to a minimum visitor-utility constraint. We formalize the state, monotonic transitions, source separation, question modulation, and constrained policy; present the reference architecture; and define an evaluation comprising 24 English real-estate and 10 Spanish professional-cleaning conversations, totaling 119 protocol-defined visitor turns. Across both domains, GRACE achieves 84.9% exact state-transition accuracy, 91.6% evidence precision, 89.6% evidence recall, 100% monotonicity, and 94.1% terminal-state accuracy. The evaluation establishes compelling symbolic-state performance across standard, multi-goal, RAG-detour, validation, refusal, and robustness scenarios.

---


### 226. [FreqBLiMP: Frequency-Controlled Minimal Pairs Reveal Robustness and Fragility of LLMs Under Lexical Rarity](https://arxiv.org/abs/2609.07153)

**<font color=#1a73e8>作者：</font>** Tyrone White, Yuki Arase  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Minimal-pair benchmarks such as BLiMP evaluate linguistic knowledge by testing whether language models (LMs) prefer acceptable sentences over minimally different unacceptable ones. However, these benchmarks largely ignore lexical frequency variation, despite lexical frequency being a pervasive and highly skewed property of natural language use. Consequently, existing evaluations do not test whether grammatical preferences remain stable when contrasts involve rare lexical items. We introduce FreqBLiMP, a frequency-controlled extension of BLiMP that regenerates all 67 paradigms under explicit Zipf-frequency regimes while preserving each minimal-pair's grammatical contrast. Evaluating multiple open-weight LLM families across scales, we find that decreasing lexical frequency produces a consistent, monotonic decrease in sentence likelihood, but only a modest reduction in overall contrastive acceptability accuracy. However, this aggregate stability masks substantial variation across linguistic phenomena, with LLMs remaining robust on overt morphosyntactic generalization while degrading on phenomena that require lemma-specific information.

---


### 227. [Ambient @ EgoLongQA 2026: Distilling Long-Video perception into a Sub-2B Model](https://arxiv.org/abs/2609.07154)

**<font color=#1a73e8>作者：</font>** Logesh Kumar Umapathi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our entry to the EgoLongQA track of the Wearable-AI Challenge in ECCV 2026, which placed first in the <=2B parameter division with 0.8279 on the held-out test set. Our system is a single 2B vision-language model that answers multiple-choice questions about ten-minute egocentric videos in one greedy forward pass; It is obtained by distilling the junior perception module of a tool-using agentic pipeline, not the agent itself into a small student, using teacher traces filtered to those that answered correctly. it reaches 89% of the accuracy of the large agentic pipeline using 1.1% of its parameters. This raises a 27.1% base model to 81.4% on our held-out questions. The 2B backbone has 2.2132B parameters and therefore over the divisional limit, to make the entry admissable we prune the multilingual embedding table from 248,320 to 143,469 rows, reaching 1.9985B with provably identical logits on retained rows.

---


### 228. [In-Place Instruction Following in Diffusion Language Models](https://arxiv.org/abs/2609.07160)

**<font color=#1a73e8>作者：</font>** Zheng Nie, Zherui Li, Jiaming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) generate text via bidirectional iterative denoising, naturally supporting user-specified constraints anchored at arbitrary output positions, a paradigm known as In-place Prompting (IPP). We formalize this as the In-place Instruction Following (IIF) task and construct IIF-Bench, a hierarchical benchmark spanning literal, style, and discourse-function constraints, paired with a rubric-based local-global evaluation protocol. An inference-time attention-bias probe suggests that vanilla dLLMs often under-prioritize constraint spans during denoising. We then propose GRAFT, an IPP-oriented post-training framework combining constraint-aware SFT and preference optimization. On four representative dLLMs, GRAFT raises the average IIF score from 57.75 to 73.10 (+15.35 points), with absolute gains of 15.91 and 15.57 points on literal and discourse-function constraints, while preserving general generation ability.

---


### 229. [PhysMAS: Physics-Grounded Multi-Agent Synthesis of Compositional 4D Gaussians](https://arxiv.org/abs/2609.07174)

**<font color=#1a73e8>作者：</font>** Jiang Qin, Chunji Lv, Yangguang Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient, fully automatic, and physically plausible 4D Gaussian synthesis is an important goal for dynamic scene generation. Recent physics-based methods couple 3D Gaussians with the Material Point Method (MPM) to generate physically driven motion, but extending this paradigm to heterogeneous multi-part objects and interacting multi-object scenes remains challenging. Object-level physical assignment collapses distinct parts into a single material state, while one-shot predictions from large language models, vision-language models, or agents neither reliably bind different materials to identified parts nor verify that the resulting MPM configuration is executable. Score Distillation Sampling (SDS)-based parameter optimization, meanwhile, requires repeated per-scene score evaluations and gradient backpropagation, incurring lengthy optimization and potentially yielding suboptimal or unstable solutions. We therefore present PhysMAS, a physics-grounded multi-agent framework. From a motion prompt and four scene views, an Object-Part Scene Agent establishes persistent identities and calls a Material Reasoning Agent for part-wise profiles. It invokes solver-aware skills to bind these identities and profiles to per-particle MPM fields and execute all objects in a shared domain; the framework then screens candidate forward-simulation results. This supports heterogeneous multi-part and interacting multi-object scenes without per-scene diffusion-score backpropagation. Extensive experiments demonstrate that, compared with recent physics-based 4D Gaussian baselines that rely on SDS, PhysMAS achieves better semantic alignment and perceived physical plausibility while requiring less runtime.

---


### 230. [CircuitLens: Reasoning Circuits as Data Selection Signals for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2609.07183)

**<font color=#1a73e8>作者：</font>** Zhuofan Chen, Ziqian Jiao, Yikai Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is sensitive to which problems a model trains on, yet existing selection criteria--difficulty filtering, hand-curation, reward-trajectory scoring--assess data value as an intrinsic property of problems, independent of the model that will learn from them. We introduce Circuit Reasoning Score (CRS), a selection signal derived from 46 reasoning-sensitive attention heads identified via contrastive ablation, computed in a single forward pass on the frozen base model without reward labels or rollouts. CRS runs against the intuitive hypothesis that stronger reasoning-circuit engagement produces better training data: on Qwen2.5-Math-7B, the lowest-engagement decile improves over random selection on three medium-difficulty benchmarks (GSM8K +2.0 pp, OlympiadBench +1.6 pp, Minerva +2.9 pp), while the highest-engagement decile gains less and is indistinguishable from the middle decile. The advantage has boundary conditions: on a domain-curated pool no selection method separates from the others; at 1.5B scale the useful direction differs; and the lowest-reward training condition produces the strongest downstream generalization. Within the Qwen2.5-Math settings tested, RLVR data selection appears regime-dependent rather than reducible to a static ranking of problem quality.

---


### 231. [SIFTING: A Novel LLM-Based Framework for Structured and Transparent Information Extraction from Clinical Free-Text Reports, with Application to Tumor Staging in Lung Cancer](https://arxiv.org/abs/2609.07185)

**<font color=#1a73e8>作者：</font>** Mirco Hess, Gerben van Veenendaal, Joris Wakkie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Large language models (LLMs) show promise for extracting information from clinical free-text documents, but their outputs are often unstructured and lack traceability, complicating validation and adoption in clinical workflows. In this work we introduce SIFTING, an LLM-based framework designed to address these shortcomings.
Methods: SIFTING combines the language comprehension capabilities of LLMs with segment-level processing and structured prompts with strict output control, linking findings to the source text to enable both accurate and transparent information extraction. To demonstrate its capabilities, we applied the framework to the task of extracting tumor T-stage information from 130 lung cancer radiology reports (SIFTING-T-stage). A compact 4-bit quantized version of the open-source LLM Llama-3.3-70B (35 GB) was used in a fully self-hosted setup, providing full control over data and model. Performance was evaluated against a reference standard created by four clinical experts and compared with a range of LLMs as used in a conventional single-prompt approach, using bootstrap resampling to estimate confidence intervals.
Results: SIFTING-T-stage achieved an accuracy of 90% (95% CI: 84-95) against the reference standard. We found its performance to be comparable to even the largest state-of-the-art LLMs with reasoning capabilities and to be interchangeable with clinical experts (p < 0.001), while at the same time offering full traceability through source text references.
Conclusion: SIFTING enables accurate, structured, and traceable information extraction from clinical free-text documents. It ensures data control, reproducibility, and verifiable outputs that can support clinical validation and workflow integration.

---


### 232. [EmoMed: An Emotionally-Aware Agent for Multimodal Medical Support with Real-Time Information Retrieval](https://arxiv.org/abs/2609.07194)

**<font color=#1a73e8>作者：</font>** Ivan Nasonov, Nikita Glazkov, Ivan Makovetskiy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present EmoMed - a multimodal medical consultation agent that adapts its responses based on users' emotional states while maintaining clinical accuracy. The system processes text and medical images, detects affect indicators (anxiety, confusion, urgency) from user input, and adjusts response tone, structure, and detail level accordingly. To ensure factual reliability, the agent grounds clinical information through a dual retrieval mechanism: web-based fact-checking and an API-connected, continuously updated medical knowledge base. We evaluate our approach across seven state-of-the-art language models (GPT-4/5, Qwen3, Llama 4, Gemini 2.5, Grok4, Claude3) using comprehensive metrics including LLM-as-judge assessments, MedQA style accuracy tests, BERT Score, safety/helpfulness ratings, and multimodal medical benchmarks. The results demonstrate that emotionally adaptive responses consistently outperform neutral baseline across evaluation dimensions, without compromising clinical accuracy. A controlled user study validated these findings, with participants reporting improved perceived empathy and communication clarity, while maintaining trust in factual accuracy. Source code: this https URL

---


### 233. [Agentic Algorithm Engineering: Improving Shared-Memory Exact Minimum Cuts](https://arxiv.org/abs/2609.07204)

**<font color=#1a73e8>作者：</font>** David A. Bader, Adil Chhabra, Ernestine Großmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The minimum cut problem for an undirected edge-weighted graph asks us to divide its set of nodes into two blocks while minimizing the weighted sum of the cut edges. Over the last years, we engineered a range of fast algorithms for this problem. Our fastest exact algorithm uses an inexact algorithm to obtain a better bound for the problem, reductions that depend on this bound, improved data structures and parallel contraction routines. It is available in the open-source package VieCut and, on real-world instances, outperformed the previously fastest solvers by a factor of up to 2.5 sequentially and up to 12.9 when run in parallel. We improve this algorithm using agentic algorithm engineering (AAE), a methodology that we introduce here, in which autonomous large language model agents run the algorithm engineering cycle on an existing code base: they form hypotheses about where running time is lost, implement them, benchmark the result on a fixed instance set and keep or discard the change. Even though we had already tuned our algorithm by hand extensively, the agent finds significant optimizations, in particular on the DIMACS core instances: factors of 1.28 (sequential) and 1.63 (32 threads) on real-world k-cores, and 6.26 and 127 on the DIMACS core instances.

---


### 234. [Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2609.07229)

**<font color=#1a73e8>作者：</font>** Manwen Yang, Leqian Ding, Yu Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models offer a promising approach for zero-shot anomaly detection (ZSAD). However, due to object-centric bias, normal and anomalous text prototypes exhibit a high semantic overlap. While enforcing strict orthogonality between them improves discriminability, mapping highly contiguous visual inputs onto drastically orthogonal prototypes introduces a geometric dilemma, disrupting the pre-trained structural continuity. To address this problem, we propose Proximity-CLIP, a framework that visually calibrates the semantic margin to guide visual adaptation. First, we introduce a visually-calibrated semantic proximity learning mechanism that uses a bounded dynamic regularization to learn an appropriate semantic margin, ensuring discriminative separation while preserving structural alignment. Second, we design an Anomaly Query Module (AQM) driven by these text priors. Using the calibrated anomalous prototype as a semantic query, the AQM actively retrieves localized defect cues from contextual visual patches, mitigating the dilution of subtle anomalies during global pooling. Extensive experiments demonstrate that Proximity-CLIP outperforms current state-of-the-art methods across multiple ZSAD benchmarks with minimal architectural modifications.

---


### 235. [Parallelism Strategy Chaining for Fast Training Convergence](https://arxiv.org/abs/2609.07236)

**<font color=#1a73e8>作者：</font>** Minchul Kang, Changyong Shin, Younghun Go 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting a parallelism strategy - the configuration of data, tensor, and pipeline parallelism degrees together with micro- and global-batch sizes - largely determines the training efficiency of large language models. State-of-the-art methods search for a parallelism strategy offline and select the single strategy that minimizes per-iteration time. But we find that they neglect the target validation perplexity and time-to-perplexity (TTP). In particular, our analysis reveals that the best strategy yielding the fastest perplexity improvement changes multiple times during training. As a result, state-of-the-art methods are 1.8-11.4x slower in TTP than the strategy sequence that selects the best strategy at each iteration. This paper proposes CONA, a new training method that introduces online strategy chaining. Instead of a single strategy selected offline, CONA ranks candidate strategies during training using a surrogate metric built from compute throughput and gradient statistics, and switches the current strategy to a new strategy with a higher metric. In our evaluation with GPT-3 1.3B, BERT-Large, and Llama-3.2-1B, CONA reaches the target validation perplexity 1.4-9.6x faster than state-of-the-art methods. Moreover, CONA closely tracks the perplexity achieved by the sequence that selects the best strategy at each iteration, within 2.6%.

---


### 236. [CEDAR: Error-Bounded Residual Routing for Efficient Long-Context Attention](https://arxiv.org/abs/2609.07237)

**<font color=#1a73e8>作者：</font>** Siyu Li, Dong Wang, Jie Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-hoc sparse attention accelerates long-context prefill by routing each query to a small set of token-level interactions. Hard selection, however, assigns zero probability to every omitted chunk: a routing miss cannot be recovered, and a fixed expansion budget spends the same work on easy and ambiguous queries. We introduce Coarse-to-fine Error-aware Dynamic Attention Routing (CEDAR), a coarse-to-fine method that keeps the language model frozen while preserving global coverage. Each semantic chunk contributes a cheap key--value summary to a residual attention path; chunks with high estimated approximation error are then expanded to exact token attention. Exact and summarized contributions are combined in a single softmax normalization, so refinement replaces, rather than duplicates, coarse evidence. We derive an output-error bound governed by within-chunk key/value dispersion and use it to allocate a variable refinement budget. A controlled clustered-attention study shows that residual summaries reduce reconstruction error by more than 98% relative to hard dropping at equal exact-chunk budgets. Experiments on long-context benchmarks demonstrate that CEDAR recovers most of the quality lost by hard sparse routing while maintaining approximately $3\times$ kernel speedup at 128K context.

---


### 237. [Elastic Horizon: Discovering the Effective Interaction Frontier in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.07247)

**<font color=#1a73e8>作者：</font>** Gangyi Zhang, Junjie Meng, Letian Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling the interaction horizon-the maximum number of environment interactions per episode-improves LLM agents on long-horizon tasks, and curriculum-based methods that progressively expand the horizon outperform fixed-horizon alternatives. However, existing schedules are open-loop: they monotonically increase the horizon until a manually specified maximum, with no mechanism to detect when further expansion stops helping. We propose the effective interaction frontier hypothesis: a dynamic boundary beyond which additional interactions yield diminishing returns while cost grows linearly. We then introduce Elastic Horizon, a closed-loop controller that tracks this boundary via the 90th percentile of successful trajectory lengths. On AppWorld and BFCL, fixed-horizon sweeps reveal clear saturation plateaus; Elastic Horizon stabilizes the horizon inside the saturation band from both under- and over-capacity initializations, attains the best success rates across 7B and 14B backbones, and saves up to 25% of per-step trajectory tokens. Our work shifts the paradigm from how to scale interaction horizons to when to stop scaling.

---


### 238. [SkillAlign: Aligning Skill Interfaces for LLM-based Agents](https://arxiv.org/abs/2609.07255)

**<font color=#1a73e8>作者：</font>** Shuo Ren, Xiaomian Kang, Jiajun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly rely on skills: reusable procedural knowledge for reasoning, tool use, and interaction. Existing work studies how skills are acquired, retrieved, compressed, or composed, but often assumes that once a skill is selected, its interface to the agent is fixed. We argue that this overlooks a key source of skill utility: the same skill can help, distract, or mislead depending on how it is exposed. We propose SkillAlign, a provider-agnostic framework that represents candidate skills as multi-view procedural cards and renders them through alternative exposure interfaces, including full instructions, hints, compressed summaries, workflows, or no exposure. This enables counterfactual evaluation where the task, agent, and candidate skills are fixed while only the exposure interface varies. Across ALFWorld and SkillsBench, we show that exposure form substantially affects task success and rendered context cost, and that compact top-k exposure can outperform full-library injection. We further conduct a replay-based policy-learning analysis on ALFWorld, showing that adaptive exposure contains learnable signal but remains far from oracle selection. Our results suggest that skill-augmented agents should optimize not only which skills to use, but also how those skills are presented.

---


### 239. [MV-STRIDE: Enabling MLLMs to Master Multi-View Spatial Reasoning via Hierarchical Capability Modeling](https://arxiv.org/abs/2609.07258)

**<font color=#1a73e8>作者：</font>** Jin Xu, Xiaojian Huang, Zhuodong Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of Multimodal Large Language Models (MLLMs) in 2D vision-language tasks, robust multi-view spatial reasoning remains a fundamental bottleneck due to the lack of structured 3D cognitive pathways in existing datasets. To address this, we introduce MV-STRIDE, a Multi-View hierarchical SpaTial Reasoning dataset with Interdependent and DEcomposed capabilitiEs. Moving beyond flat data structures, MV-STRIDE explicitly models the dependency relationships between foundational perception, scene understanding, and complex contextual reasoning, providing a coherent learning pathway aligned with human spatial cognition. We develop a systematic QA generation pipeline leveraging diverse 3D scene sources that enforces cross-view dependency constraints to prevent single-view solvability, generating multi-level spatial reasoning tasks supported by cognitively grounded chain-of-thought supervision for complex inference. Extensive evaluations demonstrate that our multi-stage training framework based on our hierarchical dataset achieves state-of-the-art performance across multiple spatial reasoning benchmarks, notably the multi-view oriented MMSI-Bench. Our approach enables MLLMs to maintain robust, 3D-consistent spatial reasoning across diverse viewpoints. The code and dataset are available at this https URL.

---


### 240. [Merging Cyber Threat Intelligence Through Retrieval-Augmented Generation and Small Language Models for Rich Threat Representation](https://arxiv.org/abs/2609.07280)

**<font color=#1a73e8>作者：</font>** Nicola Deidda, Leonardo Regano, Alessandro Sanna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cybersecurity operations rely on CTI collected from heterogeneous sources, including semi-structured threat representations, IoCs, and narrative technical reports. However, these artifacts are often insufficient in isolation to reconstruct how an attack unfolds, under which conditions each step is feasible, and which traces it leaves behind. In practice, analysts must manually correlate partial evidence scattered across multiple and only partially structured sources, delaying the design of effective prevention, detection, and response actions. To address this gap, we propose an automated pipeline that derives an actionable representation of a cyberattack from heterogeneous CTI sources. The pipeline combines a RAG architecture with a locally deployable SLM, used to consolidate such evidence and infer missing operational details. Starting from a semi-structured threat representation and auxiliary CTI documents, the pipeline produces an enriched Attack Graph that captures a coarse, tactic-aligned progression of the attack and annotates each step with explicit pre-conditions and post-conditions, and an enriched description. This representation supports prevention by exposing execution requirements, detection by highlighting observable traces, and response by clarifying the temporal progression of the attack. Then, due to the lack of validated datasets with ground-truth information on the temporal evolution of real-world attacks, we test the complete pipeline on 10 real-world case studies spanning multiple threat types, including backdoors and staged downloaders delivered via phishing. A manual assessment across 10 real-world case studies provides initial evidence that the generated graphs are consistent with expected attack progressions, indicating that the proposed approach can support analysts by consolidating dispersed CTI evidence into a structured and actionable view of attacks.

---


### 241. [Separating Stream Stability from Long-Term Recall in Language Models](https://arxiv.org/abs/2609.07282)

**<font color=#1a73e8>作者：</font>** Peipei Cao, Xin Zhang, Jie Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Methods for streaming language models are often discussed alongside long-context and memory systems, although they solve different problems. An attention sink can stabilize autoregressive generation over an indefinitely long stream while the model remains unable to use content that has left its recent-token cache. We argue that this distinction should be explicit in system claims and evaluation. We introduce three horizons: the stability horizon, over which predictive behavior remains well behaved; the access horizon, over which past content can still causally affect the output; and the utility horizon, over which a task retains acceptable performance. We show constructively that the stability horizon can be infinite while the access and utility horizons are finite. We then propose ThreeH, an evaluation contract that measures all three horizons under a common state and compute budget. Applying the framework to attention-sink streaming clarifies its strength, constant-memory, stable generation, without treating anchor tokens as semantic memory. The framework exposes roles for cache policies, recurrent state, retrieval, and external memory. Experiments on 128K-token streams, delayed binding recall, and delayed decisions show that attention sinks preserve local modeling but not content beyond the active cache; recurrent and retrieval state extend the semantic horizon.

---


### 242. [Probing the Structure and Dynamics of LLM Value Expression through Value Conflicts](https://arxiv.org/abs/2609.07296)

**<font color=#1a73e8>作者：</font>** Kaicheng Zhang, Jingyi Xiao, Renjun Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ethical evaluation of Large Language Models (LLMs) often characterizes model values as static and monolithic. In contrast, we argue that LLM value expression is better understood as a structured yet dynamic phenomenon. To investigate this, we introduce Conflict-driven Value Probing, a controlled framework that places LLMs in value conflicts and implements four types of interventions that perturb these conflicts to probe LLM value expression. Applying this framework to ten LLMs, we identify three recurring patterns. (1) Expression duality: models shift from broad idealistic orientations in abstract assessment toward more pragmatic priorities in concrete conflicts. (2) Functional steerability: models readily reconfigure their expressed value profiles toward task-defined value objectives. (3) Bounded plasticity: such reconfiguration is not without constraints, i.e. pressure induces a security- and goal-oriented priority shift while negative framing distinguishes protected values from those more amenable to redirection. Together, these findings characterize both the structure and dynamics of LLM value expression: context flexibly reconfigures expressed priorities, yet within behavioral boundaries. This behavioral account provides a foundation for understanding controllability, alignment, and safety in LLMs. Code and data are available at this https URL.

---


### 243. [Long-Horizon Language Model Reinforcement Learning via Progressive Point Matching](https://arxiv.org/abs/2609.07303)

**<font color=#1a73e8>作者：</font>** Preston Fu, Kevin Frans, Oleh Rybkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current paradigms for training language models via reinforcement learning rely heavily on sparse outcome rewards. However, as we pursue tasks that require longer and more complicated trajectories, such strategies result in slow learning. Prior work has attempted to address this problem by rewarding partial progress; however, naive formulations are often biased and converge to suboptimal policies. We show that a simple and unbiased dense reward formulation, which we term progressive point matching, scales exponentially more efficiently to long-horizon tasks by rewarding partial progress on a segment level, both theoretically and empirically via synthetic environments. We then show how progressive point matching can be practically instantiated using a single reference trajectory per task. On extremely hard math reasoning problems, sparse outcome rewards cannot make any progress, whereas segment-level rewards enable improvements at larger test-time token budgets when measured by success rate or pass@k.

---


### 244. [SPARROW: Scalable Taxonomy Induction via Structure-Preserving Partitioning and Constraint-Guided Merging](https://arxiv.org/abs/2609.07307)

**<font color=#1a73e8>作者：</font>** Yirui Zhang, Yixuan Tang, Yandong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Taxonomy induction aims to organize concept sets into coherent hierarchical structures. Recent LLM-based methods can induce taxonomies directly from flat term lists, avoiding the need for corpora, but degrade sharply as concept sets scale up. We argue that this degradation stems not only from context length limitations, but also from structural failures in hierarchical reasoning. To address this, we adopt a divide-and-merge paradigm that partitions concepts into smaller subsets, induces local taxonomies, and merges them into a global hierarchy. However, we identify two structural failure modes inherent to this paradigm: Structural Fragmentation, where partitioning weakens local hierarchical signals, and Parent Displacement, where locally plausible relations are misplaced in the global hierarchy. To address both, we propose SPARROW, a scalable taxonomy induction framework that combines structure-preserving spectral partitioning to retain hierarchical connectivity within each block, and constraint-guided incremental fusion that treats block-level relations as structural constraints rather than ground truth for global placement. Experiments on large-scale benchmarks show that SPARROW consistently achieves the strongest global structural quality across backbones. The code is available at this https URL.

---


### 245. [LANTERN: Language Model Assessment on Noisy and Transformed Tasks for Understanding Error and Robustness Nuances](https://arxiv.org/abs/2609.07309)

**<font color=#1a73e8>作者：</font>** Vamsi Krishna Kodavali, Rituraj Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Robustness evaluation of large language models (LLMs) remains a critical challenge, particularly in assessing their sensitivity to perturbations in input data. In this work, we systematically evaluate LLM robustness across multiple dimensions, including word error rate, character repetition and duplication, modifications in choices, and variability in instruction following. To facilitate this evaluation, we construct a synthetic and augmented dataset encompassing a diverse set of LLM benchmarks, specifically targeting multiple-choice question (MCQ) datasets and instruction-following tasks. We conduct extensive experiments on LLMs of varying scales-small, medium, and large-as well as across base and instruction-tuned variants. Our analysis quantifies the variability in model responses under perturbed conditions and highlights discrepancies relative to baseline models. The findings provide insights into the stability of LLMs across different evaluation scenarios contributing to the development of more robust and reliable language models as well as robust evaluation methodologies.

---


### 246. [AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning](https://arxiv.org/abs/2609.07334)

**<font color=#1a73e8>作者：</font>** Janek Groß, Jens Heidrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Asset Administration Shell (AAS) is a cornerstone of Industry 4.0 and the Digital Product Passport, providing standardized digital representations of industrial assets. While manufacturers already maintain extensive technical product documentation, generating AAS instances from existing product datasheets remains a labor-intensive task because technical information is extracted from heterogeneous document structures and often involves company-specific terminology and conventions. In this work, we present AAS-RAIL, a retrieval-augmented information extraction (IE) approach that automatically generates Asset Administration Shells from PDF product datasheets using large language models (LLMs). Instead of relying on a fixed set of few-shot examples, the proposed retrieval-augmented in-context learning (RAIL) approach retrieves LLM-generated extraction helpers from similar Asset Administration Shells to provide instance-specific in-context learning (ICL). This enables the model to adapt its extraction behavior to company-specific naming conventions and formatting styles without fine-tuning. Our core contribution is the dynamic selection of company-specific AAS examples for each datasheet, replacing static prompting with an extraction pipeline that adapts to instances and combines semantic retrieval and structured information extraction. The proposed approach is evaluated on a collection of industrial product datasheets using a selection of open- and closed-weight LLMs. Experimental results show that RAIL consistently improves extraction quality over conventional few-shot prompting, yielding relative improvements of 30.4-52.4%. These results demonstrate that our approach provides an effective improvement for company-specific AAS generation.

---


### 247. [Staying on the Attack Path: Structured State for Long-Horizon Automated Penetration Testing](https://arxiv.org/abs/2609.07344)

**<font color=#1a73e8>作者：</font>** Weizhe Wang, Yitong Zhang, Yao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) based agents are increasingly applied to cybersecurity tasks such as vulnerability discovery and automated penetration testing. On long-horizon security tasks, however, such agents remain limited by context forgetting and intent drift: early critical facts and causal reasoning chains are lost over extended interactions, and the agent falls into aimless, repetitive exploration. This paper proposes Intentest, an intent-graph-guided automated penetration testing agent that externalizes long-horizon state from the LLM's context window onto a persistent fact-intent directed acyclic graph (DAG), thereby substantially reducing invalid transitions. We evaluate Intentest on automated penetration testing of web applications, a representative long-tail task in cybersecurity. In the DAG, verified network states are stored as immutable fact nodes, and exploration directions are constrained as intent edges bounded by predecessor facts. The system adopts a three-layer architecture, in which the fact-intent mapping layer maintains the global state, the task scheduling and allocation layer ensures execution stability through two-phase degradation recovery and multi-dimensional adaptive load balancing, and the intent retrieval and prediction layer provides tactical priors through a top-down five-stage filtering algorithm. On a benchmark of real CTF challenges covering more than ten vulnerability types across three difficulty levels, Intentest achieves an overall success rate of 88.2% and a success rate of 75.0% on hard tasks, improving over the baseline by approximately 44 and 50 percentage points. Ablation experiments further show that the intent retrieval and prediction reduce the average number of rounds on successful medium and hard tasks by about 33% and 48%, respectively, without changing the set of solvable tasks.

---


### 248. [Human-like moral judgments conceal divergent motive attributions in large language models](https://arxiv.org/abs/2609.07353)

**<font color=#1a73e8>作者：</font>** Xiaoyan Wu, Jean-Claude Dreher  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are used to simulate human participants in psychological research. We asked whether LLMs that reproduce human evaluations of a whistleblower's moral character also reproduce the motive attributions that accompany them. Five LLMs and two human samples (N = 125 and N = 742) evaluated a physician who either remained silent about fraudulent billing or reported it to a hospital, regulator, or newspaper. Models reproduced the human ranking of the physician's moral character but portrayed whistleblowers as more helpful, less self-interested, and less hostile. In four of five models, competitive motives were less strongly associated with moral-character judgments. Model ratings changed little when prompts reproduced the narratives and demographic profiles of both human samples, although this comparison cannot isolate a perspective effect. Thus, agreement in average ratings can conceal differences in attributed motives, relationships among judgments, and sensitivity to context. Validating LLMs as simulated participants therefore requires testing psychologically informative response patterns, not average agreement alone.

---


### 249. [BlueprintAgent: Constraint-Triggered Targeted Revisits for Simulation-Ready Generation from Scanned Structural Blueprints](https://arxiv.org/abs/2609.07362)

**<font color=#1a73e8>作者：</font>** Zhouyuan Xu, Chen Yang, Linhao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Converting in-service reinforced-concrete (RC) building blueprints into simulation-ready models---structured frame representations that support deterministic FEM export and qualified-engineer review---underpins safety assessment and seismic retrofit, but the process remains manual. Direct prompting of a multimodal large language model (MLLM) over a scanned sheet is unreliable: outputs often violate engineering constraints on beam--column support, span count, or 3D continuity. We present BlueprintAgent (BPA), a constraint-triggered multimodal agent for simulation-ready frame extraction from scanned blueprints. BPA treats the MLLM as the primary reader and decision maker, with OCR and computer vision supplying localized evidence. Its central mechanism realizes engineering constraints as callable validators whose entity-level conflict reports trigger targeted MLLM revisits over the local region---an inference-time control distinct from fixed pipelines and free-form self-reflection. We evaluate BPA on 300 real scanned blueprint sheets from 20 anonymized RC frame projects, against five baselines and six ablations. BPA reaches a macro-averaged Beam F1 of 0.994, against 0.301 for single-MLLM zero-shot and 0.820 for a fixed pipeline; removing MLLM-led axis adjudication collapses Beam and Column F1 on complex multi-sheet projects. For dense technical drawings, engineering constraints are best deployed as triggers for entity-level targeted revisits rather than as post-hoc output filters.

---


### 250. [Beyond Fluent Generation: A CPU Reliability Benchmark for MCP-Style Tool Calling in Sub-2B Small Language Models for Edge Deployment](https://arxiv.org/abs/2609.07370)

**<font color=#1a73e8>作者：</font>** Abrar Shahriar Qurat-Ul-Ain Mastoi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Resource constrained single-board computers including Raspberry Pi, NVIDIA Jetson Nano, Arduino UNO Q, Orange Pi, and LattePanda motivate on-device small language model (SLM) agents that reduce cloud dependence, improve data locality, and tolerate intermittent connectivity. Model Context Protocol (MCP)-style tool invocation demands more than fluent generation: an agent must emit machine-readable JSON, select the correct tool, supply all required arguments, and avoid unintended actions. We establish a platform-agnostic CPU baseline by evaluating five open-weight models below two billion parameters Phi-1.5, Pythia-1.4B, TinyLlama-1.1B-Chat, Qwen2.5-0.5B, and Qwen2.5-1.5B on 100 prompts spanning weather retrieval, web search, calculation, email composition, and task creation, under greedy decoding and nucleus sampling. A recovery parser strips Markdown fences, extracts brace-delimited substrings, and scores parseability, tool-name correctness, argument completeness, and value agreement. Under this criterion, Qwen2.5-1.5B achieves 75% (greedy) and 79% (sampling); Qwen2.5-0.5B achieves 72% (greedy) but drops to 32% under sampling. Phi-1.5 scores 0%; Pythia and TinyLlama reach at most 7%. A strict post-hoc audit finds only 5 of 1,000 raw responses directly parseable as JSON, exposing near-total dependence on output recovery. A CPU resource probe shows Qwen2.5-1.5B requires 7,960 MiB and 30.782 s mean latency; Qwen2.5-0.5B uses 3,637 MiB and 10.627 s, revealing a reliability-resource trade-off for edge deployment. These results do not cover the named boards directly or a full MCP implementation. Safe deployment requires schema validation, constrained generation, least-privilege execution, and human escalation for consequential actions.

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-483](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
