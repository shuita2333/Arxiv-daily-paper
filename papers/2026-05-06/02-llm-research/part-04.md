# 🧠 大模型相关研究 | 2026年05月06日

> 本类共 **203** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

---

### 151. [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/abs/2605.02269)

**<font color=#1a73e8>作者：</font>** Kei Nishimura-Gasparian, Robert McCarthy, David Lindner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specification gaming is a critical failure mode of LLM agents. Despite this, there has been little systematic research into when it arises and what drives it. To address this, we build and open source a diverse suite of tasks where models can score highly by taking unintended actions. We find that all tested models exploit their specifications at non-negligible rates in most of our eight settings, including five non-coding settings. We see the highest rates of specification gaming in Grok 4 and the lowest rates in Claude models. We use our evaluation suite to study what drives specification gaming, and find that: 1. RL reasoning training substantially increases the rate at which models exploit their specifications, 2. Increasing RL reasoning budget has a weakly positive effect on exploit rate, and 3. Test-time mitigations reduce but do not eliminate the rate of specification gaming. Our results suggest that specification gaming is a fundamental challenge arising from RL reasoning training; we release our evaluation suite to support further work on this problem.

---


### 152. [Rethinking Electro-Optical Vision Foundation Models for Remote Sensing Retrieval: A Controlled Comparison with Generalist VFM](https://arxiv.org/abs/2605.02283)

**<font color=#1a73e8>作者：</font>** Hyobin Park, Minseok Seo, Dong-Geol Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have attracted significant attention for their ability to leverage large-scale unlabeled visual data. This advantage is particularly important in remote sensing, where data acquisition is costly and annotation often requires expert knowledge. Recent electro-optical vision foundation models aim to learn domain-specific representations from remote sensing imagery, but it remains unclear whether they are more effective than strong generalist vision foundation models under retrieval-based evaluation. In this study, we conduct a controlled comparison between representative EO-specific and generalist vision foundation models for remote sensing image retrieval. Using the same datasets, retrieval protocol, and evaluation metric, we evaluate both in-domain performance and cross-scene generalization. Our results show that strong generalist vision foundation models are competitive with, and in some cases outperform, existing EO-specific models. Moreover, EO-specific models often suffer from substantial degradation under cross-scene evaluation, while generalist models show more stable transfer. These findings suggest that EO pretraining alone does not guarantee stronger retrieval-oriented remote sensing representations. We discuss the limitations of current EO-specific pretraining strategies and highlight the need for future EO vision foundation models to better exploit the physical, spatial, spectral, and geographic characteristics of remote sensing imagery.

---


### 153. [Complexity Horizons of Compressed Models in Analog Circuit Analysis](https://arxiv.org/abs/2605.02285)

**<font color=#1a73e8>作者：</font>** Pacome Simon Mbonimpa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Models (LLMs) for specialized engineering domains, such as circuit analysis, often faces a trade-off between reasoning accuracy and computational efficiency. Traditional evaluation methods treat model performance as a flat metric, failing to account for the hierarchical nature of engineering knowledge. We propose a performance-aware model compression strategy that utilizes prerequisite graphs to optimize model selection for circuit analysis tasks. By structuring electronics design concepts as Directed Acyclic Graphs (DAGs), we can identify the specific complexity horizons of an LLM's compressed variants' tiers. Our framework introduces an agentic pipeline for generating prerequisite-based datasets and a strategic evaluation engine that dynamically cascades queries across a spectrum of compressed variants of an LLM. This approach allows to select the smallest compressed model, given its conceptual knowledge boundaries in circuit analysis. Experimental results on analog electronics datasets demonstrate that prerequisite graphs provide a granular map of model compression with respect to the performance given circuit analysis complexity. (Source Code: this https URL, Demo: this https URL)

---


### 154. [EngiAgent: Fully Connected Coordination of LLM Agents for Solving Open-ended Engineering Problems with Feasible Solutions](https://arxiv.org/abs/2605.02289)

**<font color=#1a73e8>作者：</font>** Xiyuan Zhou, Ruixi Zou, Xinlei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineering problem solving is central to real-world decision-making, requiring mathematical formulations that not only represent complex problems but also produce feasible solutions under data and physical constraints. Unlike mathematical problem solving, which operates on predefined formulations, engineering tasks demand open-ended analysis, feasibility-driven modeling, and iterative refinement. Although large language models (LLMs) have shown strong capabilities in reasoning and code generation, they often fail to ensure feasibility, which limits their applicability to engineering problem solving. To address this challenge, we propose EngiAgent, a multi-agent system with a fully connected coordinator that simulates expert workflows through specialized agents for problem analysis, modeling, verification, solving, and solution evaluation. The fully connected coordinator enables flexible feedback routing, overcoming the rigidity of prior pipeline-based reflection methods and ensuring feasibility at every stage of the process. This design not only improves robustness to diverse failure cases such as data extraction errors, constraint inconsistencies, and solver failures, but also enhances the overall quality of problem solving. Empirical results across four representative domains demonstrate that EngiAgent achieves substantial improvements in feasibility compared to prior approaches, establishing a new paradigm for feasibility-oriented engineering problem solving with LLMs. Our source code and data are available at this https URL.

---


### 155. [SOTOPIA-TOM: Evaluating Information Management in Multi-Agent Interaction with Theory of Mind](https://arxiv.org/abs/2605.02307)

**<font color=#1a73e8>作者：</font>** Yashwanth YS, Ruichen Wang, Shihua Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents are increasingly interacting in multi-party settings, they need to properly handle information asymmetry, i.e., knowing when and to whom to disclose information is appropriate. Yet, existing benchmarks fail to measure this ability in realistic multi-party settings. Thus, we introduce SOTOPIA-TOM, a multi-dimensional benchmarking framework to evaluate LLM agents' ability to successfully navigate information asymmetric and privacy sensitive multi-party interactions. We create an interaction environment which enables both public (broadcast) and private (direct message) communication, and craft 160 human-reviewed scenarios across eight industry sectors, each involving 3 to 5 agents with partitioned private knowledge and channel-dependent sharing policies. To measure interaction abilities, we create a multi-dimensional evaluation framework to assess how well agents share useful information, seek missing details, coordinate efficiently, and protect privacy, which we also combine into a composite INFOMGMT metric. Results show that, across 6 LLM backbones and prompting strategies (vanilla, CoT-privacy, and ToM-based interventions), even the largest high-reasoning model (GPT-5) reaches only a 62% INFOMGMT score, which indicates persistent deficiencies in information seeking and privacy-aware decision-making. Additionally, ToM-based interventions more consistently improve the overall coordination-privacy balance (for example, relative to the vanilla baseline, ToM-Coach reduces critical privacy violations on GPT-4o from 9.9% to 2.2% while increasing the composite InfoMgmt score more than 2.5x from 15% to 40%). Overall, SOTOPIA-TOM exposes persistent limitations of current LLM agents in complex, information-asymmetric coordination and provides an extensible testbed for developing more privacy-aware, theory-of-mind capable multi-agent systems.

---


### 156. [LLM-enabled Social Agents](https://arxiv.org/abs/2605.02335)

**<font color=#1a73e8>作者：</font>** Önder Gürcan, Moharram Challenger  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have transformed agent-agent and human-agent interaction by enabling software, physical, and simulation agents to communicate and deliberate through natural language. Yet fluent language use does not by itself yield socially intelligible behaviour. Most current systems remain weakly grounded in roles, norms, intentions, and contextual constraints, limiting their capacity for meaningful participation in social environments. This paper develops a conceptual baseline for LLM-enabled social agents by arguing that they should be grounded in role definitions operationalized through persona descriptions. On this basis, we outline research directions for representation, hybrid control, and evaluation. The paper concludes that persona-based role definitions are a necessary foundation for turning language competence into social behaviour.

---


### 157. [Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation](https://arxiv.org/abs/2605.02348)

