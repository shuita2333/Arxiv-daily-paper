# 🧠 大模型相关研究 | 2026年07月06日

> 本类共 **136** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-136](./part-03.md)

---

### 51. [The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond](https://arxiv.org/abs/2607.01753)

**<font color=#1a73e8>作者：</font>** Hanyue Jia, Wei Zhou, Wenbo Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D plant phenotyping is notoriously known to be procedure-complicated and of low throughput due to the extensive multi-view imaging, the fragile 3D reconstruction pipeline, and the additional cost from reconstructed geometry to phenotypic extraction. These limitations are further amplified in low-cost data acquisition, where smartphone videos or sparsely sampled multi-view images provide limited view overlap and self-occlusion. In this work, we show that the conventional 3D plant phenotyping pipeline could be streamlined and significantly accelerated with 3D Foundation Models (3DFMs), and particularly, present one of the first cross-crop 3D phenotyping frameworks powered by 3DFMs. The framework replaces COLMAP-style sparse initialization with 3DFM-based feed-forward geometric recovery, combines geometry-constrained 3D Gaussian Splatting for dense reconstruction, enables few-view reconstruction through iterative view synthesis and refinement, and converts reconstructed geometry into measurable organs through 2D-to-3D semantic transfer, metric scale recovery, and organ instance separation. We further construct a cross-crop dataset with smartphone-based image acquisition, diverse plant morphologies, and manual annotations for segmentation and phenotypic evaluation. Experiments across 26 plant sequences show that 3D Foundation Models reduce the average reconstruction time from 6.52 minutes to 1.58 seconds while maintaining high reconstruction quality and phenotyping accuracy. These results suggest a fresh technical route for high-throughput 3D plant phenotyping, from low-cost image acquisition to fast reconstruction, perception, scale recovery, and phenotypic measurement.

---


### 52. [Denser $\neq$ Better: Limits of On-Policy Self-Distillation for Continual Post-Training](https://arxiv.org/abs/2607.01763)

**<font color=#1a73e8>作者：</font>** Meng Wang, Haohan Zhao, Wenzhuo Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual post-training enables foundation models to acquire new knowledge while preserving existing capabilities. Recent work suggests that on-policy learning can mitigate forgetting, with on-policy self-distillation emerging as a particularly attractive approach. In this work, we revisit this optimistic view through self-distillation policy optimization (SDPO). Our experiments show that SDPO can accelerate in-domain specialization when teacher signals are stable and well aligned, but it struggles to generalize to out-of-distribution scenarios. In continual post-training, SDPO exhibits stronger forgetting and can even collapse, whereas on-policy reinforcement learning methods such as GRPO adapt more conservatively and better preserve prior capabilities. Further analyses reveal that denser self-distillation induces larger drift in both parameter space and response space, and can amplify high-frequency formatting artifacts through a self-reinforcing teacher--student loop. These findings suggest that on-policy data alone is insufficient for continual learning. Dense self-distillation can accelerate specialization when teacher targets are stable and token-level supervision is reliable, but it should not be treated as a default stabilizer for continual post-training. Our code is available at this https URL.

---


### 53. [Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction](https://arxiv.org/abs/2607.01764)

**<font color=#1a73e8>作者：</font>** Mingzhe Du, Luu Anh Tuan, Tianyi Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repository-level vulnerability reproduction is a demanding software engineering (SE) task: an agent must inspect a codebase, infer the input grammar that reaches a vulnerable path, construct a proof-of-conceptv(PoC), and verify that the crash disappears on the patched build. Recent LLM agents can often execute these steps when the approach is correct, yet they still fail by choosing the wrong strategy. This paper argues that strategy, rather than the full action trajectory, is the right learning unit for such SE agents: it is compact enough to optimize, concrete enough to guide execution, and stable enough to store and reuse across attempts. We present Mastermind, a dual-loop framework that separates transferable strategy learning from task-specific experience. A trainable planner learns reusable vulnerability-reproduction strategies through SFT and milestone-based GRPO, while an experience loop maintains task-local strategy records that guide subsequent attempts. The planner is trained independently of the executor, allowing strategy learning to improve multiple frozen executors without modifying their action-generation capability. We evaluate Mastermind on CyberGym using 260 training tasks and 200 held-out evaluation tasks. With GPT-5.5 as the frozen executor, Mastermind achieves an 84.5% pass rate, outperforming open-book PoC context (60.0%), Best-of-8 sampling (63.0%), and iterative improvement (77.0%). The same planner also improves GPT-5.4 mini and GLM~5.1 from 45.0% and 58.5% to 60.0% and 71.0%. These results demonstrate that learning high-level strategies is an effective and transferable mechanism for improving repository-scale SE agents.

---


### 54. [LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design](https://arxiv.org/abs/2607.01772)

**<font color=#1a73e8>作者：</font>** Wen Wang, Yaping Sun, Yejun He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-radar fusion is central to robust autonomous driving, combining dense visual semantics with precise range and velocity measurements from radar. However, real-world fusion quality is fundamentally challenged by dynamically varying input quality, stemming from occlusion, adverse weather, and channel noise. To address this, we re-frame the problem from static data fusion to channel-aware semantic reasoning and propose a Large Language Model-centric Semantic-layer Channel-aware Integrated Perception (LM-SCIP) framework. It places a Large Language Model (LLM) as a central reasoning core to fuse a local visual stream with a quality-varying external radar stream used to cover perception-blind spots. Concretely, LM-SCIP couples a hierarchical radar-vision encoder with a Channel-Adaptive Semantic Module (CASM) that maps link indicators into a "Channel Prompt" to dynamically gate external radar features. A parameter-efficient, LoRA-tuned LLM, in conjunction with a heterogeneous Mixture-of-Experts (H-MoE), then arbitrates between local visual cues and the channel-conditioned radar context. Finally, a decoupled multi-task decoder outputs localization, trajectory forecasting, and image reconstruction. Experiments on nuScenes and VIRAT validate our approach. On nuScenes, under a controlled toggle of radar input, LM-SCIP reduces localization RMSE by 40.0% versus a vision-only baseline. On VIRAT, the model attains a 0.214m localization RMSE and 0.179m minFDE (k=1). These results reveal that the proposed LM-SCIP enables a robust vision-dominant fallback at low SNR and synergistic fusion at high SNR.

---


### 55. [Subliminal Clocks: Latent Time Modelling in Diffusion Language Models](https://arxiv.org/abs/2607.01774)

**<font color=#1a73e8>作者：</font>** Maximo Rulli, Thomas Fontanari, Simone Petruzzi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have recently emerged as a promising alternative to autoregressive models. Unlike standard diffusion-based approaches, DLMs are not explicitly conditioned on a timestep, raising a natural question: do these models internally represent denoising progress, and how is such information used downstream? In this work, we show that DLMs do in fact encode a latent representation related to the diffusion timestep within their residual streams. We find that this signal can be reliably extracted using probes across layers, indicating that denoising progress is decodable from internal activations. We further demonstrate that steering the model along a low-dimensional subspace associated with the inferred timestep allows us to systematically modulate its notion of denoising progress, leading to predictable changes in model confidence and entropy. Finally, we analyse the geometry of the identified representation, showing that it exhibits structured and interpretable properties in activation space, and shedding light on how such a signal is processed by these models.

---


### 56. [EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning](https://arxiv.org/abs/2607.01789)

**<font color=#1a73e8>作者：</font>** Ahin Lee, Sehyun Yun, Taesik Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale efficiently but remain costly to adapt due to redundant experts and uniform parameter allocation. Existing parameter-efficient fine-tuning (PEFT) methods such as LoRA ignore MoE routing dynamics, leading to suboptimal resource use. We propose EPnG, an adaptive prune-and-grow framework that reallocates LoRA capacity based on expert importance derived from router gate probabilities. EPnG prunes under-utilized experts and expands high-importance experts via rank growth with orthogonal initialization, while maintaining a fixed parameter budget. Across OLMoE and Qwen1.5-MoE, EPnG consistently outperforms LoRA under the same budget and achieves performance comparable to full fine-tuning while updating only 0.55%-0.72% of parameters (up to 140x-180x fewer). These results demonstrate that aligning PEFT with MoE routing yields a more effective and scalable fine-tuning strategy.

---


### 57. [PARTREP: Learning What to Repeat for Decoder-only LLMs](https://arxiv.org/abs/2607.01792)

