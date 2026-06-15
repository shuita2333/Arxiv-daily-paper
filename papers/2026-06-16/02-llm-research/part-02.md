# 🧠 大模型相关研究 | 2026年06月16日

> 本类共 **66** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-66**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-66**

---

### 51. [IndustryBench-MIPU: Benchmarking Multi-Image Attribute Value Extraction for Industrial Products](https://arxiv.org/abs/2606.14383)

**<font color=#1a73e8>作者：</font>** Haonan Qi, Jin Cao, Yongqi Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial products such as valves and circuit breakers are defined by dense technical specifications that govern procurement, compatibility, and safety across supply chains. These specifications are scattered across multiple heterogeneous product images, including specification tables, nameplates, and technical drawings, yet whether Multimodal Large Language Models (MLLMs) can reliably recover them remains underexplored. To fill this gap, we introduce IndustryBench-MIPU, the first large-scale benchmark for multi-image industrial product understanding, built around structured attribute extraction -- recovering property-value pairs from product images. This task jointly probes text recognition on specification tables and nameplates, visual reasoning over technical drawings, domain knowledge to decode industrial terminology, and cross-image evidence integration to assemble scattered specifications. Concretely, the benchmark comprises 4,559 products across 27,652 images with 103,703 annotations spanning 18 industrial categories, constructed through multi-model consensus and three-tier quality assurance. Evaluating nine MLLMs under both single-image and product-level multi-image settings reveals a stark completeness gap: models achieve high precision (86--94%) but the best recovers only 49.9% of product-level attributes; moving from single-image to multi-image extraction costs 15--34 percentage points of recall. Multi-image completeness, not single-image accuracy, is the core bottleneck. Dataset and code are publicly available.

---


### 52. [A Low-Rank Subspace Analysis of LLM Interventions](https://arxiv.org/abs/2606.14388)

**<font color=#1a73e8>作者：</font>** Angira Sharma, Christian Schroeder de Witt, Philip Torr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interventions designed to modify a particular behavior in LLMs, such as refusal or sycophancy, often produce unintended changes in other behaviors. This lack of targeted control makes it difficult to design and implement reliable safety controls. To understand these side-effects, we introduce a diagnostic framework for analyzing interacting behaviors in LLMs. We model behaviors as low-rank subspaces in activation space, and study how interventions influence across behaviors. Across multiple instruction-tuned models (7B-70B) and across refusal, jailbreak, and sycophancy settings, we find that different behaviors share internal representations, and intervening on one behavior alters others in asymmetric ways. Some behaviors act as upstream control points whose interventions propagate broadly across other behaviors, while others remain more isolated. We relate these effects to two geometric quantities: (i) the overlap between behavior subspaces, measured as the average squared cosine of principal angles, and (ii) the angle between each behavior subspace and the decision subspace (capturing the model's final decision e.g., refuse vs. comply). Empirically, intervention effects on other behaviors tend to be larger for behavior pairs with higher subspace overlap, and for source behaviors whose subspaces lie closer (smaller angle) to the decision subspace. These findings highlight a challenge for targeted behavior control: behaviors are difficult to modify independently, as interventions can propagate through shared representations and asymmetric interactions.

---


### 53. [When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More](https://arxiv.org/abs/2606.14476)

**<font color=#1a73e8>作者：</font>** Zhongyuan Wang, Pratyusha Vemuri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A growing line of work equips large language model (LLM) agents with graph neural networks (GNNs) as callable tools, assuming the agent exercises judgment over when and how much to rely on such a tool. We test this directly. We expose a frozen GNN to a ReAct-style LLM agent as an explicit tool and measure, on node classification over a text-attributed graph (ogbn-arxiv, replicated on WikiCS), whether the agent uses the tool or merely obeys it. We find the agent does not exercise judgment: its predictions agree with the raw GNN's 97.6-99.2% of the time (5 seeds), collapsing into a GNN parrot that adopts the tool's output wholesale and bypasses its own reasoning. Sweeping backbone capability (Qwen2.5 0.5B-7B), the deference is not a weak-model artifact: among models able to invoke the tool, agreement rises with capability (0.60 to 0.98 from 1.5B to 7B). Crucially, the cost of deference does not shrink as capability grows and grows where alternatives emerge: a per-node oracle over the available actions beats the parrot by 0.09-0.18 at 3B and 0.12-0.22 at 7B, roughly doubling at high homophily, because the parrot is pinned to the frozen GNN while the agent's alternatives improve; at 7B a simple neighbour-label tool overtakes the GNN at high homophily (0.81 vs 0.71) yet the agent still defers. A simple selective-invocation gate recovers about half of that high-homophily gap (0.71 to 0.83) but yields no net global gain, and held-out estimates bound the best achievable gate over standard test-time features to at most a third of the oracle headroom: reliable selective invocation looks limited by available information, not merely router design. Our results are a cautionary measurement: evaluations of agent+tool systems cannot assume the agent adds judgment on top of the tool, and selective invocation must be designed in rather than expected to emerge from scale.