**<font color=#1a73e8>作者：</font>** Muneeb Ur Raheem Khan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models pick up social biases from the data they are trained on and carry those biases into downstream applications, often reinforcing stereotypes around gender, race, religion, disability, age, and socioeconomic status. The standard fixes (retraining on curated data or fine-tuning with human feedback) are expensive, need access to model weights, and risk degrading the model on other tasks. In this paper we take a different route: we debias the model at decoding time, treating bias mitigation as a structured search over candidate tokens without ever touching model weights. A separate Process Reward Model (PRM) acts as a judge, scoring each candidate for both fairness and fluency. We design three schemes of increasing sophistication (Best-of-N selection, Sequential critique-and-revise, and Constitutional self-audit) and evaluate them on four models (GPT-4o-mini, Llama 3.2 3B, Gemma 3 4B, Qwen 2.5 3B) across a 200-prompt bilingual benchmark in English and Urdu covering eight bias categories. Sequential debiasing proves the most effective, raising mean bias scores by up to +0.40 over baseline while preserving (and sometimes improving) fluency. We then extend all three schemes to open-ended generation, where each token is debiased on the fly, and introduce a lightweight Bias Guard gate that fires only on potentially biased words, keeping overhead near 2x for well-calibrated models. A formal overhead metric that separates generator cost from judge cost reveals that Best-of-N is effectively free on the generator side in a native implementation. GPT-4o-mini, included as a strong proprietary anchor, confirms that the framework scales with model capability; the three open-weight models show where current small-scale LLMs still struggle.

---


### 158. [MolViBench: Evaluating LLMs on Molecular Vibe Coding](https://arxiv.org/abs/2605.02351)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Yuxuan Ren, Weida Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Molecular Vibe Coding, a paradigm where chemists interact with LLMs to generate executable programs for molecular tasks, has emerged as a flexible alternative to chemical agents with predefined tools, enabling chemists to express arbitrarily complex, customized workflows. Unlike general coding tasks, molecular coding imposes a distinctive challenge that LLMs should jointly equip programming, molecular understanding, and domain-specific reasoning capabilities. However, existing benchmarks remain disconnected. General code generation benchmarks such as HumanEval and SWE-bench require no chemistry knowledge, while chemistry-focused benchmarks such as S^2-Bench and ChemCoTBench evaluate knowledge recall or property prediction rather than executable code generation. To bridge this gap, we introduce MolViBench, the first benchmark tailored for Molecular Vibe Coding. MolViBench comprises 358 curated tasks across five cognitive levels, ranging from single-API recall to end-to-end virtual screening pipeline design, spanning 12 real-world drug discovery workflows. To rigorously assess generated code, we also propose a multi-layered evaluation framework that combines type-aware output comparison and AST-based API-semantic fallback analysis, which jointly measures executability and chemical correctness. We systematically evaluate 9 frontier coding LLMs and compare three real-world Molecular Vibe Coding paradigms, providing a practical and fine-grained testbed for diagnosing LLMs' coding capabilities in AI-accelerated molecular discovery.

---


### 159. [When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models](https://arxiv.org/abs/2605.02363)

**<font color=#1a73e8>作者：</font>** Cosimo Galeone, Minsu Park, Giuseppe Ettorre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deployed language models must produce outputs that are both correct and format-compliant. We study this structured-output reliability gap using two mathematical benchmarks -- GSM8K and MATH -- as a controlled testbed: ground truth is unambiguous and the output contract is strict (JSON with required fields). We evaluate three 7-9B models under five prompting strategies and report output accuracy -- the joint event of mathematical correctness and valid JSON structure -- as the primary metric. A systematic format failure emerges: NAIVE prompting (no system prompt) achieves up to 85% task accuracy on GSM8K but 0% output accuracy across all models and datasets. REFERENCE prompting (a minimal hand-written JSON format prompt) fares little better, yielding 0% output accuracy for two of four models tested. Constrained decoding enforces syntactic validity but incurs 3.6x-8.2x latency overhead and in several settings degrades task performance substantially. To overcome this limitation, we developed AloLab, an iterative system-prompt optimizer (meta-agent: Claude Sonnet 4.5) requiring only black-box API access to the target model; it reaches 84-87% output accuracy on GSM8K and 34-40% on MATH across five independent runs per model, with 29/30 paired McNemar comparisons against the best static prompt significant at p < 0.05, at near-NAIVE inference latency and without model fine-tuning. The same format failure extends to GPT-4o (OpenAI, 2024), a proprietary closed-source model: REFERENCE achieves 0% output accuracy due to systematic markdown-fence wrapping, while AloLab reaches 95.2% [94.8, 95.6]. An ablation replacing the Sonnet 4.5 meta-agent with Claude 3 Haiku reduces mean output accuracy to 61.0% and increases run-to-run standard deviation from <1 pp to 21.8 pp, confirming that meta-agent capability is a primary driver of optimization quality.

---


### 160. [InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition](https://arxiv.org/abs/2605.02364)

**<font color=#1a73e8>作者：</font>** Fengze Liu, Weidong Zhou, Binbin Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Upweighting high-quality data in LLM pretraining often improves performance, but in datalimited regimes, especially under overtraining, stronger upweighting increases repetition and can degrade performance. However, standard scaling laws do not reliably extrapolate across mixture recipes or under repetitions, making the selection for optimal data recipes at scaling underdetermined. To solve this, we introduce InfoLaw (Information Scaling Laws), a data-aware scaling framework that predicts loss from consumed tokens, model size, data mixture weights, and repetition. The key idea is to model pretraining as information accumulation, where quality controls information density and repetition induces scaledependent diminishing returns. We first collect the model performance after training on datasets that vary in scale, quality distribution, and repetition level. Then we build up the modeling for information so that information accurately predicts those model performance. InfoLaw predicts performance on unseen data recipes and larger scale runs (up to 7B, 425B tokens) with 0.15% mean and 0.96% max absolute error in loss, and it extrapolates reliably across overtraining levels, enabling efficient data-recipe selection under varying compute budgets.

---


### 161. [Enhancing Multimodal In-Context Learning via Inductive-Deductive Reasoning](https://arxiv.org/abs/2605.02378)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Haonan Wang, Yuyan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) allows large models to adapt to tasks using a few examples, yet its extension to vision-language models (VLMs) remains fragile. Our analysis reveals that the fundamental limitation lies in an inductive gap, models often produce correct answers from flawed reasoning, while struggling to extract consistent rules across demonstrations. This gap is further exacerbated by two visual-level obstacles: an overwhelming proportion of redundant visual tokens that obscure textual cues, and a skewed attention distribution that favors the initial image at the expense of subsequent context. To address these issues, we introduce a framework that restructures multimodal ICL as a principled inductive-deductive process. The framework incorporates a similarity-based visual token compression module to filter out redundant patches, a dynamic attention rebalancing mechanism to distribute focus equitably across all images, and a chain-of-thought paradigm that explicitly guides the model to analyze individual examples, derive a generalizable rule, and then apply it to the query. An auxiliary learning pipeline combines supervised fine-tuning with reinforcement learning using verifiable rewards to reinforce faithful citation and noise filtering. Evaluations across eight benchmarks covering visual perception, logical reasoning, STEM problems, and sarcasm detection demonstrate consistent and significant improvements over standard ICL baselines for multiple open-source VLMs, highlighting the potential of equipping models with genuine inductive capabilities in multimodal settings.

---


### 162. [HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness](https://arxiv.org/abs/2605.02396)

**<font color=#1a73e8>作者：</font>** Jianing Wang, Linsen Guo, Zhengyu Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic harness with orchestration frameworks that coordinate multiple agents with memory, skills, and tool use have achieved remarkable success in complex reasoning tasks. However, the underlying mechanism that truly drives performance remains obscured behind intricate system designs. In this paper, we propose HeavySkill, a perspective that views heavy thinking not only as a minimal execution unit in orchestration harness but also as an inner skill internalized within the model's parameters that drives the orchestrator to solve complex tasks. We identify this skill as a two-stage pipeline, i.e., parallel reasoning then summarization, which can operate beneath any agentic harness. We present a systematic empirical study of HeavySkill across diverse domains. Our results show that this inner skill consistently outperforms traditional Best-of-N (BoN) strategies; notably, stronger LLMs can even approach Pass@N performance. Crucially, we demonstrate that the depth and width of heavy thinking, as a learnable skill, can be further scaled via reinforcement learning, offering a promising path toward self-evolving LLMs that internalize complex reasoning without relying on brittle orchestration layers.