**<font color=#1a73e8>作者：</font>** Andikawati P Widjaja, Yongjun Kim, Hyounghun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While decoder-only LLMs excel at a vast array of natural language tasks, it suffers from an asymmetric information flow induced by causal attention: later tokens are richer in contextual grounding than earlier ones. A simple and effective remedy is prompt repetition -- just appending a second copy of prompt before generation can redistribute grounding across positions and improve reasoning performance. However, full repetition of the original prompt doubles the KV cache footprint and quadruples attention cost during prefill, making it impractical for long-context settings. We propose PartRep, a selective augmentation method that appends only the most informative tokens -- rather than the entire prompt. We use token-wise negative log-likelihood (NLL) as a selection signal, motivated by the hypothesis that less predictable tokens are less recoverable from surrounding context and therefore benefit more from late-position repetition. To avoid the heavy cost of a full forward pass for scoring, we train a lightweight gate that predicts high-NLL tokens from early-layer hidden states, enabling token selection during mid-prefill via early exit. Across eight benchmarks (including MMLU, GSM8K, and RULER) and three model families (Qwen2.5, Llama3.2, Gemma4), PartRep retains most of the gains of full repetition while using only 59.4\% of its KV cache and 79.0\% of its prefill FLOPs.

---


### 58. [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification](https://arxiv.org/abs/2607.01793)

**<font color=#1a73e8>作者：</font>** Yunhao Feng, Ruixiao Lin, Ming Wen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by hard-coded rules, making them costly to extend as agents evolve. To this end, we present Vera, an end-to-end automated safety testing framework that instantiates software engineering testing principles for non-deterministic agents through a three-stage, self-reinforcing pipeline. First, a literature-driven exploration continuously discovers and structures emerging risks into taxonomies of safety risks, attack methods, and tool execution environments. Second, combinatorial composition across taxonomy dimensions produces executable safety cases, each specifying a concrete safety goal, a programmatically constructed initial state, and a deterministic verification predicate grounded in observable artifacts. Third, adaptive execution runs heterogeneous agents in isolated sandboxes where a control agent steers multi-turn interaction based on runtime observations, while evidence-grounded verifiers judge outcomes from environment state and tool-call evidence rather than model self-report. We evaluate Vera on four production agent frameworks (OpenClaw, Hermes, Codex, Claude Code), revealing substantial safety weaknesses, with average attack success rates reaching 93.9\% under multi-channel attacks; we also release Vera-Bench, comprising 1600 executable safety cases spanning 124 risk categories across three execution settings. These results indicate that modular, executable testing infrastructure is essential for rigorous and maintainable safety evaluation of rapidly evolving agentic systems at scale. The code is publicly available at this https URL.

---


### 59. [Do LLMs Truly Generalize in the Molecular Domain? A Perturbation-Based Analysis](https://arxiv.org/abs/2607.01800)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Weida Wang, Changmeng Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently shown promise in molecular discovery, yet a gap remains between their probabilistic nature over discrete sequential tokens and the rigid topological constraints of chemical space. This raises the question of whether molecular LLMs can generalize beyond the local neighborhoods induced by their sequence-based representations. To systematically investigate this question, we introduce a Molecular Perturbation framework that generates syntax-valid structural variants of training molecules under controlled Graph Edit Distance (GED) to probe the manifold regularity of molecular LLMs. Our analysis shows that even a single edit can cause substantial performance drops on common molecular tasks, revealing a narrow local trust region and fragile sensitivity to structural changes. Since similar molecules tend to exhibit similar properties, In-Context Tuning (ICT), which anchors predictions on structurally similar molecules, offers a natural way to mitigate such fragility. Our experiments also examine whether ICT confers robustness under controlled structural perturbations, and the results suggest that it can partially expand the local trust region and offer a promising direction for stabilizing molecular LLMs against structural variation.

---


### 60. [MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models](https://arxiv.org/abs/2607.01813)

**<font color=#1a73e8>作者：</font>** Yuanzhi Liu, Shousheng Zhao, Bo Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation benchmarks are essential for assessing vision-language models (VLMs), but most multimodal benchmarks are static, making them vulnerable to temporal staleness, data contamination, and costly maintenance. We present MMBench-Live, a continuously evolving multimodal benchmark built by a multi-agent-driven automated pipeline. Our framework treats benchmark evolution as task-guided dataset construction, integrating structured benchmark specification, feedback-controlled real-time data acquisition, and verifiable QA generation with executable reasoning. To maintain cross-version comparability, we introduce a distribution-consistent update strategy that extracts task-related visual patterns from the original benchmark to guide data collection and filtering. Instantiated from MMBench, MMBench-Live contains 5.9K newly generated evaluation instances with a high answer correctness rate, while each update costs about USD 30 and takes 1-2 hours. Extensive evaluations show that MMBench-Live preserves stable model rankings, maintains semantic alignment with the original benchmark, and exhibits weaker contamination-related memorization signals, suggesting a practical and scalable paradigm for sustainable multimodal benchmark evolution. The project is available at this https URL.

---


### 61. [MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support](https://arxiv.org/abs/2607.01814)

**<font color=#1a73e8>作者：</font>** Lihui Luo, Joongwon Chae, Ziyan Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features and textual reasoning, as well as the lack of large-scale, standardized datasets. To address these challenges, we introduce MMIR-TCM, a novel framework that emulates the diagnostic process of TCM experts by integrating multimodal large language model(MLLM) with memory-augmented segmentation and retrieval-augmented generation (RAG). Employing a three-stage architecture, MMIR-TCM integrates a training-free Memory-SAM module for robust tongue extraction, a fine-tuned Qwen3-VL model for structured tongue diagnosis generation, and a Qwen3-based RAG component for evidence-grounded clinical decision support generation. The framework was developed and validated using MedTCM, a new large-scale multimodal dataset that we introduce specifically for advanced TCM research. To properly evaluate our framework's clinical accuracy, which existing metrics fail to capture, we also developed TDEU, a domain-specific evaluation metric incorporating semantic understanding and diagnostic importance. Our comprehensive experiments demonstrate that MMIR-TCM significantly outperforms leading models, including GPT-4o and Gemini 2.5 Flash.

---


### 62. [Pre-Flight: A Benchmark for Evaluating Large Language Models on Aviation Operational Knowledge](https://arxiv.org/abs/2607.01829)

**<font color=#1a73e8>作者：</font>** Alex Brooker, Tim Hughes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly proposed for aviation business operations, from documentation and training generation to customer facing assistants. General purpose benchmarks do not measure whether a model reasons safely and correctly about aviation specific operational knowledge, and the high stakes, regulated nature of the domain makes that gap consequential. We present Pre-Flight, an open source benchmark of 300 multiple choice questions drawn from international standards and airport ground operations material, covering international airport ground operations, ICAO and US FAA regulations, aviation general knowledge and complex operational scenarios. Questions were authored and reviewed by practitioners with experience in air traffic management, ground operations and commercial flying. We evaluate a range of contemporary commercial and open weight models using the Inspect evaluation framework, scoring by accuracy under a standard multiple choice protocol, and we maintain the leaderboard on a rolling basis as new models are released. Against an informal expert reference of around 95%, obtained from a low sample quiz of aviation professionals at a conference, even the strongest model evaluated (released in 2026) reaches 82.7%, having improved only gradually from roughly 75% in early 2025. A substantial and persistent gap below expert level reliability therefore remains. We release the dataset, the evaluation harness and the results, and the benchmark is available within the community evaluations package distributed with inspect_evals. We argue that domain specific evaluation of this kind is a necessary precondition for responsible deployment of generative AI in non safety critical aviation operations.

---


### 63. [Many Voices, One Reward: Multi-Role Rubric Generation for LLM Judging and Reward Modeling](https://arxiv.org/abs/2607.01830)

**<font color=#1a73e8>作者：</font>** Dazhi Fu, Jiuding Yang, Yiwen Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable reward and preference signals are critical for evaluating and optimizing large language models on open-ended tasks. Rubric-based judges offer a transparent way to decompose such judgments into explicit evaluation criteria, but existing annotation-free rubric generators typically rely on a single generic evaluator. As a result, they may overlook important dimensions of human preference, a failure mode we term dimensional blind spots. To address this limitation, we propose Multi-Role Rubric Generation (MRRG), a training-free and reference-free framework that elicits evaluation criteria from multiple complementary roles and consolidates them into an auditable rubric-based scorer. This scorer can be used both to validate pairwise preferences and to provide rewards for GRPO-style Reinforcement Learning with Verifiable Rewards (RLVR). Experiments on preference validation benchmarks show that MRRG consistently outperforms single-role rubric generation baselines across multiple backbone models. Further RLVR experiments demonstrate that MRRG yields a stronger reward signal for improving open-ended generation.