---


### 54. [From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI](https://arxiv.org/abs/2606.14502)

**<font color=#1a73e8>作者：</font>** Yongheng Zhang, Ziang Liu, Jiaxuan Zhu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are undergoing a fundamental transformation from conversational generators into integrated AI systems capable of reasoning, action, memory, and self-improvement. We conceptualize this transition as a shift from Chatbot to Digital Colleague: from conversational answers to persistent work. We organize this transition along two tightly coupled dimensions. First, at the cognitive core level, LLMs are advancing from Chatbot-era "fast thinking" systems driven by next-token prediction toward Thinking LLMs that leverage inference-time computation, Chain-of-Thought reasoning, reflection, process supervision, and reinforcement learning to support more deliberate and reliable cognition. Second, at the tool-augmented task execution level, LLMs are progressing from tool-calling Agents that invoke external resources in an ad hoc manner toward OpenClaw-style workstation systems (OpenClaw) equipped with persistent Workspaces, skills, verification loops, and governance. The "Workspace + Skill" paradigm makes episodic tool use colleague-like via state persistence, reusable procedures, task closure, and experience reuse. We examine data construction shifts from instruction-response pairs to State-Action-Observation trajectories and evaluation from static benchmarks to sandboxed, auditable, self-evolving AI ecosystems.

---


### 55. [Dense Coordinate-List Fine-Tuning Induces a Controllable Interference Surface in Vision-Language Models](https://arxiv.org/abs/2606.14507)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Boguang Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning vision-language models to emit dense coordinate lists improves visual grounding but also changes how models serialize, repeat, and terminate structured outputs. We study this behavior as a generation and control surface. In Gemma 4 12B, high-capacity q/k/v/o LoRA raises class-aware F1@0.3 from 0.007 to 0.448 while inducing repeated-tail pressure (duplicate rate 0.080, max repeat 23). A q/v rank sweep keeps max repeat at 21-22 across ranks 4-64, showing capacity persistence. The target signal is separable: object-level repeat-stop removes exact repeated records (duplicate rate 0.000, max repeat 1) while preserving F1 (0.494 to 0.490) and stricter F1@0.5 (0.381 to 0.385). Structure-axis probes localize the effect to bbox-coordinate object lists; dense non-bbox and spatial/count JSON remain repeat-clean, including under high-capacity adapters. Qwen3-VL-8B reproduces a clean controlled endpoint (F1@0.3 0.318, duplicate rate 0.000), and COCO 2017 reproduces acquisition plus duplicate pressure. Dense coordinate-list adaptation therefore creates a structure-bound, cross-family interference surface that can be measured and controlled.

---


### 56. [BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM](https://arxiv.org/abs/2606.14528)

**<font color=#1a73e8>作者：</font>** Qingkai Fang, Shoutao Guo, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time, full-duplex speech interaction is a key feature of next-generation spoken chatbots, allowing the model to listen and speak at the same time and to handle natural phenomena such as overlap, hesitation, and barge-in. Existing speech language models (SpeechLMs) such as LLaMA-Omni and GLM-4-Voice are still turn-based and rely on an external Voice Activity Detection (VAD) module to mark the end of the user's turn, which fundamentally limits their interactive ability. In this paper, we introduce BayLing-Duplex, a native full-duplex SpeechLM where a single autoregressive LLM decides when to listen, when to speak, and when to stop, with no auxiliary turn-taking module. The design adds only a few special tokens to the standard vocabulary, so it transfers across LLMs and reuses existing training and serving stacks with no architectural adaptation. Starting from the public GLM-4-Voice checkpoint and using only 400K full-duplex samples for fine-tuning followed by a lightweight DPO stage, BayLing-Duplex reaches 92% turn-taking success and 100% interruption success on InstructS2S-Eval, while improving the speech-response score from 2.17 to 3.39 over Moshi. BayLing-Duplex also matches or surpasses its turn-based counterpart on Llama Questions, Web Questions, and Alpaca-Eval, showing that simultaneous listen-and-speak modeling does not sacrifice response quality.

