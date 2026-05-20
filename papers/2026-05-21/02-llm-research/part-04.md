# 🧠 大模型相关研究 | 2026年05月21日

> 本类共 **172** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-172**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-172**

---

### 151. [InterLight: Leveraging Intrinsic Illumination Priors for Low-Light Image Enhancement](https://arxiv.org/abs/2605.19982)

**<font color=#1a73e8>作者：</font>** Ziqi Wang, Xu Zhang, Laibin Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-Light Image Enhancement (LLIE) has long been a challenging problem in low-level vision, as insufficient illumination often leads to low contrast, detail loss, and noise. Recent studies show that deep learning-based Retinex theory can effectively decouple illumination and reflectance. However, existing methods frequently suffer from over-enhancement or color distortion, and often assume uniform noise or ideal lighting. To address these limitations, we propose InterLight, a novel framework that systematically excavates and operationalizes intrinsic illumination priors for this http URL core insight is that robust enhancement requires not just estimating illumination, but constructing an illumination-aware pipeline. We first inject sensor-level illumination-response priors via physics-guided augmentation, then represent the degradation through adaptive prompts conditioned on the scene's latent illumination state. This explicit representation directly guides a luminance-gated intrinsic memory mechanism to selectively compensate for information loss, prioritizing reconstruction in dark regions while preserving fidelity in bright ones. Finally, the entire process is regularized by a self-supervised consistency objective that distills illumination-invariant features. By deeply exploiting intrinsic illumination priors, our method achieves clearer textures and more visually coherent enhancement results. Extensive experiments across multiple benchmarks demonstrate the effectiveness of our approach. Code is available at: this https URL.

---


### 152. [LLM Benchmark Datasets Should Be Contamination-Resistant](https://arxiv.org/abs/2605.19999)

**<font color=#1a73e8>作者：</font>** Ali Al-Lawati, Jason Lucas, Dongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs. However, recent studies reveal that many benchmark datasets are included in pretraining corpora, i.e., $\textit{contaminated}$, which diminishes their value as reliable measures of model generalization. In this paper, we argue that benchmark datasets should be $\textit{contamination-resistant}$, i.e., $\textit{unlearnable}$, but support $\textit{inference}$. To accomplish this, we first highlight the wide prevalence of benchmark dataset contamination and outline the properties of contamination-resistant datasets. Second, we highlight how the asymmetry between the inference and training pipelines in the Transformer architecture can be leveraged to support contamination-resistance. Third, we outline mathematical advancements to make these datasets interoperable across various LLM architectures. Based on the above, we call on the community to ensure the reliability of LLM benchmarking by: (i) advancing novel contamination-resistant methodologies, (ii) developing supporting methods and platforms, and (iii) adopting contamination-resistant benchmarks into existing evaluation pipelines.

---


### 153. [Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates](https://arxiv.org/abs/2605.20005)

**<font color=#1a73e8>作者：</font>** Parjanya Prajakta Prashant, Jiongli Zhu, Aldan Creo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models on new data improves task performance but degrades capabilities learned during pretraining, a phenomenon known as catastrophic forgetting. Existing methods mitigate this by modifying the fine-tuning objective to suppress high-loss tokens or sequences, but these tokens are essential for learning new tasks, especially those with poor pretraining coverage. In such settings, hard tokens should still contribute to learning, so forgetting must be controlled without suppressing them. We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss. This suggests that high-loss batches are especially prone to inducing forgetting. Motivated by this observation, we introduce FINCH, a loss-adaptive learning-rate schedule that reduces the learning rate on high-loss batches and increases it as the model converges, while leaving the fine-tuning objective unchanged. Across knowledge acquisition, science, and low-resource language adaptation benchmarks, FINCH reduces forgetting by 93% on average while matching the task performance of standard fine-tuning. On Qwen3-4B knowledge acquisition, FINCH cuts TruthfulQA degradation by 5x and reverses HaluEval degradation, while better preserving confidence calibration. Overall, our results show that learning-rate schedules are an effective tool to shape model behavior during fine-tuning, beyond just target-task optimization.

---


### 154. [A Nash Equilibrium Framework For Training-Free Multimodal Step Verification](https://arxiv.org/abs/2605.20033)