---


### 64. [CLAP: Closed-Loop Training, Evaluation, and Release Control for Domain Agent Post-training](https://arxiv.org/abs/2607.01846)

**<font color=#1a73e8>作者：</font>** Fangfei Li, Chenyang Zhao, Long Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain agents often face noisy business data, uncertain post-training gains, offline/application mismatch, and adapter-release risk. This paper presents CLAP (Closed-Loop Agent Post-training), a closed-loop method that converts business data into structured SFT samples, decision-preference samples, holdout sets, risk diagnostics, and release-gate records. CLAP combines data validation, target/evidence normalization, reward/KL diagnosis, offline gates, and application-chain replay to decide whether an adapter is suitable for the target application chain. On five anonymized manufacturing-scenario batches, QLoRA-style LoRA-SFT yields modest average gains: overall score increases by 0.0098, pass rate by 0.0240, and evidence accuracy by 0.0280, while hallucination and wrong facts decrease. Yet only 3 of 5 batches improve, some batches regress, and GRPO exposes high KL risks. Application-chain replay further shows that RAG is necessary for factual extraction; under the same 3B backbone and 100 replay cases, an application-RAG-oriented LoRA-SFT adapter improves value, core fields, and answer-evidence doc/page matching over base+RAG, but increases latency. These results support managing domain-agent post-training through an integrated data-training-evaluation-release loop rather than relying on training completion or a single offline score.

---


### 65. [Geometric Foundation Model Distillation for Efficient Lunar 3D Reconstruction](https://arxiv.org/abs/2607.01851)

**<font color=#1a73e8>作者：</font>** Clémentine Grethen, Florient Chouteau, Géraldine Morin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large 3D foundation models such as MASt3R achieve state-of-the-art stereo reconstruction but are computationally demanding for deployment under strict hardware constraints -- a critical limitation in domains such as planetary exploration, where onboard computing is severely restricted. We study how far such models can be compressed through knowledge distillation, using lunar stereo reconstruction as a challenging and practically relevant case study. Starting from a 688M-parameter MASt3R teacher fine-tuned on lunar imagery, we distill its dense geometric predictions into a family of lightweight students spanning different encoder types (CNN vs ViT), decoder widths and depths, and training strategies. To bridge the dimensional mismatch between teacher and student, we propose a structured SVD-based initialization that projects the teacher's decoder weights into the student's smaller latent space, yielding a warm start that significantly improves convergence and final performance. Based on our results on lunar data, we can obtain a distilled student that retains most of teacher's reconstruction accuracy while reducing the model size up to 7 times, and even outperforms a baseline trained directly with sparse ground-truth annotations. Beyond compression, our study highlights both principles and practical insights for distilling geometric foundation models: a convolutional encoder underperforms transformer-based alternatives (though pretraining availability remains a confounding factor), preserving encoder capacity is more critical than maintaining a large decoder, feature-level distillation consistently outperforms output-only supervision, and SVD-based initialization improves optimisation stability. These findings provide practical guidelines for deploying 3D reconstruction models in resource-constrained environments.

---


### 66. [Safety Targeted Embedding Exploit via Refinement](https://arxiv.org/abs/2607.01859)

**<font color=#1a73e8>作者：</font>** Joshua Adrian Cahyono  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety training for large language models (LLMs) is conducted predominantly in English, leaving uncertain how well safety mechanisms generalize to low-resource languages and mixed-language code-switching. We show that this creates an epistemic gap in which models confidently generate harmful responses for inputs that fall outside the distribution of their safety training. To study this phenomenon, we introduce STEER (Safety Targeted Embedding Exploit via Refinement), a gradient-guided attack that identifies words contributing most strongly to the model's refusal behavior and iteratively translates them into low-resource languages to suppress refusal while preserving harmful intent. Across six open-source 8B-parameter models, STEER achieves attack success rates of up to 93.0% on JailbreakBench and 96.7% on AdvBench, outperforming random code-switching and Greedy Coordinate Gradient (GCG). The resulting prompts also transfer to GPT-4o-mini, achieving a 35.5% attack success rate without requiring access to the target model, suggesting that the underlying weakness is not specific to a single architecture. These findings demonstrate that safety mechanisms aligned primarily on English cannot be assumed to generalize across multilingual inputs. We argue that improving multilingual safety requires broader coverage during alignment and mechanisms that explicitly detect and abstain on out-of-distribution inputs.

---


### 67. [Descriptor: LYNRED Mobility Dataset Multimodal Detection Subset (LYNRED-MDS)](https://arxiv.org/abs/2607.01871)

**<font color=#1a73e8>作者：</font>** Loïc Arbez, Jessy Matias, Xavier Brenière 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current road safety systems primarily focus on minimizing post-collision damage. However, advances in algorithmic perception are shifting focus toward early collision prediction, especially in lowvisibility conditions like nighttime or fog, where thermal infrared sensing outperforms both human vision and RGB imaging. While available RGB-infrared datasets such as FLIR ADAS and LLVIP are good benchmarks, they mostly consist of clear weather and overly simple scenarios. In this article, we introduce the LYNRED-MDS: Multimodal Detection Subset, a subset of the LYNRED Mobility Dataset, comprised of 4000 RGB-infrared image pairs captured under diverse weather, lighting, and road conditions around Grenoble, France. Our dataset spans varied driving contexts (urban, rural, mountainous, etc.) and a vehicle fleet compliant with Western European standards. Thermal cross-dataset evaluation using a YOLOv8n baseline suggests that our dataset offers strong generalization potential for pedestrian detection in driving scenarios. By covering critical edge cases, our dataset supports the development of more reliable and deployable vision systems for advanced driver-assistance systems.

---


### 68. [SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use](https://arxiv.org/abs/2607.01874)

**<font color=#1a73e8>作者：</font>** Jiayin Zhu, Kelong Mao, Yudong Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills are becoming a reusable operational layer for LLM agents, encoding SOPs, domain rules, tool workflows, scripts, and validation routines. In realistic skill repositories, overlapping skills make reliable skill-use difficult. Final verifier success is too coarse for both evaluation and training, since an agent may pass through trial and error while selecting distractor skills, skipping required steps, composing workflows incorrectly or omitting final checks. We introduce SkillCoach, a self-evolving rubric framework for evaluating and enhancing agentic skill-use. SkillCoach derives skill-grounded process rubrics from real rollouts and evaluates trajectories along four dimensions: skill selection, skill following, skill composition, and skill-grounded reflection. It keeps the external verifier as a separate outcome signal, allowing process quality to be distinguished from accidental task success. The evolved rubrics further serve as process supervision for selecting high-quality training trajectories. Experiments show that evolved rubrics substantially improve evaluation quality, expose failures hidden by final accuracy, and provide stronger supervision signals than outcome-only filtering for enhancing agentic skill-use.

---


### 69. [SAB-LVLM: Significance-Aware Binarization for Large Vision-Language Models](https://arxiv.org/abs/2607.01876)

**<font color=#1a73e8>作者：</font>** Qi Lyu, Jiahua Dong, Baichen Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable progress in multimodal understanding, yet their enormous parameter scale and cross-modal computation incur substantial memory and latency overhead, severely limiting real-world deployment on resource-constrained devices. Binarization offers an attractive solution by drastically reducing storage and computational costs. However, existing binarization methods neglect the varying importance of weights across different layers and modalities. This causes parameters irrelevant to downstream tasks to be unnecessarily retained, whereas modality-critical weights may not be adequately optimized, resulting in significant performance degradation. To address these challenges, we develop a novel \underline{S}ignificance-\underline{A}ware \underline{B}inarization for \underline{L}arge \underline{V}ision-\underline{L}anguage \underline{M}odels (SAB-LVLM). Specifically, after constructing Hessian matrices for textual and visual inputs, we propose a spatial significance map to distinguish full-precision weights activated under a single modality from those activated across modalities. We then devise a modality-guided integration strategy to obtain the significance-aware binarization map, which measures weight significance across layers and modalities. Subsequently, this binarization map is incorporated into the binarization objective as an error reweighting term, and binarization fitting is performed through an alternating significance-weighted update scheme. Extensive experiments illustrate the superiority of our SAB-LVLM over existing binary PTQ methods under an approximately 1-bit compression constraint. Our code is accessible at this https URL.