---


### 57. [Code Correctness Signals in LLM Hidden States: Pre-Generation Probing and Repair Geometry](https://arxiv.org/abs/2606.14530)

**<font color=#1a73e8>作者：</font>** Carlo Di Cicco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models encode rich information in their hidden states. This work asks whether code correctness is legible in the hidden states of Qwen3-4B-Instruct-2507, before it generates and as it repairs a failed attempt, studied on 444 LiveCodeBench tasks. It reports two findings connected by a single confound-control tool: residualization. First, the correctness of the model's first-attempt code is linearly decodable from the prompt-final hidden state, with a leakage-free held-out AUC of 0.931 +/- 0.008 across 50 outer splits. After the linear effect of prompt length is removed from each hidden state dimension, the probe still reaches 0.911 +/- 0.010, well above a prompt-length baseline of 0.754 +/- 0.014. Second, on 236 cleaned cases where the model attempts to repair a failed first attempt, the hidden state shift from the failing attempt to its repair carries a statistically detectable contrastive direction, significant on both a magnitude and a split-half test against label-shuffled nulls. This direction does not survive a conditional residualization against repair-context covariates that differ between successful and failed repairs, marking it as a correlate of repair success driven by the repair context rather than an isolated repair-comprehension feature. The probe layer is selected by nested cross-validation, and the same residualization approach that upholds the pre-generation correctness result overturns the repair-direction interpretation. The contribution is as much methodological as empirical: a diagnostic honest enough to report a negative result alongside a positive one.

---


### 58. [Rethinking Global Average Pooling: Your Classifier Is Secretly a Multi-Instance Learner](https://arxiv.org/abs/2606.14555)

**<font color=#1a73e8>作者：</font>** Aray Karjauv  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image classifiers widely adopt global average pooling (GAP) followed by a linear classification head. This linearity ensures that the image-level logits equal the average of logits obtained by applying the classification head pointwise to the feature grid prior to GAP. Consequently, standard classifiers may inherently retain spatial class evidence that remains recoverable even when the image-level prediction is incorrect. This structure naturally suggests a multiple-instance learning (MIL) interpretation, where an image is viewed as a bag of spatial instances. Within this formulation, we demonstrate that standard classifiers trained with a single label per image can still learn the intended classification task in multi-object scenes. We further exploit this property to decompose image-level logits into a prediction grid, providing a post-hoc diagnostic to extract spatial class evidence that GAP otherwise obscures. Our systematic evaluation reveals that off-the-shelf models consistently recover the ground-truth class within foreground regions. The MIL interpretation further suggests that common classifier failures reflect known limitations of mean aggregation.

---


### 59. [NEST3D: A High-Resolution Multimodal Dataset of Sociable Weaver Tree Nests](https://arxiv.org/abs/2606.14562)

**<font color=#1a73e8>作者：</font>** Constanza A. Molina Catricheo, Simon Boeder, Ting-Jia Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sociable weaver nests function as complex ecological structures offering thermoregulatory microhabitats and sustaining diverse species; however, datasets used in prior studies lack fine-grained 3D structural detail. Producing usable and accurate 3D weaver nest data is challenging due to their irregular geometry and integration with complex host vegetation. We bridge this gap with an open-access, 1.4 TB multimodal drone dataset of 104 nest-bearing trees, comprising 27,945 RGB images, 111,780 multispectral images, approximately 781 million 3D points, and expert-annotated semantic segmentation labels. We benchmark semantic segmentation using KPConv, RandLA-Net, and Point Transformer V3, with PT-v3 achieving an mIoU of 86.35% on the test set. While the results demonstrate strong performance for transformer-based and point-wise methods, they also highlight architecture-dependent challenges, particularly for convolution-based approaches such as KPConv. By uniquely combining spectral, spatial, and structural information, the presented dataset advances 3D reconstruction, segmentation, and classification algorithms, enabling ecological applications from nest volume estimation to species conservation, and serves as a demanding benchmark that exposes architecture-dependent performance under extreme class imbalance.

---