**<font color=#1a73e8>作者：</font>** Rohit Sinha, Kunal Tilaganji, Tanuja Ganu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models often generate reasoning chains containing subtle errors that lead to incorrect answers. Current verification approaches have notable limitations. Learned critics need extensive labeled data and show inconsistent performance across different tasks. Meanwhile, existing training-free methods simply average scores from different sources, missing a key insight: when these scores disagree, that disagreement itself carries important information about whether a reasoning step is truly valid or not. We propose a training-free verification approach that treats step-wise verification as a coordination problem among specialized judges. We formalize these judges' interaction as a Nash equilibrium game where agreement signals valid steps while disagreement reveals instability. Our method computes equilibrium scores through a closed-form solution, enabling both disagreement-aware filtering and stability-conscious ranking of reasoning steps. Evaluated across six benchmarks, our approach achieves consistent improvements of 2.4% to 5.2% over baseline models and shows competitive performance against learned critics, demonstrating that cross-modal agreement (not just average confidence) provides robust verification signals without task-specific adaptation.

---


### 155. [Stage-adaptive Token Selection for Efficient Omni-modal LLMs](https://arxiv.org/abs/2605.20035)

**<font color=#1a73e8>作者：</font>** Zijie Xin, Jie Yang, Ruixiang Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (om-LLMs) achieve unified audio-visual understanding by encoding video and audio into temporally aligned token sequences interleaved at the window level. However, processing these dense non-textual tokens throughout the LLM incurs substantial computational overhead. Although training-free token selection can reduce this cost, existing methods either focus on visual-only inputs or prune om-LLM tokens only before the LLM with fixed per-modality ratios, failing to capture how cross-modal token importance evolves across layers. To address this limitation, we first analyze the layer-wise token dependency of om-LLMs. We find that visual and audio dependencies follow a block-wise pattern and gradually weaken with depth, indicating that many late-layer non-textual tokens become redundant after cross-modal fusion. Motivated by this observation, we propose SEATS, a training-free, stage-adaptive token selection method for efficient om-LLM inference. Before the LLM, SEATS removes spatiotemporal redundancy via attention-weighted diversity selection. Inside the LLM, it progressively prunes tokens across blocks and dynamically allocates the retention budget from temporal windows to modalities using query relevance scores. In late layers, it removes all remaining non-textual tokens once cross-modal fusion is complete. Experiments on Qwen2.5-Omni and Qwen3-Omni demonstrate that SEATS effectively improves inference efficiency. Retaining only 10% of visual and audio tokens, it achieves a 9.3x FLOPs reduction and a 4.8x prefill speedup while preserving 96.3% of the original performance.

---


### 156. [Probing Embodied LLMs: When Higher Observation Fidelity Hurts Problem Solving](https://arxiv.org/abs/2605.20072)

**<font color=#1a73e8>作者：</font>** Oussama Zenkri, Oliver Brock  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly proposed as cognitive components for robotic systems, yet their opaque decision processes make it difficult to explain success or failure in closed-loop embodied tasks. Following an empirical AI methodology, we study embodied LLM agents behaviorally by varying the information available to the agent and measuring the resulting changes in behavior. Using the Lockbox, a sequential mechanical puzzle with hidden interdependencies, we evaluate LLMs across RGB, RGB-D, and ground-truth symbolic observations in a physical robotic setup and use controlled simulation to probe the resulting behavior. Counterintuitively, agents perform best under raw RGB input and worst under perfect ground-truth observations. In simulation, we probe this effect by randomly flipping perceived action outcomes and find that moderate noise improves performance, peaking at a 40% flip probability with a 2.85-fold success rate increase over the noise-free baseline. Further analysis links this gain to a reduction in repetitive action loops. These findings suggest that success rates alone are insufficient for evaluating LLMs, as measured performance may reflect the interaction between perceptual errors and reasoning failures rather than robust problem solving.

---


### 157. [Towards Distillation Guarantees under Algorithmic Alignment for Combinatorial Optimization](https://arxiv.org/abs/2605.20074)