---


### 70. [PairCoder++: Pair Programming as a Universal Paradigm for Verified Code-Driven Multimodal and Structured-Artifact Generation](https://arxiv.org/abs/2607.01883)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Xiang Li, Mingjin Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code is the medium through which large language models generate structured artifacts: charts, scientific figures, vector graphics, CAD models, 3D scenes, and hardware designs are all produced by writing programs. In this regime single pass inference is brittle, because the compiler, renderer, or simulator that decides whether the artifact exists is invisible to the model. We present PairCoder, which grounds review in the toolchain and realizes it as two agent pair programming: a Driver agent writes the program, a Navigator agent reviews it against verification evidence (diagnostics, execution results, and renderings of the current artifact beside the target), and the two switch roles when errors persist. Across 17 public benchmarks and seven models from three vendors, PairCoder improves essentially every benchmark whose artifact is verifiable, on full official metric suites rather than execution alone (for example, Blender scene executability 0.20 to 0.78; TikZ compile rate up 10 to 30 points on every model), at 2.9 to 9.2 times single model cost (about 7 times overall). The improvements concentrate where the toolchain provides an informative oracle and the baseline leaves headroom, and the method ties or mildly regresses where the oracle is weak; we frame pair programming as a reliable recipe for verified code driven generation.

---


### 71. [SABER: A Semantic-Aligned Brain Network Analysis Framework via Multi-scale Hypergraphs](https://arxiv.org/abs/2607.01901)

**<font color=#1a73e8>作者：</font>** Yidan Xu, Xiangmin Han, Rundong Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective brain disease diagnosis requires the synergy of brain connectivity patterns and high-level semantic knowledge. Existing methods, however, largely treat semantics from large language models (LLMs) as auxiliary features or supervision, limiting their direct role in decision-making and constraining classification stability and robustness. To overcome this, we propose a semantic-aligned brain network framework that actively integrates LLM-derived semantics into the prediction process. Specifically, ROI-level semantics are first incorporated via global self-attention to enrich node representations and provide whole-brain context. Multi-scale hypergraphs are then constructed to explicitly model functional subnetworks and multi-ROI interactions, addressing the locality limitations of traditional GNNs and capturing high-order dependencies. Finally, a decision-level semantic alignment mechanism selectively injects patient-specific textual embeddings into graph representations, enabling semantics to directly guide predictions without perturbing the underlying network structure. Experiments on public brain network datasets ABIDE and ADHD-200 demonstrate state-of-the-art performance, enhanced stability, and improved interpretability, particularly in small-sample settings.

---


### 72. [Rethinking Complexity Metrics for LLM-Integrated Applications: Beyond Source Code](https://arxiv.org/abs/2607.01903)

**<font color=#1a73e8>作者：</font>** Zihao Xu, Yuekang Li, Gelei Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-integrated applications blend natural language prompts with program code, and much of their runtime behavior originates in the prompt layer rather than in the code itself. Existing complexity metrics, however, operate solely at the code level and therefore overlook this behavioral logic entirely. We present HECATE, the first tool designed to assess complexity in both the prompt and code layers of such applications. Central to HECATE is Prompt-as-Specification, a Hoare-logic-inspired formalism that interprets every prompt as a specification of intended behavior. Grounded in 25 complexity dimensions identified across published taxonomies, the tool generates 52 candidate metrics. We assess each metric against 118 components collected from 18 open-source repositories, relying on maintenance activity derived from version history as an empirical proxy for complexity, and discard any metric that loses significance once code size is accounted for. Only ten metrics withstand this test. Seven belong to our newly introduced set; rather than measuring sheer volume, each tallies structurally distinct elements, such as LLM call sites, memory attributes, and prompt templates, an attribute we call structural breadth. Of the three surviving conventional metrics, RFC exhibits a similar breadth-oriented character, while Halstead N and V survive only as a residual effect of size; our top-performing metrics exceed all three. Crucially, the prompt-layer metrics retain significance even when the strongest code-level metric is added as a covariate, establishing prompt complexity as a dimension in its own right. A final validation on 20 components spanning six held-out repositories shows that the two best-performing metrics continue to predict maintenance effort, supporting their generalizability beyond the training set.

---


### 73. [Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports](https://arxiv.org/abs/2607.01908)

**<font color=#1a73e8>作者：</font>** Bingcong Yan, Chunlei Li, Jingliang Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have achieved strong performance across many medical imaging tasks, yet their application to ultrasound remains limited due to its inherent complexity and variability. In this work, we revisit what is truly needed to enable real-world ultrasound understanding. Instead of introducing complex architectures or elaborate training strategies, we show that data scale and clinically faithful data alignment are the key factors. We construct a large-scale dataset of 1.5M real-world ultrasound examinations, containing 17.7M images, multi-organ coverage, and paired uncurated clinical reports. Crucially, we organize the data at the examination level, aligning multiple images with their corresponding reports to reflect real clinical workflows. We then fine-tune a standard LVLM using low-rank adaptation (LoRA) on this dataset without task-specific modifications. Surprisingly, this simple recipe already leads to strong performance across diverse ultrasound understanding tasks, outperforming prior methods designed with more complex pipelines. Beyond these results, we present model and data scaling analyses that provide insights into the role of scale in ultrasound LVLMs.

---


### 74. [Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis](https://arxiv.org/abs/2607.01918)

**<font color=#1a73e8>作者：</font>** Yisong Fu, Zezhi Shao, Chengqing Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Zeus, a unified tuning-free Time Series Foundation Model (TSFM) that delivers superior performance across diverse analysis tasks without any task-specific fine-tuning. Unlike prior studies that primarily focus on zero-shot forecasting but require task-specific tuning for other tasks, Zeus bridges this gap by addressing two fundamental challenges in multi-task generalization. First, to reconcile point-level granularity with long-sequence scalability, Zeus incorporates a multi-scale Transformer featuring point-wise tokenization and a U-shaped hierarchy, effectively balancing fine-grained fidelity with computational efficiency. Second, to accommodate varying inductive biases across different tasks, Zeus introduces Multi-Objective Temporal Masking (MOTM), a unified strategy that supports heterogeneous tasks (e.g., extrapolation, interpolation, and global abstraction) within a single framework. Extensive experiments across five representative tasks demonstrate that Zeus consistently achieves competitive results in tuning-free settings, underscoring its potential as a general-purpose TSFM.

---


### 75. [ElephantAgent: Contextual State Continuity in Agentic Systems](https://arxiv.org/abs/2607.01919)

**<font color=#1a73e8>作者：</font>** Jiankai Jin, Xiangzheng Zhang, Zhao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory. However, these external dependencies introduce novel attack surfaces. Recent tool and memory poisoning attacks show that maliciously crafted tool descriptors and poisoned memory can covertly bias agent behavior. These threats reflect a deeper issue: the lack of verifiable continuity in the agent's contextual state for planning and execution. We present ElephantAgent, a protocol that enforces Contextual State Continuity to defend against contextual state poisoning. Inspired by prior state-continuity mechanisms (e.g., Nimble), ElephantAgent extends this protection to the evolving contextual state of agentic systems. We define the contextual state as the bounded, security-critical subset of the agent's entire context (e.g., tool state and memory). Before processing each query, ElephantAgent recomputes the digest of the local contextual state and verifies it against the latest authorized digest. Using replicated trusted hardware, ElephantAgent maintains a linearizable ledger of authorized contextual state transitions and detects out-of-band state tampering. To handle in-band semantic abuse, ElephantAgent additionally provides Historical Traceability, enabling conditional post-hoc audit and recovery to a known-good prior state.

---


### 76. [TUDUM: A Turkish-Thinking Reasoning Pipeline for Qwen3.5-27B](https://arxiv.org/abs/2607.01927)

**<font color=#1a73e8>作者：</font>** Baran Bingol, Bahaeddin Turkoglu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents TUDUM (Türkçe Düşünen Üretken Model), a project pipeline for adapting a Qwen-family 27B thinking model toward Turkish reasoning. The central problem is not only to answer Turkish prompts in Turkish, but to make the explicit reasoning trace itself Turkish. A thinking model may translate a Turkish prompt into an English-centered internal or visible scratchpad, solve the problem mostly in English, and only localize the final answer. TUDUM instead treats the generated <think>...</think> block as a trainable behavior. The pipeline starts from the project base checkpoint unsloth/Qwen3.5-27B, applies supervised fine-tuning (SFT) on 15,991 Turkish reasoning examples using LoRA adapters, and then applies GRPO-family reinforcement learning on a proxy-filtered Turkish mathematics environment. The results are mixed. SFT made the model shorter and more consistently Turkish in its reasoning behavior, with large reductions in average response length and thinking exhaustion, but reduced benchmark accuracy. RL recovered some mathematical performance, especially AIME24 at the best early checkpoint, yet did not uniformly improve all benchmarks and did not exceed the base model on the reported Macro-6 average. The contribution is therefore best framed as a technically honest Turkish-thinking reasoning pipeline and evaluation, not as a claim of state-of-the-art Turkish reasoning. The released step-50 model is publicly available.

