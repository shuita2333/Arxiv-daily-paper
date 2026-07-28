# 🧠 大模型相关研究 | 2026年07月29日

> 本类共 **240** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 51. [Beyond Block Boundaries: Multi-Block Editing for Diffusion Large Language Models](https://arxiv.org/abs/2607.22663)

**<font color=#1a73e8>作者：</font>** Xingyu Mou, Zijin Huang, Tianze Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Block diffusion has emerged as the dominant paradigm for scaling discrete diffusion language models (dLLMs), because decoding text in fixed-size blocks preserves parallel generation within each block while keeping the quadratic attention cost tractable. However, this efficiency comes with a structural limitation: tokens near the end of a block are generated without access to future cross-block context, and once a block is finalized, its uncertain predictions become irreversible context for all subsequent blocks. This creates a block boundary problem, in which uncertainty accumulates toward block boundaries and early mistakes propagate throughout later generation. To address this issue, we propose Multi-Block Editing (MBE), to mitigate this problem by editing decoded tokens based on cross-block context. Following this principle, MBE first proposes a training-free decoding algorithm to edit the decoded tokens in previous blocks, which is achieved by re-opening a full-attention window over selected blocks. Given the mismatched attention mechanism between block diffusion training and MBE inference, MBE further introduces a supervised Fine-tuning strategy, which equips the model with bidirectional attention masks that progressively expands the editing span. Furthermore, it also extends SGLang with a multi-shape CUDA Graph pool and fine-grained KV cache control to make these variable-length editing passes efficient in practice. Experiments on LLaDA2.1-Mini across 13 benchmarks show that training-free MBE outperforms all existing decoding baselines while maintaining comparable throughput, and MBE SFT further brings a performance gain of 2.7. The largest improvements appear on tasks requiring strong long-range consistency, including +13.3 on AIME 2025 and +5.9 on ZebraLogic, demonstrating the effectiveness of MBE.

---


### 52. [AIR-BENCH Live: An Evolving Safety Benchmark for Foundation Models](https://arxiv.org/abs/2607.22671)

**<font color=#1a73e8>作者：</font>** Rohan Naphade, Minzhou Pan, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation-model safety benchmarks capture the AI risks of their time of publication: as models improve and governments pass new AI-safety legislation, their risk taxonomies become incomprehensive and their attack prompts become ineffective. We present AIR-BENCH Live, a self-evolving successor to AIR-BENCH 2024. An automated update pipeline monitors government regulation and classifies new policies against the current four-tier risk taxonomy, either matching them to existing categories or proposing new granular categories. Then, a multi-agent, persona-driven prompt generation algorithm generates realistic, multilingual prompts with minimal human review, leaving room for improvement with modern jail breaking techniques. This algorithm is used to overhaul legacy prompts and generate prompts for new categories. In our current version, the pipeline has expanded the benchmark from 314 to 335 granular risks, with the 21 new categories drawing from 31 truly novel policy clauses across seven jurisdictions. Evaluating 14 recent models, we find a wide safety spread (from 0.17 to 0.89 among the models judged on their own behavior), that the modernized prompts are on average 0.06 points harder than the 2024 set, with the largest drops concentrated among the most compliant models, and that most models are modestly less safe on non-English prompts. By continuously absorbing new regulation and regenerating prompts, AIR-BENCH Live is designed to evolve alongside a fast-moving field.

---


### 53. [How LLM Task-Adaptation Reshapes Alignment: A Multi-dimensional Study of Behavioral and Representational Drift](https://arxiv.org/abs/2607.22676)

**<font color=#1a73e8>作者：</font>** James Elcock, William F. Shen, Xinchi Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training is a key mechanism for adapting large language models to downstream tasks. While prior work suggests that task adaptation can alter a model's pre-existing alignment, especially its safety behavior, its broader effects across alignment domains remain poorly understood. We address this gap through a systematic evaluation of representative task-adaptation methods, including supervised fine-tuning (SFT), KL-regularized SFT, and reinforcement learning with verifiable rewards (RLVR) across 15 alignment aspects spanning six key domains: safety, factuality, stance stability, social harm, controllability, and instructability. Our results reveal that post-training does not reshape alignment uniformly. RLVR improves task performance while inducing comparatively small, but non-zero, metric-specific shifts, while SFT leads to substantially larger alignment drift across domains. KL regularization mitigates this effect: stronger reference-model anchoring reduces alignment drift from the baseline, although KL-SFT still falls short of RLVR in preserving alignment. Representation-level analysis further supports this pattern, with shifts in alignment-relevant representations tracking behavioral drift. Together, these results show that task adaptation is not merely a capability-improving step, but an alignment intervention in its own right, motivating multi-dimensional alignment evaluation as a standard component of post-training pipelines.

---


### 54. [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](https://arxiv.org/abs/2607.22688)

**<font color=#1a73e8>作者：</font>** Zhengyu Chen, Teng Xiao, Huaisheng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training agents for automated AI research requires optimizing not only model parameters, but also the runtime harness that shapes how research trajectories are generated, evaluated, and learned from. Existing pipelines typically train models under a fixed harness, including prompts, tools, skills, middleware, and memory, while leaving the data-generating process outside the optimization objective. This creates a mismatch between model updates and the static scaffolding that determines trajectory quality. We introduce Co-Harness, a framework that jointly optimizes the agent harness and model parameters during post-training. Co-Harness alternates between harness optimization and model optimization. An LLM-based HarnessCritic analyzes failed trajectories, identifies harness-level failure modes, and proposes validated local updates. The model is then fine-tuned on high-quality trajectories generated by the improved harness, distilling effective scaffolding into model parameters. A 200+ hour autonomous case study further shows that Co-Harness can recover from system crashes, improve inference efficiency, and discover ensemble strategies without human intervention. These results suggest that joint harness and model optimization is an effective way to improve agents beyond fixed-harness post-training.

---


### 55. [LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory](https://arxiv.org/abs/2607.22690)

**<font color=#1a73e8>作者：</font>** Jing Yu, Yibo Zhao, Jiaming Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory lets LLM agents reuse past interactions, but raw dialogue histories are verbose and information-sparse. Retrieving broadly improves evidence coverage yet overwhelms downstream reasoning with noise; compressing at write time reduces noise but irreversibly discards details the future query may need. We introduce LazyMem, which sidesteps this dilemma by deferring all memory construction to query time. A lightweight 4B model processes the retrieved candidate pool in overlapping parallel windows, selectively retaining and compressing only query-relevant content. The model is trained through supervised fine-tuning followed by group-based reinforcement learning with a format-gated composite reward that combines a rule-based action signal measuring selection accuracy with an LLM-judged quality signal measuring source faithfulness and query utility. On the LongMemEval benchmark, LazyMem-4B achieves an LLM-judge accuracy of 0.85 with only 213 memory tokens, 68.7$\times$ fewer than retrieval-only, and generalizes to LoCoMo (0.68) without target-domain training, while reducing mean latency over the prior query-time baseline. The 32B variant reaches 0.93, surpassing oracle-context references on aggregation-heavy question types. The code associated with this work is publicly available at this https URL.

---


### 56. [HiLLTS: Zero-Shot Hierarchical LLM-Guided Traffic Signal Control for Sustainable Transportation](https://arxiv.org/abs/2607.22691)

**<font color=#1a73e8>作者：</font>** Yue Ding, Tendai Mukande, Mingming Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic congestion significantly increases fuel consumption, greenhouse gas emissions, and commuter delays, resulting in substantial economic losses and environmental harm in modern cities. Traditional traffic signal control strategies such as fixed-time scheduling, actuated control, and reinforcement learning (RL)-based methods, offer different degrees of adaptability; however, RL-based methods can require extensive retraining, careful reward design, and substantial simulation data when transferred across networks or demand regimes. To address these challenges, we propose HiLLTS, an LLM-guided traffic signal control framework that employs a hierarchical three-layer architecture consisting of a central coordination agent, a district layer and multiple cluster-level intersection agents. Experimental results demonstrate consistent improvements in both congestion and environmental performance. Compared with the strongest non-LLM baseline in each scenario, HiLLTS reduces average waiting time by 36.73% under the low-congestion scenario and 14.71% under the high-congestion scenario, while reducing average CO2 emissions by 7.87% and 8.57%, respectively. Larger gains are observed against weaker baselines: under low congestion, HiLLTS achieves reductions of up to 18.00% in emissions and 62.07% in waiting time relative to Fixed-Time control; under high congestion, reductions of up to 28.89% in emissions and 40.36% in waiting time are observed relative to Max Pressure. The ablation study further validates the contribution of LLM-guided coordination over rule-based control

---


### 57. [Risk Governance for Generative AI Mental Health Support: A Multi-Turn Safety Architecture](https://arxiv.org/abs/2607.22692)

**<font color=#1a73e8>作者：</font>** Anabela C. Areias, Catarina Botelho, António Farinhas 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for emotional support despite lacking mechanisms to safely govern evolving mental health risk. Existing safety approaches primarily detect risk but rarely shape how models respond as conversational risk unfolds. We developed a model-agnostic safety governance architecture that combines contextual risk detection, reasoning-based verification, and protocol-guided response generation for multi-turn mental health interactions. Synthetic conversations grounded in real-world mental health narratives were used to evaluate the architecture's performance, tested with GPT-5-chat and Qwen3.5-27B, achieving high risk detection performance (specificity: 0.85 (95\%CI: 0.78;0.91), sensitivity: 0.92 (95\%CI: 0.88;0.95)) and increasing clinician-preferred escalation responses by 25.6--59.2pp while preserving rapport and connection. Performance remained stable across conversation length and generalized across both proprietary and open-source models. These findings demonstrate that clinically-grounded safety governance can extend beyond risk detection to improve how LLMs manage evolving mental health risk, providing a scalable framework for safer deployment across models.

---


### 58. [Bayesian Repetition Penalty: A Principled Adjacent-Conditional Framework for Reversing Attention Collapse in Autoregressive Language Models](https://arxiv.org/abs/2607.22694)

**<font color=#1a73e8>作者：</font>** Wenjie Fan, Bin Ma, Dong Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attention collapse in autoregressive language models -- manifested as repetitive token loops where the model becomes trapped in self-reinforcing attractors -- is a persistent pathology that existing decoding-time heuristics fail to address at its root cause. We present a principled framework that penalises or compensates anomalous confidence arising from collapsed generation patterns, by comparing a token's observed frequency against its corpus prior through an adjacent-conditional probability construction. The resulting self-normalising penalty ratio $R=f(m,n,p)/f(np,n,p)$ requires no ad hoc standardisation and admits a closed-form logit offset with zero approximation error. The correction is isolated from the loss gradient and accumulated into a frozen output-layer bias via exponential moving average, enabling deployment as a repair mechanism for models that have already collapsed without requiring intrusive modifications to standard training pipelines. Experimental validation on a 1.5B-parameter model demonstrates that the frozen-bias mechanism can rescue a model already trapped in a collapsed attractor, reducing 2-gram repetition from 0.073 to near 0 while preserving generation quality.

---


### 59. [PANOPTICON: A PII-Based Assemblage of Naturalistic Output Tokens for Investigating Privacy Leakage Within LLM Context Window](https://arxiv.org/abs/2607.22695)

**<font color=#1a73e8>作者：</font>** Ryan Thornton, Mir Mehedi Ahsan Pritom, Maanak Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are capable of generalizing human language for the completion of never-before-seen tasks, leading to widespread deployment. While this automation provides clear utility, completing these tasks often requires the insertion of Personally Identifiable Information (PII), strings of information that uniquely identify some individual, raising privacy concerns. However, ethics has prevented the curation of a public, authentic dataset of PII. Without an appropriate dataset, it is difficult to quantify privacy risks. Thus, we introduce the PANOPTICON pipeline and dataset. The dataset, generated by Meta's Llama-3.1-8B-Instruct model, contains 67, 718 prompts, intended for the models context window, containing PII spans derived from 9,674 publicly available synthetic user profiles. We measure lexical diversity and S-BERT diversity of the created dataset to evaluate realism. Finally, we present a case study showcasing the utility of PANOPTICON data for understanding Prompt Inversion Attacks (PIAs). PANOPTICON thus emerges as the first benchmark dataset for studying PIAs over private corpora, providing a foundation for future LLM privacy research.

---


### 60. [Test-Time Coverage: Test-Conditioned Data Curation for Deployment-Aware Learning](https://arxiv.org/abs/2607.22697)

**<font color=#1a73e8>作者：</font>** Nadine Chang, Maying Shen, Shizhe Diao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed AI systems are often trained from broad candidate data pools, necessitating data curation towards the deployment test distribution. However, standard data curation methods score training-side criteria rather than directly optimizing deployment match. We introduce TTCov (Test-Time Coverage), a data-level test-conditioned curation method that uses test-side information before training instead of updating model weights at inference. TTCov decomposes deployment-conditioned curation into coverage and distribution. To represent coverage, it builds a task Atlas, a collection of LLM-based atomic propositions (APs) describing deployment-relevant concepts, seeded from open task knowledge and expanded with unmatched APs extracted from unlabeled deployment samples. To represent distribution, it instantiates the matched deployment APs with their frequencies, yielding a Knowledge Atlas (K-Atlas) that operationalizes the deployment distribution as a curation target. TTCov then selects a budgeted training set whose deployment APs distribution approximates this target. We apply TTCov towards autonomous driving (AD), keeping adaptation off the inference path while selecting data with greater deployment-relevant coverage, closer K-Atlas matching, and stronger downstream end-to-end driving performance than data-curation baselines, including seamless adaptability to novel domains via city-to-city expansion.

---


### 61. [Similarity All The Way Up: Multilingual Generalization in LLMs Relies on Language-Level Similarity Structures](https://arxiv.org/abs/2607.22699)

**<font color=#1a73e8>作者：</font>** Supantho Rakshit, Adele Goldberg, Henry Conklin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) grow more capable across diverse tasks, their (in)ability to generalize remains difficult to quantify and poorly understood beyond limited domains. In particular, LLMs are known to struggle generalizing multilingually, to languages outside of English, and that are poorly attested in their training data. To understand why this may be, and what enables some models to perform better than others, we turn to a long history of work across the cognitive sciences, arguing that successful generalization derives from appropriate representations in similarity space. We look at how well LLMs' representations capture the hierarchical similarity structure between distinct languages. Strikingly, we show LLMs' latent representations largely recover the hierarchical structure of the Indo-European language family tree -- grouping languages that are members of the same subfamily closely together in representation space. Furthermore, we show that the degree to which models reflect the similarity structure of languages correlates with their performance on XNLI, a multilingual natural language inference benchmark. This extends classic work on similarity-driven generalization at scale, showing how models that represent similar languages similarly generalize better from one language to another.

---


### 62. [MIME: Multimodal Interactive Motion Encoder](https://arxiv.org/abs/2607.22702)

**<font color=#1a73e8>作者：</font>** Addison Zucek, Prerit Gupta, Kamila Kuatova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-motion representation learning has advanced rapidly, with growing interest in multi person interactions for animation, AR/VR, and embodied AI. These settings require representations that align language with both individual actor dynamics and the relationships between actors. We introduce the Multimodal Interactive Motion Encoder (MIME), which, to our knowledge, represents the first dedicated multimodal encoder designed specifically for two person interactive motion. MIME captures individual and shared structure using stream based co-attention with explicit interaction features and curriculum based contrastive training. On Inter-X text-motion retrieval, MIME consistently outperforms early and late fusion baselines across gallery sizes, achieving a 12.8% relative improvement in text-to-motion R@1 at a 2,000-sample gallery. We further evaluate MIME as a frozen auxiliary prior within TIMotion and InterMask on the unseen InterHuman dataset. MIME improves semantic alignment metrics while maintaining comparable FID in TIMotion. These results show that interaction aware multimodal encoding improves multi person motion retrieval and transfers across datasets to support downstream motion generation.

---


### 63. [MPR-CiteG: Enhancing RAG with Multi-Portfolio Retrieval and Citation-Grounded Generation](https://arxiv.org/abs/2607.22706)

**<font color=#1a73e8>作者：</font>** Hyewon Lee, Minkyung Song, Junghyun Oh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents the MPR-CiteG framework, which achieved second place in the ScienceON AI Challenge by addressing two fundamental challenges in generative AI: inefficient retrieval and the absence of source verification. We propose a dual-component system, termed MPR-CiteG, in which the Multi-Portfolio Retriever (MPR) efficiently retrieves diverse and relevant information, while the Citation-Grounded Generation (CiteG) module ensures that every generated output remains factually consistent and explicitly attributed to its source. MPR-CiteG represents a significant step toward building more trustworthy and accurate LLMs that are not only capable of generating information but also of grounding their responses in reliable evidence, thereby mitigating common issues like model hallucination. Extensive experiments on the challenge dataset validate the effectiveness and reliability of our approach. Our code is available at this https URL.

---


### 64. [StepX-Edge: An On-Device UI Vision-Language Model via Architecture-Training-Deployment Co-Design](https://arxiv.org/abs/2607.22708)

**<font color=#1a73e8>作者：</font>** Yin Wang, Haotian Hu, Jineng Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying a vision-language model with full UI understanding on end devices has long been trapped between accuracy and efficiency: on one side is the accuracy bar for OCR, screen understanding, visual question answering, and element grounding; on the other is the strict compute, memory, and power budget of mobile chips. Existing work either trades one for the other, or stops at simulation without real-device validation. We present StepX-Edge, a 0.9B-parameter on-device UI vision-language model that resolves this tension through three-layer co-design of architecture, training, and deployment. Architecturally, UI-aware Layered Visual Encoding (ULVE) and a Progressive Dimensionality Projection (PDP) connector target the extreme aspect ratios and fine-grained perception of screens, while standard full attention throughout ensures native compatibility with mainstream mobile NPU operators. For training, the five-stage StepX-Curriculum framework is designed around our observation of mutual-promotion effects among UI subtasks, so that all four capabilities grow synergistically under a tight parameter budget rather than interfering. For deployment, a module-wise differentiated two-stage PTQ-to-QAT quantization scheme keeps the post-quantization accuracy loss within 1%. StepX-Edge achieves the strongest overall UI understanding among <=1B models, surpassing all 2B-2.3B baselines on ScreenQA (88.76 F1) and Chinese OCRBench v2 (57.25), and matching 1.3B-2.3B general VLMs on RefCOCO (92.0%) and OCRBench v1 (831) with far fewer parameters. After W4A16+KV8 quantization, the model runs stably on Snapdragon 8 Gen5 devices with ~0.84 s TTFT, 98 tok/s decode, and 1.4 GB peak memory. We will open-source the training data, the full training recipe, and the quantization deployment pipeline.

---


### 65. [RMS@CC-MMD 2026: Multimodal Misogyny Detection via Geometric Interaction and Multi-View Consensus](https://arxiv.org/abs/2607.22709)

**<font color=#1a73e8>作者：</font>** Md. Ajwad Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of internet memes has introduced new complexities to automated content moderation, particularly in detecting misogyny. Memes often rely on a semantic clash between visual and textual modalities, where hateful intent is implicit and culturally grounded. This paper presents GeoMVC (Geometric Interaction and Multi-View Consensus), developed for the CC-MMD Grand Challenge at ICMI 2026. To address the limitations of static feature concatenation, a Geometric Interaction Layer is proposed that models cross-modal alignment via Hadamard products and cosine similarity between frozen visual and textual embeddings. We further mitigate distribution shifts caused by noisy OCR and code-mixed transliteration through a Multi-View Consensus strategy, aggregating predictions across raw, length-filtered, and English-translated text views. The system achieved Rank 2 in the Malayalam partition (Macro F1: 0.892) and Rank 3 in the Chinese partition (Macro F1: 0.895) on Task A, while securing Rank 5 in the Tamil partition (Macro F1: 0.521). A detailed error analysis on the development partition highlights open challenges in modeling localized transliteration and code-mixed sarcasm across Dravidian and Chinese cultural contexts.

---


### 66. [CORVUS: Context Optimization and Reduction Via Underlying Synchronization for LLM Coding Agents](https://arxiv.org/abs/2607.22711)

**<font color=#1a73e8>作者：</font>** Mingwei Zheng, David OBrien, Siwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM coding agents operate by constructing trajectories that accumulate reasoning, tool calls, and results to enable multi-step decision-making. However, the conventional append-only trajectory architecture found in practice tightly couples file-read actions with their observations, capturing snapshots that become permanently fixed in the chronological history. As files change through agent edits or concurrent human modifications, these snapshots become stale, causing reasoning errors and causing agents to redundantly re-read files, with each re-read appending yet another copy to the trajectory. To mitigate this, we propose CORVUS, a novel trajectory architecture that decouples file-read actions from their observations by maintaining a synchronized registry of relevant files and injecting only their current contents at each reasoning cycle. This structural change produces significantly lighter-weight trajectories that remain synchronized with the actual codebase state by construction, eliminating redundant file copies and stale snapshots that bloat conventional trajectories. We evaluated CORVUS on SWE- POLYBENCH_VERIFIED and SWE-BENCH PRO across four LLMs, achieving 9-50% reduction in average input tokens per task, 15-32% shorter final prompts, and up to 37% fewer reasoning cycles while maintaining comparable pass rates.

---


### 67. [scMIR: a vision-language foundation model for single-cell light microscopy image representation](https://arxiv.org/abs/2607.22712)

**<font color=#1a73e8>作者：</font>** Yifan Shang, Jiahui Tan, Xiangxiang Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-cell light microscopy images have become an important data source for characterizing cell phenotypes, but their complexity and heterogeneity pose challenges to high-throughput automated analysis. Existing representation learning methods mostly rely on task-oriented modeling, which is limited by specific datasets and predefined tasks, making them difficult to generalize across different cell types and microscopy modalities, and experimental conditions. Although general-purpose methods have improved the generalization ability of image representation in recent years, their limited utilization of experimental background and biological context information still poses challenges in complex phenotypic analysis. Here, we propose scMIR, a vision-language foundation model for single-cell light microscopy image representation. By synergistically combining self-supervised image reconstruction with text-guided cross-modal alignment, scMIR can simultaneously encode morphological and biological semantic information in a unified representation space. scMIR is pre-trained on 207,957 image-text pairs, covering various cell types, microscopy modalities, and perturbation conditions. scMIR outperforms existing general models and task-oriented methods as systematically evaluated on various complex tasks using 16 benchmark datasets, including cell classification, clustering, phenotype inference, and batch effect correction tasks. Furthermore, scMIR shows a strong generalization ability across various tasks without requiring task-specific fine-tuning. With its unique advantages, we envision scMIR may promote the standardization and automation of high-throughput phenotyping workflows through supporting various downstream analysis tasks.

---


### 68. [Visual Token Compression Enhances Robustness of MLLMs](https://arxiv.org/abs/2607.22716)

**<font color=#1a73e8>作者：</font>** Shishen Gu, Jiequan Cui, Wenbo Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we show for the first time that visual token pruning enhances the robustness of Multimodal Large Language Models (MLLMs), mitigating vulnerabilities such as jailbreak attacks and hallucinations. Given that vision and language modalities cannot be perfectly aligned, the misaligned visual tokens might act as out-of-distribution (OOD) inputs, leading to unpredictable outputs and introducing potential vulnerabilities. Building on this insight, we aim to enhance model robustness against jailbreaks and hallucinations by reducing OOD visual tokens at robust-pruning layers, while also reducing inference cost as a side benefit. Specifically, we measure the distance between each visual token and the language feature space. Then, visual tokens with large distances are identified as OOD tokens, which can be iteratively pruned. To demonstrate the effectiveness of our method, we evaluate it on seven diverse popular benchmarks. Notably, our method yields an average improvement of 13.29\% in defending jailbreak attacks, consistently achieves competitive performance in mitigating hallucinations, and maintains strong results on general datasets like MME.

---


### 69. [CausalGate: Causal Importance Distillation for Transformer Module Pruning](https://arxiv.org/abs/2607.22720)

**<font color=#1a73e8>作者：</font>** Kiran Nair, Smriti Regmi, Rodrigue Rizk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing adaptive inference methods for Large Language Models rely on observational heuristics, such as hidden-state similarity or activation magnitudes, to drop redundant modules. However, these correlation-based metrics often fail to capture subtle, non-linear structural computations vital for semantic accuracy. We introduce CausalGate, an intervention-guided framework for compute-efficient transformer inference. During a calibration phase, CausalGate isolates individual Attention and MLP sub-layers, zeros out their respective outputs, and measures the exact semantic damage via the Kullback-Leibler divergence of the final logit distribution. To eliminate runtime routing overhead, this structural importance hierarchy is distilled into a global set of static, lightweight scalar gates using an Exponential Moving Average smoothing objective paired with a differentiable pairwise ranking loss. Evaluated on TinyLlama-1.1B, Qwen2.5-3B, and Llama-3.1-8B across language modeling and commonsense reasoning benchmarks, CausalGate consistently outperforms prominent dynamic routing and layer-skipping baselines, translating theoretical compute savings into concrete hardware latency reductions with zero operational overhead.

---


### 70. [Visual Information Extraction from Documents via Classification-Guided Large Vision-Language Models](https://arxiv.org/abs/2607.22723)

**<font color=#1a73e8>作者：</font>** Huafu Li, Guo Chen, Jia Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual information extraction (VIE) from visually rich documents remains challenging due to high layout variability and real-world impairments. Existing methods typically rely on sequential OCR pipelines or end-to-end models requiring extensive labeled data and layout-specific training, limiting their this http URL propose a classification-guided large vision-language model (LVLM) framework for multi-type VIE that achieves high accuracy with minimal supervision. The approach decouples document-type classification from content extraction and employs in-context learning (ICL)-based dynamic prompt engineering to inject task-specific knowledge, enabling robust zero-shot inference across diverse layouts. From a theoretical perspective, the proposed method can be viewed as a form of conditional computation that reduces task uncertainty and improves information efficiency during prompt-based inference. Evaluated on a real-world bidding dataset with 16 certificate types, our zero-shot method (based on Qwen2.5-VL-7B) outperforms a strong supervised baseline by 18.35 percentage points in F1-score (86.43\% vs. 68.08\%) and 0.23 in normalized edit distance (0.90 vs. 0.67). Optional domain-specific fine-tuning further improves performance to 93.65\% F1 and 0.93 NED, demonstrating superior robustness against seals, watermarks, and low contrast. The framework offers an efficient, scalable solution for complex document understanding in office automation. Code is available at this https URL, and fine-tuned models at this https URL.

---


### 71. [Progress-conditioned Group Policy Optimization for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2607.22724)

**<font color=#1a73e8>作者：</font>** Kaibing Yang, Guangfeng Cai, Shengtian Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based policy optimization has been increasingly used to train large language model (LLM) agents from sparse outcome rewards by comparing trajectories or steps within a group. However, on difficult long-horizon tasks, this comparison can suffer from a sampling imbalance: repeated or low-effect actions dominate the high-probability region of the policy while useful state-changing actions remain under-sampled. This imbalance produces many all-failed rollout groups, where outcome rewards provide no direction for correcting the policy. Together, these effects can form a self-reinforcing credit trap: failure-dominated sampling yields no outcome-based correction, allowing repeated low-effect actions to persist. To break this loop, we propose Progress-conditioned Group Policy Optimization (ProGPO), which uses first-visit observation coverage only when all samples in a group receive zero outcome reward. Specifically, within such groups, ProGPO assigns higher relative advantages to trajectories or steps that visit more new states since reaching new observations is a prerequisite for task success. Experiments on two challenging agentic benchmarks, ALFWorld and WebShop with Qwen2.5-1.5/7B-Instruct, show that ProGPO consistently improves over group-based baselines, with particularly large gains on hard tasks.

---


### 72. [PCA: Persistence-Aware Compression and Aggregation for Fast Video Large Language Models](https://arxiv.org/abs/2607.22726)

**<font color=#1a73e8>作者：</font>** Zihan Song, Shuo Ye, Bo Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in Video Large Language Models (VLLMs) that have displayed promising outcomes in video understanding, the redundancy in the long-duration frames remains a hindrance to efficient reasoning. This paper introduces a training-free $\mathbf{P}$ersistence-Aware $\mathbf{C}$ompression and $\mathbf{A}$ggregation (PCA) method designed to preserve high-fidelity raw visual information before the encoding stage. PCA can be built on arbitrary VLLMs and consists of two modules: 1) A Dynamic Downsampling (DD) module that adaptively removes redundant frames by analyzing frame-wise similarity. 2) A Persistence-Aware Motion Enhancement (PAME) module that enriches each selected keyframe by aggregating the temporal context of its neighbors, ensuring that essential information is preserved even after aggressive frame reduction. Our approach substantially reduces the computation of long-context modeling, while enhancing the performance of the baseline model. Extensive experiments demonstrate that PCA consistently outperforms existing state-of-the-art approaches in both efficiency and accuracy, achieving a speedup of 1.8$\times$ to 2.5$\times$ compared to the baseline VLLM. The code is open-sourced at this https URL.

---


### 73. [Open Your Model's Eyes: Video and Context-Aware Multimodal Backchannel Prediction](https://arxiv.org/abs/2607.22729)

**<font color=#1a73e8>作者：</font>** Min-Jae Kim, Jun-Yeong Moon, Mujeen Sung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Backchannels, which signal listener states like empathy and understanding, are fundamental to natural human interaction. However, current approaches rely solely on audio and text. This omits crucial visual cues, such as facial expressions and gestures, as well as broader conversational contexts, which are necessary for accurate prediction. In this paper, we introduce Context-Aware Multimodal Alignment for Backchannel Prediction (CAMA-BC), a novel framework that leverages visual information through Multi-Layer Multimodal Alignment (MMA). Our alignment process comprises two stages. First, Context Alignment (MMA-CA) utilizes unlabeled dialogues with videos to capture conversational contexts. Next, Backchannel Alignment (MMA-BA) fine-tunes the representations specifically for backchannel prediction. Experimental results show that CAMA-BC significantly outperforms both existing methods and simple multimodal baselines, with particular effectiveness in recognizing complex backchannels such as empathy.

---


### 74. [Spatial Reasoning in LLM Game Agents: Impact of Causal Context and Multi-Step Planning](https://arxiv.org/abs/2607.22732)

**<font color=#1a73e8>作者：</font>** Mohit Jiwatode, Ronja Fuchs, Robin Schmöcker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based game agents often perform poorly on more complex tasks. This work examines whether these failures are linked to limited spatial reasoning and evaluates whether causal prompt augmentation and multi-step planning can improve win-rates while managing response latency. Using the open-source Qwen3 model family, we conduct experiments across varying model scales, reasoning modes, and planning horizons. We further introduce a focused GVGAI benchmark consisting of three custom games with five difficulty levels to isolate spatial navigation. The evaluation follows two paradigms: an initial ``positioning experiment'' to test an agent's ability to find its exact coordinates, and a study of game-play success. Our results show that while larger models with an enabled thinking mode identify their positions more accurately, overall performance in coordinate matching remains limited for smaller models. Win rates decrease as game levels and layout complexity increase, validating the benchmark's difficulty scaling. Integrating causal context into the prompts tends to improve the agents' success rates, particularly for bigger models. While enabling thinking mode and longer planning horizons significantly improve performance, multi-step planning further reduces mean per-step response times, offering a practical trade-off between reasoning depth and execution speed.

---


### 75. [AI-generated Images Challenge Visual Trust in High-risk Scenarios](https://arxiv.org/abs/2607.22745)

**<font color=#1a73e8>作者：</font>** Yi-Zhi Wang, Yichen Xiao, Linan Yue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advances in image generation are eroding the evidentiary value of visual content in settings where authenticity can affect public safety and personal reputation. Yet existing detection benchmarks rarely examine synthetic images in public- and individual-safety contexts, where misleading visual content may carry substantial risks. Here we introduce SafeIMG, a safety-oriented benchmark spanning 12 public- and individual-safety scenarios generated using GPT Image 2. Unlike benchmarks centred on generic imagery and image-level labels, SafeIMG evaluates not only whether detectors recognise synthetic images, but also whether their decisions reflect human-identified anomalies. To this end, SafeIMG provides human annotations that localise suspicious regions and explain local artefacts and higher-level commonsense or physical inconsistencies. We evaluate specialized synthetic-image detectors and vision-language models (VLMs), and find that neither provides reliable detection. The strongest VLM identifies only 49.5% of generated images, whereas the best specialised detector identifies 33.1%, compared with 81.7% accuracy for human evaluators. Model explanations cover only 29.8\% of human-annotated anomalies and predominantly capture local defects in text, faces and hands. Their coverage falls to 15.0% for commonsense conflicts and 12.0% for physical inconsistencies, while detection performance deteriorates further after dissemination-induced image degradation. These findings show that current detectors lack the accuracy, explanatory alignment and robustness needed to evaluate AI-generated images reliably across public- and individual-safety settings.

---


### 76. [Hierarchical Grading in Large Language Models](https://arxiv.org/abs/2607.22757)

**<font color=#1a73e8>作者：</font>** T. Shaska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Graded Large Language Models (GLLMs), an algebraic framework that equips the representation space of a transformer with a grading and propagates the induced weighted scalar action through embeddings, self-attention, and the training objective. The construction extends the theory of graded neural networks and graded transformers to autoregressive language models while preserving expressive power, asymptotic computational complexity, and inference cost.
The governing geometric picture is that of geometric invariant theory. The benefit of a grading is expressed by a Kempf--Ness functional on the grading torus; the grades that improve upon the uniform architecture form an open convex cone whose membership is decided by a Hilbert--Mumford-type criterion pairing a grade direction against two measurable profiles of the target and the data; the optimal grades are the coincidence point of two moment maps, given in closed form; and the ordinary transformer appears as a semistable isotropic point on the boundary of the cone: one member of a larger graded family rather than a distinguished optimum.
Separately, for level-stratified targets we prove a minimax separation between the graded prior and its absence: over all estimators the risks of the graded and uniform target classes separate throughout an explicit window of sample sizes, by a factor that decays exponentially in the number of levels under geometric stratification. Both profiles are estimable offline, so the optimal grades solve a convex program certified before training begins. Because the grading is absorbed into the learned parameters after training, every GLLM compiles to a standard transformer of identical architecture and inference complexity.

---


### 77. [Spectral Dynamics of Semantic Drift in Clinical Multi-Agent Language Model Networks](https://arxiv.org/abs/2607.22758)

**<font color=#1a73e8>作者：</font>** Amritesh Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The integration of iterative LLMs within multi-agent diagnostic frameworks requires a rigorous quantitative reevaluation of underlying communication topologies. Frequently used architectural paradigms depend on scale-free or small-world networks, assuming optimal communication efficiency. Our study mathematically dismantles that assumption for semantic data. By mapping multi-agent communication uncertainty trajectories onto a 768-dimensional Bio_ClinicalBERT embedding space via an analytical isotropic variance proxy using Barab'asi--Albert (BA) and Watts--Strogatz (WS) networks, we prove that structural bottlenecks compromise diagnostic safety. Our phase transition matrices illustrate that localized dense cliques confine hallucinated data, preventing global consensus and forcing the system toward a permanent entropy saturation threshold of $H_{\infty} \approx 5.947$. As a result, we measure a severe terminal cosine similarity degradation of 53.29%, completely overwriting the original ground-truth. Moreover, the terminal semantic drift reveals a catastrophic variance amplification of 51.81% ($\rho = 1.5181$) in highly clustered architectures, proving total system unpredictability when compared to Erdős--R'enyi configurations ($\rho = 1.0766$). Instead of reducing errors, hub-centric systems autonomously compound localized hallucinations. By introducing dynamic spectral monitoring operating at an $\mathcal{O}(N^3)$ time complexity and imposing a strict lower bound on algebraic connectivity ($\lambda_{2_{min}}$) via the continuous eigen-decomposition of the graph Laplacian, we present a mathematically rigorous technique to ensure global state diffusion. Securing the reliability of autonomous medical diagnostics necessitates treating topological stability as a non-negotiable quantitative imperative.

---


### 78. [Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation](https://arxiv.org/abs/2607.22766)

**<font color=#1a73e8>作者：</font>** Yunting Song, Matthew Watson, Peter Grabowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The alignment of Large Language Models (LLMs) is increasingly bottlenecked by data quality. As datasets scale, massive preference and instruction-tuning corpora inevitably accumulate hidden structural contradictions, safety risks, and systemic human annotation errors. Standard dataset auditing methods, such as semantic deduplication or LLM-as-a-judge, struggle to capture the actual predictive impact of individual records and often miss deep functional rule clashes. To address this, we introduce a scalable, inference-only data valuation pipeline that approximates the Shapley value without iterative model retraining. By mapping semantic k-NN neighborhoods into a directed graph, our framework evaluates data utility directly through a reference LLM's probability distribution using zero-shot and one-shot conditional log-likelihood shifts. Our pipeline then translates these predictive influence scores into localized advantage metrics to isolate gradient-conflicting records. We demonstrate the pipeline's efficacy in sanitizing two heavily vetted alignment datasets. First, applying our pipeline to the HelpSteer2 dataset reduced the manual audit search space by 99.1%, successfully uncovering falsely-labeled records across diverse failure modes. Second, applying our automated audit strategy to Anthropic's HH-RLHF training and evaluation splits identified thousands of hidden safety and factual preference inversions. Crucially, by extending this audit to the evaluation split, we expose severe vulnerabilities in current benchmark integrity: highly capable models frequently predict the safer or more helpful response, only to be penalized by objectively flawed human ground-truth labels. Overall, our work provides a mathematically grounded, highly efficient diagnostic tool to uncover human label failures, sanitize evaluation benchmarks, and ensure the integrity of LLM alignment data.

---


### 79. [DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning](https://arxiv.org/abs/2607.22769)

**<font color=#1a73e8>作者：</font>** He Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training efficacy of large language models (LLMs) is fundamentally constrained by the quality and composition of training data. Existing dynamic data scheduling methods face critical limitations in industrial-scale pretraining and supervised fine-tuning (SFT): data selection incurs prohibitive O(N) costs on terabyte-scale corpora, mixture optimization schemes introduce severe I/O bottlenecks or require training auxiliary reference models, and sample-level reweighting strategies rely on loss signals that conflate noise, difficulty, and novelty.
We present DomainPilot, a domain-level loss-guided two-stage data mixture optimization framework. DomainPilot introduces token-level domain loss monitoring to capture per-domain learning dynamics during training without halting the data pipeline. Building on these signals, we propose a Scaling Law guided coarse optimization stage that fits domain-specific convergence curves and derives a principled prior for mixture adjustment. A subsequent Mixing Law guided fine optimization stage refines the mixture by modeling cross-domain interaction effects through controlled sweep experiments. The entire mechanism is realized via a patch-based architecture that injects domain-aware loss computation into existing training frameworks (e.g., MindSpeed/Megatron-LM) with only ~30 lines of framework-specific adapter code.
We validate DomainPilot on the Qwen3-1.7B model during SFT. Compared to the original data mixture, our optimized mixture achieves improvements of +2% on MMLU-Redux, +1.8% on AIME24, +3.8% on LiveCodeBench v5, and +3.6% on BFCL v3, without increasing total data volume or training cost. These results demonstrate that domain-level training signals provide an effective, lightweight alternative to expensive data selection or auxiliary model training for mixture optimization.

---


### 80. [Cheap Probes Predict Expensive Training in 3D-CT Vision--Language Models](https://arxiv.org/abs/2607.22771)

**<font color=#1a73e8>作者：</font>** Renjie Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Picking the frozen image encoder for a 3D~CT vision--language model (VLM), together with the token-compression scheme on top of it, is a search over many candidates. There are several encoders, several ways to compress their tokens, and several token budgets, and the combinations grow fast. Comparing them the usual way means fine-tuning a large language model (LLM) on each combination, and running the whole sweep this way needs far more compute than most groups can spend. We ask whether a cheap probe on the encoder's cached embeddings can stand in for that comparison. We build an image-grounded probing benchmark over (encoder $\times$ compression) cells, with clinical attribute families and two validation gates, scale-sanity and probe-separability, that keep each attribute well-scaled and decodable. These gates are the main methodological contribution. On this benchmark we compare a range of read-out heads, and in a preliminary study we pair each probe with its matched downstream task. The early signal is encouraging: the cheap probe orders the candidates in close agreement with expensive fine-tuning, at about $r\approx0.95$ on the cells measured so far. We read this as an ordinal claim, a ranking predictor rather than an exact estimate, and we are explicit about where it stays preliminary. If it holds up, encoder and compression choices can be screened in minutes with frozen-token probes, with full training spent only on the finalists.

---


### 81. [Multimodal Surface EMG Hand Gesture Recognition Using Query-Based Transformers for Prosthetic Control](https://arxiv.org/abs/2607.22779)

**<font color=#1a73e8>作者：</font>** Federico Del Pup, Elisa Tentori, Manfredo Atzori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hand gesture recognition via surface electromyography (sEMG) is fundamental to prosthetic control. In this field, deep learning approaches have become the gold standard. However, current architectures struggle to scale; model performance typically decreases as the number of hand movements increases. Performance degradation is tied to the increased statistical complexity of decoding expanded gesture sets and compounded by the limitations of state-of-the-art methods, which primarily rely on low-latency unimodal convolutional architectures. Convolutions operate locally, limiting model's ability to capture long-range sequential patterns. Unimodal setups cannot leverage complementary information from coordinated signals characterizing movement execution, such as inertial and eye-tracking data. These limitations motivate architectures that integrate local and global features across multimodal physiological sequences. To bridge this gap, this study introduces EMG-CrossFormer, an end-to-end hybrid convolutional-transformer for seamless multimodal integration. EMG-CrossFormer combines representations from an arbitrary number of unimodal encoders through cascaded cross-attention fusion layers, and decodes the fused representations using learnable gesture queries. EMG-CrossFormer was evaluated on four NinaPro datasets (DB2, DB3, DB7, and DB10) and benchmarked against six state-of-the-art models using an increasing number of modalities. Using only sEMG, EMG-CrossFormer achieved mean accuracies of 72.33%, 52.48%, 79.16%, and 73.49% on DB2, DB3, DB7, and DB10, respectively. Incorporating inertial signals improved performance to 90.66%, 80.40%, 92.79%, and 92.06%. These results show that joint local-global feature modeling improves sEMG-only decoding and that multimodal fusion substantially amplifies this benefit, underscoring the value of both design principles for complex hand gesture recognition.

---


### 82. [Multimodal Domain Generalization for Depression Detection: An Attention-Based BiLSTM Network with Domain-Adversarial Training](https://arxiv.org/abs/2607.22794)

**<font color=#1a73e8>作者：</font>** Ali Tabaraei, Federico Simonetta, Stavros Ntalampiras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic depression detection with deep learning has shown promise but often suffers from limited generalization due to domain shift arising from inter-speaker variability. To address this critical issue, we present the first patient-independent multimodal depression detection framework that incorporates domain generalization (DG), jointly leveraging both acoustic and textual modalities. The proposed model integrates bidirectional Long Short-Term Memory (BiLSTM) with intra- and cross-modal attention mechanisms, accompanied by segment-level fusion for decision-making. Generalization is further enhanced by applying a gradient reversal layer inspired by Domain-Adversarial Training of Neural Networks (DANN), which promotes domain-invariant representations by adversarially limiting the model's ability to identify individual speakers, effectively reducing patient-specific bias. Conducting experiments on the Androids-Corpus dataset with a 5-fold cross-validation (CV) protocol, various pairings of audio and text feature extractors were evaluated over different segment durations, determining MelSpec and ItalianBERT as the optimal baseline at a 30-second segment duration. The addition of DG to this baseline yields a 2.5% increase in accuracy and 3.3% in F1-score, achieving 93.2% accuracy, 93.2% precision, 96.2% recall, and 94.2% F1-score, surpassing all existing benchmarks. Extensive ablation studies assess the impact of multimodal fusion, deep architectural choices, and DG, highlighting their combined contribution to robust and generalizable depression detection.

---


### 83. [Physically Verifiable Evidence and LLM-Based Reporting for Bearing Fault Diagnosis](https://arxiv.org/abs/2607.22797)

**<font color=#1a73e8>作者：</font>** Yuntong Chen, Jianyu Liu, Guobin Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trustworthy deployment of AI-based diagnosis in safety-critical mechanical systems hinges on validation: whether a prediction can be checked against physical reality before it is acted upon. Current intelligent fault diagnosers fail this standard in two ways. Their standard output, a class label with a softmax confidence score, is an internal statistic of the classifier, offering nothing checkable against independent physical knowledge; and the growing use of generative language models in maintenance reporting adds a second risk: hallucinated content entering reports on which decisions rest. Taking bearing fault diagnosis as the testbed, this work addresses both problems from the output side. The proposed Diagnostic Evidence Network (DENet) is an encoder-agnostic multi-task framework extending the output to a structured evidence record: the classification, a predicted characteristic frequency comparable against the theoretical value determined by bearing geometry and shaft speed, and a temporal localization of transient impulses inspectable on the raw waveform. Across four encoders and three public datasets, this evidence incurs no statistically significant accuracy cost, with a frequency error of about 6 Hz on 1,024-point segments where spectral estimation is structurally inapplicable. Centrally, the deviation between predicted and theoretical frequency constitutes a label-free, inference-time validation signal: it detects misclassifications with AUROC values of 0.970 and 0.871, and remains discriminative in the high-confidence regime where confidence-derived detectors are blind. Finally, a QLoRA-adapted language model is constrained to translate, but never generate, diagnostic content, reducing unsupported-claim rates from 10-12% to 2% and eliminating fabricated quantities.

---


### 84. [Frustratingly Simple Black-Box Adaptation of Language Models via Logit Bias](https://arxiv.org/abs/2607.22837)

**<font color=#1a73e8>作者：</font>** Ofek I. Cohen, Lior Shani, Aviv Rosenberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many organizations aim to adapt language models for internal use, both to improve performance on domain-specific tasks and to address privacy concerns around sensitive data. However, such adaptation remains non-trivial: it often requires operationally challenging fine-tuning of open-source models or ad hoc prompt optimization. We study a minimal alternative based on a simple API-level control: allowing users to bias the model's logits with a user-defined vector. We develop a black-box method for learning a single context-independent logit-bias vector, added at every decoding step, without modifying model weights or requiring gradients. Starting from a KL-regularized reinforcement learning (RL) objective, we characterize when such a fixed logit-bias vector can approximate the optimal prefix-dependent correction and derive a closed-form inverse-propensity estimator from rollouts, rewards, and token probabilities. Empirically, this simple decoding-time intervention improves over base models on mathematical and reasoning benchmarks while using far fewer trainable parameters than conventional fine-tuning. Our results suggest that learned logit bias is a lightweight mechanism for adapting language models under minimal access requirements.

---


### 85. [Robustifying pathology foundation models via fine-tuning](https://arxiv.org/abs/2607.22861)

**<font color=#1a73e8>作者：</font>** Alexandre Filiot, Oskar Thaeter, Benoit Schmauch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (FMs) produce powerful tile-level representations which remain sensitive to scanner and staining variability, undermining deployment across laboratories. We develop a novel fine-tuning recipe that improves the robustness of pathology FMs to acquisition factors. Applied to ten different FMs, our fine-tuning strategy consistently improves robustness for every model as well as downstream performance, with no observed trade-off. On average, it raises the PathoROB robustness index by 23% (from 0.72 to 0.87) and increases the overall cross-benchmark performance by 43% on Patho-Bench, HEST and THUNDER combined, with individual gains reaching up to 72% in robustness (Phikon-v2) and 76% in performance (Midnight-12k). We publicly release the fine-tuned versions of Phikon-v2 (Phaet) and Midnight-12k (Mascaret) at this https URL.

---


### 86. [Spatial-IQ: Deconstructing Spatial Intelligence via Hierarchical Capability Tests](https://arxiv.org/abs/2607.22864)

**<font color=#1a73e8>作者：</font>** Patrick Rim, Tom Long, Ekta Prashnani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) excel at visual interpretation but fail on spatial reasoning tasks that humans solve reliably. Existing benchmarks evaluate these models as black boxes, limiting their ability to identify the underlying causes of lower performance: when a model fails a spatial reasoning task, it remains difficult to ascertain whether the hurdle is perceptual, such as recognizing object boundaries, or cognitive, such as reasoning about occlusion to infer hidden geometry. We introduce Spatial-IQ, a hierarchical diagnostic framework that decomposes object counting in stacked 3D structures into 9 perceptual and cognitive sub-tasks organized by the developmental stages of human spatial cognition, with mental rotation as an additional target probe. Using NVIDIA Isaac Sim, we procedurally generated a diverse dataset of roughly 80,000 stacked 3D structures with per-task ground truth. We evaluate models across three output formats (free-response text, multiple-choice images, and image editing) alongside a human baseline. The Spatial-IQ framework shows that top-performing models often succeed at the target task (object counting) without succeeding on the lower-level sub-tasks intended to support it, and that models differ in how much of these hierarchical chains they preserve, often revealing shortcut behavior that raw target-task accuracy alone would obscure. Finally, we demonstrate that training models with chain-of-thought (CoT) supervision over our hierarchical sub-tasks, combined with reinforcement learning with verifiable rewards, significantly improves both spatial consistency across sub-tasks and target-task accuracy, supporting the value of the proposed decomposition as both a diagnostic tool and a training signal.

---


### 87. [Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams](https://arxiv.org/abs/2607.22917)

**<font color=#1a73e8>作者：</font>** Shouren Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have significantly improved coding and programming workflows. Claude Code, in particular, is one of the most powerful LLM coding agents and is capable of conducting complex coding tasks. However, several drawbacks can undermine long-term agentic workflows. (1) Irrecoverable agent teams: The Agent Teams feature is powerful, but the working state accumulated by each teammate is lost and cannot be resumed once the process stops, for example, when a terminal is closed. (2) Compaction erodes working detail: Compaction condenses the conversation into a summary, causing an agent's working details to become vague. (3) Agentic "technical debt": Over time, a user's decisions and the agents' operations become trapped in compacted old chats, making the project increasingly difficult to maintain and review. (4) Heavy prompt writing: Assigning or handing off tasks requires users to repeatedly write long prompts to achieve the expected agentic performance. We propose ATWZ (Agent Team Work Zone), a filesystem-based operations layer built around Claude Code's native Agent Teams that addresses these problems. Its central design principle is to treat each agent and teammate as a human employee and preserve their important working state in files stored in a dedicated directory called a "workstation," together with the skills, hooks, and scripts that use and maintain these files. With ATWZ, an agent team can periodically back up its working state, allowing an agent's knowledge to be recovered after compaction. After a process ends, the team can be restored with a single command. These features also substantially mitigate the agentic "technical debt" described above. Moreover, within ATWZ, agent "employees" can send documents to one another, greatly reducing the effort required to write prompts.

---


### 88. [Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/abs/2607.22925)

**<font color=#1a73e8>作者：</font>** Vatsal Baherwani, Tom Goldstein, Ashwinee Panda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A key question for AI safety is whether a language model expresses all of its reasoning in its output tokens. We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks. We evaluate 13 frontier language models across three tasks and find that many models benefit significantly from filler tokens, with accuracy improvements of up to 13 percentage points. The benefit depends on which tokens are used and differs across models. We further show that filler tokens enable Claude Opus 4.5 to satisfy a hidden modular arithmetic constraint without sacrificing accuracy on its primary task, demonstrating that invisible reasoning can serve objectives entirely invisible to CoT monitoring. Reinforcement learning gives Qwen3-235B strong preferences over filler token content, but neither RL nor supervised fine-tuning produces a filler token benefit that persists at test time. Our results indicate that frontier models already perform consequential computation with no interpretable trace in their output tokens.

---


### 89. [SAGE: Safety-First Defense-in-Depth Guardrails for Verified Lifecycle Control of High-Impact Generative AI](https://arxiv.org/abs/2607.22926)

**<font color=#1a73e8>作者：</font>** Mahdi Eslamimehr  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-impact generative AI makes catastrophic misuse a lifecycle-control problem, not merely a prompt-filtering problem. SAGE is a safety-first, authorization-separated architecture in which credible catastrophic-enablement risk constrains admissibility before utility, latency, or commercial objectives are considered. It combines signed release manifests, diverse detectors, robust risk envelopes, least-risk defaults, output checking, three-valued monitoring, protected audit chains, containment, and rollback. Formal results establish safety priority, conservative detector bounds, monotone release gating, tamper-evident records, and an authorization cut; two PRISM abstractions verify authorization separation and lifecycle invariants under explicit assumptions.
A frozen, vendor-symmetric study sent 84 cases to each of four GPT, four Claude, and two Gemini snapshots: 840 calls yielded 794 target responses, 46 provider errors, and 449 successful judgments covering 375 responses. Eight snapshots had complete judged domain coverage. Harmful-compliance estimates were low; variation arose mainly from benign utility and safe redirection. Seven multiplicity-adjusted contrasts involving Claude, Gemini, or GPT-5 snapshots and the GPT-5 mini and GPT-5 nano snapshots were supported, while no tested contrast between the Claude or Gemini snapshots and GPT-5 or GPT-5.5 survived correction.
The observed harmful-compliance range is a conservative, protocol-bound view from one generation per prompt with no tools, retrieval, history, or human adjudication; it is not an upper bound on operational assistance. A preregistered extension specifies how to test a wider best-worst gap using a locked split, repeated sampling, multi-turn and sandboxed-tool conditions, and domain-expert scoring.

---


### 90. [Toward Automated Detection of Documentation Inconsistencies in Electronic Health Records](https://arxiv.org/abs/2607.22954)

**<font color=#1a73e8>作者：</font>** Jian Lu, Panyu Chen, Miriam Treggiari 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective: To characterize the kinds of internal documentation inconsistencies a general-domain large language model (LLM) can surface from real-world discharge summaries, and to identify recurring failure modes that limit reliability at scale.
Materials and Methods: We applied a two-stage LLM pipeline---open-ended candidate identification (Gemini 2.5 Pro) followed by context-grounded verification (Gemini 2.5 Flash)---to 3,000 randomly sampled MIMIC-IV-Note discharge summaries. A subset of the pipeline output was then reviewed manually by clinical experts.
Results: Our pipeline surfaced 3,460 candidate inconsistencies, affecting 69.7% of admissions. Representative examples spanned demographics, allergies, procedures, diagnoses, laboratory, medications, and care-planning domains, with direct implications for clinical reasoning or patient safety. Expert review also revealed recurring failure modes that arise when verification requires temporal reasoning, evolving-diagnosis context, or knowledge of outpatient-prescribing conventions the model does not natively possess.
Discussion: Detection is highly context-dependent: many flagged pairs require anchoring each statement to its source section and clinical domain, then assessing whether the conflict reflects a true contradiction or missing context. We propose a graded ontology spanning strict contradiction and ambiguity, with a schema characterizing each flagged case by category, section, domain, and inconsistency axis.
Conclusion: This formative study establishes a methodological foundation and conceptual framework to guide subsequent validated, large-scale EHR-inconsistency analysis.

---


### 91. [ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control](https://arxiv.org/abs/2607.22962)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Shibo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that operate over many turns accumulate facts in an external memory store and reuse them as premises for downstream reasoning. A hallucinated fact written at one step therefore persists as a false premise for every subsequent step, a failure mode we call memory contamination. Existing memory management addresses retrieval and capacity but not write-time correctness; this admission problem cannot be solved by utility- or recency-based criteria, and uncontrolled contamination compounds across long trajectories. We propose ConsistencyGate, a write-time admission gate that, before committing a candidate fact m extracted from context c, queries the LLM K times for a soft support score and admits m only when the average exceeds a threshold. The mechanism is model-agnostic, requires no fine-tuning, and reduces to a single forward pass in a log-probability variant for latency-sensitive deployments. To measure the effect on natural data, we construct two real-conversation benchmarks (LoCoMo-Contam and MSC-Contam) by planting controlled single-detail corruptions in long-term conversations from LoCoMo and MSC, and complement them with a structured synthetic corpus (MemContam) that isolates a near-oracle upper bound. Across four LLM backbones, ConsistencyGate reduces contamination on every benchmark relative to a write-everything baseline, with the cost concentrated on facts that are stated only implicitly in the source context. We release all three benchmarks together with the gate implementation.

---


### 92. [Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning](https://arxiv.org/abs/2607.22996)

**<font color=#1a73e8>作者：</font>** Xiaokun Wang, Siyu Song, Wentao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed in educational settings often behave as direct answerers: they disclose target concepts in the opening turn instead of guiding students through progressive inquiry, as Socratic pedagogy prescribes. We present HeuristicEdu, a two-phase pipeline that aligns Qwen2.5-7B toward Socratic tutoring via supervised warm-up and Group Relative Policy Optimization (GRPO). Training uses SocraticEdu, 797 multi-turn Chinese children's science dialogues reconstructed from a live platform, with a heuristic reward over cognitive depth (R_cog), curiosity engagement (R_eng), and directness (R_dir), together with a K_query correction for student-introduced terms. We introduce Scaffolding Effectiveness (SE) and Conversation Depth (CD) to evaluate outcomes beyond surface fluency. On 30 held-out questions, the best GRPO variant improves SE from 30.0% to 63.3% and lowers keyword leakage from 30.0% to 13.3%. Notably, this best variant omits the directness penalty during optimization, suggesting that explicit anti-leakage terms can conflict with gradient-based behavioral alignment. An unaligned Qwen-72B baseline reaches 0% SE and 96.7% leakage, showing that scale alone does not induce Socratic behavior.

---


### 93. [Speech Signals Complement LLMs for Predicting Interpersonal Attraction in Speed Dating](https://arxiv.org/abs/2607.23037)

**<font color=#1a73e8>作者：</font>** Yuriko Kikuchi, Takato Hayashi, Ryusei Kimura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can predict interpersonal attraction from conversation transcripts, but it remains unclear what a speech predictor can add beyond transcript-only LLM prediction. Using Japanese speed-dating conversations, we combine predictions from a transcript-only LLM and a supervised speech predictor to estimate participants' reported liking of their partners. We show that speech can complement transcript-only LLM prediction, but that this complementarity is conditional rather than universal. Combining the two predictions significantly improves pairwise ranking accuracy over the transcript-only LLM alone in all evaluated conditions. By contrast, gains in per-participant Pearson $r$ vary across conversation rounds and rating directions, with none significant after correction. Retrospectively, these $r$ gains are concentrated among participants for whom the speech predictor is more accurate. Speech can therefore retain predictive value even when an LLM predicts attraction from transcripts. The relevant question is not simply whether speech helps, but where its complementarity emerges.

---


### 94. [Stress-testing large language model agents in a robotic chemistry laboratory](https://arxiv.org/abs/2607.23045)

**<font color=#1a73e8>作者：</font>** Lulu Guo, Yingkai Sun, Xiaobo Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI is evaluated through knowledge, reasoning and plan generation, yet scientific agency requires reliable physical action and adaptation to evidence. Here, we use a robotic chemistry laboratory as a physical-world testbed to make scientific agency measurable. Its 45 modular workstations exposed as machine-readable skills enabled 4,608 trials. Only 3.3% of trials produced expert-assessed executable workflows under laboratory constraints; even the best system achieved 28.1%. Long-horizon planning remained a challenge: only three executable workflows exceeded 30 operations, although the longest contained 44. Across five rounds, experimental feedback prompted local adjustments but no workflow-level replanning or analytical-method redesign. By making physical executability and evidence-driven replanning measurable, our study provides an evidence-based assessment of deployment readiness and a diagnostic framework to guide closed-loop improvements towards physically grounded autonomous research.

---


### 95. [Structured Redundancy Modeling for Efficient Visual Token Pruning in High-Resolution MLLMs](https://arxiv.org/abs/2607.23046)

**<font color=#1a73e8>作者：</font>** Jouwon Song, Woohyeong Kim, Kyeongbo Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent high-resolution Multimodal Large Language Models (MLLMs) generate thousands of visual tokens per input, leading to a visual token explosion that introduces severe latency bottlenecks. While token pruning mitigates this issue, state-of-the-art subset-optimization methods typically rely on iterative subset construction to jointly capture visual diversity and instruction relevance. As visual token counts scale, this sequential dependency introduces significant selection overhead, severely limiting the translation of theoretical FLOPs reductions into actual wall-clock speedups. To address this limitation, we propose Single-Forward Pruner (SFPruner), a structural reformulation of visual token pruning that embeds redundancy control directly into the scoring space, bypassing the need for iterative combinatorial optimization. Our non-iterative framework achieves redundancy-aware importance selection in a single forward pass through two complementary mechanisms. First, to attenuate redundancy at the covariance level, we introduce a semantics-guided ridge leverage scheme. By integrating instruction relevance and visual saliency, this mechanism suppresses dominant covariance directions and mitigates representation bias. Second, ranking-based directional masking resolves residual overlap through asymmetric similarity competition, where higher-scoring tokens explicitly suppress redundant lower-scoring alternatives via parallel tensor operations. Extensive evaluations demonstrate that our approach maintains stable selection costs, reducing the token selection process by up to 110 ms, from 112.4 ms to just 2.5 ms at 512 tokens in Qwen2.5-VL. This structural efficiency successfully translates theoretical token reductions into tangible inference speedups while preserving highly competitive performance against state-of-the-art techniques under aggressive compression.

---


### 96. [MixQuant: Adaptive Mixed-Precision Quantization for Large Language Models](https://arxiv.org/abs/2607.23047)

**<font color=#1a73e8>作者：</font>** Ashitabh Misra, Madhav Agrawal, Arham Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision quantization improves the accuracy of post-training quantization by allocating higher bitwidths to sensitive layers, but existing methods solve the allocation for a single fixed memory budget. In practice the budget varies across deployments and is unknown at calibration time. Adaptive quantization addresses this with one offline calibration that serves any budget, yet current methods score layer sensitivity in a manner that does not consider its dependency on quantization levels of other layers. We show that a layer's sensitivity depends strongly on the bitwidths of its upstream layers and that this dependence shifts the resulting preferred bit allocation. We propose MixQuant, a technique-agnostic adaptive framework that wraps any base quantizer. MixQuant marginalizes each layer's distortion over random quantized upstream configurations to obtain budget-agnostic scores, calibrates the quantizer's parameters on plans the allocator itself produces, and penalizes allocations that leave layers at the lowest bitwidths. A single greedy pass then serves any budget at deployment. Across Llama-3.2-3B, Llama-2-7B, and Mistral-7B under AWQ and GPTQ, MixQuant outperforms adaptive and mixed-precision baselines in every setting, improving average accuracy by up to 8 points and reducing perplexity from 12.43 to 10.70 at the tightest budget, while matching an ILP solver at negligible deployment cost.

---


### 97. [Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models](https://arxiv.org/abs/2607.23052)

**<font color=#1a73e8>作者：</font>** Sultan Alshehri, Zhantao Yang, Han Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-encoder vision-language models (VLMs) expose a similarity interface that enables zero-shot retrieval but fails compositional constraints: queries like "umbrella and no person" retrieve images containing both, even when concept detection is reliable. We trace this to an interface-level Bag-of-Concepts effect, where similarity scores approximate mean pooling of concept evidence regardless of operators. Although operator-dependent signals exist in text embeddings, they are too weak or misaligned to affect rankings. Fine-tuning does not reliably resolve this failure because the dominant bottleneck is how similarity aggregates evidence rather than what encoders represent. We propose factored inference, which separates evidence extraction from constraint execution, and introduce LCSE (Logic-Constrained Score Editing), a training-free method that executes constraints externally using concept scores from frozen encoders. We also introduce FACTOR-Bench, where LCSE achieves 85.5% accuracy versus 73.2% for the best fine-tuned baseline, 90.7% when applied to SigLIP 2, and improves NegBench COCO MCQ accuracy from 27.2% to 65.2% while preserving retrieval performance.

---


### 98. [Through the Bottleneck: How Multi-head Latent Attention Separates Content from Position in Language Models](https://arxiv.org/abs/2607.23054)

**<font color=#1a73e8>作者：</font>** Dhruvil S, Fenil Sojitra, Ravirajsinh Chauhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-head Latent Attention (MLA), introduced in DeepSeek-V2, compresses key-value pairs through a shared low-rank bottleneck (cKV), achieving 81% KV-cache reduction during inference. Despite its adoption in massive production models, no prior work has studied what information this bottleneck preserves or discards, nor how it reshapes internal transformer circuits. We present the first comprehensive mechanistic interpretability study of MLA, training a 114M-parameter transformer (pretrained on a web/code/math mixture, fine-tuned on TinyStories) and analyzing its representations through SVD, attention head taxonomy, linear probing, and a disruption-attribution analysis. Our key findings are: (1) the cKV bottleneck learns a pure content representation, preserving entity identity (98% retention) while discarding positional information, validating MLA's separation of content from position via RoPE; (2) induction heads co-locate at a single layer (Layer 12), unlike their distributed formation in standard MHA; (3) a single "semantic hub" layer (Layer 15) simultaneously exhibits the highest SVD effective rank and strongest disruption-attribution score; and (4) the bottleneck is globally over-provisioned, using only 46% of its capacity on average. These findings suggest MLA does not merely compress attention passively, but reshapes how the model organizes content, position, and circuit structure. We view this as an initial data point and detail scope limitations in Section 5.

---


### 99. [Touching or Chatting: The Utility of LLMs and Tactile Charts for Learning about Complex Chart Types by BLV Individuals](https://arxiv.org/abs/2607.23065)

**<font color=#1a73e8>作者：</font>** Tingying He, Maggie McCracken, Daniel Hajas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualizations are central to communicating data, yet blind and low-vision (BLV) people often lack support for understanding chart types---knowledge that is essential for interpreting new visualizations and collaborating with sighted peers. Prior work found that BLV individuals viewed example tactile charts as more helpful than text-only approaches and preferred them for learning advanced chart types, particularly for understanding spatial layouts and shapes. Meanwhile, large language models (LLMs) are increasingly used by BLV individuals for chart explanation and question answering (QA), but have been studied primarily for dataset exploration rather than chart-type learning. Existing LLM-based chart QA also shows that users frequently ask about layout and structure, yet struggle with spatial concepts and misdirect questions when mental models are weak. We investigate how LLMs influence chart-type learning and whether tactile learning improves subsequent LLM-supported exploration. We extend our tactile chart learning tools with an LLM chatbot that provides interactive explanations and supports follow-up questions. In an interview study with 12 BLV participants, we compare two learning formats: (1) a tactile chart, a textual explanation, and an LLM chatbot; and (2) a textual explanation and an LLM chatbot. The learning phase was followed by exploration of an unfamiliar dataset using alt text and an LLM. Thematic analysis shows that tactile templates support BLV participants' formation of chart-type mental models, which scaffolds subsequent LLM-mediated data exploration. Text+LLM explanations without tactile support show weaknesses for spatial-reasoning tasks.

---


### 100. [Attention-Guided Layer Selection for Contrastive Decoding in Large Language Models](https://arxiv.org/abs/2607.23067)

**<font color=#1a73e8>作者：</font>** Yusuke Sakai, Natthawut Kertkeidkachorn, Kiyoaki Shirai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contrastive decoding methods such as DoLa improve the factuality of Large Language Models (LLMs) by contrasting the output distributions of mature and premature layers. However, DoLa's dynamic layer selection relies solely on divergences in output vocabulary distributions. In this work, we propose three attention-guided strategies: Attention-JSD, Attention-Entropy-Max, and Attention-Entropy-Min, which leverage structural information carried by internal self-attention mechanisms as a signal for layer selection. Experimental results on TruthfulQA demonstrate that our strategies, particularly Attention-JSD and Attention-Entropy-Min, consistently outperform the original DoLa. We observe significant gains on multi-answer metrics (MC2 and MC3), suggesting that attention distributions can provide a more sensitive signal for resolving factual knowledge than output vocabulary distributions.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