**<font color=#1a73e8>作者：</font>** Thien Le, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation transfers knowledge from a large model trained on broad data to a smaller, more efficient model suitable for deployment. In structured prediction settings, prior knowledge about the task can guide the choice of a target architecture that is algorithmically aligned with the underlying problem. Building on recent learning-theoretic analyses of decision-tree (DT) distillation (Boix-Adsera, 2024), we study when distillation succeeds for combinatorial optimization tasks. We focus on the case where the target model is a graph neural network whose architecture is aligned with a dynamic programming (DP) algorithm for the task. Assuming that the source model is sufficiently rich, formalized through the linear representation hypothesis (LRH) (Elhage et al., 2022; Park et al., 2024), we show that the distillation problem can be solved efficiently in the complexity parameters of the DP transition function, represented as a DT. Our results provide a rigorous sufficient condition for successful distillation in the flavour of algorithmic alignment.

---


### 158. [CopT: Contrastive On-Policy Thinking with Continuous Spaces for General and Agentic Reasoning](https://arxiv.org/abs/2605.20075)

**<font color=#1a73e8>作者：</font>** Dachuan Shi, Hanlin Zhu, Xiangchi Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) is a standard approach for eliciting reasoning capabilities from large language models (LLMs). However, the common CoT paradigm treats thinking as a prerequisite for answering, which can delay access to plausible answers and incur unnecessary token costs even when the model is able to identify an answer before extended thinking, a behavior known as performative reasoning. In this paper, we introduce CopT, a reformulated reasoning pipeline that reverses the usual order of thinking and answering. Instead of thinking before answering, CopT first elicits a draft answer and then invokes subsequent on-policy thinking conditioned on its own draft answer for reflection and correction. To assess whether the draft answer should be trusted, CopT recasts continuous embeddings as inference-time contrastive verifiers. Specifically, it contrasts the model's support for the same generated tokens under discrete-token inputs and continuous-embedding inputs, yielding a sequence-level reverse KL estimator for answer reliability. Our analysis shows that under certain assumptions, the expected estimate equals the mutual information between the unresolved latent state and the emitted answer token, explaining why it captures answer-relevant uncertainty rather than arbitrary uncertainty in the latent state. When the answer is deemed insufficiently reliable, CopT performs further on-policy thinking, where a second KL estimator dynamically controls draft-answer visibility, preserving useful partial information while reducing the risk of being misled by unreliable content. Across mathematics, coding, and agentic reasoning tasks, CopT improves peak accuracy by up to 23% and reduces token usage by up to 57% at comparable or higher accuracy, without any additional training. The code is available at this https URL.

---


### 159. [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/2605.20084)

**<font color=#1a73e8>作者：</font>** Zijun Jia, Yuanchang Ye, Sen Jia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can enhance factuality via retrieval-augmented generation (RAG), but applying RAG to every query is unnecessary when the model-only answer is reliable. This motivates cascaded RAG: each query is first handled by an LLM-only branch, escalated to a RAG fallback only if the primary branch is uncertain, and abstained from when neither branch is sufficiently trustworthy. However, calibrating such cascades stage by stage may be conservative, since the final utility depends on joint uncertainty thresholding of LLM-only and RAG. In this work, we develop BalanceRAG to certify threshold pairs at a target risk level. Given uncertainty scores from the two branches, BalanceRAG frames each threshold pair as an operating point on a two-dimensional lattice and identifies safe operating points using sequential graphical testing. This enables risk-adaptive threshold calibration, controlling the system-level error rate among accepted points, while retaining more examples. Furthermore, BalanceRAG extends to multi-risk calibration, allowing retrieval usage to be bounded together with the selection-conditioned risk. Experiments on three open-domain question answering (QA) benchmarks across multiple LLM backbones demonstrate that BalanceRAG meets prescribed risk levels, preserves higher coverage and more accepted correct examples, and reduces unnecessary retrieval calls compared with always-on RAG.

---


### 160. [ThoughtTrace: Understanding User Thoughts in Real-World LLM Interactions](https://arxiv.org/abs/2605.20087)

