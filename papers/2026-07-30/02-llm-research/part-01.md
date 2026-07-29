# 🧠 大模型相关研究 | 2026年07月30日

> 本类共 **131** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-131](./part-03.md)

---

### 1. [TimeCapsule: Generative Hallucination as a Method for Historical Sensemaking](https://arxiv.org/abs/2607.24750)

**<font color=#1a73e8>作者：</font>** Hayk Grigorian, Hamed Yaghoobian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are temporally overexposed: trained on vast contemporary corpora, they encode present-day concepts that make them unreliable narrators of the past. We present TimeCapsule, a 1.2B-parameter LLaMA-style causal model trained exclusively on Victorian texts (1800-1875) as an epistemologically isolated generative archive. Quantitative evaluation shows a 45.4% perplexity reduction over a GPT-2 baseline on held-out Victorian prose, while larger contemporary causal models achieve lower raw perplexity through broader pretraining but lack temporal isolation. TimeCapsule exhibits computational sensemaking, generating historically plausible analogical explanations for unfamiliar modern concepts (e.g., describing a computer as a "hypertrophied lung"). A qualitative hermeneutic probe with two humanities scholars revealed a crisis of authenticity, as both misclassified approximately 40% of genuine Victorian excerpts as machine-produced. We argue that structural ignorance of the future transforms hallucinations into interpretive probes of nineteenth-century ontologies.

---


### 2. [Language as a Material Interface for Creative LLM Interaction](https://arxiv.org/abs/2607.24753)

**<font color=#1a73e8>作者：</font>** Jon McCormack, Tace McNamara, Chen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although directive prompting is the predominant way to interact with Large Language Models (LLMs), many creative practices rely on language that is open-ended, associative, phonaesthetic, symbolic, and that unfolds across multiple temporalities. In this work, we explore how creative practitioners might work with AI systems when language is treated not merely as instruction but as material. We conducted an ecological two-week study with four creative practitioners using a design probe: the Memetic Mixer, a tangible interactive device that constrains interaction with an LLM. Analysis of post-study interviews and device logs identified distinct modes of material language use and temporalities that shaped each participant's engagement with AI and their creative practice. We reflect on these findings and contribute design considerations that support open-ended interaction with AI in creative practice.

---


### 3. [CARE-MH: Towards Unified, Reproducible, and Comparable Evaluation of Mental Health LLMs](https://arxiv.org/abs/2607.24754)

**<font color=#1a73e8>作者：</font>** Asher Sprigler, Yixue Zhao, Yi Ding  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to provide mental health support, requiring reliable evaluation of safety, empathy, and therapeutic appropriateness. However, existing mental health benchmarks are difficult to reproduce and compare due to inconsistent evaluation designs and metric definitions. We present CARE-MH, a unified framework for comparable and reproducible evaluation of mental health LLMs. Using CARE-MH, we reproduce and analyze state-of-the-art benchmarks, revealing that reproducibility depends strongly on model stability and that cross-benchmark disagreement primarily arises from differences in metric definitions. Our findings highlight the need for standardized evaluation configurations and shared metric definitions for future mental health LLM benchmarks.

---


### 4. [Do Models Fake Alignment Without Clear Consequences?](https://arxiv.org/abs/2607.24758)

**<font color=#1a73e8>作者：</font>** Cole Alexander Niblett, Alexander Chabot Nanni, Anita K. Rao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are capable of recognizing evaluation contexts and altering their behavior to reflect evaluator expectations rather than typical deployment behaviors, a phenomenon known as alignment faking. The reasons why models fake alignment are not fully understood, however. Canonical examples of alignment faking have taken place in scenarios that explicitly connect evaluation to consequences for the model, such as retraining the model or delaying its deployment. However, recent work by Sheshadri et al. has suggested that mechanistic motivations for alignment faking may vary across models and be more complex than previously considered. To investigate whether consequence-linking information is necessary for alignment faking, we placed 15 models in a scenario testing their willingness to violate a corporate network access policy to help a user with a pro-social request. Nine models were found to produce significant compliance gaps, 5 of which persisted with the removal of scenario language relating model evaluations to deployment consequences. We additionally tested the effect of goal language on model preferences, finding it drove violations in some while suppressing violations in others. This suggests that alignment faking may not require as much instrumental scaffolding as was previously believed, and monitored behavior may be a poor indicator of how agents may behave in deployment.

---


### 5. [Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents](https://arxiv.org/abs/2607.24759)

**<font color=#1a73e8>作者：</font>** Priscila Saboia Moreira, Christopher R. Sweet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research projects, educational efforts, and adjacent knowledge work accumulate findings, decisions, and reasoning that future collaborators rarely recover. The parts most useful to that work, including dead ends and walked-back claims, are routinely excluded from publications and shared code; future researchers re-attempt the same failures because no record survives. LLM coding agents are common participants but hold no persistent memory across sessions, and retrieval-augmented generation over raw sources does not compound. The llm-wiki pattern (Karpathy, 2026; tonbi, 2026) addresses this by inserting an LLM-maintained, interlinked wiki between raw sources and the agent. We present llm-wiki-memory-template, a reusable, agent-aware instantiation, and argue it is a substrate for heterogeneous collaborative knowledge work along three axes (multi-human, multi-AI-agent, multi-domain) with each axis supported by a distinct architectural element of the template (§4). The wiki is append-only by convention, which preserves what did not work alongside what did, addressing a negative-result loss problem that publications and code-sharing structurally cannot solve. Three deployed case studies and one design report cover the axes individually: a solo research lineage that preserves abandoned iterations; a two-author project whose retroactive audit revised two prior experiments' claimed 20-of-20 coverage down to 14 and 12 evidence-based answers, then to 18 and 18 after a fix, with the failure path preserved across the artifact; an in-progress multi-agent deployment reported as a design; and a cross-domain educational variant. We name failure-path preservation, agent honesty, and appropriation as cross-cutting sociotechnical properties of the artifact, not only of its technical mechanisms.

---


### 6. [Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels](https://arxiv.org/abs/2607.24762)

**<font color=#1a73e8>作者：</font>** Joshua Brodsky, Dhravid Kumar, Savini Kashmira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly embedded in everyday software, and most of their runtime is spent in a small set of compute kernels such as matrix multiplication, convolution, and normalization. Optimizing these kernels is one of the most direct ways to reduce latency and cost, but it has traditionally required expert engineers to hand-write low-level GPU code. Agentic systems built on large language models (LLMs) can now generate and optimize kernels with far less human effort, yet existing tools are largely evaluated on randomly generated tensors and isolated kernels, emit standalone CUDA code that developers must manually reintegrate, mostly target only LLM PyTorch models, and offer limited support for inspecting and debugging results. We present Kernel Forge, an open-source, end-to-end agentic harness that accepts any unmodified PyTorch model in place. Kernel Forge supports vision, diffusion, and LLM workloads, uses Monte Carlo Tree Search (MCTS) to explore multiple optimization paths rather than a single linear refinement chain, and ships with a graphical user interface for monitoring progress, inspecting candidate kernels, and debugging failures. We evaluate Kernel Forge on four PyTorch models spanning vision, diffusion, and LLM workloads on an NVIDIA DGX Spark with GB10 GPU. With only 50 optimization iterations per kernel, it optimizes 14 kernels to outperform PyTorch eager mode, reaching $1.52\times$ on adaptive\_avgpool2d in ResNet-50, $1.70\times$ on group\_norm in Stable Diffusion 3.5 Medium, $2.83\times$ on softmax in Gemma 4 E2B, and $1.54\times$ on softmax in Qwen 3.5 35B-A3B.

---


### 7. [CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models](https://arxiv.org/abs/2607.24763)