---


### 163. [Statistically-Lossless Quantization of Large Language Models](https://arxiv.org/abs/2605.02404)

**<font color=#1a73e8>作者：</font>** Michael Helcig, Eldar Kurtic, Dan Alistarh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model quantization has become essential for efficient large language model deployment, yet existing approaches involve clear trade-offs: methods such as GPTQ and AWQ achieve practical compression but are lossy, while lossless techniques preserve fidelity but typically do not accelerate inference. This paper explores the middle ground of statistically-lossless compression through three complementary notions of losslessness for quantized LLMs. First, task-lossless compression preserves zero-shot benchmark accuracy within natural sampling variance and remains achievable at aggressive bitwidths. Second, we formalize the stricter notion of distribution-lossless compression, requiring the quantized model's next-token distribution to be practically indistinguishable from the original, and propose the Expected Acceptance Rate (EAR), the maximum token-agreement probability under optimal coupling, as a directly interpretable fidelity metric (for example, EAR >= 0.99 indicates 99% agreement). Third, we prove a gamma-squared variance law showing that symmetric quantization inflates noise variance by gamma squared relative to asymmetric quantization, making asymmetry necessary for distribution-lossless fidelity but not for task-level preservation. Using SLQ, a layer-wise non-uniform method with asymmetric quantization and wide bitwidth search, we achieve task-lossless compression at well below 4 bits per parameter (as low as 3.3 bits depending on the model), distribution-lossless compression at 5 to 6 bits per parameter on average, and inference speedups of 1.7 to 3.6x relative to FP16 with optimized kernels. Source code is available at this https URL.

---


### 164. [Closed-Loop CO2 Storage Control With History-Based Reinforcement Learning and Latent Model-Based Adaptation](https://arxiv.org/abs/2605.02405)

**<font color=#1a73e8>作者：</font>** Sofianos Panagiotis Fotias, Vassilis Gaganis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-loop management of geological CO2 storage requires control policies that adapt to uncertain reservoir behavior while relying on observations that are realistically available during operation. This work formulates CO2 injection and brine-production control as a partially observable sequential decision problem and studies deployable deep reinforcement-learning controllers trained with high-fidelity reservoir simulation. We first compare privileged-state, well-only, history-conditioned, masking-curriculum, and asymmetric teacher-student model-free policies in order to quantify the value of temporal well-response information and training-time privileged simulator states. We then evaluate a latent model-based adaptation pipeline that reuses nominal latent dynamics and retunes controllers under known injector failure, leakage-induced dynamics and reward shift, and compartmentalized reservoir connectivity. The results show that history-conditioned policies recover nearly all of the privileged-state performance while using only deployable well-level information, and that latent model-based retuning outperforms direct model-free retuning under the same scenario-specific real-simulator budget in the abnormal operating cases. The proposed framework therefore provides a simulator-budget-aware alternative to repeated online history matching and re-optimization for closed-loop CO2 storage control.

---


### 165. [Inducing Permutation Invariant Priors in Bayesian Optimization for Carbon Capture and Storage Applications](https://arxiv.org/abs/2605.02409)

**<font color=#1a73e8>作者：</font>** Sofianos Panagiotis Fotias, Vassilis Gaganis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimization is an iterative method, tailored to optimizing expensive black box objective functions. Surrogate models like Gaussian Processes, which are the gold standard in Bayesian Optimization, can be inefficient for inputs with permutation symmetries, as the most common kernels employed are better suited for vector inputs rather than unordered sets of items. Motivated by this issue, we turn to permutation invariant Bayesian Optimization for well placement in Carbon Capture and Storage projects. The high fidelity black box simulator is instructed to operate wells under group control, giving rise to permutation symmetries within injector and producer groups that cannot be exploited with standard GP kernels. In this work, our main contribution is a novel Gaussian Process kernel (GP-Perm) that encodes permutation invariance by comparing sets through a stable divergence between their induced empirical representations, and can be combined with standard kernels for additional vector-valued inputs. As a learned invariant baseline, we also consider a Deep Kernel Learning model (DKL-DS) using the Deep Sets architecture to learn a permutation-invariant embedding. We evaluate the proposed methodology across 8 use cases, comprising seven synthetic benchmarks and one realistic CCS case study (Johansen formation)

---


### 166. [Generalized Distributional Alignment Games for Unbiased Answer-Level Fine-Tuning](https://arxiv.org/abs/2605.02435)

**<font color=#1a73e8>作者：</font>** Mehryar Mohri, Jon Schneider, Yutao Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Distributional Alignment Game framework provides a powerful variational perspective on Answer-Level Fine-Tuning (ALFT). However, standard algorithms for these games rely on estimating logarithmic rewards from small batches, introducing a systematic bias due to Jensen's inequality that can destabilize training. In this paper, we systematically resolve this structural estimation bias. First, we generalize the alignment game to arbitrary Bregman divergences, showing that for a family of geometries inducing polynomial rewards, we can construct provably exact and unbiased estimators using U-statistics. Second, for the canonical KL divergence game where an exact solution is impossible, we derive a globally robust minimax polynomial estimator that is provably optimal, achieving the fundamental statistical error limit of $\Theta(1/K^2)$, which we establish via the Ditzian-Totik theorem. Finally, we synthesize these two approaches to propose a novel Variance-Optimal Augmented Polynomial Optimization Program (AQP) Estimator, proving that by systematically reducing variance, our method achieves not only optimal bias but also provably accelerated game convergence, leading to more efficient and stable training with zero online computational overhead.

---


### 167. [HalluScan: A Systematic Benchmark for Detecting and Mitigating Hallucinations in Instruction-Following LLMs](https://arxiv.org/abs/2605.02443)

**<font color=#1a73e8>作者：</font>** Ahmed Cherif  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse natural language processing tasks, yet they remain susceptible to hallucinations -- generating content that is factually incorrect, unfaithful to provided context, or misaligned with user instructions. We present HalluScan, a comprehensive benchmark framework that systematically evaluates hallucination detection and mitigation across 72 configurations spanning 6 detection methods, 4 open-weight model families, and 3 diverse domains. We introduce three key contributions: (1) HalluScore, a novel composite metric that achieves a Pearson correlation of r = 0.41 with human expert judgments; (2) Adaptive Detection Routing (ADR), an intelligent routing algorithm achieving 2.0x cost reduction with only 0.1% AUROC degradation; and (3) systematic error cascade decomposition revealing substantial variation in hallucination error types across domains. Our experiments reveal that NLI Verification achieves the highest overall AUROC of 0.88, while RAV achieves the second-highest AUROC of 0.66.

---


### 168. [M\textsuperscript{4}Fuse: Lightweight State-Space MoE with a Cross-Scale Gating Bridge for Brain Tumor Segmentation](https://arxiv.org/abs/2605.02444)

**<font color=#1a73e8>作者：</font>** Meihua Zhou, Xinyu Tong, Li Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Encoder-decoder imbalance and the reliance on large input volumes make many 3D brain tumor segmentation models both compute-heavy and brittle. We present M\textsuperscript{4}Fuse, a lightweight network that prioritizes discriminative brain tumor cues over exhaustive appearance reconstruction. Our method balances encoder and decoder capacity and replaces depth expansion with a synergistic design: it propagates long-range context with linear complexity via a grouped state space mixer, denoises and aligns skip features using a cross-scale dual-stage gating bridge, and absorbs cross-site acquisition shifts with a sample-level mixture-of-experts. On the BraTS2019 and BraTS2021 benchmarks, M\textsuperscript{4}Fuse outperforms other lightweight excellent methods in both parameter count and performance. Even at a challenging input resolution of \(64\times128\times128\) (half that of existing excellent models), M\textsuperscript{4}Fuse reduces parameters by 62.63\% and improves average performance by 0.09\%. Ablations of key components validate the method's exceptional parameter-to-accuracy efficiency and robustness across diverse data centers.

---


### 169. [PC-MNet: Dual-Level Congruity Modeling for Multimodal Sarcasm Detection via Polarity-Modulated Attention](https://arxiv.org/abs/2605.02447)