### 60. [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](https://arxiv.org/abs/2606.14574)

**<font color=#1a73e8>作者：</font>** Xiaoxin Lu, Ranran Haoran Zhang, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments. While existing benchmarks evaluate whether LLM-generated plans execute successfully, they overlook a critical type of failure: latent failures. Unlike immediate failures that trigger instant feedback at execution time and enable timely correction, latent failures do not immediately halt plan execution but silently compromise goal achievement. In severe cases, they cause irreversible harm. To address this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM planning through a human-curated symbolic world model grounded in the kitchen domain. SIMMER defines a world model comprising 77 actions, 262 unique objects, and approximately 46,800 possible interactions that are semantically realistic, derived from real-world cooking scripts. It then leverages a state machine executor that validates plans against the world model and detects immediate precondition violations, latent hazards, and irreversible failures. Experiments across six LLMs show that even frontier models achieve at most 17% error-free plans. Moreover, up to 56% of plans contain latent failures, the majority of which lead to irreversible consequences. We further demonstrate that explicit state reasoning via counterfactual foresight simulation can reduce latent failures by up to 72% and irreversible cases by up to 75%, suggesting a promising direction for more robust LLM planners.

---


### 61. [CARE: Controlling LLM-Generated Policies through Auditable Review of Evidence in Scientific Experimentation](https://arxiv.org/abs/2606.14581)

**<font color=#1a73e8>作者：</font>** Guanyu Liu, Weiyi Kong, Zeyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Granting LLMs direct control over costly, irreversible scientific experiments leads to unsafe exploration and unstable performance, but discarding LLM creativity entirely sacrifices significant optimization potential. We introduce CARE (Controlling LLM-Generated Policies through Auditable Review of Evidence in Scientific Experimentation), an auditable controller for high-throughput experimentation (HTE) optimization that keeps a non-LLM incumbent optimizer as the default action path while using LLMs to revise challenger ranking policies. Before each outcome is revealed, a public-evidence intervention gate compares the challenger with the incumbent. It authorizes the challenger's selection only when the evidence available before selection supports the change, with the decision recorded in the audit log. CARE outperforms all other evaluated methods on Minerva/Olympus and ChemLex benchmarks, with final-best improving from 80.0 to 88.5 on Minerva/Olympus and from 83.9 to 92.1 on ChemLex, relative to the public incumbent. Our experiments indicate that LLM self-evolution is more reliable when it expands the proposal space under an auditable controller, rather than directly choosing experiments.

---


### 62. [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/abs/2606.14672)

**<font color=#1a73e8>作者：</font>** Shikun Liu, Mufei Li, Dongqi Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as execution engines for agentic systems, yet they still consume context through a sequential text interface. This creates a mismatch with modern structured agent workflows, in which independent branches explore subtasks, retrieve evidence, or generate candidate solutions before a final synthesis step. Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. In this work, we introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents. Parallel-Synthesis combines a cache mapper that calibrates independently generated branch caches with a fine-tuned synthesizer adapter that enables generation from this non-sequential cache interface. We train Parallel-Synthesis using data that exposes the synthesizer to parallel cache contexts, teaches aggregation across cached branches, and distills reasoning behavior from standard text-concatenation-based synthesis. Across nine downstream datasets spanning math, science QA, code generation, GAIA, and multi-agent database diagnosis, Parallel-Synthesis matches or outperforms text-based synthesis on seven datasets and remains close on the other two. It also reduces time-to-first-token by 2.5x-11x, suggesting that direct cache-based synthesis is a promising interface for more native and efficient synthesis over parallel agent branches.

---


### 63. [CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment](https://arxiv.org/abs/2606.14691)

**<font color=#1a73e8>作者：</font>** Jiayue Cao, Zhicong Lu, Xuehan Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has successfully elicited the reasoning capabilities of large language models, motivating its extension to multimodal scenarios. Existing methods primarily focus on improving the visual coverage of reasoning traces and mitigating visual hallucinations, but underestimate the semantic inconsistency between the reasoning process and the final answer. In this paper, we delve into thinking-answer inconsistency in RLVR for large vision-language models (LVLMs), showing thorough analyses of rollouts collected throughout Group Relative Policy Optimization (GRPO) training process and post-RLVR evaluation outputs that this issue persists during training and remains present during inference. Motivated by the analysis, we propose Consistency-Oriented Reasoning Alignment (CORA), which introduces thinking-answer semantic consistency into RLVR through a lightweight plug-and-play consistency reward model, and further incorporates Hybrid Reward Advantage Splitting (HRAS) to stably coordinate task and consistency optimization. Extensive experiments across representative multimodal reasoning benchmarks and mainstream LVLMs show that CORA improves task performance while effectively mitigating thinking-answer inconsistency, leading to more faithful reasoning traces.