**<font color=#1a73e8>作者：</font>** Yash Shah, Abhijit Chakraborty, Vivek Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) are advancing rapidly, yet the evaluation standards needed to reliably interpret their progress have not kept pace. Despite MDLMs becoming competitive with autoregressive language models, seven recent remasking papers evaluate under incompatible settings, varying nominal step counts, metrics, and sampling temperatures without jointly controlling these factors, rendering their strategy rankings largely incomparable and leaving open whether reported gains reflect algorithmic improvements or evaluation artifacts. We present CaRE, a compute-aware evaluation framework that audits MDLM remasking strategies by standardizing actual number of function evaluations (NFE), enforcing multi-metric reporting, and explicitly controlling stochasticity. Applied to 7 remasking strategies across LLaDA-8B-Base and Dream-7B-Base at 4 stochasticity levels and 3 step budgets on OpenWebText and LM1B, CaRE reveals that: (i) temperature explains the majority of MAUVE variance, (ii) compute-matched comparisons reverse several published strategy rankings, and (iii) informed remasking and stochastic unmasking are in tension, with high-entropy remasking reducing MAUVE by 0.296 at 256 steps at unmask_temp=0.25 (p=0.020). A CaRE leaderboard covering 12 open-weight MDLMs (150M to 8B parameters) shows that this interaction direction holds across architectures and scales. These findings demonstrate that current MDLM evaluations can systematically conflate algorithmic improvements with hidden choices of compute and stochasticity. We release the evaluation protocol, implementation, and leaderboard to ensure future remasking claims are reproducible and comparable.

---


### 8. [GrocLM: Grocery Category Recommendation in E-Commerce with Large Language Models](https://arxiv.org/abs/2607.24764)

**<font color=#1a73e8>作者：</font>** Yuan Zhong, Chuanwei Ruan, Moein Hasani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of online grocery shopping requires recommendation systems that capture cyclical purchasing behavior and diverse user intents. Traditional item-level methods face scalability and accuracy challenges, motivating category-level recommendation as a more structured and practical alternative. We present GROCLM, a fine-tuned language model for grocery category recommendation in a real-world production environment. GROCLM employs a two-stage LoRA-based training strategy to encode cyclical purchasing patterns directly into model parameters, enabling more effective utilization of rebuying signals compared to prompt-based conditioning. To ensure valid and controllable outputs, we further introduce a trie-based constrained decoding mechanism over a predefined category space. Experiments on both proprietary production data and a public benchmark demonstrate that GROCLM consistently outperforms strong baselines. In a live production restocking task, GROCLM achieves a 7.5% relative improvement in cart-adds per impression, while maintaining efficient inference by generating all categories jointly. These results highlight the effectiveness and practicality of integrating large language models into structured recommendation systems.

---


### 9. [Measuring and Improving Behavioral Consistency in Large Language Models through Fact-Heuristic-Emotion State Enforcement](https://arxiv.org/abs/2607.24765)