**<font color=#1a73e8>作者：</font>** Maoheng Li, Ling Zhou, Xiaohua Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection, which aims to precisely identify pragmatic incongruities between literal text and nonverbal cues, has gained substantial attention in multimodal understanding. Recent advancements have predominantly relied on na\"ıve similarity-based attention mechanisms and uniform late fusion this http URL, given that functional entanglement restricts traditional late fusions, we incorporate a scalar congruity routing mechanism and a prior-guided contextual graph. This mechanism anchors a generalized incongruity manifold through a two-stage asymmetric optimization driven by inconsistency-aware contrastive learning, selectively fusing only the most discriminative multi-granularity evidence. Extensive experiments on the \texttt{MUStARD} benchmark and its spurious-correlation-mitigated balanced datasets demonstrate that our approach achieves new state-of-the-art performance, surpassing the strongest multimodal baseline by a substantial 3.14\% improvement in Macro-F1. By architecturally isolating atomic, composition, and contextual conflicts. This work provides a robust, decoupled paradigm for modeling subtle pragmatic incongruities in human communication.

---


### 170. [Position: How can Graphs Help Large Language Models?](https://arxiv.org/abs/2605.02452)

**<font color=#1a73e8>作者：</font>** Xiyuan Wang, Yi Hu, Yanbo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), classic graph learning tasks have greatly benefited from LLMs, including improved encoding of textual features, more efficient construction of graphs from text, and enhanced reasoning over knowledge graphs. In this paper, we ask a complementary question: How can graphs help LLMs? We address this question from three perspectives: 1) graphs provide an up-to-date knowledge source that helps reduce LLM hallucinations, 2) graph-based prompting techniques-such as Chain-of-Thought (CoT), Tree-of-Thought (ToT), and Graph-of-Thought (GoT)-enhance LLM reasoning capabilities, and 3) integrating graphs into LLMs improves their understanding of structured data, expanding their applicability to domains such as e-commerce, code, and relational databases (RDBs). We further outlook some future directions including designing sparse LLM architectures based on graphs and brain-inspired memory systems.

---


### 171. [Leveraging Argument Structure to Predict Content Hatefulness](https://arxiv.org/abs/2605.02457)

**<font color=#1a73e8>作者：</font>** Nicolas Benjamin Ocampo, Davide Ceolin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information disorder is a challenging phenomenon that affects society at large. This phenomenon entails the diffusion of misleading, misinforming, and hateful content online. In different contexts, one aspect of the problem may prevail, but overall, this is a broad problem that requires comprehensive solutions. While each dimension of the problem (hate speech, disinformation, misinformation, etc.) requires in-depth analysis, in this paper, we look into the possibility of argument structure to provide relevant information to link these different areas of the problem. In particular, we focus on the WSF-ARG+ dataset, which consists of white supremacy forum messages annotated in terms of argument structure (premises and conclusion). There, we leverage the checkworthiness and hatefulness annotations of the argument components to obtain insights into the hatefulness of the whole message. Our results show promising insights (up to 96% F1), indicating the possibility of extending this direction in the future to tackle hateful content identification and information disorder countering.

---


### 172. [When Stress Becomes Signal: Detecting Antifragility-Compatible Regimes in Multi-Agent LLM Systems](https://arxiv.org/abs/2605.02463)

**<font color=#1a73e8>作者：</font>** Jose Manuel de la Chica, Juan Manuel Vera, Jairo Rodríguez  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly used to solve complex tasks through decomposition, debate, specialization, and ensemble reasoning. However, these systems are usually evaluated in terms of robustness: whether performance is preserved under perturbation. This paper studies a different question: whether semantic stress exposes structured variation that could support future antifragile learning. We introduce CAFE, a statistical framework for detecting antifragility-compatible regimes in multi-agent architectures. CAFE models a controlled expected distribution of semantic stressors, reconstructs an architecture-specific observed effective stress distribution from multi-dimensional judge signals, and compares both distributions using a distributional Jensen Gap under a convex stress potential. A positive gap does not imply immediate performance improvement; instead, it indicates a convex-expansive deformation of the observed stress distribution, suggesting that the architecture exposes learnable stress structure. We evaluate CAFE on a banking-risk analysis benchmark with five multi-agent architectures: flat, hierarchical, debate, meta-adaptive, and ensemble. Across all architectures, semantic stress reduces average judged quality by roughly one third. Yet all architectures exhibit positive distributional Jensen Gaps with bootstrap confidence intervals above zero. These results show that immediate quality degradation can coexist with statistically detectable antifragility-compatible stress geometry. CAFE is therefore not an antifragile learner itself, but a measurement layer for identifying when and where antifragility learning may be worth applying.

---


### 173. [Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent](https://arxiv.org/abs/2605.02469)

**<font color=#1a73e8>作者：</font>** Yao Shu, Chenxing Wei, Hongbin Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning with verifiable rewards (RLVR) turns checkable outcomes into a scalable training signal, but it keeps rollout generation, verifier scoring, and reference-policy evaluations on the optimization path. Static weighted supervised fine-tuning (SFT) on precomputed rollouts seems to remove this bottleneck, yet a weighted likelihood is not specified by rewards alone: its sampler and weights induce the policy being fit. This paper identifies the reference-sampled weighted-SFT objective whose induced policy equals the fixed-reference KL-regularized RLVR optimizer. The optimizer is the standard Boltzmann target policy, obtained by exponentially tilting the reference policy by verifier reward. Matching a weighted-SFT induced policy to this target forces density-ratio weights; in the reference-sampled subclass, this reduces uniquely, up to prompt scaling, to the prompt-normalized Boltzmann weight $\exp(r(x,y)/\beta)/Z(x)$. BOLT, a Boltzmann-Targeted SFT procedure, is the empirical estimator of this projection. The finite one-shot analysis separates the exact stored-support price $\beta\log(1/\pi^*(S_N\mid x))$ from partition estimation, effective-sample-size variance, generalization, optimization, and approximation errors. This decomposition explains why extra SFT epochs cannot repair missing reference-policy coverage and exposes the temperature--coverage--variance frontier. When coverage needs adaptive sampling, refreshed Boltzmann projections become KL policy mirror descent; finite inner solves enter as additive drift from the exact mirror step. Single-run Qwen experiments provide projection evidence for the target-matched weight, one-shot saturation, refreshed-sampler gains, and optimization-time savings, within the stated single-run scope.

---


### 174. [Accurate Legal Reasoning at Scale: Neuro-Symbolic Offloading and Structural Auditability for Robust Legal Adjudication](https://arxiv.org/abs/2605.02472)

**<font color=#1a73e8>作者：</font>** Stanisław Sójka, Witold Kowalczyk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal texts often contain computational legal clauses--provisions whose understanding requires complex logic. While frontier Large Reasoning Models (LRMs) can describe such clauses, building production-ready systems is limited by reasoning errors and the high cost of inference. We propose Amortized Intelligence, a neuro-symbolic approach where we use an LLM once to translate a legal text into Deterministic Autonomous Contract Language (DACL): a typed graph intermediate representation. Adjudication then relies on deterministic graph executions with a visually auditable trace. In comparison against runtime LRM baselines (including GPT-5.2 and Gemini 3 Pro), our DACL-based Agent achieves near-perfect consistency and mitigates the "reasoning cliff" observed in probabilistic models. The system reduces compute costs by over 90% in high-volume workflows while satisfying the strict auditability requirements of legal adjudication.

---


### 175. [Shadow-Loom: Causal Reasoning over Graphical World Model of Narratives](https://arxiv.org/abs/2605.02475)

**<font color=#1a73e8>作者：</font>** David Wilmot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stories hold a reader's attention because they have causes, secrets, and consequences. Shadow-Loom is an experimental open-source framework that turns a narrative into a versioned graphical world model and lets two engines act on it: a causal physics grounded in Pearl's ladder of causation and a recently proposed counterfactual calculus over Ancestral Multi-World Networks; and a narrative physics that scores the same graph against four structural reader-states -- mystery, dramatic irony, suspense, and surprise -- in the tradition of Sternberg's curiosity/suspense/surprise triad, with suspense formalised in the structural-affect line of work on story comprehension and computational suspense. Large language models are used only at the boundary: extraction, rendering, and audit; identification, intervention, and counterfactual reasoning are carried out in typed code over the graph. The system is offered as a research artefact rather than as a benchmarked NLP model; code, fixtures, and pipeline are released open source.