**<font color=#1a73e8>作者：</font>** Chuanyang Jin, Binze Li, Haopeng Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI has now reached billions of users, yet existing datasets capture only what people say, not what they think. We introduce ThoughtTrace, the first large-scale dataset that pairs real-world multi-turn human--AI conversations with users' self-reported thoughts: their reasons for sending prompts and reactions to assistant responses. ThoughtTrace comprises 1,058 users, 2,155 conversations, 17,058 turns, and 10,174 thought annotations collected across 20 language models. Our analysis shows that ThoughtTrace captures long-horizon, topically diverse interactions, and that thoughts are semantically distinct from messages, difficult for frontier LLMs to infer from context, diverse in content, and tied to conversation stages. We further demonstrate the utility of thoughts for downstream modeling. First, thoughts improve user-behavior prediction as inference-time context. Second, thought-guided rewrites provide fine-grained alignment signals for training personalized assistants. Together, ThoughtTrace establishes user thoughts as a new data modality for studying the cognitive dynamics behind human--AI interaction and provides a foundation for building assistants that better understand and adapt to users' latent goals, preferences, and needs.

---


### 161. [MetaEarth-MM: Unified Multimodal Remote Sensing Image Generation with Scene-centered Joint Modeling](https://arxiv.org/abs/2605.20090)

**<font color=#1a73e8>作者：</font>** Zhiping Yu, Chenyang Liu, Jinqi Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal remote sensing images are vital for Earth observation, yet complete paired observations are often scarce in practice. Existing generative methods commonly address this problem through isolated pairwise modality translation, but their versatility and scalability remain limited as the number of modalities and generation tasks increases. Here, we develop a generative foundation model MetaEarth-MM for multi-modal remote sensing imagery, enabling paired joint generation and any-to-any translation across five modalities within a unified model. Recognizing the intrinsic scene consistency underlying multi-modal observations, we introduce a scene-centered joint modeling paradigm in MetaEarth-MM. Unlike previous methods that rely on direct appearance-level cross-modal mapping, our model organizes the generation around the underlying scene content. Specifically, MetaEarth-MM adopts a decoupled architecture that first infers a latent scene representation from available observations, and then generates target modalities conditioned on this intermediate state. To support training, we further construct EarthMM, a large-scale dataset comprising 2.8 million multi-resolution global images with 2.2 million aligned pairs. Extensive experiments demonstrate that MetaEarth-MM not only exhibits strong generative capability and robust generalization across diverse generation tasks, but also supports downstream tasks at both data and representation levels, highlighting its potential as a general foundation model for cross-modal Earth observation. The code and dataset will be available at this https URL.

---


### 162. [Draft Less, Retrieve More: Hybrid Tree Construction for Speculative Decoding](https://arxiv.org/abs/2605.20104)

**<font color=#1a73e8>作者：</font>** Yuhao Shen, Tianyu Liu, Xinyi Hu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates large language model inference by leveraging a draft-then-verify paradigm. To maximize the acceptance rate, recent methods construct expansive draft trees, which unfortunately incur severe VRAM bandwidth and computational overheads that bottleneck end-to-end speedups. While dynamic-depth pruning can reduce this latency by removing marginal branches, it also discards potentially valid candidates, preventing the acceptance rate from reaching the upper bound of dense trees. In this paper, we identify a critical opportunity in resource allocation: the transition from dense to pruned drafting frees up significant computational budget. To break this Pareto tradeoff, we introduce Graft, a compensation framework that couples pruning and retrieval as mutually reinforcing operations. Pruning supplies sufficient budget for retrieval, while retrieval compensates for pruning-induced coverage loss and recovers accepted length. By employing a sequential `prune-then-graft' mechanism, Graft attaches highly predictive retrieved tokens into positions opened by pruning, filling the topological gaps with near-zero overhead. Graft is entirely training-free and lossless. Comprehensive evaluations show that Graft establishes a new Pareto frontier across practical deployment settings, including short-context generation, long-context generation, and large-scale models. On short-context benchmarks, it achieves up to 5.41$\times$ speedup and improves average speedup over EAGLE-3 by up to 21.8% on the large-scale Qwen3-235B. We also provide a preliminary exploration of applying Graft to the DFlash-style block drafting paradigm, offering initial evidence and insights for extending grafting beyond autoregressive draft trees.

---


### 163. [MixRea: Benchmarking Explicit-Implicit Reasoning in Large Language Models](https://arxiv.org/abs/2605.20128)