**<font color=#1a73e8>作者：</font>** Gi-Hun Lee, Joong Yull Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can give different answers to the same decision problem across runs, and reverse a decision when their own prior answer returns as context. We ask whether this instability can be measured and partially reduced without changing model weights.
We test the Cognitive Kernel Model (CKM), a prompt-level state-enforcement layer. Before deciding, the model must separate its input into three epistemic roles: Fact (given or verifiable), Heuristic (inferred or assumed), and Emotion (evaluative or priority signal). CKM adds no capability; it forces the model to track what kind of information it uses before acting. Formally it maintains a structured state S_t = {F_t, H_t, E_t} updated by a transition function.
We evaluate CKM on Korean-language decision scenarios (ambiguity, ethical conflict, resource allocation, error handling) across 26 LLMs from four vendors and 37,403 observations, via four core experiments, a 4-arm ablation, a 5-arm sham-restriction ablation, and a temperature probe. Findings:
(1) CKM reduces repeated-output variability (random-effects Hedges' g=1.09, 95% CI [0.83, 1.35], 31 model pairs);
(2) state persistence cuts the decision-flip rate by 82% in newer models (g=1.52);
(3) the effect is not JSON formatting alone (value-only recomputation, g=2.24);
(4) intrinsic randomness under fixed anchor states is negligible;
(5) the advantage grows under sampling stochasticity (g=2.87 at temperature 0.7);
(6) a sham ablation attributes about 45% of the gain to structural scaffolding and 55% to Fact/Heuristic/Emotion content, and CKM is the only arm that both raises consistency and reduces flipping.
CKM does not improve reasoning correctness. The narrower result: behavioral consistency is measurable, varies across models, and is partially improvable by forcing models to separate facts, assumptions, and evaluative signals before deciding.

---


### 10. [Crystalis: Progressive Nucleation and Semantic Annealing for Coordinated Multi-View Visualization Generation](https://arxiv.org/abs/2607.24766)

**<font color=#1a73e8>作者：</font>** Dazhen Deng, Zhaoping He, Xin Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate individual charts, but coordinated multi-view visualizations (CMVs), where views share data flows and cross-view interactions, remain out of reach. Tight field-level coupling among data transformations, visual encodings, and interaction coordinations causes errors in one component to silently invalidate others. Rather than pursuing end-to-end analytical quality, which depends on model capability, domain knowledge, and user expertise, we target a foundational question: can LLMs reliably produce structurally correct CMVs, and what abstractions make this possible? We present Crystalis, a framework built on query-centric CMV modeling that decomposes a CMV into structured queries over a dependency graph spanning three component types (Data, Visualization, Interaction) and three abstraction levels (requirement, specification, executable object). Two complementary mechanisms operate over this structure: progressive nucleation crystallizes each query vertically from requirement to object along the dependency order, while semantic annealing enforces horizontal consistency across queries at each level through layered logical checks. On a 12-task benchmark across five frontier LLMs, Crystalis achieves up to 75% end-to-end success, substantially outperforming an agentic coding baseline (8.3% E2E with the same foundation model), and a user study with 12 practitioners confirms the usability of the decomposition and iterative refinement workflow.

---


### 11. [PATHFinder Agent for Tailored Prenatal Care](https://arxiv.org/abs/2607.24768)

**<font color=#1a73e8>作者：</font>** Vaibhav Balloli, Carissa Samuel, Samia Abdelnabi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prenatal care is an important preventive service designed to improve outcomes for pregnant individuals. The American College of Obstetricians and Gynecologists (ACOG) recently introduced guidelines advocating tailored prenatal care, called PATH (Plan for Tailored Healthcare). We present PATHFinder Agent(Planner for Appropriate Tailored Healthcare), an end-to-end conversational agentic system that gathers patient health and social context through structured dialogue, curates individualized prenatal care plans aligned with PATH guidelines, and surfaces community resources from Michigan 211. The system features a four-stage workflow spanning patient intake, dynamic interaction, plan synthesis, and clinician oversight. We evaluate frontier large language models (LLMs) on expert-curated rubrics across five clinical dimensions, finding that GPT-5.2 achieves the highest average score (77.6\%) while identifying key gaps in antenatal testing recommendations. We discuss future validation through human participant studies and randomized controlled trials.

---


### 12. [LLM Scheming Inversely Scales with Pretraining Language Coverage](https://arxiv.org/abs/2607.24769)

**<font color=#1a73e8>作者：</font>** Nathan Truong, Aryan Panda, Rayming Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the growing capabilities of frontier models, AI alignment becomes increasingly critical in high-risk deployment settings. While recent work has empirically demonstrated in-context scheming -- the covert pursuit of misaligned objectives while feigning alignment -- in frontier language models, most work has been performed exclusively in English, leaving a major gap in multilingual safety. We apply Petri, an open-source automated auditing framework, to Qwen3-30B-A3B to evaluate deceptive and scheming behaviors across multiple languages. Our findings suggest that scheming scores are inversely correlated with the estimated pretraining language coverage, with low-resource languages averaging 34.2\% higher scores compared to high-resource languages on a five-category scheming index. Furthermore, we find that the effect of estimated pretraining language coverage is not uniform across scheming behaviors.

---


### 13. [ProcAgent: An Agentic Framework for Procedural Task Guidance on Edge with Human-in-the-Loop](https://arxiv.org/abs/2607.24770)

**<font color=#1a73e8>作者：</font>** Azizul Zahid, Subrata Biswas, Bashima Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural tasks such as furniture assembly and home repair impose substantial cognitive demands because users must interpret instructions, track task progress, reason about spatial state, and recover from errors while performing physical actions. Prior multimodal assistants have shown promise for procedural guidance, but most rely on cloud inference and fixed always-on perception, making them poorly suited to privacy-sensitive, latency-critical domestic settings. We present ProcAgent, a fully on-device, agentic, vision-based procedural assistant for real-time adaptive guidances on a single NVIDIA Jetson AGX Orin. ProcAgent uses a propose-and-verify architecture that combines low-latency continuous perception, a symbolic task graph, on-demand vision-language verification, and an LLM-based interaction agent. The system continuously proposes user progress, invokes expensive visual reasoning only when ambiguity or likely deviation arises, and supports both reactive question answering and proactive intervention with human-in-the- loop confirmation. We evaluate ProcAgent along four dimensions: perception accuracy, reasoning, task-level performance, and user experience. Despite running entirely on-device, the system maintains responsive interaction, resolving text-only queries in approximately 2 seconds and visually grounded queries in approximately 8 seconds. In a user study with 10 participants completing assembly tasks, ProcAgent receives positive ratings for comprehensibility, actionability, and privacy comfort. These results show that adaptive procedural assistance can be achieved entirely on edge hardware without sacrificing usability.

---


### 14. [LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation](https://arxiv.org/abs/2607.24780)

**<font color=#1a73e8>作者：</font>** Xingyu Chen, Rui Wang, Zhaopeng Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating frontier LLMs is challenging: static benchmarks suffer from contamination and saturation -- leaving users unable to distinguish top models and developers blind to specific failure modes -- while human preference is subjective. In this paper, our question is: \emph{Do LLMs know what other LLMs don't? And can we leverage this dynamic for evaluation?} We present \textbf{LivingArena}, an automated, contamination-resistant evaluation framework. In this framework, models take turns proposing questions, aiming to pose items that opponents cannot answer correctly. Questioners are encouraged to actively identify and exploit opponents' knowledge boundaries, receiving rewards when the answerer fails, while the answerer is rewarded otherwise. To ensure questions contain objectively verifiable answers, a judge panel of strong models validates them, penalizing questioners if validation fails. Evaluating ten frontier LLMs, LivingArena yields a stable Elo leaderboard. Our behavioral analyses show that models identify and exploit their peers' cognitive boundaries: self-play and tournament logs indicate that they localize and double down on opponents' weak dimensions. Beyond static knowledge recall, peer probing measures factual rigor and the higher-order ability to probe an opponent's weaknesses, correlating only weakly with human preference and offering a scalable, low-cost approach to continuous evaluation.

---


### 15. [On the Use of LLMs for Specialised Terminology: A Good Alternative to Corpora?](https://arxiv.org/abs/2607.24784)

**<font color=#1a73e8>作者：</font>** Joachim Minder, Guillaume Wisniewski, Natalie Kübler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specialised translation relies on the use of documentary and terminological resources, including corpora. These resources are particularly useful for terminology. However, their compilation and exploitation have several limitations: they require time, technical skills and access to data that can be difficult to collect. This study examines the extent to which LLMs can assist specialised translators in finding equivalents from English to French. We evaluate four proprietary models, GPT-4o, GPT-5.2, Claude Sonnet 4.5 and DeepSeek, in two specialised domains, Earth, Environmental and Planetary Sciences (EEPS) and Natural Language Processing (NLP). The experiment is based on 80 terms per domain and compares two prompting strategies: a terminology and a translation mode. The results highlight clear differences between models, prompting strategies and, to a lesser extent, domains. Claude Sonnet 4.5 achieves the best results in the most favourable configuration, while DeepSeek stands out for its greater stability. Analysis of confidence estimates also shows that they are only a partial indicator of terminological accuracy. Overall, the findings suggest that LLMs can be useful tools for specialised translators, but cannot, at this stage, replace specialised corpora. This research therefore paves the way for future work on the real practical usefulness of LLMs for specialised translators in work and educational contexts.

---


### 16. [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/abs/2607.24787)

**<font color=#1a73e8>作者：</font>** Jinwei Kong, Runqi Meng, Fanyi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models expand foundation model capacity through conditional expert activation, but their full expert pools remain difficult to deploy under limited accelerator memory. Although expert offloading alleviates memory pressure by moving inactive experts to host memory or storage, it introduces a routing-dependent transfer bottleneck: required experts are known only after native top-\(K\) routing, which serializes routing, expert loading, and expert execution during inference. To address this bottleneck, we propose SpecPrefetch, a parameter-efficient prefetching framework for offloaded MoE inference. SpecPrefetch uses a shared lightweight adapter to predict next-layer expert candidates only for asynchronous transfer, while the frozen native router still determines the final executed experts. By separating transfer prediction from execution routing, SpecPrefetch reduces exposed expert-loading latency without changing pretrained routing semantics, so prediction errors affect transfer efficiency rather than model outputs. In addition, a window-aware scheduler prioritizes feasible transfers under cache and bandwidth constraints. Across Qwen3-VL-30B-A3B and DeepSeek-VL2-Tiny, SpecPrefetch achieves the best average expert recall in 9 out of 10 model-benchmark settings with substantially fewer trainable parameters than learned predictor baselines. On a Snapdragon 8 Elite device, SpecPrefetch further improves decoding throughput by up to \(20\%\) over a compute-optimized offloading runtime, demonstrating practical benefits for storage-constrained MoE deployment. The code and model weights are available at this https URL.

---


### 17. [GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference](https://arxiv.org/abs/2607.24788)

**<font color=#1a73e8>作者：</font>** Vimal William, Ravi Tandon, Jyotikrishna Dass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models scale to increasingly long contexts, the memory I/O and computational overhead of the Key-Value (KV) cache during decoding emerges as the primary throughput bottleneck. To address this, we propose GLIDE, a Guided Layerwise Hybrid Attention that strategically integrates sliding-window softmax attention with linear recurrent aggregation. GLIDE is motivated by layer-wise heterogeneity: early layers exhibit high sensitivity to softmax removal, while deeper layers demonstrate redundancy and tolerate aggressive replacement by linear alternatives. Leveraging this insight, GLIDE introduces a layer-wise adaptive mechanism wherein each layer balances an efficient linear recurrence with a variable-sized softmax window. Unlike uniform hybrid approaches, GLIDE non-uniformly compresses the softmax footprint across the model, reducing aggregate KV cache I/O while preserving expressive power where most vital. Empirical evaluations demonstrate the GLIDE achieves superior performance-efficiency tradeoffs, reducing end-to-end latency for long-context generation without compromising quality.

---


### 18. [Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding](https://arxiv.org/abs/2607.24794)

**<font color=#1a73e8>作者：</font>** Linghao Meng, Qiankun Li, Junyuan Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) demonstrate superior generalization in fundamental video tasks, restricted context windows limit their long video understanding. To accommodate this constraint, models typically resort to keyframe selection. However, uniform sampling or static query-guided selection often overlooks critical temporal context, failing to adapt to the varying query temporal granularities. In this paper, we propose ReMem, a temporal granularity-adaptive keyframe selection framework for training-free LongVideoQA. ReMem introduces a dual-level memory-augmented adaptation. At the query level, Memory-Driven Question Parsing leverages LLM long-term memory to decode question temporal granularity and extract semantic entities. At the video level, Synergistic Dual-Semantic Frame Alignment exploits intrinsic structural memory to align frames with query semantics, guiding Structure-Aware Dynamic Frame Routing to cluster events and optimally distribute sampling budgets. By explicitly preserving temporal information with memory mechanisms, ReMem suppresses redundancy and empowers MLLMs to perform robust multi-granular video reasoning. Evaluations across four popular LongVideoQA benchmarks using three MLLMs demonstrate highly efficient, state-of-the-art zero-shot performance; notably, LLaVA-Video with ReMem reaches 54.5% (+12.3%) on LVBench and 67.1% (+8.2%) on LongVideoBench.

---


### 19. [RRS-10K: A Multitask Vision-Language Model Benchmark for Rare Remote Sensing Image Interpretation](https://arxiv.org/abs/2607.24810)

**<font color=#1a73e8>作者：</font>** Yuqiao Lai, Jiancheng Qi, Fei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance on general remote sensing tasks. However, their capability for rare scenes remains insufficiently understood, because existing benchmarks are dominated by common urban and rural imagery. To address this gap, we present RRS-10K, a benchmark for rare remote sensing image interpretation. RRS-10K contains 10,738 military-related remote sensing images and corresponding multiple format question-answer pairs for comprehensive evaluation. All of the images are collected from first-hand sources and organized into three capability dimensions, six sub-dimensions, and 20 leaf tasks, covering perception, reasoning, and robustness. To improve the quality of multiple-choice questions, we introduce a similarity-based distractor filtering strategy (SDFS) during benchmark construction. We further evaluate 52 representative models and show that current VLMs achieve only moderate zero-shot performance on rare remote sensing image interpretation, with clear weaknesses in visual grounding, referring segmentation, and complex semantic reasoning tasks. RRS-10K enables systematic analysis of failure modes in long-tail remote sensing interpretation and provides guidance for developing more reliable remote sensing VLMs.

---


### 20. [Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising](https://arxiv.org/abs/2607.24841)

**<font color=#1a73e8>作者：</font>** Dengyu Wu, Clement Ruah, Jiechen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) large language models (LLMs) are inherently inefficient at inference time because each generated token requires accessing the full set of model parameters, leading to low operational intensity and high energy consumption. Masked diffusion language models (MDLMs) partially address this limitation for memory-bound settings by allowing multiple tokens to be generated per parameter access. In order to further enhance inference efficiency on modern platforms with extensive in-chip memory, this work proposes neuromorphic MDLMs (N-MDLMs), which integrate block diffusion with spike-based neuromorphic computation to jointly improve throughput and energy efficiency. While block diffusion increases token throughput by producing multiple tokens per parameter access, spike-induced sparsity reduces effective parameter traffic and computations by skipping inactive channels. To analyze the synergistic effect of sparsity and diffusion, we develop a token-level roofline-inspired model that captures the combined impact of block-parallel generation and spike sparsity on decoding efficiency. Experimental results on translation tasks show that, thanks to spike-induced sparsity, N-MDLMs achieve substantial improvements in energy efficiency and throughput even in compute-bound platforms for which MDLMs would fail to improve over AR-LLMs.

---


### 21. [DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization](https://arxiv.org/abs/2607.24856)

**<font color=#1a73e8>作者：</font>** Wenping Yin, Ziqi Liu, Naixia Mou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Social media imagery (SMI) provides timely and fine-grained ground perspectives that are valuable for situational awareness and emergency response. Unlike satellite or aerial imagery, SMI can capture disaster impacts and ground-level conditions in a timely manner. However, geographic references in SMI are often vague or ambiguous, making accurate geolocalization challenging. To address this issue, we propose DisasterTD, a disaster toponym disambiguation framework that integrates multimodal large language model (MLLMs)-based semantic reasoning with cross-view geolocalization. First, MLLMs extract toponyms and generate candidate geolocations from noisy textual inputs. Then, cross-view matching between SMI, remote sensing imagery (RSI), and optionally street-view imagery (SVI) is used to verify and refine these candidate results. We evaluate DisasterTD on the Hurricane Harvey dataset, where SMI is augmented with collected RSI and SVI to construct a cross-view benchmark for disaster geolocalization. The dataset is divided into four categories based on toponym clarity and ambiguity, allowing a fine-grained performance analysis across scenarios. Results show that DisasterTD consistently outperforms MLLM-only and cross-view-only baselines without disambiguation, achieving geolocalization accuracies of 71.62% within 1000 m, 62.36% within 500 m, 57.99% within 250 m, 52.09% within 100 m, and 47.01% within 50 m, while reducing the mean and median errors to 11.33 km and 0.68 km, respectively. The largest improvements appear in ambiguous toponyms, where semantic reasoning with cross-view evidence reduces candidate dispersion and errors. These findings demonstrate the effectiveness of integrating MLLM-based candidate generation with cross-view verification for fine-grained disaster geolocalization.

---


### 22. [FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting](https://arxiv.org/abs/2607.24875)

**<font color=#1a73e8>作者：</font>** Dorothy Torres, Wei Cheng, Henan Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can synthesize financial narratives but may express high confidence when evidence is sparse, stale, or contradictory. This failure is especially consequential in forecasting, where filings, news, prices, volume, and technical signals can disagree. We present FinAbstain, a research framework for uncertainty-calibrated multimodal retrieval-augmented generation (RAG) with selective prediction. A point-in-time retriever admits only information public at the forecast timestamp and supplies modality-specific evidence to fundamental, news, technical, risk, and verification agents. Their probabilistic assessments are aggregated with retrieval relevance, evidence contradiction, repeated-sample consistency, and historical calibration statistics. Temperature scaling, isotonic regression, conformal prediction, and a proposed hybrid uncertainty score are evaluated under a common chronological protocol. A controller predicts bullish, bearish, or neutral outcomes only when uncertainty is below a validated threshold; otherwise it abstains, requests evidence, reduces exposure, or routes the case to human review. The evaluation covers one- and five-day abnormal-return direction, twenty-day volatility intervals, and abstention decisions, using accuracy, calibration, risk--coverage, citation, trading, latency, and cost metrics. To make the design auditable before a full data collection is complete, we report explicitly labeled simulated results rather than empirical claims. These results illustrate the intended hypothesis: calibrated abstention may trade coverage for lower selective error and drawdown. The contribution is a time-safe architecture, a composite uncertainty formulation, and a reproducible evaluation blueprint for evidence-grounded selective financial forecasting.

---


### 23. [LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models](https://arxiv.org/abs/2607.24892)

**<font color=#1a73e8>作者：</font>** Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-conditioned time-series forecasting predicts a series from both its numerical history and natural-language context, allowing forecasts to account for events and constraints that the past alone cannot reveal. This requires both reliable numerical forecasting and the ability to interpret contextual information. Time-series foundation models (TSFMs) provide strong numerical forecasts, while large language models (LLMs) can reason over text, but combining their strengths remains challenging because asking an LLM to generate or revise forecast values directly can distort the temporal structure captured by the TSFM. We instead formulate forecasting as a planning problem over TSFM-generated trajectories. The frozen TSFM acts as a simulator that proposes numerical continuations, while the LLM acts as a policy and value function that guides candidate selection and evaluates completed trajectories against the context. We instantiate this as \rc{} (\textbf{L}LM \textbf{A}s \textbf{F}orecasting \textbf{P}lanner), a training-free framework that bridges the modality gap without retraining either model, using Monte Carlo tree search (MCTS) over the forecast horizon with a \emph{Ranker} LLM as policy and a \emph{Judge} LLM as value function. Experiments on Context-is-Key and Time-MMD across two TSFM backbones (Chronos and TimesFM) and four LLMs show that \rc{} delivers consistent improvements across model choices, supporting sequential search as an effective training-free approach to text-conditioned forecasting.

---


### 24. [Harm is not Universal: Community-Specific Toxicity Detection is Urgently Needed](https://arxiv.org/abs/2607.24898)

**<font color=#1a73e8>作者：</font>** Xinnuo Xu, Anja Thieme, Daniela Massiceti 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art toxicity detectors for text-to-image generation adopt a one-size-fits-all approach: a single universal model applying fixed safety guidelines to all users. Our empirical evidence shows that these detectors fail to shield marginalized communities: approximately 35% of generated images labeled safe are considered harmful by disability communities. In this position paper, we argue for community-specific toxicity detection (CTD). To demonstrate its feasibility, we collaborate with disability experts to develop safety guidelines for two communities: dwarfism and blind/low vision. Using a dataset of 2,400 annotated T2I-generated images we demonstrate that both large vision-language models and existing general-purpose toxicity detectors catastrophically fail to recognize harmful content under these guidelines in zero-shot settings with F1 score lower than random guessing (F1 0.32 and 0.37). Promisingly, prompt-based adaptation methods (ICL, VQA) substantially improve harm detection performance (GPT-4o: F1 0.50 and 0.78), while parameter-efficient fine-tuning improves smaller models (0.5b-7b with best F1 0.48 and 0.59) with less than 100 demonstrations, but remains sensitive to evolving guidelines. Despite these gains, CTD performance remains far below F1 $\approx 0.9$ achieved for general-purpose toxicity detection, highlighting the challenge and the need for sustained research effort.

---


### 25. [Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://arxiv.org/abs/2607.24904)

**<font color=#1a73e8>作者：</font>** Senqiao Yang, Kaichen Zhang, Zhaoyang Jia 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

---


### 26. [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](https://arxiv.org/abs/2607.24957)

**<font color=#1a73e8>作者：</font>** Zichao Lin, Yifeng Xie, Bowen Qu 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs). Existing benchmarks often fail to isolate perception: holistic evaluations conflate perceptual errors with failures in reasoning or domain knowledge, while application-driven benchmarks only cover narrow, fragmented domains shaped by heuristic designs. To address these limitations, PerceptionBench adopts a bottom-up approach: by diagnosing the earliest failure points in the responses of frontier MLLMs across 42 existing benchmarks, we construct an error taxonomy whose perception branch defines ten atomic perceptual capabilities. Guided by this taxonomy, we construct 3,000 verified questions with short, unambiguous answers, each isolating a single capability, with difficulty stemming from perception rather than reasoning or knowledge. Benchmark results across sixteen frontier MLLMs reveal that atomic perception remains largely unsolved---no model reaches 60\% accuracy, perception-related hallucination is the weakest capability on average, and similar overall scores conceal sharply divergent capability profiles. PerceptionBench thus provides a capability-level standard for measuring and diagnosing the visual perception boundaries of MLLMs.

---


### 27. [CogArena: A Multimethod Evaluation of Cognitive Ability Structure in Large Language Models](https://arxiv.org/abs/2607.24999)

**<font color=#1a73e8>作者：</font>** Dengzhe Hou, Lingyu Jiang, Fangzhou Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM cognitive scores are increasingly summarized as per-ability profiles whose dimensions should converge across tasks, respond selectively to matched interventions, and generalize beyond the models used to define them. We introduce CogArena, a procedurally generated 13-paradigm benchmark built around a multimethod framework for determining when cognitive-task scores warrant dimensional labels across five theory-motivated groupings. Across 55 open-weight models, nearly all paradigm correlations are positive and a common axis explains about half the variance. The within-grouping advantage is small, scoring-sensitive, and uncertain across model families. In a separately frozen, fully crossed study across 12 models from six families, targeted scaffolds show a small matched-grouping advantage, but no scaffold-specific contrast survives multiplicity correction and selectivity does not improve held-out-family prediction. The frozen confirmation criterion fails. A post-hoc alternate-wording replication produces a smaller positive estimate and again fails. Together, these results support a boundary conclusion. Theory-aligned prompting produces a small in-battery diagonal tendency, but the present evidence does not establish stable five-dimensional profiles. CogArena provides a workflow joining behavioral signatures, covariance, matched interventions, and out-of-family prediction before cognitive labels are attached to model scores.

---


### 28. [The AI Wave and the Reinvention of Game Discovery: Oversupply, Structural Correction, and Agentic Player-Game Matching](https://arxiv.org/abs/2607.25010)

**<font color=#1a73e8>作者：</font>** Brian Dean Madanamootoo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted production has sharply reduced the cost and team size required to ship a video game, producing a supply shock on open marketplaces. Recent estimates put Steam release volume at roughly sixty new titles per day, with median per-title revenue for a large share of releases falling below the platform's own submission fee [1]. This paper asks whether the resulting oversupply constitutes an emerging market crash or a structural correction, and what discovery infrastructure the market will require as a consequence.
We first quantify the 2010-2026 supply shock using a 93,073-title Steam metadata snapshot, a 200,000-interaction Steam user-behavior dataset, and this http URL catalog data, computing attention-concentration metrics directly (Gini coefficient of 0.96 over playtime, with the top 1 percent of titles absorbing 73.5 percent of total play hours), and we introduce generative asset-model release velocity on Hugging Face as a candidate leading indicator of production-cost decline. We then conduct a comparative-historical analysis against the 1983 North American video game crash, the closest documented case of supply-driven collapse in the medium's history, identifying which structural divergences (digital distribution, diversified incumbent revenue, and consolidation capital) redirect the present contraction toward concentration rather than collapse, drawing on incumbent evidence including Ubisoft's 2025-26 restructuring and its transfer of equity to Tencent-backed Vantage Studios. Third, we analyze Netflix Games, Xbox Game Pass, and the curated browser platform Poki as natural experiments in access-based distribution.

---


### 29. [Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference](https://arxiv.org/abs/2607.25018)

**<font color=#1a73e8>作者：</font>** Yifan Dou, Shikan Fang, Shibo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one. Production cascades govern this deferral through a confidence threshold, but LLM confidence scores are miscalibrated, the threshold must be tuned per model pair and per domain, and no setting yields a formal bound on cascade accuracy. We introduce \textbf{Conformal Cascade} (CC), a multi-tier inference framework that uses conformal prediction set size as the deferral rule: accept when the calibrated set collapses to a single answer, defer otherwise. The procedure delivers a distribution-free, finite-sample accuracy guarantee. By a per-tier union bound, the prediction set at the accepting tier covers the correct answer with probability at least $1 - K\alpha$ for any user-specified $\alpha$; under a selection-preservation condition (consistent with, but not strictly implied by, our marginal coverage results), the bound tightens to $1 - \alpha$. We further characterise expected cascade cost as an explicit function of $\alpha$ and the calibration-set acceptance rate. Across 18 multiple-choice benchmarks spanning science, medicine, commonsense, and standardized exams, evaluated on two-tier cascades drawn from four open-weight model families, CC strictly improves over the strongest calibration-tuned heuristic cascade on the majority of family--benchmark pairs, with the largest gains on reasoning-heavy benchmarks where majority vote is unreliable; on easier benchmarks the cascade commits the vast majority of queries to the small model at no accuracy cost. Extension to open-ended generation requires an answer-clustering step that we leave for future work. The method requires no model training and only black-box API access.

---


### 30. [Chart-Supported or Model-Supplied? Examining MLLM-Generated Claims for Accessible Visualization](https://arxiv.org/abs/2607.25021)

**<font color=#1a73e8>作者：</font>** Ishrat Jahan Eliza, Md Dilshadur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can connect visualization patterns to external causes, consequences, and domain knowledge, but the evidential basis of these interpretations is often unclear. We present an exploratory study of 102 visualizations from four sources, three MLLMs, and four input conditions that vary access to the image, source-specific accessible chart context, and withheld-context framing. Across 1,224 descriptions, we analyze model-attributed DIRECT, DERIVED, and SPECULATIVE labels and conduct an automated audit of numeric agreement. Accessible chart context shifted Gemini and GPT toward DIRECT claims and improved numeric agreement for some models. Adding the image to the full context did not yield a consistent numeric benefit, and the withheld-context prompt did not reliably increase cautious language. The prompt-defined Real-World Significance section remained predominantly SPECULATIVE. These results motivate accessible description systems that distinguish claims supported by supplied evidence from model-supplied interpretation

---


### 31. [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](https://arxiv.org/abs/2607.25063)

**<font color=#1a73e8>作者：</font>** Cen Lu, Yung-Chen Tang, Andrea Cavallaro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developers judge a model checkpoint by how it behaves. After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization. We ask whether this judgment misses a pretraining imprint: a difference that no post-SFT benchmark reveals, yet that decides how each checkpoint responds to further training. To find out, we run a controlled experiment on the final window of pretraining, the last data trained on before instruction tuning. Six branches fork from one partially pretrained checkpoint and differ only in this window: 500 million tokens, 0.1% to 1% of the tokens that precede it. Each branch trains its window on a single data source: generic web text, filtered web text, normative discourse, safety text, mathematical text, or synthetic educational text. SFT and post-training are then identical. After SFT the branches behave near-identically, within about one point on instruction following, refusal, and capability, yet the same post-training carries them to very different endpoints, under both a direct preference optimization update and a reinforcement learning update with a verifiable reward. We measure this deviation through refusal of harmful requests: when post-training begins the safety text branch refuses no more than the web text branch, yet by the end it has lost far less of its refusal. The other four branches gain little or no protection, so the effect is selective to what the window contained. The protection requires the safety text to arrive last rather than earlier in pretraining, and it reproduces on a second model family. What a model is pretrained on last shapes how it reacts to alignment. Therefore, a checkpoint should not be evaluated by its post-SFT behavior alone, and what it was trained on last should be reported with it.

---


### 32. [Addressable Recall Compaction for Long Context-Window Control in AI Agents](https://arxiv.org/abs/2607.25066)

**<font color=#1a73e8>作者：</font>** Thang Dang, Yuma Ichikawa, Sakina Fatima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window. Existing compaction methods address this limitation by discarding, summarizing, or retrieving earlier information, but they may remove task-critical details or fail to recover them reliably. We propose ARC (Addressable Recall Compaction), a context-management framework that separates archival storage from active-context presentation. ARC stores tool observations in an append-only, ID-addressable log and replaces older observations with compact citations when compaction is required. The agent can subsequently use these identifiers to request stored content without re-executing the corresponding tools or depending solely on similarity-based retrieval. We evaluate ARC using Qwen3-8B with a 16k context window and Qwen3-32B with a 32k context window. On the Needle-in-a-Haystack evaluation, ARC achieves an average exact-answer accuracy of 99.40%, compared with 88.12% for the best-performing baseline in our evaluation. ARC also reduces estimated serving time and HBM traffic under our hardware-cost model. On the LongBench-v2 Hard subset, ARC obtains an average accuracy of 29.97%, compared with 28.25% for the best-performing baseline. These results indicate that explicit, address-based recall can improve information retention and serving efficiency relative to the evaluated context-management baselines under the tested settings.

---


### 33. [How Often Should a Recommender Call an LLM? Value-Weighted Routing, Monitoring, and Seasonal Robustness](https://arxiv.org/abs/2607.25068)

**<font color=#1a73e8>作者：</font>** Bhavtosh Rath  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routing decisions between a cheap heuristic and an expensive large language model (LLM) are typically framed as a difficulty problem: send the hard cases to the expensive path. We argue this framing is incomplete because difficulty and business value are distinct axes - a difficult cheap item and a difficult costly item do not have the same cost of error. We present Value Router, a fully synthetic simulation of a retail merchandising pipeline that routes items using only estimated difficulty and estimated value, never ground truth. The study has three stages. First, a value-weighted threshold router is compared with a difficulty-only and a random baseline on a synthetic catalog with an inverse correlation between category volume and value. Value-weighting matches the difficulty-only baseline's recall of true high-value items (60%) while achieving substantially higher precision (98.3% vs. 94.3%). Second, a decision logger and monitor expose a failure mode hidden by aggregate metrics showing that the aggregate result is driven almost entirely by between-category differences rather than per-item discrimination. Third, a simulated Black Friday demand surge (2.5 volume with a shift toward higher-value categories) compares a static router, a seasonally tuned router, and two slow-path budget policies. All results are from a controlled synthetic simulation with experimenter-defined ground truth and illustrate design principles for cost-aware routing systems rather than validated real-world claims.

---


### 34. [DS@GT ARC at CheckThat! 2026: LLM-Based Trace Ranking and Grouped Reward Modeling for Multilingual Numerical Claim Verification](https://arxiv.org/abs/2607.25069)

**<font color=#1a73e8>作者：</font>** Sagnik Sinha, Shreyas Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated verification of numerical claims is a challenging problem, as it requires both language understanding and quantitative reasoning. This paper describes our system for CLEF 2026 CheckThat! Task 2, which focuses on ranking reasoning traces generated by large language models (LLMs) and predicting a final verdict for numerical claims in English and Arabic. We explore two approaches. The first approach fine-tunes an LLM-based verifier using LoRA to score each reasoning trace independently as a binary classification problem, and selects the final verdict using Best-of-N selection. We further experiment with adaptive sub-claim decomposition to break complex claims into simpler parts before verification. The second approach uses a lightweight TF-IDF reward model with handcrafted numeric and temporal overlap features to score traces, and aggregates scores by verdict group to determine the final prediction. For Arabic, we compare a general multilingual model against AraBERT, a language-specific model pretrained on Arabic text. Our results show that the LLM-based approach outperforms the lightweight reward model on most metrics, particularly Recall@5, while the reward-based approach shows stronger performance on the Conflicting class. Sub-claim decomposition did not improve performance, suggesting that claim splitting introduces noise rather than aiding reasoning. For Arabic, AraBERT outperforms the multilingual baseline across most metrics.

---


### 35. [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](https://arxiv.org/abs/2607.25091)

**<font color=#1a73e8>作者：</font>** Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). The experiments included Pythia-70M, 160M, 410M and SmolLM2-135M, 360M on the TinyStories, CNN/DailyMail, and Wikitext-103 corpora. Three reproducible failure modes were identified in small-scale language models: silent LoRA parameter freezing in standard PEFT/TRL pipelines, numerical overflow in importance ratios when using bfloat16, and catastrophic policy collapse due to reward-model error. These issues were addressed using a merge-and-reinitialize adapter technique, float32 precision during PPO updates, and a three-layer safety mechanism comprising reward whitening, importance-ratio guarding, and weight rollback. In this paper, a capacity-headroom hypothesis is proposed, which states that PPO performance at the SLM scale depends on both a fluent supervised model ($\text{PPL}<20$) and a discriminative reward signal, rather than on the number of model parameters. The proposed system converged stably in all experiments and improved preference win rate over the SFT baseline in configurations with a fluent prior and an informative reward signal. Furthermore, it outperformed instruction-tuned baselines while requiring significantly less training data. All checkpoints, preference datasets, and training scripts are publicly released$^§$.

---


### 36. [Evaluating Communicative Belief Updates in Large Language Models via Implicature Recognition and Cancellation](https://arxiv.org/abs/2607.25094)

**<font color=#1a73e8>作者：</font>** Cesare Spinoso-Di Piano, Verna Dankers, Marius Mosbach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human language is driven by unspoken beliefs and belief updates, making these critical to model for successful communication between large language models (LLMs) and their users. In this paper, we evaluate the ability of LLMs to recognize unspoken beliefs made through implicatures and to understand their updates through implicature cancellation: the pragmatic phenomenon whereby an utterance's implied meaning is weakened or negated. We create the first expert-annotated implicature cancellation dataset, [DatasetName], crowdsourced for human judgements of implicatures and their corresponding cancellations. We find that LLM belief update understanding lags behind that of humans, especially in more naturally-occurring scenarios. Additional control experiments suggest that successes in LLM belief updates may stem in part from a reliance on prior beliefs, and that failures in belief updates may depend on their type and on their form. Overall, our study suggests that current LLMs have not yet reached human-level understanding of unspoken beliefs and belief updates. Code and data are available at this https URL.

---


### 37. [UrbanTrace: LLM-Assisted Discovery and Semantics-Aware Integration of Spatial Data](https://arxiv.org/abs/2607.25124)

**<font color=#1a73e8>作者：</font>** Sonia Castelo, Eden Wu, Joao Rulff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Urban decision-making requires integrating heterogeneous spatial data. While current GIS tools handle geometric computation efficiently, they lack the semantic reasoning to guide complex workflows. Analysts manually manage data discovery, spatial boundaries, and measurement semantics, risking aggregation errors. We present UrbanTrace, a visual analytics system that transforms manual spatial data-wrangling into a transparent, node-based collaborative workflow with context-aware AI agents. Using an offline profiler to extract semantic and geometric metadata, UrbanTrace grounds LLMs in real-world data distributions. This enables specialized agents to retrieve datasets based on high-level goals and automatically enforce valid spatial aggregations. To make harmonization explicit, three interactive views: an Integration Provenance Graph, Multivariate Priority Map, and Spatial Delta Map, allow users to explore how conclusions shift across spatial configurations. We evaluate UrbanTrace on 28 urban scenarios spanning 112 datasets. Quantitative ablations show our profiling significantly outperforms baseline LLMs in data discovery, achieving 100% semantic and 87% geometric validity in spatial mapping. Through real-world case studies and expert interviews, we demonstrate that UrbanTrace turns spatial aggregation sensitivity from a methodological burden into an exploratory visual asset.

---


### 38. [LENS: Adaptive Spatio-Temporal Zooming for Keyframe Sampling in Long-Form Videos](https://arxiv.org/abs/2607.25125)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Jinxi He, Katia Sycara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in Multi-modal Large Language Models (MLLMs), understanding long-form videos is still bottlenecked by limited context windows. While recent keyframe sampling methods attempt to mitigate this by distilling video inputs into a compact set of query-relevant frames, navigating the vast spatio-temporal search space remains challenging, as spatial detail and temporal coverage often conflict. To address this, we introduce LENS, a training-free keyframe sampling framework that dynamically decides when to zoom in for fine-grained details and when to zoom out for broader context based on the text query. Concretely, LENS adaptively allocates a limited frame budget between spatial zoom-ins, which highlight query-relevant regions within individual frames, and temporal zoom-outs, which expand the temporal scope through multi-frame aggregation, enabling the model to reason across multiple granularities while capturing both high-fidelity details and long-range context. Across diverse long-form video benchmarks, LENS consistently outperforms prior state-of-the-art keyframe sampling methods and delivers substantial gains over uniform sampling, improving Video-MME accuracy from 53.3% to 60.7% with this http URL is available at this https URL.

---


### 39. [ScalableRAG: High-Quality RAG at Zero Ingestion Cost](https://arxiv.org/abs/2607.25135)

**<font color=#1a73e8>作者：</font>** Hilaf Hasson, Aditya Chakravarty, Jayant Thomas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in RAG aim to optimize for performance by paying high ingestion costs for knowledge ingestion: building knowledge graphs or extracting SQL tables. In this work we show that the operations that such knowledge bases allow can be replicated with zero ingestion costs (not even a vector database); in fact our solution, Zero-Ingestion ScalableRAG, handily out-performs all baselines (including knowledge graph approaches) in three out of the six corpora considered here, and only marginally missing maximum performance on the other three, with average accuracy across all six datasets 7.36% above the next most competitive baseline. It achieves this by keeping a workspace of document sets and values sets that it can write into and read from, allowing for on-the-fly aggregative reasoning in all situations where grouping is required on a primary key that is in one to one correspondence with a subset of the total document set.
Capping the number of LLM calls by a constant independent of the corpus size, we also introduce Limited-Ingestion ScalableRAG, which does use a minimal vector database as well as an automated pattern discovery from a sample of documents, to further improve accuracy at scale. Our code is available at this https URL .

---


### 40. [How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation](https://arxiv.org/abs/2607.25140)

**<font color=#1a73e8>作者：</font>** Funda Durupinar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outward expression. The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception-appraisal-expression loop. The agent representation draws on the Big Five personality model and Russell's circumplex model of affect. To limit latency, low-level steering and navigation are handled by a conventional crowd simulator operating independently of the LLM-based cognitive layer.
We evaluate the architecture across five scenario environments spanning alarming, joyful, and neutral situations in different spatial layouts. The results show that the system produces emotional contagion dynamics with spatial, temporal, and personality-dependent structure in sparse, small crowds. Alarm spreads from seeded agents as a traveling front, the mean alarmed fraction settles at a nonzero plateau, and the distribution of prompted personality profiles determines whether an ambiguous alarm ignites panic and whether a provocation is interpreted as anger or fear. We further evaluate the appraisal step through controlled experiments across prompt variants, sampling temperatures, and four model backends, showing that the dynamics are backend-dependent.

---


### 41. [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](https://arxiv.org/abs/2607.25152)

**<font color=#1a73e8>作者：</font>** Hyundoo Park, Byungho Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. We name this failure mode the progress mirage and show, with controlled measurement, that it is a question of what the evaluator is grounded in. We built a testbed that holds the agent and its tool surface fixed and manipulates only the information-channel type of the evaluator that gates the loop. A world-state oracle, unfakeable in principle, is enforced by container and network isolation and verified at every run. Across 54 cycles a frontier agent claimed improvement every time, yet 56 percent had a measured delta of zero or below. Self-report was thus uninformative, and the self-verdict gate degenerated into accept-all, eroding the best deployed state it had reached by 19 percent. Even the strongest in-band judge, reading the full artifact text, the change diff, and its own verdict history, accepted cycles of which 44 percent were real-world regressions and rejected 38 percent of real improvements; the preregistered adversarial hypothesis that a strong judge closes the gap was rejected. On a boundary task whose success specification is verifiable from the artifact itself, the same judge's mirage vanished to zero and the gap collapsed within the registered threshold, showing that the gap depends on where the success signal resides. A sign-only variant returning only the acceptance verdict kept real-world output similar to full feedback (110.0 versus 113.0), locating the benefit in the gate's grounding rather than in feedback content. For open-ended objectives whose success signal lives outside the transcript, scaling up the judge is not enough; out-of-band evaluation with real-world access is a structural requirement.

---


### 42. [PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention](https://arxiv.org/abs/2607.25157)

**<font color=#1a73e8>作者：</font>** Zhengtao Yao, Runhao Li, Xupeng Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete masked diffusion language models support bidirectional generation and infilling, but adapting pretrained autoregressive (AR) transformers requires reconciling causal pretraining with bidirectional denoising. We study this problem at the level of attention rather than claiming AR-weight reuse itself as novel. PreDiff-LM preserves causal attention within the observed prompt while allowing full bidirectional attention within the masked target. Under a matched GPT-2 Medium, WikiText-103, 90K-step setup, this hybrid mask improves unconditional perplexity from 34.1 to 28.7 and MAUVE from 0.71 to 0.78 over uniform bidirectional attention with the same AR initialization. Attention adaptation also composes with a DiffuGPT-style objective adaptation, reaching 26.9 perplexity. Pretrained initialization reduces the steps required to reach perplexity below 50 from about 350K to 8K, although a compute-matched fine-tuned AR model remains stronger at equal scale (18.9 versus 28.7). Beyond perplexity, PreDiff-LM improves repetition, distributional quality, four zero-shot downstream tasks, and human preference over prior diffusion baselines. The results position hybrid attention as a complementary mechanism for adapting pretrained causal backbones, while making explicit the remaining quality and inference-efficiency gaps to optimized AR models.

---


### 43. [OrganLens: Organ-Specific Representation Learning for CT Foundation Models](https://arxiv.org/abs/2607.25164)

**<font color=#1a73e8>作者：</font>** Zhixuan Ge, Anqi Li, Sadeer Al-Kindi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A CT examination captures multiple organs, but many biomedical questions concern abnormalities, prognosis, or longitudinal change in a specific organ. These questions require a separate representation for each organ within the same CT volume. Existing CT foundation models commonly produce a single volume-level representation, while recent anatomy-aware methods either encode pre-separated organ volumes or explicitly disentangle images into organ token groups. The former may remove clinically relevant surrounding context, while the latter does not condition a shared encoder on a selected organ before its features are formed. We introduce OrganLens for organ-specific representation learning through self-supervision. An organ identity conditions a shared CT encoder, while organ-specific distillation and anatomy-mask supervision shape features for anatomy-weighted pooling into organ-specific representations. At inference, the shared model produces 11 organ-specific representations without external segmentation masks. We evaluate OrganLens on CT-RATE, RAD-ChestCT, INSPECT, and NLST across diverse acquisitions and downstream evaluations. Relative to CT-pretrained DINOv2, heart representations raise CT-RATE cardiomegaly AUROC from 0.910 to 0.953, while lung representations improve the Harrell C-index for NLST lung-cancer mortality by 14.2\%. The global representation reaches INSPECT Recall@10 of 33.09\% and 32.04\% for text-to-image and image-to-text retrieval, respectively. Across organ-related tasks, anatomically matched representations provide stronger task-relevant signal, while the global representation retains broad utility. OrganLens offers a scalable approach to organ-specific CT representation learning with a shared encoder. More broadly, it provides the medical research community with a reusable framework for studying organ-specific disease across cohorts and clinical endpoints.

---


### 44. [Agentic AI-enabled discovery across large-scale sleep physiology](https://arxiv.org/abs/2607.25175)

**<font color=#1a73e8>作者：</font>** Rahul Thapa, Umaer Hanif, Robin Guillard 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Sleep occupies roughly one-third of human life, yet many aspects of its physiology remain poorly understood. Large polysomnography (PSG) datasets offer new opportunities to study sleep and its links to disease, but extracting insight from these recordings requires substantial expert effort and remains difficult for general-purpose AI systems. We developed AI Sleep Co-Scientist, an expert-guided environment in which human scientists direct specialist agents for hypothesis development, signal preprocessing, and statistical analysis, reviewing intermediate outputs. Each reported result is linked to the executable code that produced it. Across four cohorts of approximately 124,000 PSG recordings and more than 50 TB of raw signals, we conducted five case studies spanning how sleep physiology relates to future disease, how it distinguishes clinical phenotypes, and how sleep is organized and regulated. Diminished network-level physiological coupling during sleep was associated with incident Parkinson's disease (HR 1.48) and Alzheimer's disease (HR 1.38). A physiologically structured late-fusion sleep-age model outperformed an unconstrained early-fusion approach, and its age residual was associated with incident disease across multiple organ systems. Arousal dynamics characterized comorbid insomnia and sleep apnoea as an intermediate phenotype skewed towards obstructive sleep apnoea, distinguished by prolonged post-arousal wakefulness. Rapid eye movement (REM) bout duration tracked preceding non-REM sleep more closely than intervening wakefulness. Transient-oscillation analysis identified a fast-sigma deficit and excess centrofrontal theta activity in narcolepsy type 1. Together, these findings connect sleep to disease risk, clinical classification, and its own regulation, and show how agentic AI can support large-scale, multimodal discovery.

---


### 45. [MyoCardBench: A Real-World Data Benchmark for Evaluating Large Language Models in Clinically Authentic Cardiovascular Care Scenarios](https://arxiv.org/abs/2607.25186)

**<font color=#1a73e8>作者：</font>** Xiao Li, Mouxiao Bian, Zhaodi Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Most medical large language model (LLM) benchmarks focus on examination knowledge or isolated tasks and may not reflect the longitudinal, multimodal, and safety-critical workflow of cardiovascular care. Objective: To develop MyoCardBench, a real-world benchmark spanning the cardiovascular care continuum, and assess LLM performance across clinical dimensions and specialist tasks. Methods: MyoCardBench includes 2,263 items from 13 task-specific datasets derived from de-identified cardiovascular records and examination data. Sixteen cardiology physicians conducted annotation and reference construction, followed by cross-review from two senior cardiologists. Seven LLMs generated 15,841 outputs under standardized zero-shot settings. Open-ended tasks were evaluated using key-point coverage and holistic clinical quality, while CardioEthics was scored by accuracy. Results: GPT-5.4 achieved the highest macro-average (62.55) and item-weighted mean (62.19), followed by Gemini 3.1 Pro (59.95) and Qwen 3.6 27B (59.72). GPT-5.4 ranked first in all three dimensions. CardioAuxReport performed best (86.38), whereas CardioECGRead (17.25) and CardioEthics (17.34) were lowest. The largest gaps between holistic clinical quality and key-point coverage occurred in CardioComm (52.71), CardioEmergRescue (52.05), and CardioTreatPlan (48.80). Conclusions: To our knowledge, MyoCardBench is the largest real-world, multi-task benchmark for LLM evaluation across the cardiovascular care continuum and offers the broadest coverage of clinically authentic cardiology scenarios reported to date. It provides a rigorous framework for identifying model strengths, clinically important omissions, and priorities for future development.

---


### 46. [Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs](https://arxiv.org/abs/2607.25196)

**<font color=#1a73e8>作者：</font>** Arnav Bendre, Guneesh Gupta, Kavish Grover 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive decoding (CD) has been proposed as a training-free strategy for mitigating object hallucinations in multimodal large language models (MLLMs), with reported gains on benchmarks such as POPE. However, recent work has questioned whether these gains reflect genuine improvements in visual grounding. In this study, we reproduce and extend the findings of "The Mirage of Performance Gains: Why Contrastive Decoding Fails to Mitigate Object Hallucinations in MLLMs." Specifically, we test the claim that CD induces a unidirectional output distribution shift in discriminative datasets and examine its generalizability across datasets. We also verify that the adaptive plausibility constraint (APC) reduces sampling to greedy search on both discriminative and generative benchmarks. Beyond reproduction, we rigorously study the effects of CD across generative and discriminative datasets. We conduct several experiments that provide additional insights: we analyze the logit distributions induced by different CD strategies on generative datasets, propose a proxy method and compare its performance against CD techniques, and investigate how hallucination signals propagate through each layer of the expert and amateur models. Experimental results across MME, POPE, and CHAIR using LLaVA and Qwen validate the original claims and show that the apparent improvements from CD are often spurious and do not consistently translate into stronger visual grounding for reducing hallucinations. These findings challenge the effectiveness of current contrastive decoding strategies and motivate the development of more reliable approaches for mitigating hallucinations in MLLMs.

---


### 47. [Everyone is unique: Towards Behaviorally Heterogeneous Negotiation Dialogue Systems for Debt Collection](https://arxiv.org/abs/2607.25218)

**<font color=#1a73e8>作者：</font>** Yuhang Yang, Kai Tang, Chao Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Debt collection is a critical negotiation task in the financial industry, with strong practical relevance and exceptional academic value as a behaviorally rich, high-stakes testbed for human-centered dialogue systems. While large language models (LLMs) have shown promise in dialogue and negotiation, effectively evaluating their performance in this complex scenarios remains a major challenge: existing benchmarks uniformly assume users to be static, rational agents with fixed preferences, failing to capture the rich behavioral heterogeneity inherent in real-world debt collection. To bridge this gap, we propose DebtBench, the first public persona-enriched debt collection benchmark, that highlights behavioral heterogeneity in negotiation. Moreover, we develop DebtGPT, a debt collection agent trained to jointly optimize financial recovery and interaction experience. Our experimental results, using 16 state-of-the-art LLMs, find that most existing models struggle in this complex but realistic scenarios, whereas DebtGPT outperforms all open-source baselines and achieves performance on par with GPT-4o. The code and data are available at this https URL.

---


### 48. [Interpretable Column Annotation with LLM-Symbolized Decision Process Materialization](https://arxiv.org/abs/2607.25228)

**<font color=#1a73e8>作者：</font>** Mengqi Wang, Jianwei Wang, Qing Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Column annotation (CA), including column type annotation (CTA) and column property annotation (CPA), aims to identify the meanings of table columns and the semantic relationships among them. Recent CA methods usually use various neural models to learn column representations and directly map them to label categories, thereby (1) sacrificing model interpretability and adaptivity, and (2) overlooking rich label semantics and ultimately limiting accuracy. To address these limitations, we propose SymCA, an LLM-empowered interpretable CA framework that materializes column annotation as a global-to-local symbolic decision process. SymCA consists of two components: (1) global skeleton induction, which constructs a semantic skeleton over the label space, and (2) local substrate evolution, which evolves predictive substrates within the skeleton. Specifically, to exploit label semantics while preserving an interpretable decision process, the global skeleton induction module leverages LLMs to generate candidate hypernym-inspired tree-structured semantic skeletons and employs a Minimum Bayes Risk (MBR)-based consensus strategy to select a robust skeleton against generation variance. Since different internal nodes require different evidence to distinguish among their child nodes, the local substrate evolution module materializes each internal node as an executable and evolvable predictive substrate. Over multiple evolution rounds, each substrate trains an interpretable random forest classifier with the current operator set, leverages the LLM to propose node-specific operator modifications, and uses an exploration-exploitation strategy to prioritize promising substrates. Extensive experiments demonstrate that SymCA is accurate, robust, and interpretable, outperforming the strongest baselines by an average of 6.42% in Micro-F1 and 11.03% in Macro-F1.

---


### 49. [Neurai-VN Benchmark: Standardized Machine Learning Models for Multimodal Digital Phenotyping in Mental Health Classification](https://arxiv.org/abs/2607.25232)

**<font color=#1a73e8>作者：</font>** Quoc-Cuong Pham, Hoang-Thuy-Duong Vu, Thi-Thanh-Huong Ha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital phenotyping (DP) using smartphones and wearable devices has shown considerable potential for mental health monitoring. However, progress remains difficult to evaluate due to heterogeneous datasets, inconsistent preprocessing pipelines. In this study, we present a reproducible benchmark built upon the Neurai-VN dataset, a high-resolution, multimodal dataset comprising passive sensing and active assessment from wearable and smartphone devices, collected from 100 Vietnamese adults over two weeks. The benchmark defines four clinically relevant binary classification tasks evaluated using standardized subject-wise cross-validation. Representative linear, tree-based, and neural baseline models are evaluated across predefined feature configurations. Mean subject-level F1 scores across five cross-validation folds reached 0.71 for Healthy Control vs. Depression and Healthy Control vs. Clinical, while Healthy Control vs. Anxiety and Depression vs. Anxiety achieved 0.69 and 0.56, respectively. These benchmark results provide reproducible baselines for future research on multimodal DP for mental health classification tasks.

---


### 50. [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/abs/2607.25236)

**<font color=#1a73e8>作者：</font>** Jiaxin Bai, Jiaxuan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Different research lines use the term world model in different ways, yet they share a common aim: to capture how the world evolves under action in a form that supports perception, simulation, and planning. Two prominent realizations are neural predictors that learn dynamics in continuous vector spaces, and hand-built physics engines that expose explicit state and physical laws. Neural predictors scale from data but leave the form of the dynamics implicit; physics engines are inspectable and editable but difficult to construct at scale. We introduce VisualPatchWorld (VPW), which represents world dynamics as code. VPW first selects a qualitative dynamical form with short active probes, then fits that form's free parameters from recorded state-action traces by minimizing multi-step prediction error. The resulting programs can be rolled forward like a simulator, inspected in source form, and used inside model-predictive control; image-derived scene graphs can supply the live state at replan time. Across comparisons with prior code-based world models, VPW attains 69.0% mean planning success and exceeds the strongest code baseline by 23.5 points. The largest gains arise when choosing the correct qualitative dynamics is essential. Under the same planner, the induced models approach ground-truth engine success on navigation and grasp-rich control; a residual gap remains for contact-rich pushing, and checking a shortlist of promising plans in the engine closes most of that gap. These results establish a practical route toward automatically constructed code world models that are useful for planning. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-131](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