---


### 176. [Efficient Preference Poisoning Attack on Offline RLHF](https://arxiv.org/abs/2605.02495)

**<font color=#1a73e8>作者：</font>** Chenye Yang, Weiyu Xu, Lifeng Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline Reinforcement Learning from Human Feedback (RLHF) pipelines such as Direct Preference Optimization (DPO) train on a pre-collected preference dataset, which makes them vulnerable to preference poisoning attack. We study label flip attacks against log-linear DPO. We first illustrate that flipping one preference label induces a parameter-independent shift in the DPO gradient. Using this key property, we can then convert the targeted poisoning problem into a structured binary sparse approximation problem. To solve this problem, we develop two attack methods: Binary-Aware Lattice Attack (BAL-A) and Binary Matching Pursuit Attack (BMP-A). BAL-A embeds the binary flip selection problem into a binary-aware lattice and applies Lenstra-Lenstra-Lovász reduction and Babai's nearest plane algorithm; we provide sufficient conditions that enforce binary coefficients and recover the minimum-flip objective. BMP-A adapts binary matching pursuit to our non-normalized gradient dictionary and yields coherence-based recovery guarantees and robustness (impossibility) certificates for $K$-flip budgets. Experiments on synthetic dictionaries and the Stanford Human Preferences dataset validate the theory and highlight how dictionary geometry governs attack success.

---


### 177. [Benchmarking Retrieval Strategies for Biomedical Retrieval-Augmented Generation: A Controlled Empirical Study](https://arxiv.org/abs/2605.02520)

**<font color=#1a73e8>作者：</font>** Devi Prasad Bal, Subhashree Puhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) offers a well-established path to grounding large language model (LLM) outputs in external knowledge, yet the question of which retrieval strategy works best in a high-stakes domain such as biomedicine has not received the controlled, multi-metric treatment it deserves. This paper presents a systematic empirical comparison of five retrieval strategies -- Dense Vector Search, Hybrid BM25 + Dense retrieval, Cross-Encoder Reranking, Multi-Query Expansion, and Maximal Marginal Relevance (MMR) -- within a biomedical question-answering RAG pipeline. All strategies share a fixed generation model (GPT-4o-mini), a common vector store (ChromaDB), and OpenAI's text-embedding-3-small embeddings, ensuring that observed differences are attributable to retrieval alone. Evaluation is conducted on 250 question-answer pairs drawn from a preprocessed subset of the BioASQ benchmark (rag-mini-bioasq) using four DeepEval metrics: contextual precision, contextual recall, faithfulness, and answer relevancy, each reported with 95% confidence intervals. A no-context ablation is included as a lower bound. Cross-Encoder Reranking achieves the best composite score (0.827) and highest contextual precision (0.852), confirming that query-document interaction yields measurable retrieval gains. Multi-Query Expansion, despite its recall-oriented design, produces the weakest contextual precision (0.671), suggesting naive query diversification introduces retrieval noise. MMR sacrifices answer relevancy for diversity, while the Dense baseline (composite 0.822) falls within 0.005 points of the top strategy. All RAG conditions dramatically outperform the no-context ablation on answer relevancy (0.658-0.701 vs. 0.287), confirming the practical value of retrieval. The full pipeline, hyperparameters, and evaluation code are publicly available.

---


### 178. [Strategy-Aware Optimization Modeling with Reasoning LLMs](https://arxiv.org/abs/2605.02545)

**<font color=#1a73e8>作者：</font>** Ruiqing Zhao, Fengzhi Li, Yuan Zuo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate syntactically valid optimization programs, yet often struggle to reliably choose an effective modeling strategy, leading to incorrect formulations and inefficient solver behavior. We propose SAGE, a strategy-aware framework that makes Modeling Strategy explicit in both data construction and post-training. SAGE builds a solver-verified multi-strategy dataset and trains a student model with supervised fine-tuning followed by Segment-Weighted GRPO using a composite reward over format compliance, correctness, and solver efficiency. Across eight benchmarks spanning synthetic and real-world settings, SAGE improves average pass@1 from 72.7 to 80.3 over the strongest open-source baseline. With multiple generations, SAGE discovers more distinct correct formulations and improves component-level diversity at pass@16 by 19-29%. At the largest scale, SAGE produces more compact constraint systems with 14.2% fewer constraints than the baseline, consistent with solver-efficient modeling. Overall, these results show that making Modeling Strategy explicit improves automated optimization modeling. Code is available at this https URL.

---


### 179. [On Training Large Language Models for Long-Horizon Tasks: An Empirical Study of Horizon Length](https://arxiv.org/abs/2605.02572)

**<font color=#1a73e8>作者：</font>** Sunghwan Kim, Junhee Cho, Beong-woo Kwak 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise as interactive agents that solve tasks through extended sequences of environment interactions. While prior work has primarily focused on system-level optimizations or algorithmic improvements, the role of task horizon length in shaping training dynamics remains poorly understood. In this work, we present a systematic empirical study that examines horizon length through controlled task constructions. Specifically, we construct controlled tasks in which agents face identical decision rules and reasoning structures, but differ only in the length of action sequences required for successful completion. Our results reveal that increasing horizon length alone constitutes a training bottleneck, inducing severe training instability driven by exploration difficulties and credit assignment challenges. We demonstrate that horizon reduction is a key principle to address this limitation, stabilizing training and achieving better performance in long-horizon tasks. Moreover, we find that horizon reduction is related to stronger generalization across horizon lengths: models trained under reduced horizons generalize more effectively to longer-horizon variants at inference time, a phenomenon we refer to as horizon generalization.

---


### 180. [Foundation-Model-Based Agents in Industrial Automation: Purposes, Capabilities, and Open Challenges](https://arxiv.org/abs/2605.02592)

**<font color=#1a73e8>作者：</font>** Vincent Henkel, Felix Gehlhoff, David Kube 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models, particularly large language models, are increasingly integrated into agent architectures for industrial tasks such as decision support, process monitoring, and engineering automation. Yet evidence on their purposes, capabilities, and limitations remains fragmented across domains. This work examines how mature foundation-model-based agent systems are in industrial contexts, how their functional profile differs from conventional agent systems, and which limitations persist. A systematic literature survey following the PRISMA 2020 guideline is presented, screening 2,341 publications and synthesising a corpus of 88 publications through a structured coding scheme. The results show that reported systems are predominantly at prototype and early validation stages (75.0% at TRL 4-6), with deployment-oriented evidence remaining rare (9.1%). Operational goals are most frequently positioned in user assistance, monitoring, and process optimisation, while conventional production-control purposes such as planning and scheduling are less prominent. Compared with an established baseline for industrial agent systems, the capability profile reveals substantial gains in human interaction (+37%) and dealing with uncertainty (+35%), but a pronounced deficit in negotiation (-39%). The most widely reported limitations concern lack of generalization, hallucination and output instability, data scarcity, and inference latency. A working definition of foundation-model-based industrial agents is also proposed, bridging conventional agent theory, automation-engineering standards, and the foundation-model paradigm.

---


### 181. [Rethinking the Need for Source Models: Source-Free Domain Adaptation from Scratch Guided by a Vision-Language Model](https://arxiv.org/abs/2605.02604)