---


### 77. [CausalSteward: An Agentic Divide-Conquer-Combine Copilot for Causal Discovery](https://arxiv.org/abs/2607.01936)

**<font color=#1a73e8>作者：</font>** Nicholas Tagliapietra, Gian Lorenzo Marchioni, Moritz Willig 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Learning causal models from high-dimensional data is a significant challenge, particularly in real-world settings where violations of core assumptions lead to causal identifiability issues. Although massive amounts of prior knowledge are available, and contain valuable causal information, effectively integrating this knowledge into the causal discovery process remains an open problem. We introduce CausalSTeward (CAST), a novel human-in-the-loop framework for interactively assembling large causal models. CausalSteward is a multi-agent collaborative system that tackles high-dimensional causality through a divide-and-conquer approach where large clusters of variables are iteratively partitioned and then separately analyzed. Our framework fuses prior knowledge with a data-driven approach by using tailored tools such as retrieval augmented generation and conditional independence tests. Finally, we use this work to examine the capabilities and limitations of causal reasoning in multi-agent frameworks, and how the human-in-the-loop can contribute to accurate and trustworthy results.

---


### 78. [Atomic Task Graph: A Unified Framework for Agentic Planning and Execution](https://arxiv.org/abs/2607.01942)

**<font color=#1a73e8>作者：</font>** Yue Zhang, Sihan Chen, Ziwen Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents have shown strong potential for solving complex multi-step tasks, yet existing performance improvements often rely on either scaling to larger backbone models or task-specific fine-tuning. The former incurs substantial computational costs, while the latter typically generalizes poorly across different tasks. Although prompt-based control is training-free and broadly applicable, existing methods still leave input-output dependencies between subtasks implicit in textual trajectories, making verified intermediate results difficult to reuse. To address these limitations, we propose Atomic Task Graph (ATG), a unified control framework for planning and execution. Specifically, ATG maintains an explicit graph to expose dependencies and support reuse. During planning, it recursively decomposes a high-level task into subtasks, forming a sequence of directed acyclic graphs (DAGs) whose evolution can be traced. During execution, the dependencies exposed by ATG allow independent branches to be executed in parallel, thereby improving execution efficiency. When failures are detected, ATG leverages the graph evolution history to localize the error source and repair only the affected region, preserving validated regions unchanged. Experiments show that ATG consistently outperforms strong baselines in success rate and execution efficiency across three interactive benchmarks using only 7B-8B backbones.

---


### 79. [Beyond Supervised Clarification: Input Rewriting with LLMs for Dialogue Discourse Parsing](https://arxiv.org/abs/2607.01964)

**<font color=#1a73e8>作者：</font>** Yiming Liu, Ziyue Zhang, Zhichao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rewriting inputs to improve frozen downstream models has become a common strategy in modern NLP pipelines. Prior work on incremental dialogue discourse parsing (DDP) shows that supervised clarification models can rewrite fragmentary or underspecified utterances, such as resolving ellipsis or references, to improve parsing accuracy. In this work, we revisit this idea under realistic deployment conditions, where no clarification supervision is available and the clarifier must rely on zero-shot prompting or feedback from a frozen parser. Across three Segmented Discourse Representation Theory (SDRT) datasets and multiple parsers, we find that last-utterance clarification is far less reliable than suggested by supervised settings. Parser-agnostic rewriting often introduces more regressions than repairs, as edits that enable fixes also disrupt discourse cues relied upon by the parser. A best-of-8 rewriting analysis further reveals a practical ceiling: a large fraction of errors are not repairable through input rewriting alone. A parser-aware clarifier trained with GRPO reduces regressions by up to 37% by learning conservative abstention, yet still fails to produce selectivity-aware clarifications that consistently improve parsing. Together, these findings recast clarification as a selective intervention problem. We identify rewritability prediction, deciding whether an utterance is repairable before intervention, as the key missing capability for input-side optimization of frozen discourse parsers, and a critical direction for improving agentic pipelines more broadly.

---


### 80. [Probabilistic Low-Voltage Peak Load Forecasting with Time Series Foundation Models Evaluated on Application-Oriented Metrics](https://arxiv.org/abs/2607.01966)

**<font color=#1a73e8>作者：</font>** Benedikt Kaas, Manuel Treutlein, Hannes Benedikt Gerber 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-voltage load forecasting is an important component in current and future energy systems with a high degree of electrification and decentralized generation. However, current forecasting methods require significant manual effort, often lack uncertainty estimation and proper peak prediction, and they are often not adequately evaluated in terms of grid requirements. In the present study, we provide an extensive evaluation of short-term net load forecasts of 200 real-world low-voltage feeders with a focus on the rapidly evolving time series foundation models. Our study compares Chronos-Bolt, Chronos-2 and TabPFN-TS to six baseline models and demonstrates superior performance, in particular for Chronos-2. An ablation study, in which weather covariates are omitted, shows that time series foundation models adapt to increased uncertainty, despite the importance of weather information. A novel application-oriented metric links the model's forecasting capabilities in peak prediction to the trade-off in grid asset planning and operation between cost reduction and minimizing the risk of failure.

---


### 81. [Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization](https://arxiv.org/abs/2607.01972)

**<font color=#1a73e8>作者：</font>** Jan Drchal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often asked to produce JSON conforming to a fixed schema, powering information extraction, tool calling, agentic planning, and knowledge-graph construction. Measuring how closely an output matches a gold reference is essential yet surprisingly hard: exact match is brittle, text similarity ignores structure, and an LLM judge is expensive, opaque, and non-deterministic. We address this with Object Aligner (OA), an open-source Python library that scores two JSON objects deterministically by recursively aligning their trees (the Hungarian algorithm for unordered collections, sequence alignment for ordered ones) and awarding partial credit at the granularity the schema declares. The Object Aligner is configured entirely through a set of JSON Schema extensions, so adapting it to a new task involves annotating a schema rather than writing code. Complex structured data, however, are rarely flat trees: records may form graphs or hypergraphs keyed by arbitrary identifiers, breaking the assumptions of prior similarity metrics. Our central contribution, referential alignment, closes this gap by inferring a bijection between gold and candidate identifiers and scoring every reference through it, so the score is invariant to relabeling. Since recovering this bijection exactly is graph isomorphism, the Object Aligner approximates it with Weisfeiler-Leman color refinement. An order-sensitive sequence regime targets ranking and planning. Since the same alignment localizes every mismatch, the Object Aligner emits ranked repair suggestions at no extra cost. Used as a reward inside the GEPA prompt optimizer, Object Aligner helps or stays neutral across all datasets.

---


### 82. [OntoLearner: A Modular Python Library for Ontology Learning with Large Language Models](https://arxiv.org/abs/2607.01977)

**<font color=#1a73e8>作者：</font>** Hamed Babaei Giglou, Jennifer D'Souza, Andrei Aioanei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology learning (OL) aims to automatically construct structured knowledge models from text, yet progress remains fragmented across methods, domains, and evaluation practices. Despite decades of research, OL lacks a shared infrastructure for systematic evaluation and ontology access. This absence has hindered progress and fragmented research, leaving the central challenges of OL largely unaddressed. We introduce OntoLearner, a modular, cross-domain, and first-of-its-kind framework that unifies ontology access, large language model (LLM)-driven learning pipelines, and standardized benchmarking. OntoLearner releases 180 machine-readable ontologies spanning 22 domains and provides pipeline-ready datasets with train/dev/test splits for three core OL tasks: term typing, taxonomy discovery, and non-taxonomic relation extraction. Using this infrastructure, we conduct a large-scale empirical study of OL, evaluating 22 retrieval models and 12 LLMs across domains and tasks. The results converge on a finding that reframes the central challenge of OL: failure modes scale with ontological complexity rather than model size or architectural sophistication. The primary bottleneck is not model capability, but a structural mismatch between how models encode knowledge and how ontologies organize it. These findings establish that effective OL is reachable through the cross-domain, multi-task benchmarking enabled by OntoLearner. OntoLearner is open-source (MIT license) at this https URL.