**<font color=#1a73e8>作者：</font>** Yuanqing Cai, Ziyi Huang, Minhao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into high-stakes decision-making. Inspired by the theory of \emph{inattentional blindness} in human cognition, we investigate whether LLMs, trained on human-preferred corpora that embed attentional biases, exhibit a similar limitation: \emph{failing to attend to subtle yet important contextual cues under explicit task instructions}. To evaluate this, we introduce the task of \textbf{explicit-implicit reasoning} and present \textbf{MixRea}, a benchmark of 2,246 multiple-choice questions across 9 reasoning types with varying distributions of explicit and implicit information. Evaluation of 21 advanced LLMs shows that even the best-performing reasoning model (Gemini 2.5 Pro) achieves only 42.8\% consistency, revealing widespread inattentional blindness. To mitigate this, we propose \textbf{Potential Relation Completion Prompting (PRCP)}, a prompting method that improves reasoning by recovering overlooked causal relations. Further analysis shows that this limitation persists across diverse multi-source reasoning tasks, highlighting the need for more cognitively aligned models.

---


### 164. [PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset](https://arxiv.org/abs/2605.20147)

**<font color=#1a73e8>作者：</font>** Haojun Chen, Haoyang He, Chengming Xu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) models have recently seen notable progress around 1K and 2K resolution. With the extreme desire for better visual experience and the rapid development of imaging technology, the demand for Ultra-High-Resolution (UHR) image generation has grown significantly. However, UHR image generation poses great challenges due to the scarcity and complexity of high-resolution content. In this paper, we first introduce PixVerve-95K, a high-quality, open-source UHR T2I dataset curated with a carefully designed data pipeline, which contains 95K images across diverse scenarios (each image has a minimum pixel-count of 100M) and seven-dimensional annotations. Based on our large-scale image-text dataset, we take a pioneering step to extend various T2I foundation models to native 100MP generation with three training schemes. Finally, leveraging both conventional metrics and multimodal large language model-based assessments, our proposed PixVerve-Bench benchmark establishes a comprehensive evaluation protocol for UHR images encompassing visual quality and semantic alignment. Extensive experimental results on our benchmark and the constructive exploration of training strategies collaboratively provide valuable insights for future breakthroughs.

---


### 165. [Less Back-and-Forth: A Comparative Study of Structured Prompting](https://arxiv.org/abs/2605.20149)

**<font color=#1a73e8>作者：</font>** Saurav Ghosh, Gabriella Polach, Abdou Sow  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used for open-ended tasks, but underspecified prompts can lead to low-quality answers and additional interaction. This paper studies whether structured prompt design improves response quality while reducing user effort. We compare three prompt conditions: a raw prompt, a checklist-improved prompt, and a clarifying-question prompt. We evaluate these conditions across four task types--summarization, planning, explanation, and coding--using three LLM systems: ChatGPT, Claude, and Grok. Each output is scored with a unified rubric covering task completion, correctness, compliance, and clarity. Checklist-improved prompts achieved the highest mean rubric score, 7.50 out of 8, compared with 5.67 for raw prompts and 6.67 for clarifying-question prompts. Checklist prompts also produced the best quality-effort tradeoff, using fewer average tokens than both raw and clarifying prompts. These results suggest that a simple prompt checklist can improve LLM responses while reducing unnecessary interaction.

---


### 166. [Rethinking Visual Attribution for Chest X-ray Reasoning in Large Vision Language Models](https://arxiv.org/abs/2605.20158)

**<font color=#1a73e8>作者：</font>** Guangzhi Xiong, Qiao Jin, Sanchit Sinha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision Language Models (LVLMs) show promise in medical applications, but their inability to faithfully ground responses in visual evidence raises serious concerns about clinical trustworthiness. While visual attribution methods are widely used to explain LVLM predictions, whether these explanations actually reflect the visual evidence underlying the model's decision is largely unverified, since ground-truth annotations for internal model reasoning are typically unavailable. We address this question for chest X-ray (CXR) reasoning by developing a causal evaluation framework that retains only CXR-VQA samples for which the expert-annotated region is verified, via counterfactual editing, to be causally responsible for the model's prediction. Using this framework across 11 attribution methods, six open-source LVLMs, and two output modes (direct answer and step-by-step reasoning), we find that existing attribution methods often fail to identify the evidence used by LVLMs. To address this failure, we propose MedFocus, a concept-based attribution method that localizes clinically meaningful anatomical regions via unbalanced optimal transport and measures their causal effect on model outputs through targeted interventions. MedFocus produces spatial, concept-level, and token-level attributions and substantially outperforms prior methods, taking a step toward more trustworthy attribution for medical LVLMs. Our data and code are available at this https URL.