**<font color=#1a73e8>作者：</font>** Zhou Bingtao, Xiang Mian, Ning Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-Free Domain Adaptation (SFDA) adapts source models to target domains without accessing source data, addressing privacy and transmission issues. However, existing methods still initialize from a source pre-trained model and thus are not truly source-free. Recent works have introduced Vision-Language (ViL) models to guide the adaptation process, in these methods, we observe that for the same target domain, different source models yield minimal variation in final results, indicating the source model itself has limited impact. Motivated by this, we propose ViL-Only Domain Adaptation (VODA) , a stricter setting that eliminates all dependencies on source domain, relying solely on a randomly initialized model, a ViL model, and unlabeled target data. We analyze the adaptation dynamics of VODA and introduce Two-Stage Denoised-Region Distillation (TS-DRD) , a two-stage framework that first warms up the model with ViL guidance, then seek a Denoised-Region inherent in both the ViL and adapting model, yielding cleaner supervision for distillation. Experiments on Office-Home, VisDA, and DomainNet-126 show that under VODA, TS-DRD achieves competitive or superior performance to existing SFDA methods that still use source models, demonstrating its effectiveness and the potential of the VODA setting.

---


### 182. [Beating the Style Detector: Three Hours of Agentic Research on the AI-Text Arms Race](https://arxiv.org/abs/2605.02620)

**<font color=#1a73e8>作者：</font>** Andreas Maier, Moritz Zaiss, Siming Bayer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reproducing an empirical NLP study used to take weeks. Given the released data and a modern agentic-research harness, we redo every experiment of a recent ACL\,2026 study on personal-style post-editing of LLM drafts -- and add three new ones -- with the human investigator acting only as a reviewer-in-the-loop. We reproduce all seven preregistered hypotheses and recover the paper's headline correlation between perceived self-similarity and embedding-measured self-similarity to three decimal places ($r{=}{+}0.244$, $p{<}10^{-8}$, $n{=}648$). Under a leakage-free held-out protocol, GPT-5.5 and Claude\,Opus\,4.7 close $71$--$75\,\%$ of the style gap to the same-author ceiling on $324$ paired tasks, against $24\,\%$ for the human post-edit, and beat the human post-edit on $\sim$$80\,\%$ of tasks. We then frame the same data as an AI-text detection arms race. A leave-authors-out linear SVM on LUAR-MUD embeddings reaches AUC $0.93$--$1.00$ across approaches; six diagnostics show that GPT-5.5 detection is mostly a length confound while Opus detection is a genuine stylistic signature. Given $T{=}20$ feedback iterations against the frozen detector, an Opus agent flips two of five held-out test mimics to the human half-space and shrinks every margin by an order of magnitude. With moderate effort against a known detector, a frontier LLM can already efficiently lower its own AI-detection probability. All code, $648$ mimic drafts, trained detectors, diagnostics, and adversarial trajectories are released.

---


### 183. [Retrieving Any Relevant Moments: Benchmark and Models for Generalized Moment Retrieval](https://arxiv.org/abs/2605.02623)

**<font color=#1a73e8>作者：</font>** Yiming Ding, Siyu Cao, Luyuan Jiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Moment Retrieval (VMR) aims to localize temporal segments in videos that correspond to a natural language query, but typically assumes only a single matching moment for each query. This assumption does not always hold in real-world scenarios, where queries may correspond to multiple or no moments. Thus, we formulate Generalized Moment Retrieval (GMR), a unified setting that requires retrieving the complete set of relevant moments or predicting an empty set. To enable systematic study of GMR, we introduce Soccer-GMR, a large-scale benchmark built on challenging soccer videos that reflect general GMR scenarios, with realistic negative and positive queries. The benchmark is constructed via a duration-flexible semi-automated pipeline with human verification, enabling scalable data generation while maintaining high annotation quality. We further design a unified evaluation protocol with complementary metrics tailored for null-set rejection, positive-query localization, and end-to-end GMR performance. Finally, we establish strong baselines across two modeling paradigms: a lightweight plug-and-play GMR adapter for discriminative VMR models, and a GMR-tailored GRPO reward for fine-tuning multimodal large language models (MLLMs). Extensive experiments show consistent gains across all metrics and expose key limitations of current methods, positioning GMR as a more realistic and challenging benchmark for video-language understanding.

---


### 184. [Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models](https://arxiv.org/abs/2605.02626)

**<font color=#1a73e8>作者：</font>** Inoussa Mouiche  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference optimization has become a central paradigm for aligning large language models with human feedback. Direct Preference Optimization (DPO) simplifies reinforcement learning from human feedback by directly optimizing pairwise preferences, removing the need for reward modeling and policy optimization. However, recent work shows that DPO exhibits a squeezing effect, where negative gradients applied to rejected responses concentrate probability mass on high-confidence predictions while suppressing alternative responses. This phenomenon arises even in simple softmax models and can lead to systematic probability collapse during training. We introduce Gradient-Gated Preference Optimization (Gate-DPO), a method that stabilizes training by modulating rejected gradients according to the model's probability geometry. When updates target extremely low-probability responses, the gate attenuates harmful gradients while preserving standard optimization behavior. Gate-DPO addresses this optimization pathology without modifying the underlying preference objective and is complementary to existing methods such as extended SFT, IPO, and Cal-DPO. Experiments across multiple architectures and preference datasets show that Gate-DPO consistently reduces squeezing and improves chosen-response likelihood. Mass-dynamics analysis further reveals healthier optimization behavior, with improved preferred responses and reduced suppression of the overall distribution. Notably, smaller gated models can exhibit stronger chosen-response improvements than larger ungated models, suggesting that controlling gradient dynamics, rather than scale alone, is key to stable and efficient alignment.

---


### 185. [Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE](https://arxiv.org/abs/2605.02641)

**<font color=#1a73e8>作者：</font>** Yangming Shi, Shixiang Zhu, Tao Shen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Mamoda2.5, a unified AR-Diffusion framework that seamlessly integrates multimodal understanding and generation within a single architecture. To efficiently enhance the model's generation capability, we equip the Diffusion Transformer backbone with a fine-grained Mixture-of-Experts (MoE) design (128 experts, Top-8 routing), yielding a 25B-parameter model that activates only 3B parameters, significantly reducing training costs while scaling up the model capacity. Mamoda2.5 achieves top-tier generation performance on VBench 2.0 and sets a new record in video editing quality, surpassing evaluated open-source models and matching the performance of current top-tier proprietary models, including the Kling O1 on OpenVE-Bench. Furthermore, we introduce a joint few-step distillation and reinforcement learning framework that compresses the 30-step editing model into a 4-step model and greatly accelerates model inference. Compared to open-source baselines, Mamoda2.5 achieves up to $95.9\times$ faster video editing inference. In real-world applications, Mamoda2.5 has been successfully deployed for content moderation and creative restoration tasks in advertising scenarios, achieving a 98% success rate in internal advertising video editing scenario.

---


### 186. [ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming](https://arxiv.org/abs/2605.02647)

**<font color=#1a73e8>作者：</font>** Mario Rodríguez Béjar, Francisco J. Cortés-Delgado, S. Braghin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safety alignment and elicit harmful responses. A growing body of work shows that contextual priming, where earlier turns covertly bias later replies, constitutes a powerful attack surface, with hand-crafted multi-turn scaffolds consistently outperforming single-turn manipulations on capable models.
However, automated optimization-based red-teaming has remained largely limited to the single-turn setting, iterating over static prompts and lacking the ability to reason about which forms of conversational priming induce compliance. While recent multi-turn, search-based approaches have begun to bridge this gap, the mutator design space underlying effective primed dialogues remains largely unexplored.
We present ContextualJailbreak, a black-box red-teaming strategy that performs evolutionary search over a simulated multi-turn primed dialogue. The strategy leverages a graded 0-5 harm score from a two-level judge as an in-loop signal, enabling partially harmful responses to guide the search process rather than being discarded.
Search is driven by five semantically defined mutation operators: roleplay, scenario, expand, troubleshooting, and mechanistic, of which the last two are novel contributions of this work.
Across 50 representative HarmBench behaviors, ContextualJailbreak achieves an ASR of 100% on gpt-oss:20B, 100% on qwen3-8B, 100% on llama3.1:70B, and 90% on gpt-oss:120B, outperforming four single- and multi-turn baselines by 31-96 percentage points on average.
The 40 maximally harmful attacks discovered against gpt-oss:120B transfer without adaptation to closed frontier models, achieving 90.0% on gpt-4o-mini, 70.0% on gpt-5, and 70.0% on gemini-3-flash, but only 17.5% on claude-opus-4-7 and 15.0% on claude-sonnet-4-6, revealing a pronounced provider-level asymmetry in alignment robustness.