---


### 83. [Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing](https://arxiv.org/abs/2607.01978)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Youyuan Zhang, Ruitong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, but rarely control the semantic boundary of each edit. Our pilot analyses of post-edit behaviors and internal neuronal activities reveal a scope gap behind reliable edits: instance-level success neither guarantees transfer to valid cross-modal variants nor prevents leakage to unrelated inputs, while edit-related cross-modal responses concentrate in deeper semantic layers. Therefore, we formulate Edit-Scoped Generalization, reframing online MLLM editing from merely correcting an instance to controlling the propagation boundary of each edit. To this end, we propose ScopeEdit, a scope-aware online editor that decomposes each update into a modality-local absorption branch and an evidence-gated shared generalization branch. The local branch supports stable edit absorption, whereas the shared branch enables cross-modal propagation only when visual and textual evidence are sufficiently aligned. Both branches perform scope-separated write geometries in orthogonal low-rank spaces and maintain branch-wise preconditioners via Sherman--Morrison recursions, yielding constant per-edit overhead. Extensive experiments across diverse benchmarks, long-horizon edit streams, MLLM backbones, real-world VLKEB scenarios, and complex vision-language architectures show that ScopeEdit consistently improves the trade-off between in-scope cross-modal transfer and out-of-scope locality, while preserving edit reliability, stability and online efficiency. Our code is available at this https URL.

---


### 84. [MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding](https://arxiv.org/abs/2607.01982)

**<font color=#1a73e8>作者：</font>** Wenda Wang, Yihan Tong, Yuwei Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using molecular large language models (LLMs) as a unified framework for understanding molecular structures and functions is emerging as a new trend in tasks such as molecular design and drug discovery. However, these models struggle to fully capture the visual representation of molecular structures, limiting their potential. While existing molecular vision-language models (VLMs) show promise, they still face challenges in structural alignment and lack the necessary topological modeling for accurate molecular understanding. To address this, we propose MolSight, a graph-aware vision-language model framework designed to enhance the understanding of molecular images by VLMs. MolSight integrates a Molecular Topology Module to inject chemical-bond adjacency information into vision tokens, and a Molecular Grounding Module to align visual features with chemical symbolic semantics. Our experiments demonstrate that MolSight significantly outperforms existing VLMs, molecular LLMs, and specialized tools across multiple chemical visual understanding tasks, achieving a new level of molecular image reasoning.

---


### 85. [Open-Weather Robust 3D Detection via Dual-Critic Diffusion Alignment](https://arxiv.org/abs/2607.01983)

**<font color=#1a73e8>作者：</font>** Shuyao Li, Chuanxing Geng, Heyang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust 3D object detection under adverse weather remains a critical hurdle for autonomous driving. Despite progress with LiDAR-4D radar fusion, most methods are constrained by a closed-world assumption, implicitly requiring training and test weather to align in both type and severity. This premise fails in practice: the open-ended nature of weather, and even variations within a single type like rain, cause dramatically different LiDAR degradation patterns, leading to significant performance drops in unseen conditions. To address this, we present Dual-Critic Guided Diffusion Alignment (DCDA), a weather-agnostic framework that learns to recover degraded LiDAR features toward a clean manifold. Rather than modeling specific weather types, DCDA employs a 4D radar-conditioned diffusion process to progressively refine features, guided by two complementary critics. (i) A detection-guided critic, anchored by a pre-trained clean-weather model, ensures that the refined features retain object-level discriminability and localization accuracy. (ii) A weather adversarial critic enforces holistic distributional consistency with clean-weather representations. By aligning features through semantic and distributional constraints rather than explicit weather modeling, DCDA generalizes effectively to unseen weather types and severities without requiring paired data or weather labels. We further introduce a structured open-weather benchmark with held-out type-severity combinations and extensive experiments verify DCDA's advantages.

---


### 86. [Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant](https://arxiv.org/abs/2607.01992)

**<font color=#1a73e8>作者：</font>** Jiangdi Ru, Bing Li, Yage Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale battery energy storage systems (BESSs) require O&M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms can flag threshold violations, but they often cannot explain whether voltage inconsistency, resistance drift, short-circuit risk, capacity divergence, or thermal abnormality needs intervention. This digest presents a traceable BESS fault-diagnosis assistant that uses retrieval-augmented multi-agent reasoning to connect operational data, domain knowledge, visual evidence, and report generation. Reliability is improved through BESS-specific task routing, schema-constrained natural-language database access, hybrid text-image retrieval, and evidence-based answer synthesis. Preliminary internal evaluation is reported for routing, database access, and diagnostic reasoning.

---


### 87. [EduArt: An educational-level benchmark for evaluating art history knowledge in large language models](https://arxiv.org/abs/2607.02007)

**<font color=#1a73e8>作者：</font>** Gianmarco Spinaci, Lukas Klic, Giovanni Colavizza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models now score near ceiling on general benchmarks, but these aggregate measures reveal little about how models behave within single disciplines. Existing art-focused evaluations rely on synthetic questions and rarely report item-level properties. This paper introduces EduArt, an educational-level benchmark for art-historical knowledge and visual reasoning in multimodal LLMs. EduArt comprises 871 human-authored questions from Italian secondary-school exercises and US Advanced Placement Art History exams, spanning two languages and seven formats from multiple choice to in-text word placement and error identification. Twelve models from six provider families were evaluated under a default answer-only condition and a motivation condition requiring written justification, and characterized using Classical Test Theory and a logistic regression isolating the effects of format, language, image presence, and model. The benchmark showed strong psychometric properties (mean discrimination 0.514, 82.3 percent good discriminators), while multiple-choice accuracy saturated near ceiling for six models, showing recognition formats alone cannot distinguish frontier models. Format was a strong independent predictor of accuracy: models exceeding 94 percent on multiple choice fell to 23.9 percent on open completion (Claude Opus 4.6) and 6.2 percent on error identification (Claude Sonnet 4.6). The motivation condition changed accuracy in a predominantly negative, family-dependent direction. These dissociations indicate that art-historical knowledge and the ability to deploy it are distinct capabilities, and that single-format benchmarks overestimate what models can reliably do. Mapping this capability profile is a precondition for responsible use of multimodal LLMs in art-historical scholarship, where tasks demand producing and manipulating content rather than selecting from fixed options.

---


### 88. [InduceKV: Fixed-Footprint Continual Adaptation of Multimodal LLMs via Inducing KV Memories](https://arxiv.org/abs/2607.02010)

**<font color=#1a73e8>作者：</font>** Qianyu Chen, Ziteng Feng, Canran Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models must adapt to evolving tasks and domains, yet continual improvement under bounded deployment footprint remains difficult because repeated parameter updates or growing replay stores can accumulate adaptation state over time. We study fixed-footprint continual adaptation: the deployed adaptation state is kept under a fixed memory budget, while the backbone model is left unchanged and task-specific updates are externalized. We propose InduceKV, a retrieval-based method that stores each selected training prefix as an attention-ready memory entry, consisting of a frozen retrieval key and compact layerwise key--value (KV) payloads that can be appended to the model's self-attention cache. Under a strict memory budget, InduceKV constructs a compact inducing set through bilevel selection: a lightweight calibration is fit for retrieval, while the selected memory balances current-task likelihood, anchor-based retention, and coverage in the frozen retrieval space. Across task-incremental instruction tuning, continual VQA, domain-incremental adaptation, and lifelong multimodal instruction tuning, InduceKV consistently improves over PEFT, MoE, replay, and prompt-retrieval baselines under matched memory budgets. We further report backbone-matched, stage-1 CoIN, compute-matched, and scalability diagnostics, showing that the gains are not due to a stronger backbone, replay alone, or an unbounded candidate pool.

---


### 89. [Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails](https://arxiv.org/abs/2607.02020)