---


### 167. [CaMo: Camera Motion Grounded Evaluation and Training for Vision-Language Models](https://arxiv.org/abs/2605.20165)

**<font color=#1a73e8>作者：</font>** Hsiang-Wei Huang, Junbin Lu, Kuang-Ming Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) achieve strong performance on spatial question answering benchmarks, yet it remains unclear whether such gains reflect genuine spatial intelligence. We show that existing spatial VLMs lack basic camera motion understanding, a key component of spatial cognition. We propose the Spatial Narrative Score (SNS), an evaluation framework that requires VLMs to generate explicit spatial narratives capturing both scene semantics and camera motion, followed by reasoning with a frozen proxy LLM. Under SNS, state-of-the-art spatial VLMs exhibit significant performance degradation despite high direct question answering accuracy. To address this gap, we introduce CaMo, a camera motion grounded VLM that achieves consistent performance across SNS evaluation and direct spatial question answering accuracy. Our results highlight the importance of explicit spatial narrative externalization for evaluating VLMs with transferable 3D spatial understanding. Our code, data, and model is available at this https URL

---


### 168. [KoRe: Compact Knowledge Representations for Large Language Models](https://arxiv.org/abs/2605.20170)

**<font color=#1a73e8>作者：</font>** Davide Cavicchini, Fausto Giunchiglia, Jacopo Staiano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Models (LLMs) have shown impressive performances in user-facing tasks such as question answering, as well as consistent improvements in reasoning capabilities. Still, the way these models encode knowledge seems inherently flawed: by design, LLMs encode world-knowledge within their parameters. This way of representing knowledge is inherently opaque, difficult to debug and update, and prone to hallucinations. On the other hand, Knowledge Graphs can provide human-readable and easily editable world knowledge representations, and their application in knowledge-intensive tasks has consistently proven beneficial to downstream performance. Nonetheless, current integration techniques require extensive retraining or finetuning. To overcome this issue, we introduce KoRe, a methodology to encode 1-hop sub-graphs into compact discrete knowledge tokens and inject them into a LLM backbone. We test the proposed approach on three established benchmarks, and report competitive performances coupled with a significant reduction (up to 10x) in token usage. Our results show that compact discrete KG representations can efficiently and effectively be used to ground modern LLMs.

---


### 169. [A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents](https://arxiv.org/abs/2605.20173)

**<font color=#1a73e8>作者：</font>** Vasundra Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production LLM agents combine stochastic model outputs with deterministic software systems, yet the boundary between the two is rarely treated as a first-class architectural object. This paper names that boundary the stochastic-deterministic boundary (SDB): a four-part contract among a proposer, verifier, commit step, and reject signal that specifies how an LLM output becomes a system action. We argue that the SDB is the load-bearing primitive of production agent runtimes.
Around this primitive, we organize agent runtime design into three concerns: Coordination, State, and Control. We present a catalog of six runtime patterns that compose the SDB differently across conversational, autonomous, and long-horizon agents: hierarchical delegation, scatter-gather plus saga, event-driven sequencing, shared state machine, supervisor plus gate, and human in the loop. For each pattern, we trace its lineage to distributed-systems concepts and identify what changes when the worker is stochastic.
The paper contributes a five-step methodology for selecting runtime patterns, a diagnostic procedure that maps production failures to pattern weaknesses, and a failure mode called replay divergence, in which LLM-based consumers of a deterministic event log produce different downstream outputs under model-version or prompt changes. A stylized reliability decomposition separates per-call model variance from architectural momentum, motivating the claim that as model variance decreases, pattern choice and SDB strength become increasingly important levers for long-run reliability. We apply the methodology to five workloads and provide one runnable reference implementation for a 90-day contract-renewal agent.

---


### 170. [ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning](https://arxiv.org/abs/2605.20176)