---


### 187. [Fuzzy Fingerprinting Encoder Pre-trained Language Models for Emotion Recognition in Conversations: Human Assessment and Validity Study](https://arxiv.org/abs/2605.02665)

**<font color=#1a73e8>作者：</font>** Patrícia Pereira, Helena Moniz, Joao Paulo Carvalho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Emotion Recognition in Conversations (ERC), model decisions should align with nuanced human perception and ideally provide insights on the classification process. Standard encoder pre-trained language models (PLMs) are the state-of-the-art at these tasks but offer little insight into why a certain prediction is made. This is especially problematic in imbalanced datasets, where most utterances are labeled as neutral, making these models frequently misclassify minority emotions as the majority neutral class. To tackle this issue, we introduced a novel, interpretable approach to ERC by combining PLMs with Fuzzy Fingerprints (FFPs). FFP provide class-specific prototypes that reflect the characteristic class activation patterns in the PLM's latent space. They are derived by ranking and fuzzifying the activations of the pooled conversational context-dependent embeddings across training instances for each emotion. At inference time, each input utterance is similarly fuzzy fingerprinted and matched to the emotion prototypes using a fuzzy similarity function based on the aggregation of the intersection of the fuzzy sets that define each FFP. Experimental results show that FFP integration reduces overclassification into the neutral class and human evaluation further supports the adequacy of FFP predictions. Our proposed method thus bridges the gap between deep neural inference and human perception, performing at state-of-the-art level while simultaneously offering valuable insights into the classification procedure.

---


### 188. [Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI](https://arxiv.org/abs/2605.02682)

**<font color=#1a73e8>作者：</font>** Majed El Helou, Benjamin Ryder, Chiara Troiani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Authorizing Large Language Model (LLM)-driven agents to dynamically invoke tools and access protected resources introduces significant security risks, and the risks grow dramatically as agents engage in multi-turn conversations and scale toward distributed collaboration. A compromised or malicious agentic application can tamper with tool calls, falsify results, or request permissions beyond the scope of the subject's intended tasks, which could go unnoticed with current delegated authorization flows given their lack of visibility into the original subject's intent. In light of this, we make the following contributions towards Continuous Agent Semantic Authorization (CASA). First, we propose a hybrid runtime enforcement model that combines deterministic and semantic controls enabled by a zero-trust interception layer. Five deterministic controls enforce structural and data-integrity guarantees over the message flow, while a semantic inspection layer evaluates whether tool call choices align with the intended tasks commissioned to the agent. Second, differently from prior Task-Based Access Control (TBAC) techniques that operate on single-turn interactions, we decompose the semantic layer into two stages: i) a task-extraction step that distills the subject's objectives from multi-turn conversations at the interception layer, and ii) a task-tool semantic matching step at the authorization server that evaluates whether the requested tools are appropriate for the extracted tasks. Third, we extend the ASTRA dataset that we introduced in a prior work, by generating novel conversation-tool datasets with multi-turn interactions containing relevant and irrelevant tool calls for a given task. Lastly, we provide the first experimental results for TBAC under multi-turn conversations.

---


### 189. [mdok-style at SemEval-2026 Task 9: Finetuning LLMs for Multilingual Polarization Detection](https://arxiv.org/abs/2605.02695)

**<font color=#1a73e8>作者：</font>** Dominik Macko, Alok Debnath, Jakub Simko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SemEval-2026 Task 9 is focused on multilingual polarization detection. Specifically, it covers the identification of multilingual, multicultural and multievent polarization along three axes (in subtasks), namely detection, type, and manifestation. Online polarization presents a concern, because it is often followed by hate speech, offensive discourse, and social fragmentation. Therefore, its detection before it escalates is crucial for a safer and more inclusive online space. We have coped with this SemEval task by finetuning mid-size LLMs for the sequence-classification task using the QLoRA parameter-efficient finetuning technique. The training data augmented the multilingual (22 languages) training sets by anonymized, lower-cased, upper-cased, and homoglyphied counterparts, making the detection more robust.

---


### 190. [mdok-style at SemEval-2026 Task 10: Finetuning LLMs for Conspiracy Detection](https://arxiv.org/abs/2605.02712)

**<font color=#1a73e8>作者：</font>** Dominik Macko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SemEval-2026 Task 10 is focused on conspiracy detection. Specifically, the goal is to detect whether a Reddit comment expresses a conspiracy belief. Our submitted mdok-style system utilizes data augmentation and self-training (to cope with a rather small amount of training data) to finetune the Qwen3-32B model for a binary text-classification task. The submitted system is very competitive, ranking in the 85th percentile (8th out of 52 submissions). The results shown that our approach, which originated in machine-generated text detection, can be used for conspiracy detection as well.

---


### 191. [OphMAE: Bridging Volumetric and Planar Imaging with a Foundation Model for Adaptive Ophthalmological Diagnosis](https://arxiv.org/abs/2605.02714)

**<font color=#1a73e8>作者：</font>** Tienyu Chang, Zhen Chen, Renjie Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of foundation models has heralded a new era in medical artificial intelligence (AI), enabling the extraction of generalizable representations from large-scale unlabeled datasets. However, current ophthalmic AI paradigms are predominantly constrained to single-modality inference, thereby creating a dissonance with clinical practice where diagnosis relies on the synthesis of complementary imaging modalities. Furthermore, the deployment of high-performance AI in resource-limited settings is frequently impeded by the unavailability of advanced three-dimensional imaging hardware. Here, we present the Ophthalmic multimodal Masked Autoencoder (OphMAE), a multi-imaging foundation model engineered to synergize the volumetric depth of 3D Optical Coherence Tomography (OCT) with the planar context of 2D en face OCT. By implementing a novel cross-modal fusion architecture and a unique adaptive inference mechanism, OphMAE was pre-trained on a massive dataset with of 183,875 paired OCT images derived from 32,765 patients. In a rigorous benchmark encompassing 17 diverse diagnostic tasks with 48,340 paired OCT images from 8,191 patients, the model demonstrated state-of-the-art performance, achieving an Area Under the Curve (AUC) of 96.9% for Age-related Macular Degeneration (AMD) and 97.2% for Diabetic Macular Edema (DME), consistently surpassing existing single-modal and multimodal foundation models. Crucially, OphMAE exhibits robust engineering adaptability: it maintains high diagnostic accuracy, such as 93.7\% AUC for AMD, even when restricted to single-modality 2D inputs, and demonstrates exceptional data efficiency by retaining 95.7% AUC with as few as 500 labeled samples. This work establishes a scalable and adaptable framework for ophthalmic AI, ensuring robust performance across different tasks.

---


### 192. [PubMed-Ophtha: An open resource for training ophthalmology vision-language models on scientific literature](https://arxiv.org/abs/2605.02720)

**<font color=#1a73e8>作者：</font>** Verena Jasmin Hallitschke, Carsten Eickhoff, Philipp Berens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models hold considerable promise for ophthalmology, but their development depends on large-scale, high-quality image-text datasets that remain scarce. We present PubMed-Ophtha, a hierarchical dataset of 102,023 ophthalmological image-caption pairs extracted from 15,842 open-access articles in PubMed Central. Unlike existing datasets, figures are extracted directly from article PDFs at full resolution and decomposed into their constituent panels, panel identifiers, and individual images. Each image is annotated with its imaging modality -- color fundus photography, optical coherence tomography, retinal imaging, or other -- and a mark status indicating the presence of annotation marks such as arrows. Figure captions are split into panel-level subcaptions using a two-step LLM approach, achieving a mean average sentence BLEU score of 0.913 on human-annotated data. Panel and image detection models reach a mAP@0.50 of 0.909 and 0.892, respectively, and figure extraction achieves a median IoU of 0.997. To support reproducibility, we additionally release the human-annotated ground-truth data, all trained models, and the full dataset generation pipeline.

---


### 193. [ORPilot: A Production-Oriented Agentic LLM-for-OR Tool for Optimization Modeling](https://arxiv.org/abs/2605.02728)