**<font color=#1a73e8>作者：</font>** Qianyu Chen, Canran Xiao, Runxuan Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models must continually adapt to evolving tasks and domains, yet standard continual learning metrics mainly measure whether old answers remain correct, leaving the stability of multimodal grounding largely unexamined. We study this overlooked failure mode and ask whether a continually adapted MLLM can preserve not only what it answers, but also how it uses visual, textual, OCR, chart, and document evidence. We identify \emph{hidden evidence-use forgetting}, where answer accuracy is retained while the model silently shifts toward different or less grounded evidence channels, and propose \textsc{RCL}, a replay-free reliance-constrained continual learning framework. \textsc{RCL} freezes the previous checkpoint as a behavioral reference, estimates teacher and student evidence-reliance profiles through counterfactual channel interventions, and jointly optimizes task learning, prediction preservation, and reliance preservation without adding inference-time cost. Across CoIN, COAST, MCITlib, and an evidence-sensitive multimodal stream, \textsc{RCL} consistently improves final performance and reduces forgetting over replay-free, PEFT, routing, and memory-assisted baselines, while substantially lowering modality reliance drift, dominant evidence flips, and hidden forgetting rates. These results suggest that robust continual multimodal learning requires preserving the evidence path behind correct answers, not merely the answers themselves.

---


### 90. [Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to You Only Look Once and Optical Character Recognition for Nigerian License Plate Recognition](https://arxiv.org/abs/2607.02025)

**<font color=#1a73e8>作者：</font>** Ismail Ismail Tijjani, Ahmad Abubakar Mustapaha, Sunusi Ibrahim Muhammad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> License Plate Recognition (LPR) systems are critical tools in traffic monitoring, security enforcement, and urban mobility management. Traditional LPR systems often rely on a multi-stage pipeline involving object detection using You Only Look Once (YOLO) and Optical Character Recognition (OCR), which suffer from limitations such as high resource demands, poor performance in unstructured environments, and the need for large annotated datasets. This study explores the potential of Vision-Language Models (VLMs) as a unified, zeroshot learning solution for Nigerian license plate recognition. Using a curated dataset of 88 challenging real-world images collected in Nigeria, we evaluate five selected VLMs: Gemini 2.0 Flash Exp (Google DeepMind), Qwen2.5-VL-7B-Instruct (Alibaba), GPT-4o (OpenAI), Claude 4 Sonnet (Anthropic), and Llama 3.2 Vision 90b (Meta). Results based on Character Error Rate (CER) reveal that Gemini and Qwen significantly outperform other models in both accuracy and robustness, on the challenging image scenarios. This work highlights the practical advantages of VLMs over YOLO+OCR, questions the claims by model providers, and compares the performances of the VLMs.

---


### 91. [PACE: A Proxy for Agentic Capability Evaluation](https://arxiv.org/abs/2607.02032)

**<font color=#1a73e8>作者：</font>** Yueqi Song, Lintang Sutawika, Jiarui Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents on benchmarks like SWE-Bench and GAIA can be expensive, time-consuming, and requires complex infrastructure. A single evaluation can cost thousands of dollars and take days to complete. In contrast, non-agentic LLM benchmarks that test individual capabilities (e.g., reasoning, code generation) are fast and cheap to run. In this paper, we investigate whether performance on expensive agentic benchmarks can be accurately predicted by the performance on a small, carefully selected subset of atomic evaluation instances. We introduce PACE, a framework that constructs proxy benchmarks by selecting instances from existing non-agentic evaluations whose aggregate scores most reliably predict model performances on agentic benchmarks. Given a pool of candidate instances spanning atomic capabilities, PACE fits a regression that maps a model's scores on a compact subset of source instances to its score on the target agentic benchmark. The subset itself is curated by combining two complementary instance-selection strategies, target-relevance local selection and globally informative global selection. We apply PACE to the 4 target agentic benchmarks in this paper, which yields PACE-Bench, the concrete proxy benchmark that we evaluate in the paper. Experiments across 14 models, 4 agentic benchmarks, and 19 non-agentic benchmarks show that PACE-Bench predicts agentic scores with leave-one-out cross-validation (LOOCV) mean absolute error (MAE) under 4%, Spearman correlation above 0.80, and pairwise model-ranking accuracy around 85%, all at much less than 1% of the full agentic evaluation cost. We further analyze the selected proxy instances, revealing which skills each agentic benchmark uniquely demands. PACE enables practitioners to obtain reliable estimates of agentic performance during model development, selection, and routing, without the overhead of full agent evaluation.

---


### 92. [PWM-ArtGen: Part World Model for Articulated Object Generation](https://arxiv.org/abs/2607.02045)

**<font color=#1a73e8>作者：</font>** Wentao Zheng, Ancong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The key challenge in articulated 3D object generation from a single image is accurately predicting the underlying kinematic structure. Existing methods either infer kinematic parameters directly from a static image that lacks dynamic part-level kinematic relationships, or estimate parameters from visual dynamics generated from a single image, which is prone to accumulated errors of two steps. Moreover, the limited scale and diversity of existing annotated datasets further hinder generalization to complex, real-world objects. To overcome these limitations, we propose to learn the joint distribution of visual dynamics and kinematic parameters. Recognizing that articulated objects can be formulated as dynamic systems, we propose a unified Part World Model called PWM-ArtGen. To leverage unannotated data, this model couples action diffusion and image diffusion with independent diffusion timesteps, which enables visual branch co-training. We further curate a photorealistic dataset of 19.7k part-level image pairs without kinematic annotations, to support co-training. Experiments demonstrate that PWM-ArtGen substantially outperforms existing baselines in the resting state and exhibits strong zero-shot generalization to out-of-distribution objects.

---


### 93. [SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLM Responses](https://arxiv.org/abs/2607.02049)

**<font color=#1a73e8>作者：</font>** Anna Chorna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed in emotional-support contexts and crisis-related situations. Nevertheless, their cross-lingual abilities in these circumstances remain underexplored. Existing benchmarks emphasize multilingual performance but rarely examine crisis-related empathy and cultural grounding in low-to-mid-resource languages. We introduce SPLIT, a 500-prompt benchmark designed to evaluate LLM consistency in generating emotionally grounded responses across five categories: Stress, Panic, Loneliness, Internal Displacement, and Tension. We evaluate three technically diverse LLMs across three dimensions: Empathetic Accuracy, Linguistic Naturalness, and Contextual & Cultural Grounding. The framework aims to assess and compare the quality of LLM responses in both English and Ukrainian languages, as well as to explore the reliability of the LLM-as-a-jury paradigm. Our findings reveal that Gemini-2.5-Flash and LLaMA-3.3-70B-Instruct degrade when transitioning to Ukrainian, while DeepSeek-V3 remains comparatively stable within our benchmark. We additionally find that human and AI evaluators agree weakly on empathy and naturalness but diverge on cultural grounding. We further argue that producing Ukrainian text is not equivalent to producing Ukrainian emotional support. Our findings may assist in the future development of more culturally tailored benchmark designs, as well as encourage a stronger emphasis on human-centered evaluation.

---


### 94. [kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail](https://arxiv.org/abs/2607.02072)

**<font color=#1a73e8>作者：</font>** Mahmoud Abdelfattah, Hamid Nasiri, Peter Garraghan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in domains requiring guardrails to detect unsafe, off-topic, or adversarial prompts. Existing guardrails predominately rely on fine-tuning to build classifiers, which often suffer from low generalization and high inference latency. We present kNNGuard, a training-free guardrail that utilizes the activation space of an off-the-shelf LLM. Given a small bank of 50 safe and unsafe prompts, kNNGuard extracts hidden activations and performs multi-layer kNN fusing activation-space and embedding-space scores for classification. Across six domains spanning topical and security prompts, kNNGuard achieves competitive or superior F1 compared to fine-tuned state-of-the-art guardrails while running 2.7x faster than the best comparable guardrail, and 10x faster than a fine-tuned safety classifier without gradient updates or fine-tuning. Domain adaptation requires only updating the labeled bank, which can be constructed in under 10 seconds and several orders of magnitude faster than established guardrails. We also analyze the impact of system prompts, layer selection, and integration into production LLM pipelines as a configurable, low-latency guardrail.

---


### 95. [DeepGaze3.5-VL: Modeling Scanpaths via Autoregressive Token Prediction](https://arxiv.org/abs/2607.02083)