---


### 64. [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697)

**<font color=#1a73e8>作者：</font>** Sicheng Yang, Hangjie Yuan, Wenjun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building trustworthy medical multimodal large language models (MLLMs) is critical for reliable clinical decision support. Existing medical hallucination benchmarks mainly focus on data collection, but often ignore where hallucinations originate within the reasoning process. We find that hallucination sources vary across samples: errors may arise from visual misrecognition, incorrect medical knowledge recall, or flawed reasoning integration. To enable source-level hallucination diagnosis, we introduce ClinHallu, a benchmark for stage-wise hallucination diagnosis in medical MLLM reasoning. ClinHallu contains 7,031 validated instances, where each instance is augmented with a structured reasoning trace decomposed into Visual Recognition, Knowledge Recall, and Reasoning Integration. We also use stage-replacement interventions to measure how correcting specific stages affects the final answer. Beyond evaluation, we show that trace-supervised fine-tuning reduces stage-wise hallucinations. ClinHallu provides a fine-grained hallucination testbed for diagnosing and mitigating reasoning failures in medical MLLMs. The benchmark is publicly available at this https URL.

---


### 65. [RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space](https://arxiv.org/abs/2606.14700)

**<font color=#1a73e8>作者：</font>** Xichen Pan, Aashu Singh, Satya Narayan Shukla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used in text-to-image (T2I) systems, but they are typically limited to text encoding, while denoising is handled by newly trained generative backbones. The emergence of representation autoencoders (RAEs) shifts the generation target toward semantically structured visual representations, creating a latent space that is more compatible with pretrained LLM priors. Inspired by multimodal LLMs (MLLMs), where an MLP projector is sufficient to align clean visual representations with a pretrained LLM, we repurpose the MLLM itself as a noisy representation encoder, extending this mechanism from clean to noisy inputs. We present RepFusion, which uses the resulting MLLM outputs as the conditioning signal for a diffusion transformer. In controlled comparisons at similar inference budgets, RepFusion outperforms baselines that devote comparable capacity to newly initialized denoisers. These results demonstrate that MLLMs provide strong priors for denoising visual representations and that, by conditioning on evolving noisy representations, test-time compute can be productively spent on repeated MLLM conditioning in modern T2I systems.

---


### 66. [OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains](https://arxiv.org/abs/2606.14702)

**<font color=#1a73e8>作者：</font>** Xinyue Cai, Chaoyou Fu, Yi-Fan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current automated pipelines for audio-visual Question Answering (QA) generally adopt a ``video-caption-QA'' paradigm. However, these methods typically segment videos into short clips and generate separate descriptions for audio and visual modalities. This decoupled processing severs inherent associations between sounds and their visual sources, while independent clip processing often causes inconsistent descriptions of the same entity across segments. Furthermore, coupling long-text comprehension and QA synthesis into a single step often restricts models to localized events, yielding questions lacking long-term temporal connections and deep cross-modal reasoning. To address these issues, we propose an automated data engine featuring two mechanisms: (1) \textbf{Entity-Anchored Video Scripting} transforms videos into structured scripts, comprising summaries, main entity lists, and segment-wise audio-visual descriptions. The entity list serves as a global prior to ensure cross-segment referential consistency and reconstruct audio-visual associations. (2) \textbf{Clue-Guided QA Generation} prompts models to first mine cross-segment, multimodal clues from the script, and subsequently generate QA pairs based on these high-value clues. Leveraging this pipeline, we construct the instruction-tuning dataset \textbf{OmniVideo-100K} and a human-verified test set, \textbf{OmniVideo-Test}. Fine-tuning VITA-1.5, Qwen2.5-Omni-7B and Qwen3-Omni-30B on OmniVideo-100K yields performance gains of up to 20.59% on OmniVideo-Test, demonstrating strong generalization (up to 12.64% improvements) across established benchmarks like Daily-Omni and JointAVBench.

---


> [!TIP]
> 当前位于：**51-66**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-66**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