**<font color=#1a73e8>作者：</font>** Juncheng Wu, Letian Zhang, Yuhan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and agentic systems have shown promise for clinical decision support, but existing works largely assume that evidence has already been curated and handed to the model. Real-world clinical workflows instead require agents to actively seek, iteratively plan, and synthesize multimodal evidence from heterogeneous sources. In this paper, we introduce ClinSeekAgent, an automated agentic framework for dynamic multimodal evidence seeking that shifts the paradigm from passive evidence consumption to active evidence acquisition. Given only a clinical query and access to raw data sources, ClinSeekAgent gathers evidence by querying medical knowledge bases, navigating raw EHRs, and invoking medical imaging tools; refines its hypotheses as new information emerges; and integrates the collected evidence into grounded clinical decisions. ClinSeekAgent serves both as an inference-time agent for frontier LLMs and as a training-time pipeline for distilling high-quality agent trajectories into compact open-source models. To validate its inference-time effectiveness, we construct ClinSeek-Bench, which pairs Curated Input reasoning from fixed pre-selected evidence with Automated Evidence-Seeking over raw clinical data. On text-only EHR tasks, ClinSeekAgent improves Claude Opus 4.6 from 60.0 to 63.2 overall F1 and MiniMax M2.5 from 43.1 to 47.3, with positive risk-prediction gains in 7 out of 9 evaluated host models. On multimodal tasks, ClinSeekAgent improves Claude Opus 4.6 from 47.5 to 62.6 (+15.1); all evaluated models improve across the three CXR-related task groups. We further validate ClinSeekAgent as a training pipeline by distilling agentic evidence-seeking trajectories into ClinSeek-35B-A3B, which achieves 34.0 average F1 on existing AgentEHR-Bench, improving over its Qwen3.5-35B-A3B baseline by +11.9 points and approaching Claude Opus 4.6.

---


### 171. [From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models](https://arxiv.org/abs/2605.20177)

**<font color=#1a73e8>作者：</font>** Juncheng Wu, Hardy Chen, Haoqin Tu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) emphasize long chain-of-thought reasoning; yet, we find that their performance on visual tasks is primarily limited by a lack of visual perception as opposed to reasoning itself. In this work, we systematically study the interplay between perception and reasoning in VLM post-training by decomposing their capabilities into three separate training stages: visual perception, visual reasoning, and textual reasoning, incorporating specialized training data. We demonstrate that visual perception (a) requires targeted optimization with specialized data; (b) serves as a fundamental scaffold that should be solidified through staged training before refining visual reasoning; and (c) is more effectively learned via RL than caption-based SFT. Our experiments across multiple VLMs demonstrate that staged training consistently improves both visual perception and reasoning performance over merged training. Notably, models trained with our approach achieve 1.5% higher reasoning accuracy with 20.8% shorter reasoning traces, suggesting that superior perception reduces the need for excessive reasoning. Furthermore, we show that this capability-based staging represents a new curriculum dimension orthogonal to traditional difficulty-based curricula, and combining both yields further additive gains. Our staged-training models achieve superior performance among open-weight VLMs, establishing advanced results on several visual math and perception (e.g., +5.2% on WeMath and +3.7% on RealWorldQA) tasks compared with the base counterpart.

---


### 172. [TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload](https://arxiv.org/abs/2605.20179)

**<font color=#1a73e8>作者：</font>** Zhiben Chen, Youpeng Zhao, Yang Sui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive (AR) models, offering better hardware utilization and bidirectional context through parallel block-level decoding. However, as dLLMs continue to scale up with mixture-of-experts (MoE) architectures, their deployment on resource-constrained devices remains an open challenge. Existing AR-based methods often incur either prohibitive I/O overhead or significant compute bottlenecks. In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. Specifically, we leverage the temporal stability of expert activations during the diffusion process within the block and introduce an interval-based expert refresh strategy that updates the expert placement in an I/O-aware fashion. To ensure optimal performance, we formulate the inference scheduling as a mathematical programming problem, solving for the optimal interval that minimizes I/O traffic and CPU computation. Most importantly, TIDE is a lossless optimization that requires no model training, providing a "free lunch" acceleration for dLLM inference. In a single GPU-CPU system, we demonstrate that TIDE achieves up to 1.4$\times$ and 1.5$\times$ throughput improvements over prior baselines on LLaDA2.0-mini and LLaDA2.0-flash models, respectively.

---


> [!TIP]
> 当前位于：**151-172**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-172**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