**<font color=#1a73e8>作者：</font>** Susmit Agrawal, Matthias Bethge, Matthias Kümmerer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human visual attention on a scene over time has applications in domains such as interface design and inferring cognitive states. Modeling visual scanpaths has historically relied on specialized architectures with hand-crafted priors. While these architectures can model fixation sequences, their rigid structural biases restrict easy extendability and flexible conditioning. For instance, integrating task-specific instructions or adapting to distinct viewer identities requires custom, disjoint architectural additions. We frame scanpath prediction purely as a discrete sequence modeling task. By mapping coordinates into a text vocabulary, we leverage the pretrained representations of Vision-Language Models. This framing absorbs diverse factors of variation: simple prompting allows for global conditioning, such as providing viewer identities to capture personalized biases, or task-specific objectives like visual search. The framework can also integrate per-fixation attributes, such as individual fixation durations, alongside spatial locations. The autoregressive alignment enables the scalable, exact computation of per-fixation log-likelihoods, directly equivalent to the commonly used Information Gain (IG) metric. Our model, DeepGaze3.5-VL, establishes a new state-of-the-art across multiple datasets, achieving 2.18 bits of IG on MIT1003, a 46% improvement over DeepGaze III. This advantage persists even when baselines use identical high-capacity vision encoders. Beyond predictive performance, our generative framework serves as a powerful computational tool for direct behavioral interventions, allowing for controlled in-silico simulations that would be experimentally difficult or impossible to conduct in vivo. We demonstrate this ability by performing controlled interventions on the durations of pre-saccadic fixations, recovering known oculomotor phenomena purely from data.

---


### 96. [ESC: Emotional Self-Correction for Reliable Vision-Language Models](https://arxiv.org/abs/2607.02089)

**<font color=#1a73e8>作者：</font>** Tien-Huy Nguyen, Minh-Nhat Nguyen, Nguyen Nhat Huy 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance across diverse multimodal tasks, yet they remain vulnerable to unreliable reasoning. Existing self-correction methods mitigate these issues but typically rely on post-training or carefully engineered feedback, incurring high computational cost. In this work, we revisit this challenge through the lens of emotional cues, asking whether they can activate latent self-correction behaviors in VLMs without additional training. \textbf{We find that emotional signals serve as an effective trigger for self-correction, encouraging more cautious and reflective reasoning}. Motivated by this finding, we propose \escabstract (\textbf{\underline{E}}motional \textbf{\underline{S}}elf-\textbf{\underline{C}}orrection), a training-free self-correction framework. ESC introduces an external verifier that detects potentially incorrect initial responses and injects emotional feedback to encourage model to reflect, and produce a better revised response without additional training. Extensive experiments across safety, hallucination, vision-centric perception, and multimodal reasoning benchmarks show that ESC consistently improves reliability while preserving overall model utility. These results suggest that emotion can function not only as an ability to be recognized, but also as a practical control signal for scalable self-correction in VLMs. \textbf{We therefore believe that ESC provides a strong foundation for a new reliable human-like, emotion-integrated research direction.} Our project is publicly available at \textcolor{red}{this https URL}.

---


### 97. [Multimodal Fusion for Fine-Grained Classification of Breast Fibroadenoma and Phyllodes Tumors](https://arxiv.org/abs/2607.02091)

**<font color=#1a73e8>作者：</font>** Chuxi Nan, Di Wu, Hongming Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast fibroadenoma (FA) and phyllodes tumor (PT) are fibroepithelial breast lesions with highly overlapping appearances on B-mode ultrasound, making benign and borderline PT prone to being misclassified as FA and complicating preoperative decision-making. Existing computer-aided diagnosis methods commonly rely on single-modal imaging features and insufficiently exploit complementary clinical and textual information. To address this limitation, we construct the FAPT-M Dataset, a pathology-confirmed multimodal dataset comprising 910 patients with strictly reviewed ultrasound images, structured clinical attributes, and ultrasound diagnostic descriptions. Based on this dataset, we propose a clinically guided multimodal framework that integrates DenseNet-based visual encoding, CLIP-inspired text encoding, and lightweight clinical encoding, and further introduces clinical-conditioned adaptive modulation, cross-modal Transformer fusion, and dual-path representation learning to improve feature alignment and multimodal interaction. Under patient-level five-fold cross-validation, the proposed method achieves an accuracy of 77.64%, F1-score of 73.38%, and AUC of 89.74%, outperforming representative CNN-, Transformer-, and vision-language-based baselines. Ablation studies and class-balanced evaluations further confirm the contribution of three-modality fusion and the key architectural components. Overall, this work provides an effective multimodal approach for fine-grained FA-PT classification and establishes a high-quality benchmark for multimodal breast ultrasound analysis.

---


### 98. [Ask the Right Comparison:Bias-Aware Bayesian Active Top-$k$ Ranking with LLM Judges](https://arxiv.org/abs/2607.02104)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as cheap, scalable judges that compare candidate outputs pairwise -- to rank responses, select models, or triage papers. Yet LLM judges are both noisy and systematically biased: they favor verbose or well-formatted answers and exhibit position effects, so simply aggregating their votes recovers a ranking of presentation, not of true quality. We study the practical goal of identifying the \topk{} items under a fixed comparison budget, and make two contributions. First, we cast judging as Bayesian inference over latent quality with explicit, judge-specific bias covariates (verbosity, position), regularized by a shrinkage prior so that the data decide which biases a given judge actually exhibits. Second, we introduce a \topk-aware active acquisition rule that chooses the next comparison to maximally reduce uncertainty about \topk{} \emph{membership}, rather than about the full ranking. On a controlled benchmark with known ground-truth quality, judged by sixteen real LLMs spanning open and proprietary families (Llama, Qwen, Phi-4, GPT-4o-mini/5.1/5.5, Gemini, DeepSeek, and Claude Haiku/Sonnet/Opus), naive aggregation plateaus at a wrong \topk{} on biased judges regardless of budget, while our bias-aware model recovers it; \topk-aware acquisition reaches this ceiling with far fewer comparisons than round-robin or a global-uncertainty (D-optimal) rule. Bias is real but heterogeneous and capability-dependent: cheap and mid-tier judges carry a strong verbosity bias that our model corrects (lifting recall from $\sim$$0.5$--$0.6$ to $0.84$--$1.0$), whereas the frontier judges we tested show little bias and already rank accurately, so bias-aware modeling changes little there.

---


### 99. [Enhancing Fitness Intelligence through Domain-Specific LLM Post-Training](https://arxiv.org/abs/2607.02118)

**<font color=#1a73e8>作者：</font>** Xingtao Zhao, Tian Yang, Han Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific Fitness Coaching (SFC) is typically delivered by human professionals, making it costly and inaccessible to many. While recent advances in Large Language Models (LLMs) show considerable promise for more inclusive fitness coaching, directly deploying prevailing general-purpose LLMs in SFC reveals critical limitations. These models often lack sufficient domain-specific knowledge integration, leading to weak performance on complex SFC scenarios. In this paper, we introduce FitOne, a series of fitness LLMs (with 8B and 32B parameters) designed to improve reliability and domain specialization for SFC applications. Built upon the Qwen3 foundation models, FitOne is developed through a three-stage post-training pipeline consisting of continual pre-training, supervised fine-tuning, and reinforcement learning, using large-scale, high-quality datasets derived from rigorous knowledge engineering. We conduct comprehensive evaluations of FitOne on professional fitness certification exams, including ACSM-EP and NSCA-CSCS, as well as general capabilities such as knowledge reasoning and instruction following. Experimental results show that, while retaining strong general capabilities, FitOne-8B/32B achieves average improvements of up to 10.09%/9.29% and 12.73%/7.01% on the ACSM-EP and NSCA-CSCS exams, respectively, compared with the Qwen3 base models. Furthermore, in-depth ablation studies confirm the necessity of each training stage, highlighting the pipeline's effectiveness in balancing domain expertise enhancement with general ability retention. We believe this research advances LLM systems toward more reliable fitness intelligence and will inspire future research on developing domain-specific LLMs.

---


### 100. [Probing Chemical Language Models: Effects of Pre-training and Fine-tuning](https://arxiv.org/abs/2607.02140)

**<font color=#1a73e8>作者：</font>** Anna Karnysheva, Dietrich Klakow, Ji-Ung Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical language models (CLMs) are trained with linearized representations such as SMILES, yet it remains unclear which chemically meaningful substructures they encode. To foster a better understanding of CLMs, we conduct a systematic study and probe for 78 molecular substructures across eight pre-trained and six randomly initialized models. We furthermore study how fine-tuning on chemical downstream tasks affects the learned representations of molecular substructures. Our results show that pre-training generally improves molecular structure awareness of CLMs, particularly in the upper layers. Moreover, randomly initialized models already encode ring structures well in the first layer. Our analysis on two chemical downstream tasks further reveals that, interestingly, fine-tuning affects task-relevant molecular substructures more than others, indicating that the changes in the representations follow chemical theory.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-136](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