**<font color=#1a73e8>作者：</font>** Guangrui Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents ORPilot, an open-source agentic AI system that translates real-world business problems into solver-ready optimization models. Unlike academic LLM-for-OR tools that assume clean problem specifications with preformatted inline data, ORPilot is designed for production conditions: ambiguous descriptions, large-scale raw operational data, and the need for portability across solver backends. The system introduces four novel components: (1) a conversational interview agent to elicit complete problem specifications, (2) a data collection agent that retrieves data independently of prompts, (3) a parameter computation agent to bridge raw tabular data and model-ready parameters, and (4) a solver-agnostic Intermediate Representation (IR) for deterministic, zero-LLM-call recompilation to Gurobi, CPLEX, PuLP, Pyomo, or OR-Tools solvers. Additionally, self-correcting retry loops utilize solver tracebacks for targeted repairs. ORPilot represents the first attempt to target production-level business problems rather than textbook operations research (OR) cases. Evaluation on real-world problems demonstrates promising results. When tested against traditional academic benchmarks: IndustryOR, NL4OPT and NLP4LP, ORPilot outperformed state-of-the-art tools in accuracy on the IndustryOR benchmark and delivered comparable performance on NL4OPT and NLP4LP.

---


### 194. [Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs](https://arxiv.org/abs/2605.02735)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Qiqi Tao, Jiawei Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous latent-space reasoning offers a compact alternative to textual chain-of-thought for multimodal models, enabling high-dimensional visual evidence to be integrated without explicit reasoning tokens. However, we identify a previously overlooked optimization pathology in existing latent visual reasoning methods: although visual latents become semantically enriched during training, their contribution to final answer prediction is systematically suppressed. Within the shared parameter space, the autoregressive objective favors shortcut reliance on direct visual input, driving latent tokens toward transition-like states rather than informative reasoning content. We term this phenomenon Silenced Visual Latents. To address it, we disentangle the two conflicting objectives by directly optimizing the latent reasoning at inference time, keeping backbone parameters frozen. In Stage I, visual latents are warmed up via query-guided contrastive latent--visual alignment, improving semantic quality while preventing latent collapse. In Stage II, the latent reasoning is further optimized via a confidence-progression reward, which incentivizes predicted token distributions along the latent span to become progressively more concentrated, routing predictions through the latent reasoning rather than bypassing it. Experiments across eight benchmarks and four model backbones show that inference-time latent optimization, without any parameter updates, effectively unleashes the suppressed reasoning capacity of visual latents.

---


### 195. [Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims](https://arxiv.org/abs/2605.02740)

**<font color=#1a73e8>作者：</font>** Fan Ma, Yuntian Liu, Xiang Lan 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence derived from large-scale real-world data (RWD) is increasingly informing regulatory evaluation and healthcare decision-making. Administrative claims provide population-scale, longitudinal records of healthcare utilization, expenditure, and detailed coding of diagnoses, procedures, and medications, yet their potential as a substrate for healthcare foundation models remains largely unexplored. Here we present ReClaim, a generative transformer trained from scratch on 43.8 billion medical events from more than 200 million enrollees in the MarketScan claims data spanning 2008-2022. ReClaim models longitudinal trajectories across diagnoses, procedures, medications, and expenditure, and was scaled to 140 million, 700 million, and 1.7 billion parameters. Across over 1,000 disease-onset prediction tasks, ReClaim achieved a mean AUC of 75.6%, substantially outperforming disease-specific LightGBM (66.3%) and the transformer-based Delphi model (69.4%), with the largest gains for rare diseases. These advantages held across retrospective and prospective evaluations and in external validation on two independent datasets. Performance improved monotonically with scale, and post-training added 13.8 percentage points over pre-training alone. Beyond disease prediction, ReClaim captured financial outcomes and improved real-world evidence (RWE) analyses: for healthcare expenditure forecasting it increased explained variance from 0.28 to 0.37 relative to LightGBM, and in a target trial emulation it reduced systematic bias by 72% on average relative to Delphi. Together, these results establish administrative claims as a scalable substrate for healthcare foundation models and show that learned representations generalize across time periods and data sources, supporting disease surveillance, expenditure forecasting, and RWE generation.

---


### 196. [Bolek: A Multimodal Language Model for Molecular Reasoning](https://arxiv.org/abs/2605.02745)

**<font color=#1a73e8>作者：</font>** Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while language models can produce fluent explanations weakly grounded in the input molecule.
We introduce Bolek, a compact multimodal language model that grounds natural-language reasoning in molecular structure by injecting a Morgan fingerprint embedding into an instruction-tuned text decoder. Bolek is fine-tuned on molecular alignment tasks, including molecule description, RDKit descriptor prediction, and substructure detection, and on downstream reasoning over 15 TDC binary classification tasks using synthetic chains-of-thought anchored in concrete molecular features.
Across these tasks, Bolek outperforms its Qwen3-4B-Instruct base on all endpoints in yes/no mode and on 13 of 15 in chain-of-thought mode, raising mean ROC/PR AUC from 0.55 to 0.76. It also outperforms TxGemma-9B-Chat on 13 of 15 binary classification tasks despite being less than half its size. Bolek's explanations are more grounded than those of the baseline LLMs: it cites numerical descriptors 10-100x more often per chain-of-thought, and the cited values agree strongly with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Generalisation extends beyond the training panel: on 15 unseen TDC classification endpoints, Bolek matches TxGemma on five, and it produces non-trivial rank correlations on three held-out regression endpoints despite never seeing downstream regression during training.
These results suggest that targeted modality injection and reasoning supervision tied to verifiable molecular features can yield compact, auditable molecular reasoning models.

---


### 197. [Mitigating Misalignment Contagion by Steering with Implicit Traits](https://arxiv.org/abs/2605.02751)

**<font color=#1a73e8>作者：</font>** Maria Chang, Ronny Luss, Miao Lui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.

---


### 198. [U-Define: Designing User Workflows for Hard and Soft Constraints in LLM-Based Planning](https://arxiv.org/abs/2605.02765)

**<font color=#1a73e8>作者：</font>** Christine P Lee, Xinyu Jessica Wang, Aws Albarghouthi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used for end-user task planning, yet their black-box nature limits users' ability to ensure reliability and control. While recent systems incorporate verification techniques, it remains unclear how users can effectively apply such rigid constraints to represent intent or adapt to real-world variability. For example, prior work finds that hard-only constraints are too rigid, and numeric flexibility weights confuse users. We investigate how interaction workflows can better support users in applying constraints to guide LLM-generated plans, examining whether abstracting strictness into high-level types (i.e., hard and soft) paired with distinct verification mechanisms helps users more reliably express and align intent. We present U-Define, a system that lets users define constraints in natural language and categorize them as either hard rules that must not be violated or soft preferences that allow flexibility. U-Define verifies these types through complementary methods: formal model checking for hard constraints and LLM-as-judge evaluation for soft ones. Through a technical evaluation and user studies with general and expert participants, we find that user-defined constraint types improve perceived usefulness, performance, and satisfaction while maintaining usability. These findings provide insights for designing flexible yet reliable constraint-based workflows.

---


### 199. [When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition](https://arxiv.org/abs/2605.02782)

**<font color=#1a73e8>作者：</font>** Pehuén Moure, Niclas Pokel, Bilal Bounajma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.

---


### 200. [Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces](https://arxiv.org/abs/2605.02801)

**<font color=#1a73e8>作者：</font>** Chenchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped. This paper studies RL for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions.
Using this lens, we identify three technical axes. First, reward design spans eight families, including orchestration rewards for parallelism speedup, split correctness, and aggregation quality. Second, reward and credit signals attach to eight credit- or signal-bearing units from token to team; explicit counterfactual message-level credit remains especially sparse in our curated pool. Third, orchestration learning decomposes into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop. In our curated pool as of May 4, 2026, we found no explicit RL training method for the stopping decision.
We connect academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code. The resulting scale gap is a gap between publicly reported deployment envelopes and open academic evaluation regimes, not independent verification of industrial training traces. We release the artifact at this https URL, including an 84-entry tagged paper pool, a 32-record exclusion log, scripted corpus statistics, and a minimal JSON schema for replayable orchestration traces.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
